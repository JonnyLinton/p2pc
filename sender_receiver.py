import os
import socket
from display import display, display_notif
from parsing import build_message, parse_message
from commands import dispatcher


def sender(user_name, ip_address, port):
    # join should go somewhere here
    while True:
        user_message = input()
        parsed_message = parse_message(build_message(user_name, user_message))
        dispatcher(parsed_message, ip_address, port)
        # command = parsed_message["command"]
        # # if command is "/join":
        # #     return True
        # if command == "/leave":
        #     leave(user_name, ip_address, port)
        # else:
        #     talk(user_name, parsed_message["message"], ip_address, port)

def receiver(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", port))
    while True:
        application_message = sock.recv(1024)
        message = application_message.decode("utf-8")
        parsed_message = parse_message(message)
        if parsed_message["message"] == "left!":
            display_notif(parsed_message["user"], parsed_message["message"])
        else:
            display(parsed_message["user"], parsed_message["message"])
