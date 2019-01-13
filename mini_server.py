import socket
import time
import datetime


def wfile(fl,s):
	try:
		f = open(fl,'a+')
		f.write(s+"\n")
	except:
		f = open(fl,'w')
	f.close
	
def listen():
	ipserver   = '192.168.56.1'
	portserver = 6777

	skt = socket.socket()
	# untuk mengatasi Error : socket.error: [Errno 98] Address already in use
	skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	skt.bind((ipserver, portserver))

	skt.listen(1)
	sambung, alamat = skt.accept()

	while 1:	
		isi = sambung.recv(1024)
		if not isi:
			break
		#	for timestamp ----------
		tm = time.time()
		tmnow = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y_%H-%M-%S')	
		#	end for timestamp --------	
		isix = ' => %s : %s' % (tmnow,isi.lower())	
		
		wfile('listen_6677.py',isi.lower())
		print isix
	sambung.close()	

print "Starting Mini_Server..."	
while 1:
#	time.sleep(0.1)
	try:
		listen()	
	except Exception as e: 
		print(e)
