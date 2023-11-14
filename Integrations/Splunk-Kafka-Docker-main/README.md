This is a docker compose stack that implements an example of Kafka Connect
routing traffic to Splunk.  

In order to use it, the Splunk connector must be downloaded and extracted into the `connectors/` directory.  

Additionally, the connector image will come up, but you will need to manually add the connector, examples are in `kafka-connect/create-sink-example.sh`.

## How to use
1. Clone this Repo
2. Change directory into this folder. `cd Splunk-Kafka-Docker`
3. Run command: `docker-compose up`
4. On Splunk, create index, token
5. On other terminal, go to `cd Splunk-Kafka-Docker/kafka-connect`
6. Update values from Step 4 in Step 5.
7. Now, run `bash create-sink-example.sh`

Few useful images:

<img width="594" alt="image" src="https://github.com/rajeshpp/Splunk-Kafka-Docker/assets/19406666/c1007f72-dfa3-427f-9896-6c9195aa9345">

<img width="595" alt="image" src="https://github.com/rajeshpp/Splunk-Kafka-Docker/assets/19406666/e02ea1e1-3c9e-4bfd-b9a8-fc8162619278">

<img width="600" alt="image" src="https://github.com/rajeshpp/Splunk-Kafka-Docker/assets/19406666/00ca26fd-dc5f-48d2-bbbc-94f0ce97bcb2">

<img width="820" alt="image" src="https://github.com/rajeshpp/Splunk-Kafka-Docker/assets/19406666/29dbd761-6444-40b3-a062-97f71ae818d1">


