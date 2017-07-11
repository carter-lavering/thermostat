"""Listen for thermostat signals and send the IP, ID, and delay to the server.
Also listen for server response and activate the thermostat."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import TCPServer
from threading import Thread
from time import sleep

from requests import get

from gpiozero import OutputDevice

with open("config.json", "r") as config_file:
    CONFIG = json.load(config_file)

RELAY = OutputDevice(17)


def listen_for_signal():
    """Continuously listen for a thermostat signal. When received, send IP,
    ID, and delay to the server."""

    while True:
        # listening code goes here
        sleep(1)
        signal_received = 0  # becomes ID of AC system when received
        if signal_received:
            get(
                CONFIG['server'],
                payload={
                    'IP': CONFIG['address'],
                    'ID': signal_received,
                    'delay': CONFIG['units'][str(signal_received)]['delay']
                })


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


# RELAY.on() activate relay

# Import JSON config file as a dictionary for future reference by ID and IP.

# Thread: Listen for signal from thermostat. When received, use the function
# below and pass it the ID and IP.

# Function: send ID, IP, and delay to the server.

# Thread: Listen for activate command from server. When received, open relay.
