import threading
from sender_receiver import sender, receiver

def run():
    user_name = input("Enter your name: ")
    port = 8080
    ip = "127.0.0.1"
    threading.Thread(target=sender, args=(user_name, ip, port)).start()
    threading.Thread(target=receiver, args=(port,)).start()
