# Jenkins Calculator Pipeline - CI/CD Project

## Overview
Automated CI/CD pipeline for Python calculator using Jenkins declarative pipeline with Docker integration.

## Jenkins Setup
- Installed Jenkins on Ubuntu EC2 / local server on port 8080
- Initial admin password from /var/jenkins_home/secrets/initialAdminPassword
- Installed suggested plugins plus Docker, Git, Pipeline, JUnit

## Plugins Used
- Git Plugin: For SCM checkout
- Pipeline Plugin: For Jenkinsfile support
- JUnit Plugin: To publish test results
- Docker Pipeline Plugin: For Docker build

## Pipeline Stages
1. **Checkout**: Uses `checkout scm` to pull latest code from GitHub
2. **Build**: Installs dependencies via `pip install -r requirements.txt`
3. **Test**: Runs tests with `python -m pytest test_main.py -v --junitxml=test-results.xml`
4. **Package**: Builds Docker image `docker build -t calculator-app:${BUILD_NUMBER}` and creates tar.gz artifact
5. **Deploy**: Simulates deployment with echo

## Build and Test Configuration
- Build stage installs requirements.txt
- Test stage runs pytest and generates JUnit XML
- All 4 calculator tests (add, subtract, multiply, divide) pass

## Trigger Configuration
- SCM Polling: `H/5 * * * *` (polls GitHub every 5 mins)
- GitHub Webhook: Configured to http://<jenkins-url>/github-webhook/ for instant trigger on push to main branch

## Credentials & Security
- Docker Hub credentials stored as `docker-hub-credentials` in Jenkins Credentials Manager
- Referenced in pipeline via `credentials('docker-hub-credentials')` - no hardcoded secrets
- GitHub Personal Access Token stored securely in Jenkins
- Environment variables used for DOCKER_IMAGE and BUILD_NUMBER

## Artifact Management
- `archiveArtifacts artifacts: '*.tar.gz'` saves build artifacts
- `junit testResults: 'test-results.xml'` publishes test results
- post block handles always, success, failure

## Docker Integration
- Dockerfile uses python:3.9-slim base
- WORKDIR /app, copies requirements, installs, copies code
- Package stage builds image with BUILD_NUMBER tag

## How to Run Locally
