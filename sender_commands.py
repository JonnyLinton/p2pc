# Command logic for sender

import socket

from parsing import build_message
from user_list import current_online_users


def sender_dispatcher(parsed_message_dict, ip_address, port):
    command = parsed_message_dict["command"]
    if command == "/leave":
        leave(parsed_message_dict, ip_address, port)
    elif command == "/who":
        who(parsed_message_dict, port)
    elif command.startswith("/private"):
        private(parsed_message_dict, port)
    else:
        talk(parsed_message_dict, ip_address, port)


def broadcast_message(message_params, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    application_message = build_message(message_params["user"], message_params["ip"], message_params["command"], message_params["message"])
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(application_message.encode("utf-8"), (ip, port))


def talk(message_params, ip, port):
    broadcast_message(message_params, ip, port)


def leave(message_params, ip, port):
    broadcast_message(message_params, ip, port)
    _quit(message_params["user"], port)


# name "_quit" to avoid overriding the built-in quit() function
def _quit(user_name, port):
    quit_message = {"user": user_name, "ip": get_ip_address(), "command": "/quit", "message": "Bye now!"}
    broadcast_message(quit_message, "127.0.0.1", port)


def who(message_params, port):
    broadcast_message(message_params, "127.0.0.1", port)


def join(user_name, ip, port):
    join_message = {"user": user_name, "ip": get_ip_address(), "command": "/join", "message": "joined!"}
    broadcast_message(join_message, ip, port)


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return str(s.getsockname()[0])


def private(message_params, port):
    command_and_receiver_name = message_params["message"].split(" ")
    receiver_name = ""
    receiver_ip = ""
    if len(command_and_receiver_name) > 1:
        # get receiver name
        receiver_name = command_and_receiver_name[1]
    # Now we look if this user is currently online
    search_results = [user for user in current_online_users if user[0] == receiver_name]
    if not search_results:
        # user is not online
        print(receiver_name + " is not currently online")
    else:
        # get user ip
        receiver_ip = search_results[0][1]
        message = input("Private message to " + receiver_name + ": ")
        private_message = {"user": message_params["user"], "ip": message_params["ip"], "command": "/private", "message": message}
        print(private_message)
        broadcast_message(private_message, receiver_ip, port)
