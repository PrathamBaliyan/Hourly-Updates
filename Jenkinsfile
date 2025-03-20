pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                cleanWs() // Ensures the workspace is clean before pulling new code
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
        stage('Verify Files') {
            steps {
                sh 'ls -l'  // Debugging step to check if test.py is present
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

