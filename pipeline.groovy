pipeline {
    agent {
        node {
            label 'PDRA-agent'
            customWorkspace 'C:\\Users\\QAAPP_AT_PC2\\PycharmProjects\\AT_PDRA'
        }
    }
    stages {
        stage('Receive ATS JSON') {
            steps {
                script {
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        try {
                            if (!params.data?.trim()) {
                                error("ATS JSON 資料未提供")
                            }

                            def atsJson = readJSON text: params.data
                            env.atsBuildId = atsJson.atsInfo.atsBuildId
                            env.atsCallbackUrl = atsJson.atsInfo.atsCallbackUrl
                            env.build = atsJson.build.build
                            env.buildPath = atsJson.build.prog_path
                            env.srNo = atsJson.build.sr_no
                            env.trNo = atsJson.build.tr_no

                            if (!env.buildPath?.trim()) {
                                error("ATS JSON 缺少 buildPath")
                            }

                            echo "解析的 ATS JSON 資料："
                            echo groovy.json.JsonOutput.prettyPrint(groovy.json.JsonOutput.toJson(atsJson))

                            def callbackPayload = [
                                atsBuildId: env.atsBuildId,
                                status: "RUNNING",
                                buildId: env.BUILD_NUMBER
                            ]

                            try {
                                def response = httpRequest(
                                    httpMode: 'POST',
                                    url: env.atsCallbackUrl,
                                    contentType: 'APPLICATION_JSON',
                                    requestBody: groovy.json.JsonOutput.toJson(callbackPayload)
                                )
                                echo "初始化 RUNNING 狀態回傳結果：${response.content}"
                            } catch (Exception ex) {
                                echo "回傳 RUNNING 狀態失敗：${ex.message}"
                            }
                        } catch (Exception e) {
                            echo "接收或解析 ATS JSON 時出錯：${e.message}"
                            sendCallback(env.atsBuildId, "ERROR", [
                                result: "RECEIVE_FAILED",
                                reason: e.message
                            ])
                            throw e
                        }
                    }
                }
            }
        }
        stage('Install Build') {
            steps {
                script {
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        try {
                            if (!env.buildPath?.trim()) {
                                error("缺少 buildPath，無法安裝 APK")
                            }
                            echo "從 buildPath 安裝 APK：${env.buildPath}"

                            def installCommand = "python install_pdra.py \"${env.buildPath}\""
                            echo "執行安裝指令：${installCommand}"
                            def installResult = bat(script: installCommand, returnStatus: true)

                            if (installResult != 0) {
                                echo "安裝失敗，退出代碼：${installResult}"
                                currentBuild.result = 'UNSTABLE'
                            } else {
                                echo "安裝成功"
                            }
                        } catch (Exception e) {
                            echo "安裝過程中發生意外錯誤：${e.message}"
                            currentBuild.result = 'UNSTABLE'
                        }
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo "執行測試..."

                    // 執行測試腳本
                    def runCommand = "python main.py"
                    echo "執行指令：${runCommand}"
                    def runResult = bat(script: runCommand, returnStatus: true)

                    if (runResult != 0) {
                        echo "測試執行失敗，exit code：${runResult}"
                        currentBuild.result = 'UNSTABLE'
                    } else {
                        echo "測試執行成功"
                    }

                    echo "測試完成"
                }
            }
            post {
                always {
                    echo "生成 Allure Report..."
                    // 這裡將報告輸出到 sft-allure-report 資料夾中
                    allure includeProperties: false, jdk: '', results: [[path: 'sft-allure-results']], reportDirectory: 'sft-allure-report'

                    // 動態生成報告的路徑
                    def allureReportPath = "file://${env.WORKSPACE}/sft-allure-report/index.html"
                    env.reportUrl = allureReportPath
                    env.reportFilename = "${env.build}_Test_Report.html"
                    echo "Report 生成完畢，路徑：${env.reportUrl}"
                }
            }
        }
    }
    post {
        always {
            script {
                def status = currentBuild.result ?: 'SUCCESS' // 如果狀態未設置，預設為成功
                switch (status) {
                    case 'SUCCESS':
                        sendCallback(env.atsBuildId, "FINISHED", [
                            result: "PASS",
                            reportUrl: env.reportUrl ?: "未生成報告"
                        ])
                        break
                    case 'FAILURE':
                        sendCallback(env.atsBuildId, "ERROR", [
                            result: "FAIL",
                            reportUrl: env.reportUrl ?: "未生成報告"
                        ])
                        break
                    case 'UNSTABLE':
                        sendCallback(env.atsBuildId, "UNSTABLE", [
                            result: "UNSTABLE",
                            reportUrl: env.reportUrl ?: "未生成報告"
                        ])
                        break
                    default:
                        echo "未知狀態：${status}"
                }
            }
        }
    }
}

def sendCallback(atsBuildId, status, resultData) {
    if (!atsBuildId || !env.atsCallbackUrl) {
        echo "缺少 ATS 回傳資訊。atsBuildId: ${atsBuildId}, atsCallbackUrl: ${env.atsCallbackUrl}"
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
        echo "回傳 ${status} 狀態成功，回應內容：${response.content}"
    } catch (Exception e) {
        echo "回傳 ${status} 狀態失敗：${e.message}"
        currentBuild.result = 'UNSTABLE'
    }
}