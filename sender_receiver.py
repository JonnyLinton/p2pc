from parsing import *
from receiver_commands import receiver_dispatcher
from semaphore import s
from sender_commands import *


def sender(user_name, port):
    s.acquire()
    join(user_name, port)
    while True:
        user_message = input()
        message_dict = construct_message_parameters(user_name, user_message)
        sender_dispatcher(message_dict, port)


def receiver(current_user, ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", port))
    s.release()
    while True:
        application_message = sock.recv(1024)
        message = application_message.decode("utf-8")
        parsed_message = parse_message(message)
        receiver_dispatcher(current_user, parsed_message, ip_address, port)
