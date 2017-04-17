# Command logic for receiver

import os

from channels import channels
from current_channel import current_channel
from sender_commands import broadcast_message, get_ip_address
from display import *


def receiver_dispatcher(current_user, message_params, ip_address, port):
    user, ip, channel, command, message = message_params["user"], message_params["ip"], message_params["channel"], message_params["command"], message_params["message"]
    if command == "JOIN":
        ping(current_user, ip_address, port)
        if (user, ip) not in channels[channel]:
            channels[channel].append((user, ip))
        if (user, ip) in channels[current_channel[0]]:
            display_notification(message_params)
    elif command == "WHO":
        display_who()
    elif command == "LEAVE":
        if (user, ip) in channels[current_channel[0]]:
            display_notification(message_params)
        # remove the user from the channel they are in
        if (user, ip) in channels[channel]:
            channels[channel].remove((user, ip))
    elif command == "PRIVATE-TALK":
        display_private(message_params)
    elif command == "CHANNEL":
        #  change the channel of the user
        old_channel = message
        channels[old_channel].remove((user, ip))
        if channel not in channels:
            channels[channel] = []
        channels[channel].append((user, ip))
        if user == current_user:
            display_channel_change(channel)
    elif command == "QUIT":
        print(message)
        os._exit(0)  # TODO: Find a more comprehensive solution?
    elif command == "PING":
        # add the user to the channel they are in
        if channel not in channels:
            channels[channel] = []
        if (user, ip) not in channels[channel]:
            channels[channel].append((user, ip))
    else:  # /talk
        display(message_params)


def ping(user_name, ip, port):
    ping_message = {"user": user_name, "ip": get_ip_address(), "channel": current_channel[0], "command": "PING", "message": ""}
    broadcast_message(ping_message, ip, port)
