import os
import psutil
import win32gui
import subprocess
import win32file
import win32con
import win32process
import win32api
import msvcrt
import time
#import datetime
import socket
import glob
#import winappdbg
from winappdbg import System, system, win32
from datetime import datetime 
import binascii
import signal
from myvar import *
import subprocess as sp


#conn = False
#fileEx = ['.exe','.txt','.doc','.docx','.ppt','.pptx','.xls','.xlsx','.jpg','.jpeg','.png','.pdf'] # The First One
#fileEx = ['.txt','.doc','.docx','.ppt','.pptx','.xls','.xlsx','.jpg','.jpeg','.png','.pdf'] # the Experiment

def wtofile(fl,s):
	try:
		fl = 'LOG/'+fl
		f = open(fl,'a+')
		f.write(s+"\n")
	except:
		f = open(fl,'w')
	f.close

def wfile(fl,s):
	try:
		f = open(fl,'a+')
		f.write(s+"\n")
	except:
		f = open(fl,'w')
	f.close

def ftolist(fn):
	with open(fn,'r') as F:
		F.readlines
		for l in F:			
			l=list(l.split(' '))
#			l = sorted(l)
#			print type(l)
			print '=>',l

def watch_dir(kode,path_to_watch):
#	global fileEx
	ACTIONS = {
	  1 : "CREATED",
	  2 : "DELETED",
	  3 : "CHANGED",
	  4 : "REN_Frm",
	  5 : "REN__To"
	}
	FILE_LIST_DIRECTORY = 0x0001

	hDir = win32file.CreateFile (
	  path_to_watch,
	  FILE_LIST_DIRECTORY,
	  win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
	  None,
	  win32con.OPEN_EXISTING,
	  win32con.FILE_FLAG_BACKUP_SEMANTICS,
	  None
	)
	
	results = win32file.ReadDirectoryChangesW (
	hDir,
	1024,
	True,
	win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
	 win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
	 win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
	 win32con.FILE_NOTIFY_CHANGE_SIZE |
	 win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
	 win32con.FILE_NOTIFY_CHANGE_SECURITY,
	None,
	None
	)
	if kode == 11: # Filtered
		try:
			for action, files in results:
				for fEx in fileEx:
					if fEx in  files:
						act = ACTIONS.get(action, "Unknown")
						return ((act,os.path.join(path_to_watch,files)))
		except Exception as e:
			print 'Error in : ',str(e)

	if kode == 12:	# NON Filter
		try:
			for action, file in results:
				fl = str(os.path.join(path_to_watch, file))
				pf = ACTIONS.get(action, "Unknown") + ' : ' + fl + ', [' + str(getsigf(fl)) + '] '  # str(type(fl))   getsig(str(fl))
				return pf
		except Exception as e:
			print 'Error in : ',str(e)			
			
	if kode == 13: # only for Test
		for action, file in results:
			full_filename = os.path.join(path_to_watch, file)
			d1 = ACTIONS.get(action, "Unknown")
			d2 = ' => %s :: %s ' % (d1,full_filename)
			print d2
			
	if kode == 14:
		return results
		
def dumpWindow(hwnd, wantedText=None, wantedClass=None):
    windows = []
    hwndChild = None
    while True:
        hwndChild = win32gui.FindWindowEx(hwnd, hwndChild, wantedClass, wantedText)
        if hwndChild:
            textName = win32gui.GetWindowText(hwndChild)
#            textName = win32gui.GetOpenFileName(hwndChild)
            className = win32gui.GetClassName(hwndChild)
            windows.append((hwndChild, textName, className))
        else:
            return windows


def dumpWindow_ex(hwnd, wantedText=None, wantedClass=None):

	def Getps(hwnd):
		threadpid, procpid = win32process.GetWindowThreadProcessId(hwnd)
		# PROCESS_QUERY_INFORMATION (0x0400) or PROCESS_VM_READ (0x0010) or PROCESS_ALL_ACCESS (0x1F0FFF)
		mypyproc = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, procpid)
		procname = win32process.GetModuleFileNameEx(mypyproc, 0)
		return os.path.basename(procname)
		
	windows = []
	hwndChild = None
	while True:
		hwndChild = win32gui.FindWindowEx(hwnd, hwndChild, wantedClass, wantedText)
		if hwndChild:
		    textName = win32gui.GetWindowText(hwndChild)
		    className = win32gui.GetClassName(hwndChild)
		    ps = Getps(hwndChild)
		    tid, pid = win32process.GetWindowThreadProcessId(hwndChild)
		    windows.append((hwndChild, pid, ps,  textName, className))
		else:
		    return windows


def getexe(pid):
#	get process name from pid given
	ps = psutil.Process(pid)		
	return os.path.basename(ps.exe)

def getpidexe(name):
#	get pid from process contain the name string
	system = System()
	for process in system:
		if process.get_filename() != None and name != None:				
			if name.lower() in process.get_filename().lower() :
				return process.get_pid()

def getwinuser():
#	get windows user name 
	import getpass
	return getpass.getuser() #username #username = getpass.getuser()
	
def getuname(pid):
#	get user name from pid given
	ps = psutil.Process(pid)
	try:	
		return ps.username
	except :
		pass
		
def getuserps():
#	return all process under user/user process
#	return pids and process names
	system = System()
	userps = []
	for process in system:
		try:	
			if getwinuser() in getuname(process.get_pid()) :
				userps.append((process.get_pid(),  process.get_filename()))
		except:
			pass
	return userps

def getuserps_id():
#	return all process under user/user process
#	only return pids
	system = System()
	userps = []
	for process in system:
		try:	
			if getwinuser() in getuname(process.get_pid()) :
				userps.append((str(process.get_pid())))
		except:
			pass
	return userps

def getuserps_idx():
#	return all process 
#	only return pids
	system = System()
	userps = []
	for process in system:
		try:	
			if process.get_pid() == 0 or process.get_pid() == 4 or process.get_pid() == 8 :
				continue
			else:
				userps.append((str(process.get_pid()), process.get_filename()))
		except:
			pass
	return userps
	
curps = getuserps_id()
def detectnewps():
	global curps		
	while True:
		time.sleep(0.2)
		try:
			tps = getuserps_id()
			for ps in tps:
				if ps not in curps:
					curps = tps
#					write_modul_info(ps) # get collect the process dll
					print '.'*5 + 'New Process ->> ' + getexe(int(ps))
#					pskill(ps) # kill process after get the dll
					getfilesopenbyps(int(ps))
#					for l in getfilesopenbyps(int(ps)):
#						print ' => : [ %s : %s ] %s' % (l[0],l[1],l[2])
			if len(curps) != len(tps):
				curps = tps
				print '.'*5 + '  ->> Mising Process  ' 
			if len(curps) == len(tps):
				for ps in tps:
					if ps in curps:
						break
#						print '.'*5 + 'TPS :'+ str(len(tps)) + '...CURPS :'+str(len(curps)) +'.'*5
# penggunaan CPU lumayan rendah dibanding tidak menggunakan sleep
			
		except Exception as E:
			print 'Error 1 : ' +str(E)

curps = getuserps_id()
def resetnewdebug():
	global curps
	while True:
		try:
			tps = getuserps_id()
			if len(curps) != len(tps)  :
				curps = tps
				print '='*45
				print '.'*5 + ' -> Process Changed !.. ' 
				for ps in tps:
					print ' => ', ps, d1.is_debugee(int(ps))
				print '='*45
	#		time.sleep(1) # penggunaan CPU lumayan rendah dibanding tidak menggunakan sleep
	#		time.sleep(0.2)
		except Exception as E:
			print 'Error 1 : ' +str(E)

def testconn(ip,pr):
	try:
		skt = socket.socket()
		skt.settimeout(2)
		con = skt.connect((ip, pr))
		skt.close()	
		if con:
			return False
		else:
			return True
#		skt.send(pesan)			
	except socket.error, exc:
		pass

def sendata(conn,ip,pr,pesan):
	try:
		if conn == False:pass
		if conn == True:
			skt = socket.socket()
			skt.settimeout(2)
			skt.connect((ip, pr))
			skt.send(pesan)
			skt.close()
	except socket.error, exc:
		pass
#		print " => Caught exception socket.error : %s" % exc	


def listen():
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
		wfile('listen_6677.py',isi.lower())
	sambung.close()		
				
def ps_info_new(pid):
	ptof ='psutil27_ps_list_len.LOG'
	g    ='----------------------------'
	gg   ='============================'
	
	def wf(s,ss):
		sss = s + ' \t: ' + str(ss)
		print ' --> ' + sss
#		wtofile(ptof,sss)
		
	def glist(s,ls):
		try:
			for p in ls:
				ss = s + ' \t:: '+ str(p[0])
				print ss
#				wtofile(ptof,ss)
		except Exception as e:
			print s+'Errror : ' + str(e)
			print gg
			
#	all_pid = psutil.get_pid_list()
#	for pid in all_pid:
	
	def getinfo():
#		global pid
		ps = psutil.Process(pid)
		try:		
#			wtofile(ptof,gg)				
			wf('ps.exe',ps.exe)
			wf('ps.name',ps.name)
			wf('ps.parent',ps.parent)
			wf('ps.pid',ps.pid)
			wf('ps.ppid',ps.ppid)
			wf('ps.username',ps.username)
			wf('ps.getcwd',ps.getcwd())
			wf('ps.get_children',ps.get_children)
			glist('ps.cmdline',ps.cmdline)
			wf('ps.get_conns',ps.get_connections())
			glist('mmaps.path',ps.get_memory_maps())
			wf('ps.mmpercen',ps.get_memory_percent())
			wf('ps.getnice',ps.get_nice())
			wf('ps.getnumctx',ps.get_num_ctx_switches())
			wf('ps.getnumhandles',ps.get_num_handles())
			wf('ps.getnumthreads',ps.get_num_threads())
			glist('openf.path',ps.get_open_files())
#			wf('ps.get_threads',ps.get_threads())
			glist('ps.get_threads',ps.get_threads())
			print g
		except Exception as E:
			print ' Error : ',str(E)
#			pass
			
#	return getinfo()
	getinfo()
			
#	app = subprocess.Popen ([r"WriteTime.exe"])	
#	getinfo(app.pid)
	print gg

		
def fhwnd(thefile):
	def Getps(hwnd):
		'''Acquire the process name from the window handle for use in the log filename.
		1. how to get process name from threadpid
		2. how to get process name from hwnd
		'''
		threadpid, procpid = win32process.GetWindowThreadProcessId(hwnd)
		# PROCESS_QUERY_INFORMATION (0x0400) or PROCESS_VM_READ (0x0010) or PROCESS_ALL_ACCESS (0x1F0FFF)
		mypyproc = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, procpid)
		procname = win32process.GetModuleFileNameEx(mypyproc, 0)
		return procname
	f = open(thefile,'r')
	hfile = win32file._get_osfhandle(f.fileno())
	hflms = msvcrt.get_osfhandle(f.fileno())
	print '-> ', hfile
	print '-> ', hflms
	print Getps(hfile)
	return (hflms, hfile)
	
def get_file_ver(fn):
#	return	winappdbg.system.System.get_file_version_info(fn)
	return	system.System.get_file_version_info(fn)
		
def get_ps_from_wn(wn):
#   get process name from Window manager text/name
#	wn -> exp : 'Program Manager' return explorer.exe
	try:
		hwnd = win32.user32.FindWindowW(None,wn)
		threadpid, procpid = win32process.GetWindowThreadProcessId(hwnd)
		return ((threadpid, procpid,getexe(procpid)))
	except:
		pass

def write_modul_info(pid=None):
	try:
		if pid ==None :
			pid = os.getpid()
		
		dlls= []
		p = psutil.Process( int(pid) )
		for dll in  p.get_memory_maps():
			if '.dll' in os.path.basename(dll.path):
				dlls.append(os.path.basename(dll.path).lower())

		exe = getexe(int(pid))
#		dlls= str(sorted(set(dlls)))+ ', # '+ exe 
		dlls= str(dlls)+ ', # '+ exe 

		startsend('192.168.56.1',6777,dlls)
	except Exception as E:
		print ' Error : ', str(E)
		
def get_modul_info(pid=None):
	try:
		dlls= []
		if pid ==None :
			pid = os.getpid()		
		p = psutil.Process( int(pid) )
		for dll in  p.get_memory_maps():
			if '.dll' in os.path.basename(dll.path):
				dlls.append(os.path.basename(dll.path))
#		dlls=sorted(dlls)
		return dlls
	except Exception as E:
		print ' Error : ', str(E)

#def diffpercen(filtr,lname,list1,list2):
#	try:
#		list1,list2 = set(list1),set(list2)	
#		diffl = list(set(list1).intersection(list2))
#		lenlist1, lendiffl = len(list1), len(diffl)
#		if persen(lendiffl,lenlist1) >= int(filtr):
#			if lenlist1 == lendiffl:
#				print ' Persen:%s \t:%s ' % (str(persen(lendiffl,lenlist1)),lname) 
#			else:
#				print ' Persen:%s \t:%s ' % (str(persen(lendiffl,lenlist1)),lname) 
#	except Exception as E:
#		print ' Error : ',str(E)
def diffpercen(filtr,list1,list2):
	try:
		list1,list2 = set(list1),set(list2)	
		diffl = list(set(list1).intersection(list2))
		lenlist1, lendiffl = len(list1), len(diffl)
		if persen(lendiffl,lenlist1) >= int(filtr):
			return persen(lendiffl,lenlist1) 
	except Exception as E:
		print ' Error : ',str(E)
		
		
def difflist(lname,list1,list2):
	list1,list2 = set(list1),set(list2)	
	diffl = list(set(list1).intersection(list2))
	lenlist1, lendiffl = len(list1), len(diffl)
	if lenlist1 == lendiffl:
		print ' %s : Sama Hasil List1:%d, List2:%d, Equal:%d, Persen:%s' % (lname,lenlist1, len(list2), lendiffl, persen(lendiffl,lenlist1)) 
	else:
		print ' %s : Tidak Sama Hasil List1:%d, List2:%d, Equal:%d, Persen:%s' % (lname,lenlist1, len(list2), lendiffl, persen(lendiffl,lenlist1)) 


def difflist_1(list1,list2):
	list1,list2 = set(list1),set(list2)	
	print 'List1 %d : %s ' % (len(list1),list1)
	print 'List2 %d : %s ' % (len(list2),list2)
	diffl1  = list(set(list1) - set(list2))
	diffl2  = list(set(list2) - set(list1))
	diffl = list(set(list1).intersection(list2))
	if len(diffl1) == 0 :
		print ' All Element of List1 is in List2 [%d:%s] ' % (len(diffl1),diffl1)	
	if len(diffl2) == 0 :
		print ' All Element of List2 is in List1 [%d:%s]  ' % (len(diffl2),diffl2)			
	if len(diffl1) > 0 : 
		print ' Element of List1 not in List2 [%d:%s] ' % (len(diffl1),diffl1)
	if len(diffl2) > 0 : 
		print ' Element of List2 not in List1 [%d:%s] ' % (len(diffl2),diffl2)		
	if len(diffl) > 0 :
		print ' Element in List1 and List2 [%d:%s] ' % (len(diffl),diffl)

def persen(minA,maxB):
#	hasil = (float(minA) / float(maxB)) * 100.00
#	return str(hasil)[:5]+'%'
	hasil = (float(minA) / float(maxB)) * 100
	return int(hasil)

def checkfile(pathtofile): # fungsi tidak bekerja (sudah di coba di windows 7 tidak berhasil)
	# pathtofile bisa seperti : "c:/windows/*.bmp"
	for fl in glob.glob(pathtofile):
		print ' => ',fl
		
def pspause(pid):
	try:
		p = psutil.Process(int(pid))
		p.suspend()
	except:
		pass

def psresume(pid):
	try:
		p = psutil.Process(int(pid))
		p.resume()
	except:
		pass

def pskill(pid):
	try:
		p = psutil.Process(int(pid))
		p.kill()
		p.terminate()
	except:
		pass

def kill_tree(pid, sig=signal.SIGTERM, include_parent=True,timeout=None, on_terminate=None):
	"""Kill a process tree (including grandchildren) with signal
	"sig" and return a (gone, still_alive) tuple.
	"on_terminate", if specified, is a callabck function which is
	called as soon as a child terminates.
	"""
	if pid == os.getpid():
		raise RuntimeError("I refuse to kill myself")
	parent = psutil.Process(pid)
	children = parent.children(recursive=True)
	if include_parent:
		children.append(parent)
	for p in children:
		p.send_signal(sig)
	gone, alive = psutil.wait_procs(children, timeout=timeout, callback=on_terminate)
	return (gone, alive)

def hitevent(sc):
	try:
		t1 = datetime.now()
		while (datetime.now()-t1).seconds <= int(sc):
			#do something
			print(datetime.now())
	finally:
		print 'Menghitung....'
		print 'Selesai.......'
		
def hitevent2(sc):	
#	gunakan dibawah untuk check data count		
	try:
		t1 = datetime.now()  
		while 1:
			print ' => ' +str(t1)+ ' :: ' +str(datetime.now())
			if (datetime.now()-t1).seconds > sc:
				break	
	finally:
		print 'Selesai ....'
			
def getsigf(fname):
	try:
		with open(fname,'rb') as rf:
			dat= binascii.b2a_hex(rf.read(12))
			return dat.upper()	
	except:
		pass
		
def getsig(fname): 
	# return file_signature if match, else return None
	try:
		with open(fname,'rb') as rf:
			dat= binascii.b2a_hex(rf.read(12))
			for sig in fsign:
				if sig in dat.upper():
					return fsign.get(sig.upper(),'UNKNOWN')	
	except:
		pass			
#	except Exception as E: 
#		print ' getsig Error : ',str(E)

def getfsig(fname):
	try:
		hasil = getsig(fname)
		if hasil != None:
			return str(hasil.upper())
		else:
#			return "UNKNOWN"
			return "unknown"
	except:
		pass
#	except Exception as E: 
#		print ' getfsig Error : ',str(E)

def isfile(fname):
	try:
		if os.path.isfile(fname) == True:
			return "EXIST"
		else:
			return "MISSING"
	except:
		pass
#	except Exception as E: 
#		print ' isfile Error : ',str(E)

def luniq(lst):
    try:
        last = object()
        for item in lst:
            if item == last:
                continue
            yield item
            last = item
    except:
        pass
		
def sort_deduplicate(l):
	try:
		return list(luniq(sorted(l, reverse=True)))
	except:
		pass
    
def print_report(r1,r2,allf,fe,fs):
	try:
#		tmp=sp.call('cls',shell=True) # bersihkan layar 
		created,deleted,changed,renfom,rento =0,0,0,0,0
		opfile,crtps = 0,0
		allps = set()
	#--------------------------------------------------	

		rall = r1 + r2	
		if r1 > 0: # all data events in list1
			for l1 in r1:
				allps.add(l1[1])
				if 'OPEN_FILE'      in l1:opfile = opfile +1
				if 'CREATE_PROCESS' in l1:crtps  = crtps  +1

		if r2 > 0: # all data events in list2
			for l2 in r2:
				if 'CREATED' in l2:created = created +1
				if 'DELETED' in l2:deleted = deleted +1
				if 'CHANGED' in l2:changed = changed +1
				if 'REN_Frm' in l2:renfom  = renfom  +1
				if 'REN__To' in l2:rento   = rento   +1
				
				
		renall = int(renfom) + int(rento)
		waktu = datetime.now()			
		print '*'*55
		print ' Laporan Aktifitas Mengakses Files Oleh Prosess : '
		print '-'*55	
		print ' Laporan untuk Waktu  :', waktu										
		print ' Total Events         : %s [%s/%s]' % (str(len(rall)),str(len(r1)),str(len(r2)))

		print '    Open Events       : %s ' % str(opfile)
		print '    Created Events    : %s ' % str(created)
		print '    Changed Events    : %s ' % str(changed)	
		print '    Deleted Events    : %s ' % str(deleted) 
		print '    Renamed Events    : %s [%s/%s] ' % (str(renall),str(renfom),str(rento))
		print ' Total Files          : %s ' % str(len(allf))   
		print '    Exist Files       : %s Exist / %s Missing ' % (str(fe), str(len(allf) - fe))	# From Param
		print '    Signature Files   : %s Known / %s Unknown ' % (str(fs),str(len(allf)-fs))	# From Param 
		print ' Process              : %s ' % (str(len(allps)) + ' ' + str(list(allps)))
		print '    Process Create    : %s ' % str(crtps)
		print ' Hasil                :  ' #%
		print '    Proses dicurigai  :  ' #% 
		print '*'*55	
	except:
		pass

def getfilesopenbyps_OLD(pid,ss):
#		time.sleep(0.1)
		lps = set()
		ps = psutil.Process(pid)
		try:
			psn = ps.name		
			for psc in ps.cmdline:
				if psc != '/n':
					lps.add((pid,psn,psc))
			for psg in ps.get_open_files():
				lps.add((pid,psn,psg[0]))
#			return lps
			if len(lps)>0:
				for l in lps:
					if ss in l:
						print ' >> [ %s : %s ]  %s' % (l[0],l[1],l[2])
#					for fEx in fileEx: 
#						if fEx in l[2]:
#							print ' >> [ %s : %s ]  %s' % (l[0],l[1],l[2])
		except Exception as E:
			print ' Error : ',str(E)


def getfilesopenbyps(pid,mylist):
	ps = psutil.Process(pid)
	try:
		psn = ps.name		
		for psc in ps.cmdline:
			if psc != '/n':
				mylist.append([psn,psc])
		for psg in ps.get_open_files():
			mylist.append([psn,psg[0]])
	except:
		pass
#	except Exception as E:
#		print ' Error : ',str(E)

def getlistitem(mylist,s):
	try:
		for l in mylist:
			if s in str(l[1]):
				return l[0]
			else:
				return " N/A "
	except:
		pass
		
def testps():
	time.sleep(5)
	app = subprocess.Popen ([r"calc.exe"])	
#	print 'PID : ',app.pid	
	time.sleep(2)
	pskill(app.pid)	

