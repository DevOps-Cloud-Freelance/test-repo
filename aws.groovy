pipeline {
    agent any
    parameters {
        choice(
            name: 'AWS_EC2_TYPE',
            choices: ['Small', 'Medium','Large'],
            description: ''
        )
    }
    stages {
        stage('git clone') {
            steps {
              //git branch: 'master', credentialsId: 'sainath_git',url: "https://github.com/DevOps-Cloud-Freelance/Terraform.git" 
              //sh "ls -ll"
            }
        }
        stage('terraform plan') {
            steps {
                script {
					println params.AWS_EC2_TYPE
                    sh "export TF_LOGS=trace"
                   // sh "terraform init && terraform plan -var 'type=${params.AWS_EC2_TYPE}' -no-color" 
                }
            }
        }
        
        stage('terraform apply') {
            steps {
				script {
					def instance_type =""
					if(params.AWS_EC2_TYPE == "Small"){
						instance_type = "t2.micro"
					}
					else if (params.AWS_EC2_TYPE == "Medium"){
						instance_type = "t2.medium"
					}
					else {
						instance_type = "t2.large"
					}
					
				  sh '''
					terraform apply -var 'type=instance_type' -no-color --auto-approve"
					'''
					}
            }
        }
        
        stage('ansible playbook') {
            steps {
                sh "ls -ll && pwd"
                
              sh "ansible-playbook ansible.yml -vvvvv"
            }
        }
    }
}
