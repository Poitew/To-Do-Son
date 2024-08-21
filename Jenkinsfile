pipeline {
    agent any
    stages {
        stage('Build and Testing') {
            steps {
                echo 'Building the application...'
                sh 'python3 functions_menu.py'
                echo 'Application built'
                echo 'Testing the application...'
            }
        }
        
        stage('Docker Building') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t to-do-son .'
                echo 'Image built'
            }
        }
    }
    post {
        success {
            echo 'Test passed!'
        }
        failure {
            echo 'Test not passed!'
        }
    }
}
