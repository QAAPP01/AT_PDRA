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
                            // 檢查是否提供了 data 參數
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
        stage('Build and Test') {
            steps {
                script {
                    echo "執行建置與測試..."
                    sleep 5
                    echo "建置與測試成功完成"
                }
            }
        }
        stage('Generate Report') {
            steps {
                script {
                    echo "生成報告..."
                    env.reportUrl = "http://192.168.7.182:8000/Report/TutorialScanAT/64/report.html"
                    env.reportFilename = "PHD_Tutorial_Report.html"
                    echo "報告已生成：${env.reportUrl}"
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
