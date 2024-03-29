# Kafka Installation Steps

Let's Begin........
 - <b>Step 1:</b>Download latest version from [here](https://kafka.apache.org/downloads)</br>
    <pre>
    (venv) rajesh@rajesh:~/Rajesh/Softwares$ <b>wget https://downloads.apache.org/kafka/3.3.1/kafka_2.13-3.3.1.tgz</b>
    --2022-11-05 10:55:35--  https://downloads.apache.org/kafka/3.3.1/kafka_2.13-3.3.1.tgz
    Resolving downloads.apache.org (downloads.apache.org)... 135.181.214.104, 88.99.95.219, 2a01:4f9:3a:2c57::2, ...
    Connecting to downloads.apache.org (downloads.apache.org)|135.181.214.104|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 105053134 (100M) [application/x-gzip]
    Saving to: ‘kafka_2.13-3.3.1.tgz’

    kafka_2.13-3.3.1.tgz                  100%[=======================================================================>] 100.19M  5.33MB/s    in 28s     

    2022-11-05 10:56:04 (3.54 MB/s) - ‘kafka_2.13-3.3.1.tgz’ saved [105053134/105053134]

    (venv) rajesh@rajesh:~/Rajesh/Softwares$ <b>ls -tlrh</b>
    total 101M
    -rw-rw-r-- 1 rajesh rajesh 101M Oct  3 04:35 <b>kafka_2.13-3.3.1.tgz</b>
    </pre>

- <b>Step 2:</b>Unzip the downloaded `tgz` file
  <pre>
  (venv) rajesh@rajesh:~/Rajesh/Softwares$ <b>tar -xzf kafka_2.13-3.3.1.tgz</b>
  (venv) rajesh@rajesh:~/Rajesh/Softwares$ <b>ls -ltr|grep kafka</b>
  drwxr-xr-x 7 rajesh rajesh      4096 Sep 30 00:36 kafka_2.13-3.3.1
  -rw-rw-r-- 1 rajesh rajesh 105053134 Oct  3 04:35 kafka_2.13-3.3.1.tgz
  (venv) rajesh@rajesh:~/Rajesh/Softwares$ <b>cd kafka_2.13-3.3.1/</b>
  </pre>

- <b>Step 3:</b>Start Kafka with ZooKeeper</br>
  - Start the ZooKeeper service</br>
  <pre>
  (venv) rajesh@rajesh:~/Rajesh/Softwares/kafka_2.13-3.3.1$ <b>bin/zookeeper-server-start.sh config/zookeeper.properties</b>
  ...............
  [2022-11-05 11:11:19,291] INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)
  </pre>
  - Start the Kafka broker service</br>
  <pre>
  rajesh@rajesh:~/Rajesh/Softwares/kafka_2.13-3.3.1$ <b>bin/kafka-server-start.sh config/server.properties</b>
  ................
  [2022-11-05 11:15:24,764] INFO Initiating client connection, connectString=localhost:2181 sessionTimeout=18000 watcher=kafka.zookeeper.ZooKeeperClient$ZooKeeperClientWatcher$@495ee280 (org.apache.zookeeper.ZooKeeper)
  ................
  [2022-11-05 11:15:24,795] INFO Socket connection established, initiating session, client: /127.0.0.1:43696, server: localhost/127.0.0.1:2181 (org.apache.zookeeper.ClientCnxn)
  [2022-11-05 11:15:24,980] INFO Session establishment complete on server localhost/127.0.0.1:2181, session id = 0x100036fac160000, negotiated timeout = 18000 (org.apache.zookeeper.ClientCnxn)
  .................
  [2022-11-05 11:15:27,503] INFO Awaiting socket connections on 0.0.0.0:9092. (kafka.network.DataPlaneAcceptor)
  ................
  [2022-11-05 11:15:28,722] INFO [BrokerToControllerChannelManager broker=0 name=forwarding]: Recorded new controller, from now on will use broker rajesh:9092 (id: 0 rack: null) (kafka.server.BrokerToControllerRequestThread)
  </pre>
  
- <b>Step 4:</b>List the topics
  <pre>
  rajesh@rajesh:~/Rajesh/Softwares/kafka_2.13-3.3.1$ <b>bin/kafka-topics.sh --list --bootstrap-server localhost:9092</b>
  </pre>
  
- <b>Step 5:</b>Create Topic to Store Events
  <pre>
  rajesh@rajesh:~/Rajesh/Softwares/kafka_2.13-3.3.1$ <b>bin/kafka-topics.sh --create --topic producer-consumer-demo --bootstrap-server localhost:9092</b>
  <i>Created topic producer-consumer-demo.</i>
  rajesh@rajesh:~/Rajesh/Softwares/kafka_2.13-3.3.1$ <b>bin/kafka-topics.sh --list --bootstrap-server localhost:9092</b>
  <i>producer-consumer-demo</i>
  </pre>  
  
- <b>Step 6:</b>Write Some events into the Topic
        Each line you enter will result in a separate event being written to the topic.
  <pre>
  rajesh@rajesh:~/Rajesh/Softwares/kafka_2.13-3.3.1$ <b>bin/kafka-console-producer.sh --topic producer-consumer-demo --bootstrap-server localhost:9092</b>
  Hello
  </pre>
  
- <b>Step 7:</b>Read the events from the Topic
  <pre>
  rajesh@rajesh:~/Rajesh/Softwares/kafka_2.13-3.3.1$ <b>bin/kafka-console-consumer.sh --topic producer-consumer-demo --from-beginning --bootstrap-server localhost:9092</b>
  Hello
  </pre>

- <b>Step 8:</b>Get the number of messages in a topic
  <pre>
  rajesh@rajesh:~/Rajesh/Softwares/kafka_2.13-3.3.1$ <b>bin/kafka-run-class.sh kafka.tools.GetOffsetShell --topic producer-consumer-demo --bootstrap-server localhost:9092| awk -F  ":" '{sum += $3} END {print sum}'</b>
  234
  </pre>
