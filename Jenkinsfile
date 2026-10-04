pipeline {
  agent any
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Test') { steps { sh 'python -m pip install -r ai-engine/requirements.txt -r remediation-engine/requirements.txt pytest && PYTHONPATH=. pytest -q' } }
    stage('Build') {
      parallel {
        stage('Demo Image') { steps { sh 'docker build -t self-healing/demo-service:ci app/demo-service' } }
        stage('AI Image') { steps { sh 'docker build -t self-healing/ai-engine:ci ai-engine' } }
        stage('Remediation Image') { steps { sh 'docker build -t self-healing/remediation-engine:ci remediation-engine' } }
      }
    }
    stage('Security Scan') { steps { sh 'trivy fs --severity HIGH,CRITICAL --exit-code 0 .' } }
  }
}
