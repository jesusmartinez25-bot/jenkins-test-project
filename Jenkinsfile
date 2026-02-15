pipeline {
    agent any
    
    stages {
        stage('Construcción') {
            steps {
                echo 'Preparando el proyecto...'
                sh 'python3 --version'
                sh 'ls -la'
            }
        }
        
        stage('Pruebas') {
            steps {
                echo 'Ejecutando tests...'
                sh 'python3 test_app.py'
            }
        }
        
        stage('Despliegue') {
            steps {
                echo 'Simulando despliegue a staging...'
                sh '''
                    echo "Desplegando aplicación..."
                    python3 app.py
                    echo "Despliegue completado!"
                '''
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline completado con éxito!'
        }
        failure {
            echo '❌ Pipeline falló. Revisa los logs.'
        }
    }
}
