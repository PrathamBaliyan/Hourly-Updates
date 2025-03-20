pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                cleanWs() // Ensures the workspace is clean before pulling new code
                git branch: 'dev', url: 'https://github.com/PrathamBaliyan/Hourly-Updates.git'
            }
        }
        stage('Setup Playwright') {
            steps {
                sh '''
                . venv/bin/activate
                python -m playwright install
                '''
            }
        }
        stage('Run Playwright Script') {
            steps {
                sh '''
                . venv/bin/activate
                python test.py
                '''
            }
        }
    }
}
