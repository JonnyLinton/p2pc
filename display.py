from datetime import datetime

from commands import command_quit


def display(parsed_message):
    user_name, command, message = parsed_message["user"], parsed_message["command"], parsed_message["message"]
    current_time = datetime.now()

    if command == "/quit":
        command_quit()
    elif command in ["/leave", "/join"]:
        print(str(current_time) + " " + user_name + " " + message)
    else:
        print(str(current_time) + " " + "<" + user_name + ">: " + message)
