pipeline {
    agent any

    stages {

        stage('Test EC2 SSH') {
            steps {
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'ec2-ssh-key',
                    keyFileVariable: 'EC2_KEY',
                    usernameVariable: 'EC2_USER'
                )]) {

                    bat '''
                        ssh -i "%EC2_KEY%" -o StrictHostKeyChecking=no %EC2_USER%@18.208.222.154 "echo EC2_CONNECTION_SUCCESS"
                    '''
                }
            }
        }
    }
}
