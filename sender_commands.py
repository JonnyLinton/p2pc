# Command logic for sender

import socket
import os
from parsing import build_message


def sender_dispatcher(parsed_message_dict, ip_address, port):
    user_name, command, message = parsed_message_dict["user"], parsed_message_dict["command"], parsed_message_dict[
        "message"]
    if command == "/leave":
        leave(parsed_message_dict, ip_address, port)
    elif command == "/who":
        who(parsed_message_dict, port)
    else:
        talk(parsed_message_dict, ip_address, port)


def broadcast_message(message, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    application_message = build_message(message["user"], message["command"], message["message"])
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(application_message.encode("utf-8"), (ip, port))

def talk(message, ip, port):
    broadcast_message(message, ip, port)

def leave(message, ip, port):
    broadcast_message(message, ip, port)
    quit(message["user"], port)

def quit(user_name, port):
    dict = {}
    dict["user"] = user_name
    dict["command"] = "/quit"
    dict["message"] = "Bye now!"
    broadcast_message(dict, "127.0.0.1", port)

def who(message, port):
    broadcast_message(message, "127.0.0.1", port)

def join(user_name, ip, port):
    dict = {}
    dict["user"] = user_name
    dict["command"] = "/join"
    dict["message"] = "joined!"
    broadcast_message(dict, ip, port)

# Change this so that it is handled by the receiver instead
def command_quit():
    print("Bye now!")
    os._exit(0)
