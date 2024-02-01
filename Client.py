import socket

host = "localhost"
port = 9999

inp = input("What would you like to do? Handshake or test handshake? (h/t): ")
if inp == "h":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send("Hello".encode("ascii"))
    handshake = s.recv(1024).decode('ascii')
    print(handshake)
    s.close()
elif inp == "t":
    handshake = input("What is the handshake?\n> ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send("Im Back".encode("ascii"))
    s.recv(1024).decode('ascii')
    s.send(handshake.encode('ascii'))
    if(s.recv(1024).decode('ascii') == "Valid"):
        print("Handshake Successful / Valid")
    else:
        print("Handshake Failed / Invalid")
    s.close()
