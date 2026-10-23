pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Stage 1: Checking out source code...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Stage 2: Building Kano Calculator...'
                sh 'python3 --version'
                sh 'pip install -r requirements.txt || echo "skip"'
            }
        }
        stage('Test') {
            steps {
                echo 'Stage 3: Running tests...'
                sh 'python3 main.py'
            }
        }
        stage('Package') {
            steps {
                echo 'Stage 4: Packaging...'
                sh 'tar -czf kano-calculator.tar.gz main.py'
                archiveArtifacts artifacts: '*.tar.gz', allowEmptyArchive: true
            }
        }
        stage('Deploy') {
            steps {
                echo 'Stage 5: Deploying...'
                sh 'echo "Deploy successful"'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished - check logs'
        }
        success {
            echo 'BUILD SUCCESS'
        }
        failure {
            echo 'BUILD FAILED'
        }
    }
}
