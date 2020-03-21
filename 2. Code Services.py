from clearblade.ClearBladeCore import System
import random
import time

# System credentials
SystemKey = "9abbd2970baabf8aa6d2a9abcc47"
SystemSecret = "9ABBD2970BA6AABFE6E8AEB8B14F"

mySystem = System(SystemKey, SystemSecret)

# Log in as Riswan
Riswan = mySystem.User("Riswanclearblade.com", "Ghana2020")

# Use Riswan to access a messaging client
mqtt = mySystem.Messaging(Riswan)

# Connect
mqtt.connect()
def on_connect(client, userdata, flags, rc):
    # When we connect to the broker, subscribe to the CPU Usage topic
    client.subscribe("ComputerCPU-USAGE")

    # When we connect to the broker, start publishing our data to the Analytcis topic
    for i in range(20):
        if i % 2 == 0:
            payload = "Current"
        else:
            payload = "Statistics"
        client.publish("Analytics", payload)
        time.sleep(1)

mqtt.disconnect()