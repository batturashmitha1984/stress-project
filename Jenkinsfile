pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t stress-level-app .'
            }
        }

        stage('Check Docker Image') {
            steps {
                bat 'docker images stress-level-app'
            }
        }
    }
}
