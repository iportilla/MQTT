import paho.mqtt.client as mqtt
import time
from datetime import datetime

# Define the broker address and port
broker_address = "localhost"  
# Use "localhost" if running on the same machine
broker_port = 1883

# Create an MQTT client instance
client = mqtt.Client(client_id="TimePublisher", callback_api_version=2)

# Connect to the broker
client.connect(broker_address, broker_port)

# Function to publish date and time
def publish_time():
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client.publish("date/time", current_time)
        print(f"Published: {current_time}")
        time.sleep(5)  # Publish every 5 seconds

# Start publishing
publish_time()