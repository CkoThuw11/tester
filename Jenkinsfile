pipeline {
  agent any

  stages {
    stage('Install Dependencies') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run Tests with Coverage') {
      steps {
        sh '''
          . venv/bin/activate
          pytest --junitxml=test-results.xml
          coverage run -m pytest
          coverage xml -o coverage.xml
          coverage html
        '''
      }
    }

    stage('Publish Test Report') {
      steps {
        junit 'test-results.xml'
      }
    }

    stage('Publish Coverage HTML') {
      steps {
        publishHTML (target: [
          reportDir: 'htmlcov',
          reportFiles: 'index.html',
          reportName: 'Coverage Report',
          keepAll: true,
          alwaysLinkToLastBuild: true,
          allowMissing: false
        ])
      }
    }
  }
}
