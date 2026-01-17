pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Setting up Python virtual environment...'
                bat '''
                python --version
                python -m venv %VENV%
                %VENV%\\Scripts\\pip install --upgrade pip
                %VENV%\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat '''
                %VENV%\\Scripts\\pytest
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build and Tests completed successfully!'
        }
        failure {
            echo '❌ Build or Tests failed!'
        }
    }
}
