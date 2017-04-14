# Command logic for receiver

import os

from user_list import current_online_users
from sender_commands import broadcast_message, get_ip_address
from display import *


def receiver_dispatcher(current_user, message_params, ip_address, port):
    user, ip, command, message = message_params["user"], message_params["ip"], message_params["command"], message_params["message"]
    if command == "/join":
        ping(current_user, ip_address, port)
        display_notification(message_params)
    elif command == "/who":
        display_who()
    elif command == "/leave":
        display_notification(message_params)
        if (user, ip) in current_online_users:
            current_online_users.remove((user, ip))
    elif command == "/private":
        display_private(message_params)
    elif command == "/quit":
        print(message)
        os._exit(0)  # TODO: Find a more comprehensive solution?
    elif command == "/ping":
        if (user, ip) not in current_online_users:
            current_online_users.append((user, ip))
    else:  # /talk
        display(message_params)


def ping(user_name, ip, port):
    ping_message = {"user": user_name, "ip": get_ip_address(), "command": "/ping", "message": ""}
    broadcast_message(ping_message, ip, port)
