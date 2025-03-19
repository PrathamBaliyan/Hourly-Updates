pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/PrathamBaliyan/Hourly-Updates.git'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'echo "Running Tests..."'
                sh 'pytest website.py'  // Modify based on your Playwright script
            }
        }
    }
}
