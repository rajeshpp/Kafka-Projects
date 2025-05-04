# kafka_producer.py
from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_data():
    return {
        "machine_id": "MACH001",
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
        "temperature": round(random.uniform(60, 100), 2),
        "vibration": round(random.uniform(0.1, 2.5), 2),
        "rpm": random.randint(1000, 3000)
    }

while True:
    data = generate_data()
    producer.send('machine-sensor-data', data)
    print("Sent:", data)
    time.sleep(2)
