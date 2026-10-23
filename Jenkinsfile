pipeline {
  agent any
stages {
  stage ('Build') {
    steps {
      echo 'Biulding kano calculator ...'
    }
  }
  stage ('test') {
    steps {
      sh 'python3 main.py'
    }
  }
}
}
