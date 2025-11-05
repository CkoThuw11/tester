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

          # Run tests with pytest-cov plugin
          pytest --cov=. --cov-report xml:coverage.xml --cov-report term
        '''
      }
    }

    stage('Publish Coverage Report') {
      steps {
        recordCoverage tools: [python(pattern: 'coverage.xml')]
      }
    }
  }
}
