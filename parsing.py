import re


def build_message(user_name, ip, command, message):
    return "user: " + user_name + "\n" + "ip: " + ip + "\n" + "command: " + command + "\n" + "message: " + message + "\n\n"


def construct_message_parameters(user_name, user_message):
    from sender_commands import get_ip_address
    message_params = {"user": user_name, "ip": get_ip_address()}
    if user_message == "/leave":
        message_params["command"] = "LEAVE"
        message_params["message"] = "left!"
    elif user_message == "/who":
        message_params["command"] = "WHO"
        message_params["message"] = ""
    elif user_message.startswith("/private"):
        message_params["command"] = "PRIVATE-TALK"
        message_params["message"] = user_message
    else:
        message_params["command"] = "TALK"
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
