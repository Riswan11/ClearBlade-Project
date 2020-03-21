from clearblade.ClearBladeCore import System
import time
import random

# System credentials
SystemKey = "9abbd2970baabf8aa6d2a9abcc47"
SystemSecret = "9ABBD2970BA6AABFE6E8AEB8B14F"

mySystem = System(SystemKey, SystemSecret)

# Log in as Riswan
Riswan = mySystem.User("riswan@clearblade.com", "Ghana2020")

# Use Riswan to access a messaging client
mqtt = mySystem.Messaging(Riswan)


# Set up callback functions
def on_connect(client, userdata, flags, rc):
    # When we connect to the broker, subscribe to the CPU Usage topic
    client.subscribe("ComputerCPU-USAGE")


def on_message(client, userdata, message):
    # When we receive a message, print it out and store it in a collection of dictionary
    print("Received message '" + message.payload + "' on topic '" + message.topic + "'")


# Connect callbacks to client
mqtt.on_connect = on_connect
mqtt.on_message = on_message

# Connect and wait for messages
mqtt.connect()
while (True):
    time.sleep(1)  # wait for messages

