## MongoDB - Kafka Connect - Standalone mode
In this document, we will discuss how to setup the connection between MongoDB and Kafka using mongodb-kafka connector by making on-prem and cloud VMs as a cluster.

So, what we need for this are: 1+ on-prem VMs, 1+ Cloud VMs.

So, now let's see how this can happen in a step-by-step approach.

1. Install Java
2. Install/Setup Kafka & Test Kafka Connections
3. Install MongoDB & Test MongoDB
4. Setup mongoDB-Kafka Connector
5. Explain Source-Sink Connectors and make config changes.
6. Insert into MongoDB using connector.
7. Final testing

### Install Java
As part of this POC, I have used Ubuntu OS and here are the steps to install Java on Ubuntu: https://ubuntu.com/tutorials/install-jre#1-overview
1. Install OpenJDK JRE: `sudo apt install default-jre`
2. Install Java JDK
   - Download latest JDK deb file from here: https://www.oracle.com/java/technologies/downloads/
   - Install from deb file: `sudo dpkg -i jdk-21_linux-x64_bin.deb`
  
### Install/Setup Kafka & Test Kafka Connections
Now download latest version of Kafka package from Apache Kafka Website. Here is the url: https://kafka.apache.org/downloads

After downloading latest zip file, unzip it and use the shell scripts from bin folder for all the kafka operations.

One more configuration change that is required as part of this is the uncomment `advertised.listeners=PLAINTEXT://localhost:9092` and the set the hostname to localhost or to the IP of that specific host. This change needs to be done in `config/server.properties`.

Now, let's start Kafka by following the steps mentioned [here](https://github.com/rajeshpp/Kafka-Projects/blob/main/Installation/readme.md)

### Install MongoDB & Test MongoDB
Now, let's install and do the setup to install mongoDB. As part of that, please follow the steps mentioned [here](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

Before starting mongoDB, we need to create a folder as `mkdir -p /data/db`.

After that, Run the command `mongod` or `systemctl start mongod`.

That will start MongoDB. To connect to that, we can either use `mongosh` to use from CLI or, use `MongoDB Compass` to use from IDE.
![image](https://github.com/rajeshpp/Kafka-Projects/assets/19406666/69aaf811-4e69-47bb-9c75-8f1184d1063b)

![image](https://github.com/rajeshpp/Kafka-Projects/assets/19406666/def2fc27-629b-4871-b441-a6a6e22fde31)


