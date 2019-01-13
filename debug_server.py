import socket
from termcolor import cprint
import os
from os.path import expanduser, getmtime
import datetime
import time
import sys

#==============
#import os
#from os.path import getmtime
#==========

home = expanduser("~")
bdir = home+'/.bdir'
ldir = bdir+'/malog'
log_file, disi = '', ''


def cflog():
	global log_file
	tm = time.time()
	d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y_%H-%M-%S')
	log_file = ldir+'/DBG_'+d1+'.log' #log_file = "python_tcpserver.LOG"

def data2log(madir):	
	if not os.path.exists(madir):
		os.makedirs(madir)


def write_2log(fl,s):
	try:
		f = open(fl,'a+')
		f.write(s+"\n")
	except:
		f = open(fl,'w')
		f.close

data2log(ldir)

print "FileName \t: "+log_file
print "Home \t\t: "+home
print "Log DIR \t: "+ldir

print "Starting Debug Server..."

def colordata(data):

#	data = 'DBG. %s %s' % (tmnow, data)
#	print data
#	data = data.strip('\n')	

	if "CreateProcess" in data and "Failed!" not in data:
		cprint (data,'cyan')
	elif "Failed!" in data:
		cprint (data,'red')
#	elif "FileW" in data:
#		cprint (data,'cyan')
	elif "Key" in data:
		cprint (data,'magenta')
#	elif "I-Opening" in data:
#		cprint (data,'magenta')	
	elif "******" in data:
		cprint (data,'yellow')	
	else:
		cprint (data,'white')
#	write_2log(log_file,data)
	
def startlisten():
	global disi
	ipserver   = '192.168.56.1'
	portserver = 6677

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
		if "Connection From Debug_agent" in isi:
			cflog()
	
		disi = isi
#		sambung.send(isi)
	sambung.close()


cflog()
  
while 1:
#	time.sleep(0.2)
	try:
		startlisten()	

		#	for timestamp ----------
		tm = time.time()
		tmnow = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y_%H-%M-%S')	
		#	end for timestamp --------
		
		disi = ' %s => %s' % (tmnow, disi)		
		colordata(disi)
		write_2log(log_file,disi)
#		print disi
	except Exception as e: 
		print(e)

