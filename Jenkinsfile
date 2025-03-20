pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'dev', url: 'https://github.com/PrathamBaliyan/Hourly-Updates.git'
            }
        }

        stage('Run Playwright Script') {
            steps {
                sh '''
                source venv/bin/activate
                python test_playwright.py
                '''
            }
        }
    }
}

