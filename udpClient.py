import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()

port = 8080

s.bind((host,port))

running = True

while(running):
	try:
		data, addr = s.recvfrom(1024)
		data = data.decode()

		if data != "stop":
			print(data)
		else:
			running = False
			s.close()
	except OSError as e:
		pass
