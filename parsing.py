import re


def build_message(user_name, user_message):
    if user_message == "/leave":
        return "user: " + user_name + "\n" + "command: /leave" + "\n" + "message: left!" + "\n\n"
    else:
        return "user: " + user_name + "\n" + "command: /talk" + "\n" + "message: " + user_message + "\n\n"


def parse_message(application_message):
    dict = {}
    lines = re.split("\n+", application_message)
    message_list = [re.split(": ", entry, 2) for entry in lines]
    for elements in message_list:
        if len(elements) > 1:
            dict[elements[0]] = elements[1]
    return dict
