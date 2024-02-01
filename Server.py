import socket
import os
from cryptography import fernet
import threading

if not os.path.exists("secret"):
    with open("secret", "w") as f:
        f.write(fernet.Fernet.generate_key().decode("ascii"))
        f.close()
    print("secret file created")


def getSecretFromFile():
    with open("secret", "r") as f:
        secret = f.read()
        f.close()
    return secret


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "0.0.0.0"
port = 9999

s.bind((host, port))
s.listen(5)

key = fernet.Fernet(getSecretFromFile())

print("Server is listening on port %s" % port)


def generate_handshake():
    handshake = key.encrypt(bytes(getSecretFromFile().encode("ascii"))).decode("ascii")
    return handshake


def check_handshake(handshake):
    try:
        if(key.decrypt(handshake.encode("ascii")).decode("ascii")) == getSecretFromFile():
            return True
        else:
            return False
    except fernet.InvalidToken as e:
        return False


def handle_client(clientsocket):
    requested = clientsocket.recv(1024).decode("ascii")
    if requested == "Hello":
        handshake = generate_handshake()
        clientsocket.send(handshake.encode("ascii"))
    elif requested == "Im Back":
        clientsocket.send("Welcome Back".encode("ascii"))
        handshake = clientsocket.recv(1024).decode("ascii")
        if check_handshake(handshake):
            clientsocket.send("Valid".encode("ascii"))
        else:
            clientsocket.send("Invalid".encode("ascii"))


while True:
    clientsocket, address = s.accept()
    threading.Thread(target=handle_client, args=(clientsocket,)).start()
