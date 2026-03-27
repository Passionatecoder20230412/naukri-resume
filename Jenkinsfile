pipeline {
    agent any

    triggers {
        cron('0 8 * * *')   // ⏰ daily 8 AM
    }

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/Passionatecoder20230412/naukri-resume.git'
            }
        }

        stage('Setup') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Test') {
            steps {
                bat '''
                venv\\Scripts\\activate
                pytest --reruns 2
                '''
            }
        }
    }
}