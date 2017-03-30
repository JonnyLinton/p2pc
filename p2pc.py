import threading
from sender_receiver import sender, receiver
BROADCAST_IP = "255.255.255.255"
PORT = 8080

# if __name__ == "__main__":

def run():
    user_name = input("Enter your name: ")
    threading.Thread(target=sender, args=(user_name, BROADCAST_IP, PORT)).start()
    threading.Thread(target=receiver, args=(PORT,)).start()