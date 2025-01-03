from kafka import KafkaConsumer
import json
from collections import Counter
import time

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'clickstream',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Track page visits
page_visits = Counter()

print("Listening for messages...")
for message in consumer:
    data = message.value
    page_visits[data['page']] += 1
    time.sleep(5)
    print(f"Page Visits: {page_visits}")
