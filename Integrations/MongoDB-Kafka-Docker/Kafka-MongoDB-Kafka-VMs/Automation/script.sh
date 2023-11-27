#!/bin/bash

yum update -y
yum upgrade -y
yum install git python python-pip docker wget java -y

cd /home/ec2-user
wget https://downloads.apache.org/kafka/3.6.0/kafka_2.13-3.6.0.tgz
tar -zxvf kafka_2.13-3.6.0.tgz
wget https://github.com/mongodb/mongo-kafka/releases/download/r1.11.0/mongodb-kafka-connect-mongodb-1.11.0.zip
unzip mongodb-kafka-connect-mongodb-1.11.0.zip
rm -f mongodb-kafka-connect-mongodb-1.11.0.zip kafka_2.13-3.6.0.tgz
mv kafka_2.13-3.6.0 kafka
mv mongodb-kafka-connect-mongodb-1.11.0 connect


cat <<EOF > /etc/yum.repos.d/mongodb-org-7.0.repo
[mongodb-org-7.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2023/mongodb-org/7.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-7.0.asc
EOF

yum install -y mongodb-org
mkdir -p /data/db
service docker start
systemctl start mongod
systemctl daemon-reload
systemctl enable mongod
systemctl restart mongod
dnf erase -qy mongodb-mongosh
dnf install -qy mongodb-mongosh-shared-openssl3
yum install -y mongodb-org
systemctl restart mongod

# Bellow is some basic setup for Zookeeper, Kafka & kafka-connect
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"

# Zookeper Settings
# server.1=0.0.0.0:2888:3888
# server.2=65.0.99.246:2888:3888

# initLimit=5

# syncLimit=2