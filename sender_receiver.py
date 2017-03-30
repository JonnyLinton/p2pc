import os
import socket

from display import display, display_notif
from parsing import build_message, parse_message


def sender(user_name, ip_address, port):
    # join should go somewhere here
    while True:
        user_message = input()
        message_with_command = build_message(user_name, user_message)
        parsed_message = parse_message(message_with_command)
        command = parsed_message["command"]
        # if command is "/join":
        #     return True
        if command == "/leave":
            leave(user_name, ip_address, port)
            # not working right now...
        else:
            talk(user_name, parsed_message["message"], ip_address, port)

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

def broadcast_message(user_name, message, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    application_message = build_message(user_name, message)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(application_message.encode("utf-8"), (ip, port))

def talk(user_name, message, ip, port):
    broadcast_message(user_name, message, ip, port)

def leave(user_name, ip, port):
    broadcast_message(user_name, "/leave", ip, port)
    os._exit(0)