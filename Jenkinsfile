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
          python3 -m coverage run -m pytest
          python3 -m coverage xml -o coverage.xml
        '''
      }
    }

    stage('Publish Coverage Report') {
      steps {
        recordCoverage tools: [cobertura(pattern: 'coverage.xml')]
      }
    }

  }
}
