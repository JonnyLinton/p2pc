from datetime import datetime


def display(message_params):
    user_name, message_params = message_params["user"], message_params["message"]
    current_time = datetime.now()
    print(str(current_time) + " " + "<" + user_name + ">: " + message_params)


def display_notification(message_params):
    user_name, message_params = message_params["user"], message_params["message"]
    current_time = datetime.now()
    print(str(current_time) + " " + user_name + " " + message_params)