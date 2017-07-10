"""Listen for thermostat signals and send the IP, ID, and delay to the server.
Also listen for server response and activate the thermostat."""

from gpiozero import OutputDevice
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import TCPServer

RELAY = OutputDevice(17)


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


# RELAY.on() activate relay


# Thread: Listen for signal from thermostat. When received, use the function
# below and pass it the ID and IP.

# Function: Check JSON config file for delay using ID and IP.

# Function: send ID, IP, and delay to the server.

# Thread: Listen for activate command from server. When received, open relay.
