QUEUE = list()
NEXT_ACTIVATE = 0


def connect():
    """Ping all devices on the network."""
    pass


# Thread: Listen for incoming requests from clients. Add a tuple of IP, ID,
# and delay to QUEUE, and add delay to NEXT_ACTIVATE.

# Thread: If current time is before NEXT_ACTIVATE, wait until then and then
# send a request to the first IP in QUEUE with the ID.
