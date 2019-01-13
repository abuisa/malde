#------------------------------
# DiEdit oleh : Abu_Isa 	---
# Versi Versi Stabil 05.06  ---
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

conn = False
data3 = []
data4 = []
data5 = []
data2 = ''
pid, exe, stat, string, gtag = '','','','',''

class MyEventHandler( EventHandler ):
    sdat = False
    
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
        global pid, exe, string, gtag # set data to global variable supaya bisa diakses dari luar
        string = event.get_process().peek_string( pointer )
        pid    = event.get_pid()
        exe    = os.path.basename(event.get_process().get_filename())	
        gtag   = tag

        
    def __print_createps_unicode( self, event, tag, pointer ): # untuk win7 fungsi ini yang bekeraja
        global pid, exe, string, gtag # set data to global variable supaya bisa diakses dari luar
        string = event.get_process().peek_string( pointer, fUnicode = True )
        pid    = event.get_pid()
        exe    = os.path.basename(event.get_process().get_filename())
        gtag   = tag


    def __print_createps_success( self, event, retval ):
        global pid, exe, stat, string, gtag, data3 # set data to global variable supaya bisa diakses dari luar
        try:
            pspid  = getpidexe(os.path.basename(string))
            if retval:
                data3.append([str(pid), exe, gtag, string, str(pspid)])
                start_debug_05() #OK, masih ada error
        except Exception as E:
            print 'Error PS => ', str(E) 
                
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
            for fEx in fileEx: 
                if fEx in event.get_process().peek_string(pointer, fUnicode = True):
                    string = event.get_process().peek_string(pointer)
                    sdat, gtag  = True, tag
                    pid    = event.get_pid()
                    exe    = os.path.basename(event.get_process().get_filename())	
        else:
            sdat = False   

    def __print_opening_unicode( self, event, tag, pointer ):
        global sdat, pid, exe, string, gtag 
        if os.path.isfile(event.get_process().peek_string(pointer, fUnicode = True)) == True: 
            for fEx in fileEx: 
                if fEx in event.get_process().peek_string(pointer, fUnicode = True):
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
		print ' => CON TES : ',con
		if con == True:	conn = True
		if con == None:	conn = False

	tcon()
	sendata(conn,ip1,pr1,'Connection From Debug_agent_05')
	
	def datareport(list1,list2,list3):
		# VarMaps: list1=data3, list2=data4, list3=data5
		global missfile
		dataEQ =[] # Temporary only local
		created,deleted,changed,renfom,rento =0,0,0,0,0
		d1,d2,d3 = len(list1),len(list2),len(list3)	
		#----------------------------------------------------------------
		if d2 > 0:
			for l2 in list2:
				if 'CREATED' in l2:created = created +1
				if 'DELETED' in l2:deleted = deleted +1
				if 'CHANGED' in l2:changed = changed +1
				if 'REN_Frm' in l2:renfom  = renfom  +1
				if 'REN__To' in l2:rento   = rento   +1
			#----------------------------------------------------------------
				if d1 > 0:
					for l1 in list1:
						if l2[1] in l1[3]:
							dataEQ.append((l1[0],l1[1],l2[0],l1[3]))
		#----------------------------------------------------------------
		dataEQ = set(dataEQ)						
		lenEQ  = len(dataEQ)
		#----------------------------------------------------------------
		dx = 'Total in 4 Seconds, Event:%d, Wdir:%d, LiveEqual:%d, Created:%d, Deleted:%d, Changed:%d, RenameFrom:%d, RenameTo:%d, Equal:%d' 
		dx = dx % (d1,d2,d3,created,deleted,changed,renfom,rento,lenEQ)										
		if (int(d1)+int(d2)) > 0:
			sendata(conn,ip1,pr1,dx)	
		if d1 >= 1:
			print '*'*50
			loaddata3()
		if d2 >= 1:
			print '-'*50 
			loaddata4()
		if lenEQ >= 1:
			print '-'*50 
			for eq in dataEQ:
				lsig = getfsig(str(eq[3]))
				lexi = isfile(str(eq[3])) 
				print ' EQ => [%s:%s]:[%s:%s:%s] %s' % (eq[0],eq[1],eq[2],lsig,lexi,eq[3])
		print '*'*50 
		#----------------------------------------------------------------	
#		tm = time.time()
#		tmnow = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H-%M-%S')
		tmnow = datetime.now()
		print ' TimeDate                 :  %s ' % str(tmnow)[:-4]
		if d1 > 0:print ' Jumlah data3  [Event]    : ',str(d1)
		if d2 > 0:
			print ' Jumlah data4  [Wdir]     : ',str(d2)
			print ' ------------------------------------------'
		if d3 > 0:print ' Jumlah data5  [Equal]    : ',str(d3)	
		if lenEQ   > 0:print ' Jumlah dataEQ [Equal]    : ',lenEQ	
		if missfile >0:print ' Jumlah data4  [MISSING]  : ',missfile		
		if created > 0:print ' Jumlah data4  [CREATED]  : ',created	
		if deleted > 0:print ' Jumlah data4  [DELETED]  : ',deleted
		if changed > 0:print ' Jumlah data4  [CHANGED]  : ',changed
		if renfom  > 0:print ' Jumlah data4  [REN_Frm]  : ',renfom	
		if rento   > 0:print ' Jumlah data4  [REN__To]  : ',rento
		
#		print ' Jumlah data3 [type]    : ',str(type(list1))
#		print ' Jumlah data4 [type]    : ',str(type(list2))
#		print ' Jumlah data5 [type]    : ',str(type(list3))
		#----------------------------------------------------------------	
		print '*'*50 + '\n'					
		dataEQ = []
		
	
	def hitsc(): 
		global data3,data4, data5, missfile
		try:
			t1 = datetime.now()  
			while 1:
				time.sleep(0.02)
				if (datetime.now()-t1).seconds > 3:
					data3 = sort_deduplicate(data3) #set(data3)
#					data3 = sorted(set(map(tuple, data3)), reverse=True)
#					data3 = tuple(data3)
#					data3 = set(data3)
					data4 = set(data4)
					data5 = set(data5)
#					os.system('cls') # Nonaktifkan Sementara
					if len(data3) > 0 or len(data4) > 0:
						datareport(data3,data4,data5)
					data3 =[] # From Event
					data4 =[] # From Wdir
					data5 =[] # From Equal
					t1 = datetime.now()
					missfile = 0 
					
		except Exception as E:
			print 'Error : ', str(E)

	def loaddata3():
		global data3,data5
		try:
			for l in data3:		
				l3sig = getfsig(str(l[3]))
				l3exi = isfile(str(l[3])) 	
				if len(l) == 4:
					d3 = ' DATA3 [%s:%s]:[%s:%s] %s %s' % (l[0],l[1],l3sig,l3exi,l[2],l[3])
				if len(l) == 5:
					d3 = ' DATA3 [%s:%s]:[%s:%s] %s %s %s' % (l[0],l[1],l3sig,l3exi,l[2],l[3],l[4])
				print d3
				sendata(conn,ip1,pr1,d3)
			for l5 in data5:
				l5sig = getfsig(str(l5[3]))
				l5exi = isfile(str(l5[3])) 			
				d5 = ' DATA5 [%s:%s]:[%s:%s:%s] %s' % (l5[0],l5[1],l5[2],l5sig,l5exi,l5[3])
				sendata(conn,ip1,pr1,d5)
				print d5
		except Exception as E:
			print ' Loaddata3 Error : ',str(E)
			
			
	def loaddata4():
		global data4, missfile
		for l in data4:			
			l1 = os.path.join(driveC,l[1])
			lsig = getfsig(str(l1))
			lexi = isfile(str(l1)) 
			if lexi == "MISSING" : missfile = missfile + 1
			d4= ' DATA4 [%s]:[%s:%s]: %s' % (l[0],lsig,lexi,l1)
			sendata(conn,ip1,pr1,d4)
			print d4
		
	def compare34(a,f):
		global pid, exe, string, gtag, data5 # data5 experiment
		if f in string:
			lsig = getfsig(str(string))
			lexi = isfile(str(string)) 			
			dt = ' DATA34 [%d:%s]:[%s:%s]: %s %s' % (pid, exe,lsig,lexi, a, string)
			data5.append((pid, exe, a, string)) # Experiment
#			sendata(conn,ip1,pr1,dt)
#			print dt

	def wdir():
		global data4
		while True:	
			try:				
				for ac, fl in watch_dir(14,driveC):
					for fEx in fileEx: 
						if fEx in fl:				
							data4.append((act.get(ac,'---'),fl))
							compare34(act.get(ac,'---'),fl)				

			except:
				pass 

	th1 = threading.Thread(target=start_debug_05)			
	th1.start()
#	
	th2 = threading.Thread(target=wdir)
	th2.start()	
#	
	th4 = threading.Thread(target=hitsc)
	th4.start()
	
#===KET : ========================
#	data3  = list1 : list get from debug event 
#	data4  = list2 : list get wdir event
#	data5  = list3 : list get from compare between data4 to data3 live (var to var)
#	dataEQ = list3 : list get from compare between list2 to list3 (list to list)

	
	
