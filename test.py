from mymodule import *
from api_hook_05_test import *
#import threading
from myvar import *
#from listen_6677 import *
import os
#import listen_6677



conn = False
hlpx= """
---mymodule.py-------------------------------|
 Test Fungsi, Pilih :                        |
--------------------                         |
   1. ps_info_new                            |
   2. watch_dir                              |
   3. dumpWindow                             |
   4. dumpWindow_ex                          |
   5. fhwnd                                  |
   6. getuserps                              |
   7. getuserps_idx()                        |
   8. detectnewps                            | 
   9. subprocess.Popen(['./api_hook_01.py']) |
   a. resetnewdebug()                        |
   b. start_debug()                          |
   c. sendata()                            |    
   d. get_modul_info()                       |
   e. get_file_ver()                         |
   f. get_ps_from_wm()                       |
   g. start_debug_05()                       |
   h. compare two files                      |
   i. compare two list                       |
   j. pspause() and psresume()               |
   k. persen()                               |
   0. for Clear/CLS                          |
--------------------                         |
 q/Q : Exit                                  |
---------------------------------------------|
"""

def ginput():
	while True:
		userInput = raw_input(':')
		if len(userInput) == 1:
		    break
		print 'Please enter only one character'
#	guessInLower = userInput.lower()
	return userInput.lower()


def tcon():
	global conn
	con = testconn('192.168.56.1',6677)
	print ' => CON TES : ',con
	if con == True:	conn = True
	if con == None:	conn = False

#tcon()

while True:
	global ffn, act
#	time.sleep(0.2)
	print ' => CONN [before] : ',conn
	try:
		print hlpx
		pilih = raw_input(' Pilih : ')
#		pilih = ginput()
		print "-"*10, 'Pilih : ',pilih, "-"*10
		if pilih == "q" or pilih == "Q":
			break
			print '='*22
		
		#---MAIN----
		if pilih == "tt": #====test==========	
#			ts = raw_input('File  : ')
#			print ' Signature : %s ' % str(getsigf(ts))
#			pid = raw_input('PID  \t\t: ')
#			getfilesopenbyps(int(pid))
			mylist = []
			for pid in getuserps_id():
				getfilesopenbyps(int(pid),mylist)
			
			for l in mylist:
				print ' >> ',l	
			
			ss = raw_input('Cari String  \t\t: ')
			getlistitem(mylist,str(ss))
			print 'Hasil Pencarian \t: %s ' % getlistitem(mylist,ss)

		if pilih == "t": #====test==========
#			fileEx = ['.exe','.ini','.txt','.doc','.docx','.ppt','.pptx','.xls','.xlsx','.jpg','.jpeg','.png','.pdf']
			ts = raw_input('Is str in fileEx [input str] : ')

			for fEx in fileEx:
				if ts in fEx:
					print 'Ada dalam list'
					break
				else:
					pass
			print ' FileEx => ', fileEx
#			print 'test'
#			print 'UserName : ', os.getenv('username')
#			import getpass
#			username = getpass.getuser()
#			print username
#			print getuname(os.getpid())
#			print 'UserName Path : ', getwinuser()
		if pilih == "l": #====l=============	
			for l in mal_module:
				for pid, name in getuserps():
					if 'calc' in name:
						difflist_1(l,get_modul_info(pid))

		if pilih == "k": #====k=============
			a = raw_input('Min A : ')
			b = raw_input('Max B : ')
			if persen(a,b) > 60:
				print str(persen(a,b))
				print ' Persen %s / %s : %s ' % (a,b,str(persen(a,b)))
		
		if pilih == "j": #====j=============
			pid = raw_input('PID : ')
			pspause(int(pid))
			resume = raw_input('Resume proces [%d] : ' % int(pid))
			if resume == 'Y' or resume == 'y':
				psresume(int(pid))
		if pilih == "i": #====i=============
			# membandingkan dua list 	
			difflist(taskmgr,processhacker)
			print '*'*55
			difflist_1(taskmgr,processhacker)
		if pilih == "h": #====h=============
			i=0	

#			proc.communicate()	
		if pilih == "g": #====g=============
			try:
				sendata(conn,'192.168.56.1',6677,'Connection From Debug_agent_05')
				start_debug_05()	
			except:
				pass		
		if pilih == "f": #====f=============	
			if get_ps_from_wn('Program Manager'):
				print 'Berhasil'
		if pilih == "e": #====e=============
			fn = raw_input('Get File Ver [exe_file] : ')
			print fn
			print '*'*30
			print get_file_ver(fn)
			print '*'*30
		if pilih == "d": #====d=============
			id = raw_input('Pid Process to get Dll [exe_file] : ')
			print get_modul_info(id) 	
#			if difflist(WriteTime,get_modul_info(id)):
#				print 'Its WriteTime'
#			else:
#				print 'Its NOT WriteTime'
#				
#			if difflist(explorer,get_modul_info(id)):
#				print 'Its Explorer'
#			else:
#				print 'Its NOT Explorer'	
#			print '*'*65
#			difflist_1(WriteTime,get_modul_info(id))
		if pilih == "c": #====c=============
			sendata(conn,'192.168.56.1',6677,'tessssssssssss')   
		if pilih == "b": #====b=============
			sendata(conn,'192.168.56.1',6677,'Connection From Debug_agent_04')
#			start_debug()			
		if pilih == "a": #====a=============
			resetnewdebug()		
		if pilih == "9": #====9=============
			proc = subprocess.Popen([sys.executable,'api_hook_01.py'])
			proc.communicate()			
		if pilih == "8": #====8=============
			detectnewps()	
		if pilih == "7": #====7=============
#			argv =raw_input('App_Name/PID [exp:notepad.exe]: ')
			print "="*30
			for pid, ps in getuserps_idx():
				print ' => %s \t: %s' % (pid, ps)
			print "="*30
			for pid in getuserps_id():
				print ' =>> %s ' % pid
		if pilih == "6": #====6=============
			for pid in getuserps_id():
#				print pid
				getfilesopenbyps(int(pid))
		if pilih == "66": #====6=============
#			mal_module variable dari mydb.py
			while 1:
				try:
					time.sleep(1)
					for pid, name in getuserps():
		#				if get_ps_from_wn('Program Manager'): # explorer.exe
		#					pass
		#				if get_ps_from_wn('MSCTFIME UI'): # conhost.exe 
		#					pass
						name = os.path.basename(name)
						for ll in mal_module:
							if 'conhost.exe' in name.lower() or 'explorer.exe' in name.lower():
								pass
							else:
								pr1 = diffpercen(93,ll,get_modul_info(pid))
								pr2 = diffpercen(93,get_modul_info(pid),ll)
								if pr1 > 90:
									print 'Persen:%d, Pid:%s, \tName:%s' % (pr1,pid,name)	
									pskill(pid)
									break		
								if pr2 > 90:
									print 'Persen:%d, Pid_II:%s, \tName_II:%s' % (pr2,pid,name)	
									pskill(pid)	
									break			
					print '*'*55
				except:
					pass
		if pilih == "5": #====5=============
			fhwnd('E:\\Format_Entri.xlsx')
		if pilih == "4": #====4=============
			stf = 'dumpWindow_ex.LOG'
			while 1:
				time.sleep(1)
				line = '*'*65
				wfile(stf,'\n'+line+'\n')
				for l in dumpWindow_ex(0):
					if not 'explorer.exe' in l[2].lower():
#						write_modul_info(l[1])
						sl = 'pid:%s, ps:%s tName:%s, cName:%s' % (l[1],l[2],l[3],l[4])
						wfile(stf,sl)
						print '--> ', sl					
				print '-'*35			
		if pilih == "3": #====3=============
			for l in dumpWindow(0):
				print '--> ', l
			print '-'*35
		if pilih == "22": #====22===========
			def wdir():
				while True:	
					try:
#						print watch_dir(14,"C:\\")[1][1]
						for act, fl in watch_dir(14,"C:\\"):
							print '%s => %s' % (act, fl)
#						print watch_dir(14,"C:\\")
					except:
						pass 
			wdir()
		if pilih == "2": #====2=============
			def wdir():
				while True:	
					try:
						print watch_dir(12,"C:\\")
					except:
						pass 
			while 1:
				try:
					wdir()
				except:
					pass
						
		if pilih == "1": #====1=============
			pid = raw_input('PID : ')
			ps_info_new(int(pid))
		
		if pilih == "0": #====0=============
			os.system('cls')		

		print "-"*10, 'Pilih : ',pilih, "-"*10
	except Exception as e:
		print "-"*10, pilih, "-"*10
		print 'Errror : ' + str(e)
		print "Something Happen, it's not be good "



