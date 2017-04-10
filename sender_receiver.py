import socket

from sender_commands import *
from receiver_commands import receiver_dispatcher
from display import display
from parsing import *
from semaphore import s
from user_list import current_online_users

def sender(user_name, ip_address, port):
    s.acquire()
    join(user_name, ip_address, port)
    while True:
        user_message = input()
        message_dict = construct_message_parameters(user_name, user_message)
        sender_dispatcher(message_dict, ip_address, port)


def receiver(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", port))
    s.release()
    while True:
        application_message = sock.recv(1024)
        message = application_message.decode("utf-8")
        parsed_message = parse_message(message)
        receiver_dispatcher(parsed_message, ip_address, port)
        # display(parsed_message)
