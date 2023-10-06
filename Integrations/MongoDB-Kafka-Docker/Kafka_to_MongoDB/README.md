# MongoDB Connector for Apache Kafka Tutorials

The official MongoDB Connector for Apache® Kafka® is developed and supported by MongoDB engineers and verified by Confluent. The Connector is designed to be used with Kafka Connect and enables MongoDB to be a datasource for Apache Kafka from both a source and sink perspective.

![](https://webassets.mongodb.com/_com_assets/cms/mongodbkafka-hblts5yy33.png)

These tutorials are focused on teaching you the essential features and functionality of the connector enabling you to get up and running quickly.

# Prerequisites

The MongoDB Kafka tutorial environment requires the following installed on your client:

- [Docker](https://docs.docker.com/get-docker/)
- [Git]()

The docker compose in this repository will create an environment that consists of the following:

- Apache Kafka
- Zookeeper
- Apache Kafka Connect
- MongoDB Connector for Apache Kafka (installed in Kafka Connect)
- MongoDB single node replica set

# Starting the Docker environment

Current Architecture:<br/>
<img width="453" alt="image" src="https://github.com/rajeshpp/Kafka-Projects/assets/19406666/1b6d1a28-dcfd-4ad8-8811-23836944f366">


To start the baseline tutorial environment execute the run the following command:

```
docker-compose up
```

Now, go to ```mongo1``` container:<br/>
<img width="455" alt="image" src="https://github.com/rajeshpp/Kafka-Projects/assets/19406666/87583798-0e8c-4dea-8f0a-947b90b2c5ff">

Now check the status of sink:<br/>
<img width="566" alt="image" src="https://github.com/rajeshpp/Kafka-Projects/assets/19406666/183467a5-537b-4799-bb9f-2808107422b3">

Now, run python script to send messages to kafka and then to MongoDB:<br/>
<img width="317" alt="image" src="https://github.com/rajeshpp/Kafka-Projects/assets/19406666/ba70d644-2c26-4233-bf3b-ad46aa3e0658">

Let's check in mongoDB now:<br/>
<img width="363" alt="image" src="https://github.com/rajeshpp/Kafka-Projects/assets/19406666/312e951a-760a-4327-b391-4edb92e2e4ce">



## Shutting down the Tutorial environment

To stop and remove the Docker environment from your
machine, run the following command:

```
docker-compose -p mongo-kafka down --rmi 'all'
```

## References

- [MongoDB Kafka Connector](https://docs.mongodb.com/kafka-connector/current/) online documentation.

- [Connectors to Kafka](https://docs.confluent.io/home/connect/overview.html)
- MongoDB Connector for Apache Kafka Tutorials (Link TBD)
