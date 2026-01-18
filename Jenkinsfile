pipeline {
    agent any

    environment {
        VENV = "venv"
        PYTHON_PATH = "C:\\Users\\Deva\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    parameters {
        string(name: 'NUMBER1', defaultValue: '0', description: 'First number')
        string(name: 'NUMBER2', defaultValue: '0', description: 'Second number')
        choice(name: 'OPERATION', choices: ['add', 'subtract', 'multiply', 'divide'], description: 'Operation')
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
                bat """
                ${PYTHON_PATH} -m venv %VENV%
                %VENV%\\Scripts\\python -m pip install --upgrade pip
                %VENV%\\Scripts\\pip install -r requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat """
                %VENV%\\Scripts\\pytest
                """
            }
        }

        stage('Run Calculator') {
            steps {
                echo 'Running calculator with input parameters...'
                bat """
                set NUMBER1=%NUMBER1%
                set NUMBER2=%NUMBER2%
                set OPERATION=%OPERATION%
                %VENV%\\Scripts\\python run_calculator.py
                """
            }
        }
        
    }

    post {
        success {
            echo '✅ Build, Tests, and Calculator run completed successfully!'
        }
        failure {
            echo '❌ Something failed!'
        }
    }
}
