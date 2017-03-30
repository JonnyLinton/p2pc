import socket
import os
from parsing import build_message


def dispatcher(parsed_message_dict, ip_address, port):
    user_name, command, message = parsed_message_dict["user"], parsed_message_dict["command"], parsed_message_dict["message"]
    if command == "/leave":
        leave(user_name, ip_address, port)
    elif command == "/who":
        return True
    else:
        talk(user_name, message, ip_address, port)

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
def join(user_name, ip, port):
    broadcast_message(user_name, "/join", ip, port)