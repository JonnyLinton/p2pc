from datetime import datetime
from user_list import current_online_users


def display(message_params):
    user_name, message_params = message_params["user"], message_params["message"]
    current_time = datetime.now()
    print(str(current_time) + " " + "<" + user_name + ">: " + message_params)


def display_notification(message_params):
    user_name, message_params = message_params["user"], message_params["message"]
    current_time = datetime.now()
    print(str(current_time) + " " + user_name + " " + message_params)


def display_error(error_message):
    current_time = datetime.now()
    print(str(current_time) + " " + error_message + ".")


def display_who():
    current_time = datetime.now()
    users = []
    for user_ip_tuple in current_online_users:
        users.append(user_ip_tuple[0])
    print(str(current_time) + " Connected users: " + str(users))


def display_private(message_params):
    user_name, message_params = message_params["user"], message_params["message"]
    current_time = datetime.now()
    print(str(current_time) + " " + "[" + user_name + "] 👥 : " + message_params)
