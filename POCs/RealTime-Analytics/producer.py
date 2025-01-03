from kafka import KafkaProducer
import json
import random
import time

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

pages = ['home', 'products', 'contact', 'about', 'cart']

def generate_click():
    return {
        'user_id': random.randint(1, 100),
        'page': random.choice(pages),
        'timestamp': time.time()
    }

# Simulate streaming data
while True:
    click = generate_click()
    producer.send('clickstream', click)
    print(f"Sent: {click}")
    time.sleep(5)  # Adjust to simulate desired traffic rate
