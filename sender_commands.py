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


def broadcast_message(message_params, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    application_message = build_message(message_params["user"], message_params["command"], message_params["message"])
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(application_message.encode("utf-8"), (ip, port))


def talk(message_params, ip, port):
    broadcast_message(message_params, ip, port)


def leave(message_params, ip, port):
    broadcast_message(message_params, ip, port)
    quit(message_params["user"], port)


# name "_quit" to avoid overriding the built-in quit() function
def _quit(user_name, port):
    quit_message = {"user": user_name, "command": "/quit", "message": "Bye now!"}
    broadcast_message(quit_message, "127.0.0.1", port)


def who(message_params, port):
    broadcast_message(message_params, "127.0.0.1", port)


def join(user_name, ip, port):
    join_message = {"user": user_name, "command": "/join", "message": "joined!"}
    broadcast_message(join_message, ip, port)


# Change this so that it is handled by the receiver instead
# def command_quit():
#     print("Bye now!")
#     os._exit(0)
