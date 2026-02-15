Started by user Jesús Martínez Montalvo
Obtained Jenkinsfile from git https://github.com/jesusmartinez25-bot/jenkins-test-project.git
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/lib/jenkins/workspace/calculator-pipeline
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
using credential github-credentials
Cloning the remote Git repository
Cloning repository https://github.com/jesusmartinez25-bot/jenkins-test-project.git
 > git init /var/lib/jenkins/workspace/calculator-pipeline # timeout=10
Fetching upstream changes from https://github.com/jesusmartinez25-bot/jenkins-test-project.git
 > git --version # timeout=10
 > git --version # 'git version 2.43.0'
using GIT_ASKPASS to set credentials Token GitHub Personal
 > git fetch --tags --force --progress -- https://github.com/jesusmartinez25-bot/jenkins-test-project.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git config remote.origin.url https://github.com/jesusmartinez25-bot/jenkins-test-project.git # timeout=10
 > git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
Avoid second fetch
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision e6610439cb881abfe69990132a14f9f1121505f5 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f e6610439cb881abfe69990132a14f9f1121505f5 # timeout=10
Commit message: "Create Jenkinsfile"
First time build. Skipping changelog.
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Construcción)
[Pipeline] echo
Preparando el proyecto...
[Pipeline] sh
+ python3 --version
Python 3.12.3
[Pipeline] sh
+ ls -la
total 28
drwxr-xr-x 3 jenkins jenkins 4096 Feb 15 22:01 .
drwxr-xr-x 4 jenkins jenkins 4096 Feb 15 22:01 ..
drwxr-xr-x 8 jenkins jenkins 4096 Feb 15 22:01 .git
-rw-r--r-- 1 jenkins jenkins  920 Feb 15 22:01 Jenkinsfile
-rw-r--r-- 1 jenkins jenkins   55 Feb 15 22:01 README.md
-rw-r--r-- 1 jenkins jenkins 1257 Feb 15 22:01 app.py
-rw-r--r-- 1 jenkins jenkins 1149 Feb 15 22:01 test_app.py
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Pruebas)
[Pipeline] echo
Ejecutando tests...
[Pipeline] sh
+ python3 test_app.py
Ejecutando tests...

✓ test_add pasado
✓ test_subtract pasado
✓ test_multiply pasado
✓ test_divide pasado
✓ test_history pasado

✅ Todos los tests pasaron!
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Despliegue)
[Pipeline] echo
Simulando despliegue a staging...
[Pipeline] sh
+ echo Desplegando aplicación...
Desplegando aplicación...
+ python3 app.py
=== Calculadora Simple ===

Operaciones:
10 + 5 = 15
20 - 8 = 12
6 × 7 = 42
100 ÷ 4 = 25.0
10 ÷ 0 = Error: División por cero

Historial de operaciones:
  - 10 + 5 = 15
  - 20 - 8 = 12
  - 6 × 7 = 42
  - 100 ÷ 4 = 25.0
+ echo Despliegue completado!
Despliegue completado!
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] echo
✅ Pipeline completado con éxito!
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
