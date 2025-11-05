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
          coverage run -m pytest
          coverage xml -o coverage.xml
        '''
      }
    }

    stage('Publish Coverage Report') {
      steps {
        cobertura coberturaReportFile: 'coverage.xml'
      }
    }
  }
}
