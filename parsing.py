import re

def build_message(user_name, command, message):
    return "user: " + user_name + "\n" + "command: " + command + "\n" + "message: " + message + "\n\n"

def construct_message_parameters(user_name, user_message):
    dict = {}
    dict["user"] = user_name
    if user_message == "/leave":
        dict["command"] = "/leave"
        dict["message"] = ""
    elif user_message == "/who":
        dict["command"] = "/who"
        dict["message"] = ""
    else:
        dict["command"] = "/talk"
        dict["message"] = user_message
    return dict

def parse_message(application_message):
    dict = {}
    lines = re.split("\n+", application_message)
    message_list = [re.split(": ", entry, 2) for entry in lines]
    for elements in message_list:
        if len(elements) > 1:
            dict[elements[0]] = elements[1]
    return dict
