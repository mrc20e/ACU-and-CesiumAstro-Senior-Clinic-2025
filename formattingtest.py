import socket
import numpy as np
import json

names = ["Time", "Data_Key1", "Data_Key2", "Data_Key3", "Data_Key4"]

time = np.array(["A Certain Date"])
dynVars = np.array([.98, .7e3,  1000])
soc = np.array([.899])

# print(time.tolist())
# print(dynVars.tolist())
# print(soc.tolist())

total = np.concatenate((time, dynVars, soc)).tolist() # Combines all arrays and formats them as a list
#print(total.tolist())

dictionary = dict(zip(names, total)) # Zips the names and the list into a dict

totaljson = json.dumps((dictionary), indent=4) # Converts dict into JSON
print(totaljson)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create UDP socket.
s.sendto(totaljson.encode(), ("192.168.1.130", 8080)) #IP is for my personal Raspberry Pi