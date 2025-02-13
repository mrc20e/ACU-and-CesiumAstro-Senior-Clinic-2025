import socket
#import time
#import sys
#import os

s = socket.socket()

#host = socket.gethostname()
host = "192.168.1.130" # This is the ip address for my raspberry pi at my house - Matson

print(host,'\n')

port = 8080

s.bind((host, port))

s.listen()

conn, addr = s.accept()

print(addr, " is connected to server")

command = input(str("Enter Command : "))

conn.send(command.encode())

print("Command Sent")

data = conn.recv(1024)

if data:
    print("Command Received")
