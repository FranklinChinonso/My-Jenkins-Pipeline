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
        sh '''
          python3 --version || python --version
          python3 -m venv venv || python -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Test') {
      steps {
        echo "Running tests with pytest..."
        sh '''
          . venv/bin/activate
          pytest -q
        '''
      }
    }

    stage('Deploy') {
      steps {
        echo "Deployment stage (simulated)"
        sh 'echo "Deployment successful (simulated)"'
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
