pipeline {
    agent {
        node {
            label 'PDRA-agent' // Specify the node label
            customWorkspace 'C:\\Users\\QAAPP_AT_PC2\\PycharmProjects\\AT_PDRA' // Define custom workspace path
        }
    }
    stages {
        stage('Receive ATS JSON') { // Stage for receiving and parsing ATS JSON
            steps {
                script {
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        try {
                            // Check if the 'data' parameter is provided
                            if (!params.data?.trim()) {
                                error("ATS JSON data not provided")
                            }

                            // Parse the provided JSON string into an object
                            def atsJson = readJSON text: params.data
                            env.atsBuildId = atsJson.atsInfo.atsBuildId
                            env.atsCallbackUrl = atsJson.atsInfo.atsCallbackUrl
                            env.build = atsJson.build.build
                            env.buildPath = atsJson.build.prog_path
                            env.srNo = atsJson.build.sr_no
                            env.trNo = atsJson.build.tr_no

                            // Check if buildPath exists in the JSON
                            if (!env.buildPath?.trim()) {
                                error("ATS JSON missing buildPath")
                            }

                            echo "Parsed ATS JSON data:"
                            echo groovy.json.JsonOutput.prettyPrint(groovy.json.JsonOutput.toJson(atsJson))

                            sendCallback(env.atsBuildId, "RUNNING", [
                                buildId: env.BUILD_NUMBER
                            ])
                        } catch (Exception e) {
                            echo "Error occurred while receiving or parsing ATS JSON: ${e.message}"
                            sendCallback(env.atsBuildId, "TRIGGER_ERROR", [
                                result: "RECEIVE_FAILED",
                                reason: e.message
                            ])
                            throw e
                        }
                    }
                }
            }
        }
        stage('Install Build') { // Stage for installing the build
            steps {
                script {
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        try {
                            // Ensure buildPath is provided
                            if (!env.buildPath?.trim()) {
                                error("Missing buildPath, unable to install APK")
                            }
                            echo "Installing APK from buildPath: ${env.buildPath}"

                            // Execute the installation command
                            def installCommand = "python install_pdra.py \"${env.buildPath}\""
                            echo "Running installation command: ${installCommand}"
                            def installResult = bat(script: installCommand, returnStatus: true)

                            // Check installation result
                            if (installResult != 0) {
                                echo "Installation failed, exit code: ${installResult}"
                                currentBuild.result = 'UNSTABLE'
                            } else {
                                echo "Installation successful"
                            }
                        } catch (Exception e) {
                            echo "Unexpected error during installation: ${e.message}"
                            currentBuild.result = 'UNSTABLE'
                        }
                    }
                }
            }
        }
        stage('Test') { // Stage for running the tests
            steps {
                script {
                    echo "Running tests..."

                    // Activate virtual environment and run the test script
                    def activateEnvCommand = "call venv\\Scripts\\activate" // Activate virtual environment
                    def runCommand = "${activateEnvCommand} && python main.py ${env.srNo} ${env.trNo}" // Execute test script

                    echo "Executing command: ${runCommand}"
                    def runResult = bat(script: runCommand, returnStatus: true)

                    // Set test result based on execution status
                    if (runResult != 0) {
                        echo "Test execution failed, exit code: ${runResult}"
                        currentBuild.result = 'FAILURE'
                    } else {
                        echo "Test execution successful"
                    }

                    echo "Test phase completed"
                }
            }
            post {
                always {
                    script {
                        echo "Generating Allure Report..."
                        try {
                            allure includeProperties: false, results: [[path: 'sft-allure-results']]
                            env.reportUrl = "${env.BUILD_URL}allure"
                        } catch (Exception e) {
                            echo "Failed to generate Allure Report: ${e.message}"
                            env.reportUrl = "Report generation failed"
                        }

                        if (fileExists("${env.WORKSPACE}/sft-allure-report/index.html")) {
                            echo "Allure Report successfully generated and accessible at: ${env.reportUrl}"
                        } else {
                            env.reportUrl = "Report not generated"
                            echo "Allure Report not found. Please check the generation process."
                        }
                    }
                }
            }

        }
    }
    post {
        always {
            script {
                def status = currentBuild.result ?: 'SUCCESS' // Default to SUCCESS if status is not set
                switch (status) {
                    case 'SUCCESS':
                        sendCallback(env.atsBuildId, "FINISHED", [
                            result: "PASS",
                            reportUrl: env.reportUrl ?: "Report not generated"
                        ])
                        break
                    case 'FAILURE':
                        sendCallback(env.atsBuildId, "ERROR", [
                            result: "FAIL",
                            reportUrl: env.reportUrl ?: "Report not generated"
                        ])
                        break
                    case 'UNSTABLE':
                        sendCallback(env.atsBuildId, "ERROR", [
                            result: "UNSTABLE",
                            reportUrl: env.reportUrl ?: "Report not generated"
                        ])
                        break
                    case 'ABORTED':
                        sendCallback(env.atsBuildId, "CANCEL", [
                            result: "ABORTED",
                            reportUrl: "Pipeline aborted, report not generated"
                        ])
                        echo "Pipeline was aborted"
                        break
                    default:
                        sendCallback(env.atsBuildId, "TRIGGER_ERROR", [
                            result: status,
                            reason: "Unknown pipeline status: ${status}"
                        ])
                        echo "Unknown pipeline status: ${status}"
                }
            }
        }
    }
}

def sendCallback(atsBuildId, status, resultData) {
    if (!atsBuildId || !env.atsCallbackUrl) {
        echo "Missing ATS callback information. atsBuildId: ${atsBuildId}, atsCallbackUrl: ${env.atsCallbackUrl}"
        return
    }

    def callbackPayload = [
        atsBuildId: atsBuildId,
        status: status,
        buildId: env.BUILD_NUMBER,
        result: groovy.json.JsonOutput.toJson(resultData)
    ]

    try {
        def response = httpRequest(
            httpMode: 'POST',
            url: env.atsCallbackUrl,
            contentType: 'APPLICATION_JSON',
            requestBody: groovy.json.JsonOutput.toJson(callbackPayload)
        )
        echo "Successfully sent ${status} status callback, response: ${response.content}"
    } catch (Exception e) {
        echo "Failed to send ${status} status callback: ${e.message}"
        currentBuild.result = 'UNSTABLE'
    }
}
