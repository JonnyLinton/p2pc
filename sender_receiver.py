import socket
from parsing import build_message, parse_message

def sender(user_name, ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        user_message = input()
        application_message = build_message(user_message, user_name)
        sock.sendto(application_message, ip_address, port)

def receiver(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind("", port)
    while True:
        application_message = sock.recv(1024)
        (user_name, user_message) = parse_message(application_message)
        print(user_name, user_message)
