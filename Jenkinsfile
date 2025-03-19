pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'dev', url: 'https://github.com/PrathamBaliyan/Hourly-Updates.git'
            }
        }
        stage('Setup Environment') {
            steps {
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install pytest'
                sh 'pip3 install playwright'  // ✅ Install Playwright
                sh 'playwright install'       // ✅ Install required browsers
            }
        }
        stage('Run Tests') {
            steps {
                sh 'echo "Running Tests..."'
                sh 'python3 website.py'  
            }
        }
    }
}
