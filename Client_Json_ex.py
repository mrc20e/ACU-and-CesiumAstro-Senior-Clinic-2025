import socket
import numpy as np
import json 
from tabulate import tabulate
#import time

def convertData(values):
	array = np.fromstring(values.strip("[]"), sep = " ")
	return array

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

timeVal = '1 Jan 25 17:0:0.000'
dataVals = '[.98 .7e3  1000]'

dataArray = convertData(dataVals)

print("Starting UDP Host")

host = socket.gethostname()
port = 8080

keys = ["Data_Key1", "Data_Key2", "Data_Key3"]
dataList = [dataArray[0], dataArray[1], dataArray[2]]


data = [
	{"Time":timeVal, "Key":"Data_Key1", "Value":dataArray[0]},
	{"Time":timeVal, "Key":"Data_Key2", "Value":dataArray[1]},
	{"Time":timeVal, "Key":"Data_Key3", "Value":dataArray[2]}
]

jsondata = {"Time":timeVal, "Keys":keys, "Values":dataList}

json_string = json.dumps(jsondata, separators=(",",":"))

forData = ",".join([f"{entry['Time']}:{entry['Key']}:{entry['Value']}" for entry in data])
#Added this data array for the the table
#flat_data = [
	["Time:",jsondata["Time"]],
	["Keys:",jsondata["Keys"]],
	["Values:",jsondata["Values"]]
]

#forjson = json.dumps(jsondata, indent=4) #Added an indent but probably will take out

print(json_string)

#print(data)

#print(forData)

#print(forjson)

#table = tabulate(flat_data, headers=["Datalist", "Outputs"], tablefmt="pipe")

#print(table)

s.sendto(table.encode(), (host,port))
#time.sleep(.5)
s.sendto("stop".encode(), (host,port))
