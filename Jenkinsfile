pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'calculator-app'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS = credentials('docker-hub-credentials')
    }
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
                sh 'python -m pytest test_main.py -v --junitxml=test-results.xml'
            }
        }
        stage('Package') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                    sh 'tar -czf calculator-app-${BUILD_NUMBER}.tar.gz *.py requirements.txt Dockerfile'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        echo "Deploying ${DOCKER_IMAGE}:${DOCKER_TAG}"
                        sh 'echo Deployment simulated - ${DOCKER_IMAGE}'
                    }
                }
            }
        }
    }
    triggers {
        pollSCM('H/5 * * * *')
    }
    post {
        always {
            junit testResults: 'test-results.xml', allowEmptyResults: true
            archiveArtifacts artifacts: '*.tar.gz', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
