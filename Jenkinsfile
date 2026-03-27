pipeline {
    agent any

    triggers {
        cron('0 8 * * *')
    }

    stages {

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
