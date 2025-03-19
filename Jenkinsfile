pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git branch:'dev', url:'https://github.com/PrathamBaliyan/Hourly-Updates.git'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'echo "Running Tests..."'
                sh 'python3 website.py'  // Modify based on your Playwright script
            }
        }
    }
}
