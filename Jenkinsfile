pipeline {
  agent { docker { image 'python:3.6.9' } }
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r cidr_convert_api/python/requirements.txt --user'
      }
    }
    stage('test') {
      steps {
        sh 'python cidr_convert_api/python/tests.py'
      }   
    }
  }
}