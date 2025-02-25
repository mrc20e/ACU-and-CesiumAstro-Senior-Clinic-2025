import socket
import numpy as np
import json 
#import time

def convertData(values):
	array = np.fromstring(values.strip("[]"), sep = " ")
	return array

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

timeVal = '1 Jan 25 17:0:0.000'
dataVals = '[.98 .7e3  1000]'

dataArray = convertData(dataVals)

host = socket.gethostname()
port = 8080



data = [
	{"Time":timeVal, "Key":"Data_Key1", "Value":dataArray[0]},
	{"Time":timeVal, "Key":"Data_Key2", "Value":dataArray[1]},
	{"Time":timeVal, "Key":"Data_Key3", "Value":dataArray[2]}
]

forData = "\n".join([f"{entry['Time']}:{entry['Key']}:{entry['Value']}" for entry in data])


print(data)

print(forData)

s.sendto(forData.encode(), (host,port))
#time.sleep(.5)
s.sendto("stop".encode(), (host,port))
