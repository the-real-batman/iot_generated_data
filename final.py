import json
from urllib.request import urlopen
import datetime

with urlopen("https://api.myjson.com/bins/1a4wyz") as response:
	source=response.read() #reading file from the url

data=json.loads(source)

device_dict={} # dictionary to store the deviceId and time it was active for
random_dict={} # dictionary to store intermediate values

for datas in data:
	if (datas['previousData']==0 and datas['deviceId'] not in random_dict.keys() and datas['deviceId'] not in device_dict.keys()): # for the first entry
		random_dict[datas['deviceId']]=datas['createdAt']
	if (datas['previousData']==0 and datas['deviceId'] in random_dict.keys()):
		random_dict[datas['deviceId']]=datas['createdAt']
	if (datas['previousData']==1 and datas['deviceId'] in random_dict.keys() and datas['deviceId'] not in device_dict.keys()):
		a=datetime.datetime.strptime(str(datas['createdAt']),"%Y-%m-%dT%H:%M:%S.%fZ")
		b=datetime.datetime.strptime(str(random_dict[datas['deviceId']]),"%Y-%m-%dT%H:%M:%S.%fZ")
		new_format="%H:%M:%S"
		a1=a.strftime(new_format)
		b1=b.strftime(new_format)
		tdelta=datetime.datetime.strptime(a1,new_format)-datetime.datetime.strptime(b1,new_format)
		device_dict[datas['deviceId']]=tdelta
		random_dict[datas['deviceId']]=datas['createdAt']
	if (datas['previousData']==1 and datas['deviceId'] in random_dict.keys() and datas['deviceId'] in device_dict.keys()):
		c=device_dict[datas['deviceId']]
		a=datetime.datetime.strptime(str(datas['createdAt']),"%Y-%m-%dT%H:%M:%S.%fZ")
		b=datetime.datetime.strptime(str(random_dict[datas['deviceId']]),"%Y-%m-%dT%H:%M:%S.%fZ")
		new_format="%H:%M:%S"
		a1=a.strftime(new_format)
		b1=b.strftime(new_format)
		tdelta=datetime.datetime.strptime(a1,new_format)-datetime.datetime.strptime(b1,new_format)
		device_dict[datas['deviceId']]=tdelta+c
		random_dict[datas['deviceId']]=datas['createdAt']

for keys,values in device_dict.items():
	print(keys,':',values)
