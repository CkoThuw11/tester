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

    stage('Run Tests + Coverage') {
      steps {
        sh '''
          . venv/bin/activate
          pytest --junitxml=test-results.xml
          coverage html
        '''
      }
    }

    stage('Publish Reports') {
      steps {
        // Publish JUnit
        junit 'test-results.xml'

        // Publish HTML coverage
        publishHTML(target: [
            reportDir: 'htmlcov',
            reportFiles: 'index.html',
            reportName: 'HTML Coverage Report',
            alwaysLinkToLastBuild: true,
            keepAll: true
        ])
      }
    }
  }
}
