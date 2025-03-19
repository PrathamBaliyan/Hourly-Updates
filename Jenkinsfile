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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate  # Use "." instead of "source"
                    pip install --upgrade pip
                    pip install -r requirements.txt || pip install playwright
                    playwright install
                '''
            }
        }


        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    python website.py
                '''
            }
        }
    }
}
