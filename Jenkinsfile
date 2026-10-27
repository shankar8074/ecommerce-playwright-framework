pipeline {
    // Run on any available Jenkins machine (here: your local Windows Jenkins)
    agent any

    stages {
        // Install pytest, pytest-playwright and pytest-html
        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        // Download the Chromium browser that Playwright controls
        stage('Install browser') {
            steps {
                bat 'playwright install chromium'
            }
        }

        // Run the tests with the login details from Jenkins credentials;
        // pytest.ini also writes reports/report.html, and --junitxml adds a file Jenkins can read
        stage('Run tests') {
            steps {
                withCredentials([
                    string(credentialsId: 'TEST_USER_EMAIL', variable: 'TEST_USER_EMAIL'),
                    string(credentialsId: 'TEST_USER_PASSWORD', variable: 'TEST_USER_PASSWORD')
                ]) {
                    bat 'pytest --junitxml=reports/junit.xml'
                }
            }
        }
    }

    // Runs after the stages, whether the tests passed or failed
    post {
        always {
            // Show pass/fail results and trends on the build page
            junit testResults: 'reports/junit.xml', allowEmptyResults: true

            // Add a "Playwright Report" link to the build that opens the pytest-html report
            publishHTML(target: [
                reportName: 'Playwright Report',
                reportDir: 'reports',
                reportFiles: 'report.html',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: true
            ])
        }
    }
}
