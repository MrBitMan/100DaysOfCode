import ipaddress
import os

print("Enter a network in the following format xxx.xxx.xxx.0/xx:")
network = input()
netobj = ipaddress.ip_network(network)

for i in netobj.hosts():
	print(i)

print("Enter the address you want to ping")
ping = input()
hostname = ping
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')