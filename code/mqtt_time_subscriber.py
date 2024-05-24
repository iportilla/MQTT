import paho.mqtt.client as mqtt

# Define the broker address and port
broker_address = "localhost"  # Use "localhost" if running on the same machine
broker_port = 1883

# Define the topic
topic = "date/time"

# Callback function to handle messages
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode('utf-8')}")

# Create an MQTT client instance
#client = mqtt.Client("TimeSubscriber")
client = mqtt.Client(client_id="TimeSubscriber", callback_api_version=2)

# Attach the callback function to the client
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, broker_port)

# Subscribe to the topic
client.subscribe(topic)

# Start the client loop
client.loop_forever()