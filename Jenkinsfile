pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source..."
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Setting up Python venv and installing dependencies..."
                bat '''
                    python --version
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Running tests with pytest..."
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest -q
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Deployment stage (simulated)"
                bat 'echo Deployment successful (simulated)'
            }
        }
    }

    post {
        always {
            echo "Pipeline finished. Cleaning up workspace..."
            cleanWs()
        }
    }
}
