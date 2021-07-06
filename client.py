from icmplib import multiping
from nslookup import Nslookup
import requests
import socket
import json
import pickle
import time



def monitor(site, ip_mon, ip_acp):
	ips = [ip_mon, site, ip_acp]
	ping_response  = multiping(ips)
	pingstatus = []
#Ping test
	for n in range(3):
		if ping_response[n].is_alive:
			pingstatus.append (({ping_response[n].address},'  active'))
		else:
			pingstatus.append(({ping_response[n].address},'  error'))
#Dns test
	dns_query = Nslookup(['8.8.8.8'])
	ips_record = dns_query.dns_lookup(site)
	if ips_record.response_full != []:
		dns =  'DNS OK'
	else:
		dns =  'DNS FALHA'
#web service test
	try:
		http = requests.get('http://' + site)
	except:
		http =  'erro'

	return pingstatus, dns, http

config = 'config/config.txt'

with open(config, 'r') as file:
	config_list = file.readlines()
for index in range(len(config_list)):
	config_list[index] = config_list[index].rstrip('\n')
	
host = config_list[0]
port = int(config_list[1])
ip_mon = config_list[2]
site = config_list[3]
ip_acp = config_list[4]
print(site)

while True:
	pingstatus, dns, http = monitor(site, ip_mon, ip_acp)
	if http != 'erro':
		http_status = http.status_code
	else:
		http_status = http
	monitoring = { "ping": pingstatus, "http": http_status, "dns":dns }
	s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	b = pickle.dumps(monitoring)
	s.sendall(bytes(b))
	print (monitoring)
	time.sleep(5)
	


