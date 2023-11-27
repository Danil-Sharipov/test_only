pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                git 'https://github.com/Danil-Sharipov/test_only.git'
                sh'''
                    mkdir -p worker_data
                    mkdir -p notebook
                    docker compose up -d
                '''
            }
        }
        stage('test'){
            steps{
                sh '''
                    echo "test"
                    pip install docker
                    python3 test/test1.py
                    
                '''
            }
        }
        stage('deploy'){
            steps{
                sh 'echo "delivery in telegram bot"'
            }
        }
    }
}
