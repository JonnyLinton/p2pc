# command logic for receiver

from user_list import current_online_users
from sender_commands import broadcast_message
from display import *


def receiver_dispatcher(message_params, ip_address, port):
    user, command, message = message_params["user"], message_params["command"], message_params["message"]
    if command == "/join":
        current_online_users.append(user)
        ping(user, ip_address, port)
        display_notification(message_params)
    elif command == "/who":
        # print list of users
        print(current_online_users)
    elif command == "/leave":
        # display_notification(message_params)
        # remove user from online list
        return True
    elif command == "/quit":
        # display(message_params)
        # os.exit(0)
        return True
    elif command == "/ping":
        # check if user in online list
        # if not, add user to list
        return True
    else:  # /talk
        # display(message_params)
        return True


def ping(user_name, ip, port):
    ping_message = {"user": user_name, "command": "/ping", "message": ""}
    broadcast_message(ping_message, ip, port)