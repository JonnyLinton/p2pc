from datetime import datetime

def display(user_name, user_message):
    current_time = datetime.now()
    if user_message in ["/leave", "/join"]:
        print(str(current_time) + " " + user_name + " " + notif_message)
    else:
        print(str(current_time) + " " + "<" + user_name + ">: " + user_message)
