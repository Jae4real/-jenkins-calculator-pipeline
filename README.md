# Jenkins Calculator Pipeline - CI/CD Project

## Overview
Automated CI/CD pipeline for Python calculator using Jenkins declarative pipeline.

## Jenkins Setup
- Installed Jenkins on Ubuntu EC2 / local (port 8080)
- Initial admin password from /var/jenkins_home/secrets/initialAdminPassword
- Installed suggested plugins + Docker, Git, Pipeline, JUnit

## Plugins Used
- Git Plugin
- Pipeline Plugin
- JUnit Plugin
- Docker Pipeline

## Pipeline Stages
1. Checkout: Uses checkout scm to pull latest code from GitHub
2. Build: Installs dependencies via pip install -r requirements.txt
3. Test: Executes tests with python -m pytest test_main.py -v
4. Package: Builds Docker image and creates tar.gz artifact
5. Deploy: Simulates deployment

## Trigger Configuration
- SCM Polling: H/5 * * * * (every 5 mins)
- Webhook: GitHub webhook to http://<jenkins-url>/github-webhook/ for instant trigger

## Credentials & Security
- Docker Hub credentials stored as docker-hub-credentials in Jenkins > Manage Jenkins > Credentials
- Used via credentials('docker-hub-credentials') - no hardcoded secrets
- GitHub token stored securely

## Artifact Management
- archiveArtifacts saves *.tar.gz
- junit publishes test results
- post actions handle success/failure/always

## Docker Integration
- Dockerfile builds python:3.9-slim image
- Package stage builds and tags image with BUILD_NUMBER

## How to Run Locally
pip install -r requirements.txt
python -m pytest test_main.py -v

## Evidence
Jenkins Blue Ocean shows all 5 stages green: Checkout, Build, Test, Package, Deploy. Console log shows pytest 4 passed.
