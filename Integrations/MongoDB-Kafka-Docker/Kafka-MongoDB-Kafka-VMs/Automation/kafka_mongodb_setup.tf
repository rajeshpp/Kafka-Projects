terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "ap-south-1"
  profile = "Rajesh"
}

resource "aws_instance" "vms_setup" {
  ami           = "ami-02a2af70a66af6dfb"
  associate_public_ip_address = "true"
  key_name      = "firstVM-Mumbai"
  security_groups = ["sg-0e1688c8f506f83a9"]
  subnet_id     = "subnet-0bc416255ba3f29e6"
  instance_type = "t2.micro"
  count = "2"

  connection {
    type = "ssh"
    user = "ec2-user"
    private_key = file(".\\firstVM-Mumbai.pem")
    host = self.public_ip
  }

  provisioner "file" {
    source      = "script.sh"
    destination = "/tmp/script.sh"
  }

  provisioner "remote-exec" {
    inline = [ 
      "sudo chmod +x /tmp/script.sh",
      "sudo bash /tmp/script.sh ${count.index} ${self.public_ip}"
     ]
  }

  tags = {
    Name = "Kafka${count.index}"
  }
}

output "ec2_global_ips" {
  value = aws_instance.vms_setup.*.public_ip
}