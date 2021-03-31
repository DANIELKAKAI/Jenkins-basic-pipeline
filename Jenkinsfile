pipeline {
  agent { docker { image 'python:3.6.9' } }
  stages {
    stage('build') {
      steps {
        sh 'python -m pip install -r cidr_convert_api/python/requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python cidr_convert_api/python/tests.py'
      }   
    }
  }
}