pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                cleanWs()
                git branch: 'dev', url: 'https://github.com/PrathamBaliyan/Hourly-Updates.git'
            }
        }

        stage('Setup Python & Playwright') {
            steps {
                sh '''
                echo "Checking if Python is installed..."
                python3 --version || exit 1
                
                echo "Creating virtual environment..."
                python3 -m venv venv
                
                echo "Activating virtual environment..."
                . $(pwd)/venv/bin/activate
                
                echo "Upgrading pip..."
                pip install --upgrade pip
                
                echo "Installing dependencies..."
                pip install playwright pytest
                
                echo "Installing Playwright browsers..."
                python -m playwright install

                echo "Installing xvfb for UI support..."
                sudo apt-get update && sudo apt-get install -y xvfb
                '''
            }
        }

        stage('Run Playwright Script') {
            steps {
                sh '''
                echo "Activating virtual environment..."
                . $(pwd)/venv/bin/activate
                
                echo "Running Playwright script with xvfb..."
                xvfb-run --auto-servernum python website.py
                '''
            }
        }
    }
}
