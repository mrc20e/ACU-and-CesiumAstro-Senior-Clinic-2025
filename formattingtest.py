import socket
import numpy as np
import json

time = np.array(["A Certain Date"])
dynVars = np.array([.98, .7e3,  1000])
soc = np.array([.899])

print(time.tolist())
print(dynVars.tolist())
print(soc.tolist())

total = np.concatenate((dynVars, soc))
#print(total.tolist())

totaljson = json.dumps(total.tolist())
#print(totaljson)

dict = {"Time":time.tolist()[0], "Keys":["Data_Key1", "Data_Key2", "Data_Key3", "Data_Key4"], "Values":total.tolist()}
#print(dict)

jsondata = json.dumps(dict, indent=4)
#print(jsondata)

dict2 = {"Time":time.tolist()[0], "Key1":total.tolist()[0], "Key2":total.tolist()[1], "Key3":total.tolist()[2], "Key4":total.tolist()[3]}
#print(dict2)

jsondata2 = json.dumps(dict2, indent=4)
#print(jsondata2)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(jsondata.encode(), (socket.gethostname(), 8080))
s.sendto(jsondata2.encode(), (socket.gethostname(), 8080))
s.sendto("stop".encode(), (socket.gethostname(), 8080))