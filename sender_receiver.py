import os
import socket
import threading
import time
from display import display
from parsing import build_message, parse_message
from commands import dispatcher, join
from semaphore import s


def sender(user_name, ip_address, port):
    s.acquire()
    join(user_name, ip_address, port)
    while True:
        user_message = input()
        parsed_message = parse_message(build_message(user_name, user_message))
        dispatcher(parsed_message, ip_address, port)

def receiver(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", port))
    s.release()
    while True:
        application_message = sock.recv(1024)
        message = application_message.decode("utf-8")
        parsed_message = parse_message(message)
        display(parsed_message["user"], parsed_message["message"])
