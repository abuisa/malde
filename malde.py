#------------------------------
# DiEdit oleh : Abu_Isa 	---
# Versi Pengembangan 06.01  ---
# Perubahan nama dari : 
# 	- api_hook_05_test.py
#	- malde_test.py
#--------------------------

# Copyright (c) 2009-2014, Mario Vilas
# All rights reserved.

# $Id: 09_api_hook.py 1299 2013-12-20 09:30:55Z qvasimodo $

from winappdbg import Debug, EventHandler, System
from winappdbg.win32 import *
from mymodule import *
from myvar import *
import os
import psutil
import threading
import time
#import datetime

# data3 list untuk menampung sementara data dir monitor
# data4 list untuk menampung sementara data process debug
# data5 list untuk menampung hasil komparasi data3 dan data4 

conn  = False
data3 = []
data4 = []
data5 = []
pidtmp = set()
mylist = []
sdat = False
gohit=False
pid, exe, stat, string, gtag = '','','','',''

class MyEventHandler( EventHandler ):
    
    
    apiHooks = {

        # Hooks for the kernel32 library.
        'kernel32.dll' : [

            #  Function            Parameters
            ( 'CreateFileA'     , (PVOID, DWORD, DWORD, PVOID, DWORD, DWORD, HANDLE) ),
            ( 'CreateFileW'     , (PVOID, DWORD, DWORD, PVOID, DWORD, DWORD, HANDLE) ),
            ( 'CreateProcessA'  , 10 ),
            ( 'CreateProcessW'  , 10 ),

        ],

        # Hooks for the advapi32 library.
        'advapi32.dll' : [

            #  Function            Parameters
            ( 'RegCreateKeyExA' , (HKEY, PVOID, DWORD, PVOID, DWORD, REGSAM, PVOID, PVOID, PVOID) ),
            ( 'RegCreateKeyExW' , (HKEY, PVOID, DWORD, PVOID, DWORD, REGSAM, PVOID, PVOID, PVOID) ),

        ],
    }
	# =======Tambahan modifikasi================================================
#    Fungsi --pre_CreateProcessA-- ini tidak ada indikasi apapun, jadi baiknya dinonaktifkan	
    def pre_CreateProcessA( self, event, ra, lpApplicationName, lpCommandLine, lpProcessAttributes, lpThreadAttributes,
                            bInheritHandles, dwCreationFlags, lpEnvironment, lpCurrentDirectory, lpStartupInfo,
                            lpProcessInformation):
        self.__print_createps_ansi( event, "CREATE_PROCESS", lpApplicationName ) # untuk win7 fungsi ini tidak bekeraja

    def pre_CreateProcessW( self, event, ra, lpApplicationName, lpCommandLine, lpProcessAttributes, lpThreadAttributes,
                            bInheritHandles, dwCreationFlags, lpEnvironment, lpCurrentDirectory, lpStartupInfo,
                            lpProcessInformation):
        self.__print_createps_unicode( event, "CREATE_PROCESS", lpApplicationName ) # untuk win7 fungsi ini yang bekeraja

    def post_CreateProcessA( self, event, retval ):
        self.__print_createps_success( event, retval )                
    def post_CreateProcessW( self, event, retval ):
        self.__print_createps_success( event, retval )
        
        
    def __print_createps_ansi( self, event, tag, pointer ): # untuk win7 fungsi ini tidak bekeraja
        global pid, exe, string, gtag, gohit # set data to global variable supaya bisa diakses dari luar
        string = event.get_process().peek_string( pointer )
        pid    = event.get_pid()
        exe    = os.path.basename(event.get_process().get_filename())	
        gtag   = tag
        gohit  = True

        
    def __print_createps_unicode( self, event, tag, pointer ): # untuk win7 fungsi ini yang bekeraja
        global pid, exe, string, gtag, gohit # set data to global variable supaya bisa diakses dari luar
        string = event.get_process().peek_string( pointer, fUnicode = True )
        pid    = event.get_pid()
        exe    = os.path.basename(event.get_process().get_filename())
        gtag   = tag
        gohit  = True



    def __print_createps_success( self, event, retval ):
        global pid, exe, stat, string, gtag, data3, mylist # set data to global variable supaya bisa diakses dari luar
        try:
            pspid  = getpidexe(os.path.basename(string))
            if retval:
                data3.append([str(pid), exe, gtag, string, str(pspid)])
                start_debug_05() #OK, masih ada error
                getfilesopenbyps(int(pspid),mylist)
#        except Exception as E:
#            print 'Error PS => ', str(E) 
        except:
            pass             
                
	# =======End Tambahan=======================================================
	
    def pre_CreateFileA( self, event, ra, lpFileName, dwDesiredAccess,
             dwShareMode, lpSecurityAttributes, dwCreationDisposition,
                                dwFlagsAndAttributes, hTemplateFile ):
        self.__print_opening_ansi( event, "OPEN_FILE", lpFileName )


    def pre_CreateFileW( self, event, ra, lpFileName, dwDesiredAccess,
             dwShareMode, lpSecurityAttributes, dwCreationDisposition,
                                dwFlagsAndAttributes, hTemplateFile ):
        self.__print_opening_unicode( event, "OPEN_FILE", lpFileName )


    def post_CreateFileA( self, event, retval ):
        self.__print_success( event, retval )

    def post_CreateFileW( self, event, retval ):
        self.__print_success( event, retval )

	
    def __print_opening_ansi( self, event, tag, pointer ):
        global sdat, pid, exe, string, gtag         
        if os.path.isfile(event.get_process().peek_string(pointer)) == True:
            for dfilter in data_filter: 
                if dfilter in event.get_process().peek_string(pointer, fUnicode = True):
                    string = event.get_process().peek_string(pointer)
                    sdat, gtag  = True, tag
                    pid    = event.get_pid()
                    exe    = os.path.basename(event.get_process().get_filename())	
        else:
            sdat = False   

    def __print_opening_unicode( self, event, tag, pointer ):
        global sdat, pid, exe, string, gtag 
        if os.path.isfile(event.get_process().peek_string(pointer, fUnicode = True)) == True: 
            for dfilter in data_filter: 
                if dfilter in event.get_process().peek_string(pointer, fUnicode = True):
                    string = event.get_process().peek_string(pointer, fUnicode = True)   
                    sdat, gtag  = True, tag             
                    pid    = event.get_pid()
                    exe    = os.path.basename(event.get_process().get_filename())
        else:
            sdat = False

    def __print_success( self, event, retval ):
        global sdat, pid, exe, string, gtag, data3
        try: # tambahan ini karena selalu muncul error "--set object has no attribute 'append'--"
		    if retval :
		        if sdat:
		            data3.append([str(pid), exe, gtag, string]) 	
		    else:
		        data3.append([str(pid), exe, gtag, string])
        except Exception as E:
            print 'Error => ', str(E)
#            pass

d1 = Debug(MyEventHandler())

def start_debug_05(): # Hasil OK.
	try:
		d1.stop()
		for pid in getuserps_id():
			try:
				d1.attach(int(pid))
			except:
				pass
		d1.loop()
	except:
		pass
	finally:
		d1.stop()
	
		
if __name__ == "__main__":
#	ip1, pr1  = "127.0.0.1", 6677
	ip1, pr1  = "192.168.56.1", 6677
	driveC    = "C:\\"
	missfile = 0
	act = {
	  1 : "CREATED",
	  2 : "DELETED",
	  3 : "CHANGED",
	  4 : "REN_Frm",
	  5 : "REN__To"
	}
	
	def tcon():
		global conn
		con = testconn('192.168.56.1',6677)
		print ' Connection : ',con
		if con == True:	conn = True
		if con == None:	conn = False
	
	print ' Start Monitoring... '
	tcon()
	sendata(conn,ip1,pr1,'Connection From Debug_agent_05')
	# to do (experiment) : if new process detect then :
	
	
	def waktu_monitoring(): 
		global gohit
		try:
			t1 = datetime.now()  
			while 1:
				time.sleep(0.02)
				# versi I : hasil OK
#				if (datetime.now()-t1).seconds > 5: # periksa dan show data setiap 5 detik
#					getappid()
#					marge_comparator_data() 
#					t1 = datetime.now()
				# versi II 
				if gohit: 
					if (datetime.now()-t1).seconds > 5: # periksa dan show data 5 detik setelah process baru
						getappid()
						marge_comparator_data() 
						t1 = datetime.now()
						gohit = False
		except:
			pass
	#	except Exception as E:
	#		print 'Error : ', str(E)

	def fdata(dataz):
		# untuk mencari kesamaan file dalam data3 dan data4
		# data3 dan data4 yang sama digabung dan disusun berdasarkan event  
		global data3, data4 # data3 :event - len(2), data4 :wdir - len(2)
		try:
			if len(data3) > 0 and len(data4) > 0:
				for d4 in data4:
					for d3 in data3:
#						if d4[1] in d3[3]:
						if d4[1].lower() in d3[3].lower():
							dataz.append([d3[0],d3[1],d4[0],d3[3]]) # dataz di isi data4 kombinasi data3
			return dataz
		except:
			pass

	def getappid():
		# fungsi untuk mengambil semua pid user_proses yang mengakses file 
		# pid disimpan dalam var=pditmp : type=set(), type set secara otomatis mengabaikan dobel item (uniq)
		global mylist, data3, pidtmp		
		try:
			time.sleep(0.4)
			if len(data3) >0: 
				for d3 in data3:
					pidtmp.add(str(getpidexe(d3[1])))

			if len(pidtmp) > 0: 
				for ppid in pidtmp:
					getfilesopenbyps(int(ppid),mylist)						
#					print ' PID-TMP : ', ppid

#		except Exception as E:
#			print ' Error getappid : ', str(E)
		except:
			pass

	def marge_comparator_data():
		# fungsi untuk -menggabungkan data, -filter data, -modifikasi data
		# marge_comparator_data
		global data3, data4, mylist, pidtmp
		allf = set()
		fexi,fsig = 0,0
		try:
#--------------------------------------------------------------
			try:
				dataz = []	
				dataz = fdata(dataz)
				dataz = sort_deduplicate(dataz) 
#				for dz in dataz:
#					dz5 = " [%s:%s] %s %s " % (str(dz[0]),dz[1],dz[2],dz[3])
#					sendata(conn,ip1,pr1,dz5)
#					print ' => ', dz5
			except: 
				pass
#--------------------------------------------------------------	
			data5 = data3 + data4		
			if len(data5)>0:
				dx = len(data5)	
				data5 = sort_deduplicate(data5) 
#--------------------------------------------------------------
#				print '--- Sort|Uniq Data5 ' + str('-'*35)
				#-----------------------------------
#				for pidt in pidtmp:
#					print ' PIDx : %s' % pidt
				#-----------------------------------
				print '='*55				
				for d5 in data5:
					if len(d5) > 4:	f = d5[-2]
					else:f = os.path.join(driveC,d5[-1])
					allf.add(f)
#					#------------------------------------------					
					if len(d5) == 2:
						psdg = getlistitem(mylist,d5[1])
#						if psdg != " N/A ":	pidg = getpidexe(psdg)
#						else:pidg = " N/A "
						d5.insert(0," N/A ")
						d5.insert(1,psdg)						
						d53 = os.path.join(driveC,d5[3])
						d5.remove(d5[3])
						d5.insert(3,d53)
#					#------------------------------------------
					if len(d5) >  4:d55 = " [ %s : %s ] %s %s %s " % (d5[0],d5[1],d5[2],d5[3],d5[4])
					if len(d5) == 4:d55 = " [ %s : %s ] %s %s "    % (d5[0],d5[1],d5[2],d5[3])
					print d55	
					sendata(conn,ip1,pr1,d55)
#--------------------------------------------------------------
				print '-'*55
				i = 0
				for sl in allf:								
					cfile = isfile(sl)
					csig  = getfsig(sl)
					if cfile == 'EXIST':fexi = fexi + 1	
					if csig  == 'unknown':fsig = fsig + 1
					i = i+1	
					print ' File %d \t : [ %s : %s ] %s' % (i,cfile,csig,sl)
				ufsig = len(allf) - fsig
#--------------------------------------------------------------	
#				if len(mylist)>0:
#					print '+'*55			
#					for lv in mylist:
#						print ' >> : ',lv
#					print ' TOTAL MYLIST : ',str(len(mylist))
#					print '+'*55
#--------------------------------------------------------------
				print_report(data3,data4,dataz,allf,fexi,ufsig)
				data3 =[] # From Event
				data4 =[] # From Wdir		
				data5 =[] # From Equal
				dataz =[]
				mylist=[]
				allf.clear()
				fexi,fsig = 0,0
				pidtmp.clear()
#				print ' AF-TOTAL MYLIST : ',str(len(mylist))
		except:
			pass
#		except Exception as E:
#			print ' marge_comparator_data Error : ',str(E)	
		

	def wdir():
		global data4
		while True:	
			try:				
				for ac, fl in watch_dir(14,driveC):
					for dfilter in data_filter: 
						if dfilter in fl:				
							data4.append([act.get(ac,'---'),fl])
			except:
				pass 

	th1 = threading.Thread(target=start_debug_05)			
	th1.start()
#	
	th2 = threading.Thread(target=wdir)
	th2.start()	
#	
	th4 = threading.Thread(target=waktu_monitoring)
	th4.start()
	

#===KET : ========================
#	data3  = list1 : list get from debug event 
#	data4  = list2 : list get wdir event
#	data5  = list3 : list get from compare between data4 to data3 live (var to var)
#	mylist = mylist: list untuk menampung data hasil psutil.processs.openfile 
#	mylist = mylist: isinya <<appname : cmd.line/open.file>>

	
	
