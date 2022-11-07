# Producer-Consumer-Basic

Let's Begin..........

1. [Install Kafka](https://github.com/rajeshpp/Kafka-Projects/blob/main/Installation/readme.md)
2. Sample Producer code
<pre>
import time
from kafka import KafkaProducer
import os
import json

bootstrap_servers = ['localhost:9092']
topicName = 'producer-consumer-demo'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers, retries = 5,value_serializer=lambda m: json.dumps(m).encode('ascii'))

for file in os.listdir('./data'):
    with open('data/'+file) as f:
        head = next(f).split(',')
        for line in f:
            content = dict(zip(head, line.split(',')))
            print(content)
            ack = producer.send(topicName, content)
            metadata = ack.get()
            print(metadata.topic)
            print(metadata.partition)
            time.sleep(1)
</pre>
3. Sample Consumer Code
<pre>
from kafka import KafkaConsumer
import sys


bootstrap_servers = ['localhost:9092']
topicName = 'producer-consumer-demo'
consumer = KafkaConsumer (topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
auto_offset_reset = 'earliest')

try:
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
except KeyboardInterrupt:
    sys.exit()
</pre>
