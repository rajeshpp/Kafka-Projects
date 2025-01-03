# consumer_auto_refresh.py
from kafka import KafkaConsumer
import json
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import threading

# Kafka Consumer Configuration
consumer = KafkaConsumer(
    'clickstream',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Initialize Counters and DataFrames
PAGE_VISITS = Counter()
PAGES = ['home', 'products', 'contact', 'about', 'cart']
VISIT_HISTORY = []

# Lock for thread-safe updates
from threading import Lock
data_lock = Lock()

def process_message(data):
    """Process each Kafka message for analytics."""
    global PAGE_VISITS, VISIT_HISTORY
    
    with data_lock:
        PAGE_VISITS[data['page']] += 1
        VISIT_HISTORY.append({
            'time': datetime.now(),
            'page': data['page'],
            'visits': dict(PAGE_VISITS)
        })

# Background thread to consume Kafka messages
def start_consumer():
    print("Starting Kafka Consumer...")
    try:
        for message in consumer:
            process_message(message.value)
    except KeyboardInterrupt:
        print("Stopped consumer.")

# Start Kafka consumer in a separate thread
consumer_thread = threading.Thread(target=start_consumer, daemon=True)
consumer_thread.start()

# Real-Time Visualization
fig, ax = plt.subplots(figsize=(12, 6))

def update_plot(frame):
    """Update plot with the latest data."""
    with data_lock:
        if len(VISIT_HISTORY) == 0:
            return  # Nothing to plot yet

        df = pd.DataFrame(VISIT_HISTORY)
        df.set_index('time', inplace=True)

        for page in PAGES:
            df[page] = df['visits'].apply(lambda x: x.get(page, 0))
        
        ax.clear()
        df[PAGES].plot(ax=ax)
        ax.set_title("Real-Time Page Visits Over Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Visits")
        ax.legend(PAGES)
        ax.grid(True)

# Use FuncAnimation for auto-refreshing the plot
ani = FuncAnimation(fig, update_plot, interval=2000)  # Refresh every 2 seconds

# Display the plot
plt.show()
