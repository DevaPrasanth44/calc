pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\Deva\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                bat '''
                "%PYTHON%" --version
                '''
            }
        }

        stage('Build') {
            steps {
                bat '''
                "%PYTHON%" -m venv %VENV%
                %VENV%\\Scripts\\python -m pip install --upgrade pip
                %VENV%\\Scripts\\pip install pytest
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                %VENV%\\Scripts\\pytest tests
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
