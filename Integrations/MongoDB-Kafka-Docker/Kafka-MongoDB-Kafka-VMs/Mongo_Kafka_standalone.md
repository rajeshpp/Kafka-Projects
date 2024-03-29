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
Our requirement here is to setup a 3 node VM cluster. So, as part of that, follow the below basis steps first.

Now download latest version of Kafka package from Apache Kafka Website. Here is the url: https://kafka.apache.org/downloads

After downloading latest zip file, unzip it and use the shell scripts from bin folder for all the kafka operations.

To setup, 3 node VM cluster, we have to do some configuration settings in both `config/server.properties` and `config/zookeeper.properties` files.

Follow the steps mentioned in these links for more help. [link1](https://www.clairvoyant.ai/blog/kafka-series-3.-creating-3-node-kafka-cluster-on-virtual-box) [link2](https://himanshu27.medium.com/kafka-cluster-setup-on-centos-server-3-nodes-a4f65775c045) [link3](https://www.conduktor.io/kafka/kafka-cluster-setup-overview/)

Now, let's start Kafka by following the steps mentioned [here](https://github.com/rajeshpp/Kafka-Projects/blob/main/Installation/readme.md)

##### In some cases, you may get Error with memory issues:
```
Java HotSpot(TM) 64-Bit Server VM warning: INFO: os::commit_memory(0x00000000c0000000, 1073741824, 0) failed; error='Not enough space' (errno=12)
# There is insufficient memory for the Java Runtime Environment to continue.
```
Set below config, in those cases:

export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"


### Install MongoDB & Test MongoDB
Now, let's install and do the setup to install mongoDB. As part of that, please follow the steps mentioned [here](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

Before starting mongoDB, we need to create a folder as `mkdir -p /data/db`.

After that, Run the command `mongod` or `systemctl start mongod`.

That will start MongoDB. To connect to that, we can either use `mongosh` to use from CLI or, use `MongoDB Compass` to use from IDE.
![image](https://github.com/rajeshpp/Kafka-Projects/assets/19406666/69aaf811-4e69-47bb-9c75-8f1184d1063b)

![image](https://github.com/rajeshpp/Kafka-Projects/assets/19406666/def2fc27-629b-4871-b441-a6a6e22fde31)

### Setup mongoDB-Kafka Connector
To enable the communication between mongoDB and Kafka, we need to make lot of programming. But, that problem is solved by using Kafka-MongoDB Connector.

Some helpful information about MongoDB-Kafka Connector [here](https://www.mongodb.com/products/integrations/kafka-connector)

Download MongoDB-Kafka Connector from [here](https://github.com/mongodb/mongo-kafka/releases)

To know more about Sink Connector, click [here](https://www.mongodb.com/docs/kafka-connector/current/sink-connector/)

To know more about Source Connector, click [here](https://www.mongodb.com/docs/kafka-connector/current/source-connector/)

Steps to be followed to use this fully:
1. 


