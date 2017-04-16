import re
from current_channel import current_channel
from channels import channels

def build_message(user_name, ip, channel, command, message):
    return "user: " + user_name + "\n" + "ip: " + ip + "\n" + "channel: " + channel + "\n" + "command: " + command + "\n" + "message: " + message + "\n\n"


def construct_message_parameters(user_name, user_message):
    from sender_commands import get_ip_address
    message_params = {"user": user_name, "ip": get_ip_address(), "channel": current_channel[0]}
    if user_message == "/leave":
        message_params["command"] = "/leave"
        message_params["message"] = "left!"
    elif user_message == "/who":
        message_params["command"] = "/who"
        message_params["message"] = ""
    elif user_message.startswith("/private"):
        message_params["command"] = "/private"
        message_params["message"] = user_message
    elif user_message.startswith("/channel"):
        message_params["command"] = "/channel"
        message_params["message"] = user_message
    else:
        message_params["command"] = "/talk"
        message_params["message"] = user_message
    return message_params


def parse_message(application_message):
    message_params = {}
    lines = re.split("\n+", application_message)
    message_list = [re.split(": ", entry, 2) for entry in lines]
    for elements in message_list:
        if len(elements) > 1:
            message_params[elements[0]] = elements[1]
    return message_params

def is_unique(user_name):
    for name, ip in channels[current_channel[0]]:
        if user_name == name:
            return False
    return True


def make_user_name_unique(user_name, unique_id = 0):
    if is_unique(user_name):
        return user_name
    else:
        unique_id = unique_id + 1
        new_user_name = user_name
        if "-" in new_user_name:
            new_user_name = user_name.split("-")[0]
        new_user_name = new_user_name + "-" + str(unique_id)
        return make_user_name_unique(new_user_name, unique_id)
