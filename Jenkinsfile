pipeline {
    agent any

    triggers {
        
        cron('*/2 * * * *')
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
