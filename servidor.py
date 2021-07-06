
import socket
import pickle
import time
'''
config = 'config/config_server.txt'

with open(config, 'r') as file:
	config_list = file.readlines()
for index in range(len(config_list)):
	config_list[index] = config_list[index].rstrip('\n')
host = config_list[0]
port = int(config_list[1])
'''
host = input('Digite o ip: ')
port = input('Digite a porta: ')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,int(port)))
s.listen()
print('Aguardando conexao')
conn, ender = s.accept()
print('conectado em', ender)
html = '/var/www/html/index.html'
data = []
data_list = []

with open(html, 'w') as file:
	file.write('<head\n')
	file.write('''<title> Monitoramento de rede </title>\n''')
	file.write('</head>\n')
	file.write('<body>\n')

while True:
	conn, ender = s.accept()
	while True:
		m = conn.recv(1024)
		if m == b'':
			break
		data.append(m)
		data_r = pickle.loads(b''.join(data))
		
	with open(html, 'a') as file:
		file.write('<p>'+ time.strftime('%Y-%m-%d %H:%M:%S'))
		file.write('\n'+ str(data_r))
	print(data_r)
	data = []
