pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                cleanWs()  // Clears workspace before cloning
                git branch: 'dev', url: 'https://github.com/PrathamBaliyan/Hourly-Updates.git'  // Use 'dev' branch
            }
        }

        stage('Setup Python & Playwright') {
            steps {
                sh '''
                echo "Checking if Python is installed..."
                python3 --version || exit 1  # Ensure Python is available
                
                echo "Creating virtual environment..."
                python3 -m venv venv  # Create virtual environment
                
                echo "Checking if venv exists..."
                ls -l  # Debugging step to verify venv exists
                
                echo "Activating virtual environment..."
                source $(pwd)/venv/bin/activate  # Use absolute path
                
                echo "Upgrading pip..."
                pip install --upgrade pip
                
                echo "Installing dependencies..."
                pip install playwright pytest
                
                echo "Installing Playwright browsers..."
                python -m playwright install
                '''
            }
        }

        stage('Verify Files') {
            steps {
                sh '''
                echo "Checking workspace files..."
                ls -l
                
                echo "Checking if test.py exists..."
                if [ ! -f "test.py" ]; then
                    echo "ERROR: test.py not found!"
                    exit 1
                fi
                '''
            }
        }

        stage('Run Playwright Script') {
            steps {
                sh '''
                echo "Activating virtual environment..."
                source $(pwd)/venv/bin/activate
                
                echo "Running Playwright script..."
                python test.py
                '''
            }
        }
    }
}
