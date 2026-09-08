pipeline {
    agent any

    stages {

        stage('Test EC2 SSH') {
            steps {
                sshagent(['ec2-ssh-key']) {
                    bat '''
                        ssh -o StrictHostKeyChecking=no ubuntu@18.208.222.154 "echo EC2_CONNECTION_SUCCESS"
                    '''
                }
            }
        }
    }
}
