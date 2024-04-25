pipeline {
agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        
        stage('Pull'){
            steps{
                echo "Pulling repo stage"
                git branch: 'master', credentialsId: '214186b5-9ef1-4191-8889-0ef338cffa0c', url: 'https://github.com/MonkeyWithCoconut/Game-of-Life.git'
     
            }
        }
        
        stage('Build') {
            steps {
                echo "Build stage"
                sh '''
                docker build -t game-builder:latest .
                
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Test stage"
                sh '''
                docker build -t game-builder-test:latest -f ./Dockerfile2 .
                
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploy stage"
                sh '''
                docker run --name build_container game-builder:latest
                docker logs build_container > log_build.txt

                docker run --name test_container game-builder-test:latest
                docker logs test_container > log_test.txt

                '''
            }
        }

        stage('Publish') {
            steps {
                echo "Publish stage"
                sh '''
                TIMESTAMP=$(date +%Y%m%d%H%M%S)
                tar -czf artifact_$TIMESTAMP.tar.gz log_build.txt log_test.txt 
                
                '''
            } 
        }
    }
    post{
        always{
            echo "Archiving artifacts"

            archiveArtifacts artifacts: 'artifact_*.tar.gz', fingerprint: true
            sh '''
            chmod +x clean.sh
            ./clean.sh
            '''
        }
    }
    
}
