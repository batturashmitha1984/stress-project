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
                bat 'docker build -t batturashmitha/stress-level-app:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {

                    bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                    bat 'docker push batturashmitha/stress-level-app:latest'
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'ec2-ssh-key',
                    keyFileVariable: 'EC2_KEY',
                    usernameVariable: 'EC2_USER'
                )]) {

                    bat '''
                        icacls "%EC2_KEY%" /inheritance:r
                        icacls "%EC2_KEY%" /remove "Users"
                        icacls "%EC2_KEY%" /grant:r "SYSTEM:R"

                        ssh -i "%EC2_KEY%" -o StrictHostKeyChecking=no %EC2_USER%@18.208.222.154 "sudo docker pull batturashmitha/stress-level-app:latest"

                        ssh -i "%EC2_KEY%" -o StrictHostKeyChecking=no %EC2_USER%@18.208.222.154 "sudo docker rm -f stress-app 2>/dev/null || true"

                        ssh -i "%EC2_KEY%" -o StrictHostKeyChecking=no %EC2_USER%@18.208.222.154 "sudo docker run -d --name stress-app -p 5001:5001 batturashmitha/stress-level-app:latest"
                    '''
                }
            }
        }
    }
}