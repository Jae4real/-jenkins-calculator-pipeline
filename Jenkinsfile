pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest test_main.py -v'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Build and test successful - ready for deployment'
            }
        }
    }
    post {
        always {
            echo 'Pipeline execution completed'
        }
    }
}
