pipeline {
  agent { docker { image 'python:3.6.9' } }
  stages {
    stage('build') {
      steps {
         withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'pip install --user -r cidr_convert_api/python/requirements.txt'
         }
      }
    }
    stage('test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'python cidr_convert_api/python/tests.py'
        }
      }
    }
  }
}