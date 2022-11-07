# Producer-Consumer-Basic

Let's Begin..........

1. [Install Kafka](https://github.com/rajeshpp/Kafka-Projects/blob/main/Installation/readme.md)
2. Sample `ecommerce_data.csv` file content
<pre>
date,product_id,city_id,orders
2019-12-16,1897,26,2
2019-12-16,4850,26,4
2019-12-16,2466,26,1
2019-12-16,637,26,1
2019-12-16,3497,26,184
</pre>
3. Sample Producer code
<pre>
import time
from kafka import KafkaProducer
import os
import json

bootstrap_servers = ['localhost:9092']
topicName = 'producer-consumer-demo'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers, retries = 5,value_serializer=lambda m: json.dumps(m).encode('ascii'))

with open('ecommerce_data.csv') as f:
    head = [val.strip('\n') for val in next(f).split(',')]
    for line in f:
        content = dict(zip(head, [val.strip('\n') for val in line.split(',')]))
        print(content)
        ack = producer.send(topicName, content)
        metadata = ack.get()
        time.sleep(2)
</pre>
4. Sample Consumer Code
<pre>
from kafka import KafkaConsumer
import sys
import json

bootstrap_servers = ['localhost:9092']
topicName = 'producer-consumer-demo'
consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers, auto_offset_reset = 'latest')

try:
    for message in consumer:
        msg = json.loads(message.value)
        print(msg)
        print(msg['date'], msg['product_id'], msg['city_id'], msg['orders'])
except KeyboardInterrupt:
    sys.exit()
</pre>
