import socket
from parsing import build_message, parse_message
from display import display

def sender(user_name, ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        user_message = input()
        application_message = build_message(user_message, user_name)
        sock.sendto(application_message.encode("utf-8"), (ip_address, port))

def receiver(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", port))
    while True:
        application_message = sock.recv(1024)
        message = application_message.decode("utf-8")
        (user_name, user_message) = parse_message(message)
        display(user_name, user_message)
