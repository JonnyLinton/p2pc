def receiver_dispatcher(message, ip_address, port):
    command = message["command"]
    if command == "/join":
        return True
        # adds user to online list
        # send ping
        # display_notification(message["message"])
    elif command == "/who":
        # prints list of users
        return True
    elif command == "/leave":
        # display_notification(message)
        # remove user from online list
        return True
    elif command == "/quit":
        # display(message["message"])]
        # os.exit(0)
        return True
    elif command == "/ping":
        # check if user in online list
        # if not, add user to list
        return True
    else: # talk
        #display(message["message"])
        print("hello")
        return True
