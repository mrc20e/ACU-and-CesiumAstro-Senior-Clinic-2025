import socket
import os
import platform
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = input("Type host name:")
#host = "LAPTOP-3I9UPEM4"
host = '192.168.56.1'

port = 8080

try:
    s.connect((host,port))
except Exception as e:
    print(e)
    sys.exit()

print("Connected to Server")
print("Commands are open, edit, run, and clear")

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

elif command == "run":
    print("Command is :", command)

    os.system('python3 xml-practice.py')

elif command == "clear":
    print("Command is :", command)
    os.system('python3 clearxml.py')
