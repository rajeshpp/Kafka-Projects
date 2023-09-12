# Splunk Kafka Integration
For integrating Splunk and Kafka, we have few prerequisites.
1. Splunk Installation
2. Kafka Setup
3. Java Installation (Optional)
4. Splunk-Kafka-connect Jar
5. Connection Establishment
6. Pushing messages

## Splunk Installation
We have 3 options here.
1. Use existing Organization wide Splunk Enterprise.
2. Install Splunk Enterprise on your local by downloading from Splunk.
3. Pull Docker image and run a container from it.
   <img width="794" alt="image" src="https://github.com/rajeshpp/Kafka-Projects/assets/19406666/1c4fc6d0-d22e-4b22-a1fd-7a3cba3b7d7d">

## Kafka Setup
Please follow [these](https://github.com/rajeshpp/Kafka-Projects/blob/main/Installation/readme.md) steps for setting up Kafka.

## Java Installation
This is an optional step. Please download jdk8 and install it as it may be required for Splunk-Kafka connect.

## Splunk-Kafka Connect
We need a jar file which helps us to establish the connection between Splunk and Kafka. For that purpose, we have to follow the steps mentioned at this [link](https://github.com/splunk/kafka-connect-splunk).
Doing all these steps is a time consuming process or it may fail in between due to some other issues. Easy way is to download the jar file from this [link](https://github.com/splunk/kafka-connect-splunk/releases).

<img width="213" alt="image" src="https://github.com/rajeshpp/Kafka-Projects/assets/19406666/27c1b04f-177a-476f-bdef-ca25837a969d">

## Connection Establishment
Next step is the establishment of connection between Splunk and Kafka by using kafka-connect-splunk. Follow [these](https://github.com/splunk/kafka-connect-splunk#quick-start) steps for establishing the connection.
By using below command, created connector tasks
```
curl http://localhost:8083/connectors -X POST -H "Content-Type: application/json" -d '{
    "name": "kafka-connect-splunk",
    "config": {
        "connector.class": "com.splunk.kafka.connect.SplunkSinkConnector",
        "tasks.max": "3",
        "splunk.indexes": "splunk_kafka_index",
        "topics": "Splunk-Kafka-Topic",
      "splunk.hec.uri": "http://localhost:8088",
      "splunk.hec.token": "$TOKEN"
    }
}'
```
**Response**:
```
{"name":"kafka-connect-splunk","config":{"connector.class":"com.splunk.kafka.connect.SplunkSinkConnector","tasks.max":"3","splunk.indexes":"splunk_kafka_index","topics":"Splunk-Kafka-Topic","splunk.hec.uri":"http://localhost:8088","splunk.hec.token":"13d77f44-fa5e-4567-be89-8855ce11e618","name":"kafka-connect-splunk"},"tasks":[],"type":"sink"}
```

## Pushing messages
Now, let's push messages to the Splunk by using Splunk-Kafka Connect.
```
export TOKEN="13d77f44-fa5e-4567-be89-8855ce11e618"

curl http://localhost:8088/services/collector/event -H "Authorization: Splunk $TOKEN" -d '{"event": { "stuff": "value" } }'
=====================
{"text":"Success","code":0}
=============================

curl http://localhost:8088/services/collector/event -H "Authorization: Splunk $TOKEN" -d '{"event": "Hello World!!"}
```
