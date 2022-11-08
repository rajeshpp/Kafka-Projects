# Producer-Consumer-Basic

Let's Begin..........

1. [Install Kafka](https://github.com/rajeshpp/Kafka-Projects/blob/main/Installation/readme.md)
2. Sample `ecommerce_data.csv` file content. [Original File](https://www.kaggle.com/datasets/jyesawtellrickson/ecommerce-bookings-data/download)
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
        #time.sleep(2)
</pre>
4. Install [mysql](https://dev.mysql.com/downloads/)
5. Create DB, and required Table
<pre>
CREATE DATABASE Kafka;
use Kafka;
CREATE TABLE orders(date VARCHAR(20), product_id INTEGER(20), city_id INTEGER(20), orders INTEGER(20));
</pre>
6. Sample Consumer Code
<pre>
from kafka import KafkaConsumer
import sys
import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="XXXXXXXX",
  database="Kafka"
)

mycursor = mydb.cursor()

bootstrap_servers = ['localhost:9092']
topicName = 'producer-consumer-demo'
consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers, auto_offset_reset = 'latest')

try:
    for message in consumer:
        msg = json.loads(message.value)
        sql = "INSERT INTO orders(date, product_id, city_id, orders) VALUES (%s, %s, %s, %s)"
        val = (msg['date'], int(msg['product_id']), int(msg['city_id']), int(msg['orders']))
        print(val)
        
        mycursor.execute(sql, val)
        mydb.commit()
    # disconnecting from server
    mydb.close()
except KeyboardInterrupt:
    # disconnecting from server
    mydb.close()
    sys.exit()
</pre>
7. Data inserted into Table after producer and consumer execution
<img width="299" alt="image" src="https://user-images.githubusercontent.com/19406666/200472866-57178297-807a-4841-b85c-bfadf060a210.png">
