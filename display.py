from datetime import datetime

def display(user_name, user_message):
    current_time = datetime.now()
    print(str(current_time) + " " + user_name + ": " + user_message)
