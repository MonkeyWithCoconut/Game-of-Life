pipeline {
agent any

        environment{
            DOCKERHUB_CREDENTIALS = credentials('docker')
    }

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
                docker run --name build_container game-builder:latest
                docker cp build_container:/Game-of-Life/dist ./artifacts
                docker logs build_container > log_build.txt

                '''
            }
        }

        stage('Test') {
            steps {
                echo "Test stage"
                sh '''
                docker build -t game-builder-test:latest -f ./Dockerfile2 .
                docker run --name test_container game-builder-test:latest
                docker logs test_container > log_test.txt
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploy stage"
                sh '''
                docker build -t gameoflife-deploy:latest -f ./Dockerfile3 .
                docker run --rm -d --name deploy_container gameoflife-deploy:latest
                

                '''
            }
        }

        stage('Publish') {
            steps {
                echo "Publish stage"
                sh '''
                TIMESTAMP=$(date +%Y%m%d%H%M%S)
                tar -czf artifact_$TIMESTAMP.tar.gz log_build.txt log_test.txt artifacts

                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                docker gameoflife-deploy:latest kamildziewa/gameoflife:latest
                docker kamildziewa/gameoflife:latest
                docker logout
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
