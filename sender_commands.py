# Command logic for sender

import socket

from parsing import build_message
from channels import channels
from current_channel import current_channel


def sender_dispatcher(parsed_message_dict, port):
    command = parsed_message_dict["command"]
    if command == "/leave":
        leave(parsed_message_dict, port)
    elif command == "/who":
        who(parsed_message_dict, port)
    elif command.startswith("/private"):
        private(parsed_message_dict, port)
    elif command.startswith("/channel"):
        channel(parsed_message_dict, port)
    else:
        talk(parsed_message_dict, port)


def broadcast_message(message_params, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    application_message = build_message(message_params["user"], message_params["ip"], message_params["command"], message_params["message"])
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(application_message.encode("utf-8"), (ip, port))


def broadcast_channel_message(message_params, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    application_message = build_message(message_params["user"], message_params["ip"], message_params["command"], message_params["message"])
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    #  loop through all members of the channel and send to them (can no longer broadcast)
    for (user, ip_address) in channels[current_channel[0]]:
        print("sending to: " + user + " " + ip_address)
        sock.sendto(application_message.encode("utf-8"), (ip_address, port))


def talk(message_params, port):
    broadcast_channel_message(message_params, port)


def leave(message_params, port):
    broadcast_message(message_params, "255.255.255.255", port)
    _quit(message_params["user"], port)


# name "_quit" to avoid overriding the built-in quit() function
def _quit(user_name, port):
    quit_message = {"user": user_name, "ip": get_ip_address(), "command": "/quit", "message": "Bye now!"}
    broadcast_message(quit_message, "127.0.0.1", port)


def who(message_params, port):
    broadcast_message(message_params, "127.0.0.1", port)


def join(user_name, port):
    join_message = {"user": user_name, "ip": get_ip_address(), "command": "/join", "message": "joined!"}
    broadcast_message(join_message, "255.255.255.255", port)


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return str(s.getsockname()[0])


def private(message_params, port):
    command_and_receiver_name = message_params["message"].split(" ")
    receiver_name = ""
    if len(command_and_receiver_name) > 1:
        # get receiver name
        receiver_name = command_and_receiver_name[1]
    # Now we look if this user is currently online
    search_results = [user for user in channels[current_channel[0]] if user[0] == receiver_name]
    if not search_results:
        # user is not online
        print(receiver_name + " is not currently online")
    else:
        # get user ip
        receiver_ip = search_results[0][1]
        message = input("Private message to " + receiver_name + ": ")
        private_message = {"user": message_params["user"], "ip": message_params["ip"], "command": "/private", "message": message}
        broadcast_message(private_message, receiver_ip, port)


def channel(message_params, port):
    user, ip = message_params["user"], message_params["ip"]
    command_and_channel_name = message_params["message"].split(" ")
    new_channel_name = ""
    if len(command_and_channel_name) > 1:
        new_channel_name = command_and_channel_name[1]
    #  delete the user from the old channel
    old_channel_name = current_channel[0]
    #  change the current_channel to reflect current state
    current_channel[0] = new_channel_name

    message_to_send = old_channel_name + " " + new_channel_name
    channel_change_message = {"user": user, "ip": ip, "command": "/channel", "message": message_to_send}
    broadcast_message(channel_change_message, "255.255.255.255", port)
