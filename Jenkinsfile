pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'gcc -o output run.c'
            }
        }
        stage('run') {
            steps {
                sh './output'
            }
        }
        stage('check') {
            steps {
                sh 'python3 check.py output.txt'
            }
        }
        stage('archive') {
            steps {
                archiveArtifacts "*.txt"
            }
        }
    }
}
