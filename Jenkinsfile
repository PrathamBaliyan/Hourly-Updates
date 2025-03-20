pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/PrathamBaliyan/Hourly-Updates.git'
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
                python test_playwright.py
                '''
            }
        }
    }
}

