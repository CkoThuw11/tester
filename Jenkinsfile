pipeline {
    agent any

    stages {
        stage ('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=results.xml'
            }
        }

        stage('Publish Results') {
            steps {
                junit 'result.xml'
            }
        }
    }
}
