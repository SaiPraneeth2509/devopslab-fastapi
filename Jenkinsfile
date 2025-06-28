pipeline {
    agent any

    environment {
        IMAGE_NAME = "fastapi-devopslab"
        CONTAINER_NAME = "devopslab_app"
        APP_PORT = "8000"
    }

    stages {
        stage('Install Requirements for Testing') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt || true'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (fileExists('tests')) {
                        sh 'pytest || echo "Tests failed, continuing..."'
                    } else {
                        echo "No tests directory found, skipping tests."
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    sh "docker rm -f $CONTAINER_NAME || true"
                }
            }
        }

        stage('Run New Container') {
            steps {
                sh "docker run -d --name $CONTAINER_NAME -p $APP_PORT:$APP_PORT $IMAGE_NAME"
            }
        }
    }
}
