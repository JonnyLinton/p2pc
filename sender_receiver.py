import socket
from parsing import build_message, parse_message
from display import display

def sender(user_name, ip_address, port):
    while True:
        user_message = input()
        message_with_command = build_message(user_name, user_message)
        parsed_message = parse_message(message_with_command)
        command  = parsed_message["command"]
        if command is "/join":
            return True
        elif command is "/leave":
            return True
        else:
            talk(user_name, parsed_message["message"], ip_address, port)

def receiver(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", port))
    while True:
        application_message = sock.recv(1024)
        message = application_message.decode("utf-8")
        dict = parse_message(message)
        display(dict["user"], dict["message"])

def broadcast_message(user_name, command, message, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    application_message = build_message(user_name, message)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(application_message.encode("utf-8"), (ip, port))

def talk(user_name, message, ip, port):
    broadcast_message(user_name, "TALK", message, ip, port)
