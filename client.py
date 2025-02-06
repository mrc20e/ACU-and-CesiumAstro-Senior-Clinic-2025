import socket
import os
import platform
import sys

s = socket.socket()

host = input("Type host name:")

port = 8080

try:
    s.connect((host,port))
except Exception as e:
    print(e)
    sys.exit()

print("Connected to Server")

command = s.recv(1024)

command = command.decode()

if command == "open":
    print("Command is : ", command)
    s.send("Command received".encode())

    if platform.system() == "Windows":
        os.system('dir')
    elif platform.system() == "Linux":
        os.system('ls')

elif command == "edit":
    print("Command is : ", command)

    if platform.system() == "Linux":
        os.system('nano testfile.xml')