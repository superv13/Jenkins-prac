pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'This is job building stage'
            }
        }
        stage('Test') {
            steps {
                echo 'This is testing stage'
            }
        }
        stage('Staging') {
            steps {
                echo 'This is staging environment'
            }
        }
        stage('Deployment') {
            steps {
                echo 'This is deployment stage'
            }
        }
        stage('Monitor') {
            steps {
                echo 'This is monitoring stage'
            }
        }
    }
}
