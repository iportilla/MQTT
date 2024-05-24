# MQTT 

  MQTT was developed by Andy Stanford-Clark (IBM) and Arlen Nipper (Eurotech; now Cirrus Link) in 1999 for the monitoring of an oil pipeline through the desert. The goals were to have a protocol, which is bandwidth-efficient and uses little battery power, because the devices were connected via satellite link and this was extremely expensive at that time.
The protocol uses a publish/subscribe architecture in contrast to HTTP with its request/response paradigm. 

Publish/Subscribe is event-driven and enables messages to be pushed to clients. The central communication point is the MQTT broker, it is in charge of dispatching all messages between the senders and the rightful receivers. Each client that publishes a message to the broker, includes a topic into the message. The topic is the routing information for the broker. Each client that wants to receive messages subscribes to a certain topic and the broker delivers all messages with the matching topic to the client. Therefore the clients don’t have to know each other, they only communicate over the topic. This architecture enables highly scalable solutions without dependencies between the data producers and the data consumers.


[Architecture](./MQTT-Architecture.png)

![arc](MQTT-Architecture.png)




### Flow

In this topic, you'll follow a series of hands-on exercises that demonstrate how to use of MQTT. You'll start with the basics: creating and running your first MQTT publisher and subscriber. 



Enjoy this topic!

<h3>APPM-5360</h3>
</p>

1. login to the development virtual machine VM hosted on AWS cloud

	 `
    ssh ubuntu@XX.XXX.XXX.XXX
    `
    
    *Make sure to post your **ssh public key** to the Team channel used for this lesson
    
2. Navigate to class subdirectory

	`cd /home/ubuntu/`
3. Create & navigate to your own directory

	`mkdir userName`
	
	`cd userName`
	
	For example:
	
	`mkdir ivanp`
	
	`cd ivanp`
	
	
4. Clone Docker repository from github

	`git clone https://github.com/iportilla/MQTT.git`
	
5. Change directory to the Docker directory

	`cd MQTT/`
6. Test your `MQTT` installation by running the following command:

	`sudo systemctl status mosquitto`
	
	You will see:
	
	```script
 
        mosquitto.service - Mosquitto MQTT Broker
             Loaded: loaded (/lib/systemd/system/mosquitto.service; enabled; vendor preset: enabled)
             Active: active (running) since Fri 2024-05-24 13:44:45 UTC; 1h 20min ago
               Docs: man:mosquitto.conf(5)
                     man:mosquitto(8)
           Main PID: 6523 (mosquitto)
              Tasks: 1 (limit: 2287)
             Memory: 2.2M
                CPU: 1.695s
             CGroup: /system.slice/mosquitto.service
                     └─6523 /usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf
        
        May 24 13:44:44 ip-172-26-4-219 systemd[1]: Starting Mosquitto MQTT Broker...
        May 24 13:44:45 ip-172-26-4-219 systemd[1]: Started Mosquitto MQTT Broker.
	...
	
	```
	
### Hello World MQTT

7. Next, we are going to run a `MQTT` publisher on our system and get to know the `MQTT Subscriber` client. To get started, let's run the following in our terminal:.

	```
	python code/mqtt_time_publisher.py
	```
	You will see:
	
	```	
    Published: 2024-05-24 16:04:42
	```

	The `publisher` script will post a `topic` on the `MQTT broker` with the date and time every 5 seconds
	

8. Great! Let's now run the `MQTT client`. Open a second shell window, login back to the `ubuntu` VM, change directory to your MQTT subdirectory 

```script
	ssh ubuntu@XX.XXX.XXX.XXX
	cd <YOUR_NAME>/MQTT/
 ```
and run the following command:

 `python code/mqtt_time_subscriber.py`

9. You will see:

 ``` script
      Received message: 2024-05-24 16:06:37
      Received message: 2024-05-24 16:06:42
      Received message: 2024-05-24 16:06:47
      Received message: 2024-05-24 16:06:52
      Received message: 2024-05-24 16:06:57
      Received message: 2024-05-24 16:07:02

```
 
Congratulations!, you have master MQTT 101 topics

## Next actions:

For a more advanced lab see if you can write a code for temperature sensor using a RPi

![Temperature](./temperature.png)
