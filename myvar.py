#data_filter_tes = ['.txt','.doc','.docx','.ppt','.pptx','.xls','.xlsx','.jpg','.jpeg','.png','.pdf'] # the Experiment
#ffilter = ['.tmp','.exe','.txt','.doc','.docx','.ppt','.pptx','.xls','.xlsx','.jpg','.jpeg','.png','.pdf'] # The First One
#data_filter = ['.zip','.LNK','.lnk','.htm ','.html','.osiris','.doc','.docx','.ppt','.pptx','.xls','.xlsx','.jpg','.jpeg','.png','.pdf','.odg'] # the Experiment
data_filter = ['.zip','.osiris','.doc','.docx','.ppt','.pptx','.xls','.xlsx','.jpg','.jpeg','.png','.pdf','.odg'] # the Experiment

#filesign = ['504B0304','504B0506','504B0708','D0CF11E0A1B11AE1','89504E470D0A1A0A','25504446','FFD8FFDB','FFD8FFE0','FFD8FFE1','FFD8FFE2','FFD8FFE3','FFD8FFE8','FFD8FFE000104A4649460001']

filesign = [
'504B0304', # docx,xlsx,pptx,ods,odp,vsdx
'504B0506', # docx,xlsx,pptx,ods,odp,vsdx : Empty
'504B0708', # docx,xlsx,pptx,ods,odp,vsdx : ?
'D0CF11E0A1B11AE1', # doc,xls,ppt
'89504E470D0A1A0A', # png
'25504446', # pdf
'FFD8FFDB', # jpg,jpeg, Samsung D807 Standard
'FFD8FFE0', # jpg,jpeg Standard
'FFD8FFE1', # jpg,jpeg Standard
'FFD8FFE2', # jpg,jpeg Canon EOS Standard
'FFD8FFE3', # jpg,jpeg Samsung D500 Standard
'FFD8FFE8', # jpg,jpeg, Samsung Standard
'FFD8FFE000104A4649460001' # jpg,jpeg
]
#	act = {
#	  1 : "CREATED",
#	  2 : "DELETED",
#	  3 : "CHANGED",
#	  4 : "REN_Frm",
#	  5 : "REN__To"
#	}
fsignOLD = {
		'504B0304':'docx,xlsx,pptx,ods,odp', # docx,xlsx,pptx,ods,odp,vsdx
		'504B0506':'docx,xlsx,pptx,ods,odp', # docx,xlsx,pptx,ods,odp,vsdx : Empty
		'504B0708':'docx,xlsx,pptx,ods,odp', # docx,xlsx,pptx,ods,odp,vsdx : ?
		'D0CF11E0A1B11AE1':'doc,xls,ppt', # doc,xls,ppt
		'89504E470D0A1A0A':'png', # png
		'25504446':'pdf', # pdf
		'FFD8FFDB':'jpg,jpeg', # jpg,jpeg, Samsung D807 Standard
		'FFD8FFE0':'jpg,jpeg', # jpg,jpeg Standard
		'FFD8FFE1':'jpg,jpeg', # jpg,jpeg Standard
		'FFD8FFE2':'jpg,jpeg', # jpg,jpeg Canon EOS Standard
		'FFD8FFE3':'jpg,jpeg', # jpg,jpeg Samsung D500 Standard
		'FFD8FFE8':'jpg,jpeg', # jpg,jpeg, Samsung Standard
		'FFD8FFE000104A4649460001':'jpg,jpeg' # jpg,jpeg
	}
	
#files_signatures
fsign = {
		'504B0304':'Documentx', # docx,xlsx,pptx,ods,odp,vsdx
		'504B0506':'DocumentX', # docx,xlsx,pptx,ods,odp,vsdx : Empty
		'504B0708':'DocumentX', # docx,xlsx,pptx,ods,odp,vsdx : ?
		'D0CF11E0A1B11AE1':'Document', # doc,xls,ppt
		'89504E470D0A1A0A':'Image', # png
		'25504446':'PdfDocment', # pdf
		'FFD8FFDB':'Image', # jpg,jpeg, Samsung D807 Standard
		'FFD8FFE0':'Image', # jpg,jpeg Standard
		'FFD8FFE1':'Image', # jpg,jpeg Standard
		'FFD8FFE2':'Image', # jpg,jpeg Canon EOS Standard
		'FFD8FFE3':'Image', # jpg,jpeg Samsung D500 Standard
		'FFD8FFE8':'Image', # jpg,jpeg, Samsung Standard
		'FFD8FFE000104A4649460001':'Image' # jpg,jpeg
	}
	
fts='mydb.py'
# *****************************************************************
mal_module =[
	['oleaut32.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'wkscli.dll', 'msasn1.dll', 'kernel32.dll', 'sspicli.dll', 'locale.nls', 'iertutil.dll', 'rpcrt4.dll', 'cryptsp.dll', 'shlwapi.dll', 'profapi.dll', 'gdi32.dll', 'index.dat', 'netutils.dll', 'apisetschema.dll', 'ntdll.dll', 'comctl32.dll', 'usp10.dll', 'user32.dll', 'shell32.dll', 'index.dat', 'index.dat', 'ole32.dll', 'wldap32.dll', 'crypt32.dll', 'ntmarta.dll', 'cryptbase.dll', 'wininet.dll', 'netapi32.dll', 'imm32.dll', 'lpk.dll', 'sortdefault.nls', 'msctf.dll', 'urlmon.dll', 'rsaenh.dll', 'mpr.dll', 'srvcli.dll', 'normaliz.dll', 'dsrole.dll', 'kernelbase.dll', 'uxtheme.dll'], # 2017-01-18-locky-example-2-roaming.exe
	['apphelp.dll', 'devobj.dll', 'propsys.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'shlwapi.dll', 'locale.nls', 'rpcrt4.dll', 'dwmapi.dll', 'profapi.dll', 'setupapi.dll', 'gdi32.dll', 'version.dll', 'apisetschema.dll', 'oleacc.dll', 'ntdll.dll', 'comctl32.dll', 'usp10.dll', 'user32.dll', 'userenv.dll', 'shell32.dll', 'kernel32.dll', 'psapi.dll', 'clbcatq.dll', 'wldap32.dll', 'oleaut32.dll', 'nsi.dll', 'ntmarta.dll', 'cryptbase.dll', 'ws2_32.dll', 'oleaccrc.dll', 'imm32.dll', 'lpk.dll', 'sortdefault.nls', 'msctf.dll', 'system.dll', 'ole32.dll', 'shfolder.dll', 'cfgmgr32.dll', 'kernelbase.dll', 'uxtheme.dll'], # 2017-01-18-locky-example-3-temp_segaxy.exe
	['oleaut32.dll', 'urlmon.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'wkscli.dll', 'msasn1.dll', 'kernel32.dll', 'locale.nls', 'iertutil.dll', 'rpcrt4.dll', 'cryptsp.dll', 'gdi32.dll', 'netutils.dll', 'apisetschema.dll', 'ntdll.dll', 'usp10.dll', 'user32.dll', 'shell32.dll', 'mpr.dll', 'wldap32.dll', 'crypt32.dll', 'ntmarta.dll', 'cryptbase.dll', 'wininet.dll', 'netapi32.dll', 'imm32.dll', 'lpk.dll', 'msctf.dll', 'shlwapi.dll', 'rsaenh.dll', 'ole32.dll', 'srvcli.dll', 'normaliz.dll', 'dsrole.dll', 'kernelbase.dll', 'uxtheme.dll'], # 2017-01-18-locky-example-3-temp_segaxy.exe
	['oleaut32.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'wkscli.dll', 'msasn1.dll', 'kernel32.dll', 'locale.nls', 'iertutil.dll', 'ntdll.dll', 'shlwapi.dll', 'netutils.dll', 'gdi32.dll', 'apisetschema.dll', 'user32.dll', 'shell32.dll', 'rpcrt4.dll', 'mpr.dll', 'crypt32.dll', 'usp10.dll', 'wininet.dll', 'netapi32.dll', 'imm32.dll', 'lpk.dll', 'msctf.dll', 'urlmon.dll', 'ole32.dll', 'srvcli.dll', 'normaliz.dll', 'kernelbase.dll', 'dsrole.dll'], # 2017-01-18-locky-example-1-roaming.exe
	['apphelp.dll', 'devobj.dll', 'propsys.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'kernel32.dll', 'locale.nls', 'rpcrt4.dll', 'dwmapi.dll', 'shlwapi.dll', 'profapi.dll', 'setupapi.dll', 'gdi32.dll', 'version.dll', 'apisetschema.dll', 'oleacc.dll', 'ntdll.dll', 'comctl32.dll', 'usp10.dll', 'user32.dll', 'userenv.dll', 'shell32.dll', 'shdocvw.dll', 'wldap32.dll', 'oleaut32.dll', 'ntmarta.dll', 'cryptbase.dll', 'clbcatq.dll', 'oleaccrc.dll', 'imm32.dll', 'lpk.dll', 'sortdefault.nls', 'msctf.dll', 'ole32.dll', 'shfolder.dll', 'cfgmgr32.dll', 'kernelbase.dll', 'uxtheme.dll'], # 2017-01-18-locky-example-1-roaming.exe
#======================
	['usp10.dll', 'user32.dll', 'imm32.dll', 'kernel32.dll', 'lpk.dll', 'wintrust.dll', 'gdi32.dll', 'msvcrt.dll', 'crypt32.dll', 'msasn1.dll', 'ole32.dll', 'apisetschema.dll', 'ntdll.dll', 'kernelbase.dll', 'msctf.dll', 'rpcrt4.dll'], # 2017-01-17-pseudodarkleech-rig-v-payload-cerber-rad0f304.tmp.exe
	['apphelp.dll', 'devobj.dll', 'propsys.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'rpcrt4.dll', 'dwmapi.dll', 'shlwapi.dll', 'profapi.dll', 'setupapi.dll', 'gdi32.dll', 'version.dll', 'apisetschema.dll', 'oleacc.dll', 'ntdll.dll', 'comctl32.dll', 'usp10.dll', 'user32.dll', 'userenv.dll', 'shell32.dll', 'kernel32.dll', 'psapi.dll', 'clbcatq.dll', 'wldap32.dll', 'oleaut32.dll', 'system.dll', 'ntmarta.dll', 'cryptbase.dll', 'ws2_32.dll', 'oleaccrc.dll', 'imm32.dll', 'lpk.dll', 'msctf.dll', 'nsi.dll', 'ole32.dll', 'shfolder.dll', 'cfgmgr32.dll', 'kernelbase.dll', 'uxtheme.dll'], # 2017-01-18-locky-example-1-roaming.exe
	['oleaut32.dll', 'drprov.dll', 'advapi32.dll', 'sechost.dll', 'wkscli.dll', 'msasn1.dll', 'gdi32.dll', 'kernel32.dll', 'wininet.dll', 'winnsi.dll', 'sspicli.dll', 'uxtheme.dll', 'iertutil.dll', 'rpcrt4.dll', 'cryptsp.dll', 'nlaapi.dll', 'shlwapi.dll', 'sensapi.dll', 'browcli.dll', 'ntlanman.dll', 'ole32.dll', 'peerdist.dll', 'authz.dll', 'ntdll.dll', 'cscapi.dll', 'ws2_32.dll', 'usp10.dll', 'user32.dll', 'userenv.dll', 'shell32.dll', 'rasadhlp.dll', 'wldap32.dll', 'netutils.dll', 'winsta.dll', 'davhlpr.dll', 'dnsapi.dll', 'mswsock.dll', 'rasapi32.dll', 'rasman.dll', 'msvcrt.dll', 'ntmarta.dll', 'cryptbase.dll', 'vboxmrxnp.dll', 'netapi32.dll', 'comctl32.dll', 'rtutils.dll', 'apisetschema.dll', 'lpk.dll', 'kernelbase.dll', 'msctf.dll', 'urlmon.dll', 'crypt32.dll', 'nsi.dll', 'rsaenh.dll', 'mpr.dll', 'srvcli.dll', 'imm32.dll', 'normaliz.dll', 'davclnt.dll', 'profapi.dll', 'dsrole.dll'], # 2017-01-18-locky-example-1-roaming.exe
	['apphelp.dll', 'devobj.dll', 'propsys.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'rpcrt4.dll', 'system.dll', 'dwmapi.dll', 'shlwapi.dll', 'profapi.dll', 'setupapi.dll', 'gdi32.dll', 'version.dll', 'apisetschema.dll', 'oleacc.dll', 'ntdll.dll', 'comctl32.dll', 'usp10.dll', 'user32.dll', 'userenv.dll', 'shell32.dll', 'kernel32.dll', 'psapi.dll', 'clbcatq.dll', 'wldap32.dll', 'oleaut32.dll', 'ntmarta.dll', 'cryptbase.dll', 'ws2_32.dll', 'oleaccrc.dll', 'imm32.dll', 'lpk.dll', 'msctf.dll', 'nsi.dll', 'ole32.dll', 'shfolder.dll', 'cfgmgr32.dll', 'kernelbase.dll', 'uxtheme.dll'], # 2017-01-18-locky-example-2-roaming.exe
	['oleaut32.dll', 'drprov.dll', 'advapi32.dll', 'sechost.dll', 'kernelbase.dll.mui', 'msasn1.dll', 'gdi32.dll', 'kernel32.dll', 'msxml3.dll', 'wininet.dll', 'vssapi.dll', 'winnsi.dll', 'uxtheme.dll', 'iertutil.dll', 'rpcrt4.dll', 'cryptsp.dll', 'nlaapi.dll', 'ws2_32.dll', 'sensapi.dll', 'browcli.dll', 'ntlanman.dll', 'ole32.dll', 'peerdist.dll', 'authz.dll', 'vsstrace.dll', 'ntdll.dll', 'cscapi.dll', 'winsta.dll', 'rpcrtremote.dll', 'usp10.dll', 'user32.dll', 'userenv.dll', 'shell32.dll', 'urlmon.dll', 'rasadhlp.dll', 'wldap32.dll', 'netutils.dll', 'wkscli.dll', 'msxml3r.dll', 'davhlpr.dll', 'dnsapi.dll', 'mswsock.dll', 'rasapi32.dll', 'atl.dll', 'rasman.dll', 'msvcrt.dll', 'ntmarta.dll', 'cryptbase.dll', 'vboxmrxnp.dll', 'netapi32.dll', 'comctl32.dll', 'rtutils.dll', 'apisetschema.dll', 'lpk.dll', 'nsi.dll', 'msctf.dll', 'shlwapi.dll', 'crypt32.dll', 'sspicli.dll', 'clbcatq.dll', 'rsaenh.dll', 'mpr.dll', 'srvcli.dll', 'imm32.dll', 'normaliz.dll', 'davclnt.dll', 'kernelbase.dll', 'profapi.dll', 'dsrole.dll'], # 2017-01-18-locky-example-2-roaming.exe
	['apphelp.dll', 'devobj.dll', 'propsys.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'rpcrt4.dll', 'dwmapi.dll', 'profapi.dll', 'setupapi.dll', 'gdi32.dll', 'version.dll', 'apisetschema.dll', 'oleacc.dll', 'ntdll.dll', 'comctl32.dll', 'usp10.dll', 'user32.dll', 'userenv.dll', 'shell32.dll', 'kernel32.dll', 'psapi.dll', 'clbcatq.dll', 'wldap32.dll', 'oleaut32.dll', 'nsi.dll', 'ntmarta.dll', 'cryptbase.dll', 'ws2_32.dll', 'oleaccrc.dll', 'imm32.dll', 'system.dll', 'lpk.dll', 'msctf.dll', 'shlwapi.dll', 'ole32.dll', 'shfolder.dll', 'cfgmgr32.dll', 'kernelbase.dll', 'uxtheme.dll'], # 2017-01-18-locky-example-3-temp_segaxy.exe
	['oleaut32.dll', 'drprov.dll', 'advapi32.dll', 'sechost.dll', 'kernelbase.dll.mui', 'msasn1.dll', 'gdi32.dll', 'kernel32.dll', 'wininet.dll', 'winnsi.dll', 'sspicli.dll', 'uxtheme.dll', 'iertutil.dll', 'rpcrt4.dll', 'cryptsp.dll', 'nlaapi.dll', 'sensapi.dll', 'browcli.dll', 'ntlanman.dll', 'ole32.dll', 'peerdist.dll', 'ws2_32.dll', 'authz.dll', 'vsstrace.dll', 'ntdll.dll', 'cscapi.dll', 'winsta.dll', 'rpcrtremote.dll', 'usp10.dll', 'user32.dll', 'userenv.dll', 'shell32.dll', 'urlmon.dll', 'rasadhlp.dll', 'wldap32.dll', 'netutils.dll', 'wkscli.dll', 'davhlpr.dll', 'dnsapi.dll', 'mswsock.dll', 'rasapi32.dll', 'rasman.dll', 'msvcrt.dll', 'ntmarta.dll', 'cryptbase.dll', 'vboxmrxnp.dll', 'netapi32.dll', 'comctl32.dll', 'rtutils.dll', 'apisetschema.dll', 'lpk.dll', 'nsi.dll', 'msctf.dll', 'shlwapi.dll', 'crypt32.dll', 'clbcatq.dll', 'rsaenh.dll', 'mpr.dll', 'srvcli.dll', 'imm32.dll', 'normaliz.dll', 'davclnt.dll', 'kernelbase.dll', 'profapi.dll', 'dsrole.dll'], # 2017-01-18-locky-example-3-temp_segaxy.exe
	['apphelp.dll', 'devobj.dll', 'propsys.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'rpcrt4.dll', 'dwmapi.dll', 'shlwapi.dll', 'profapi.dll', 'setupapi.dll', 'wldap32.dll', 'gdi32.dll', 'version.dll', 'apisetschema.dll', 'oleacc.dll', 'ntdll.dll', 'system.dll', 'usp10.dll', 'user32.dll', 'userenv.dll', 'shell32.dll', 'kernel32.dll', 'psapi.dll', 'clbcatq.dll', 'imm32.dll', 'oleaut32.dll', 'ntmarta.dll', 'cryptbase.dll', 'ws2_32.dll', 'oleaccrc.dll', 'comctl32.dll', 'lpk.dll', 'msctf.dll', 'nsi.dll', 'ole32.dll', 'shfolder.dll', 'cfgmgr32.dll', 'kernelbase.dll', 'uxtheme.dll'], # 2017-01-18-locky-example-4-tempagato.exe
	['oleaut32.dll', 'drprov.dll', 'advapi32.dll', 'sechost.dll', 'kernelbase.dll.mui', 'msasn1.dll', 'gdi32.dll', 'kernel32.dll', 'wininet.dll', 'winnsi.dll', 'sspicli.dll', 'uxtheme.dll', 'iertutil.dll', 'rpcrt4.dll', 'cryptsp.dll', 'nlaapi.dll', 'ws2_32.dll', 'sensapi.dll', 'browcli.dll', 'ntlanman.dll', 'ole32.dll', 'peerdist.dll', 'authz.dll', 'vsstrace.dll', 'ntdll.dll', 'cscapi.dll', 'winsta.dll', 'wldap32.dll', 'rpcrtremote.dll', 'usp10.dll', 'user32.dll', 'userenv.dll', 'shell32.dll', 'urlmon.dll', 'rasadhlp.dll', 'netutils.dll', 'wkscli.dll', 'davhlpr.dll', 'dnsapi.dll', 'mswsock.dll', 'rasapi32.dll', 'rasman.dll', 'msvcrt.dll', 'ntmarta.dll', 'cryptbase.dll', 'vboxmrxnp.dll', 'netapi32.dll', 'comctl32.dll', 'rtutils.dll', 'apisetschema.dll', 'lpk.dll', 'nsi.dll', 'msctf.dll', 'shlwapi.dll', 'crypt32.dll', 'clbcatq.dll', 'rsaenh.dll', 'mpr.dll', 'srvcli.dll', 'imm32.dll', 'normaliz.dll', 'davclnt.dll', 'kernelbase.dll', 'profapi.dll', 'dsrole.dll'], # 2017-01-18-locky-example-4-tempagato.exe
	['apphelp.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'rpcrt4.dll', 'shlwapi.dll', 'gdi32.dll', 'apisetschema.dll', 'user32.dll', 'shell32.dll', 'ntdll.dll', 'rasadhlp.dll', 'dnsapi.dll', 'mswsock.dll', 'usp10.dll', 'ws2_32.dll', 'imm32.dll', 'lpk.dll', 'wsock32.dll', 'msctf.dll', 'nsi.dll', 'kernel32.dll', 'kernelbase.dll'], # 2017-01-18-pseudodarkleech-rig-v-payload-rad625be.tmp.exe
# ================================
	['mscoree.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'ntdll.dll', 'shlwapi.dll', 'profapi.dll', 'mscoreei.dll', 'gdi32.dll', 'apisetschema.dll', 'mscorwks.dll', 'user32.dll', 'shell32.dll', 'rpcrt4.dll', 'ole32.dll', 'usp10.dll', 'msvcr80.dll', 'imm32.dll', 'lpk.dll', 'msctf.dll', 'kernel32.dll', 'kernelbase.dll'], # ransom-jigsaw.exe
	['mscoree.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'mscorwks.dll', 'shlwapi.dll', 'profapi.dll', 'mscoreei.dll', 'gdi32.dll', 'apisetschema.dll', 'ntdll.dll', 'mscorlib.ni.dll', 'usp10.dll', 'user32.dll', 'shell32.dll', 'rpcrt4.dll', 'ole32.dll', 'cryptbase.dll', 'msvcr80.dll', 'imm32.dll', 'lpk.dll', 'msctf.dll', 'kernel32.dll', 'kernelbase.dll', 'uxtheme.dll'], # ransom-jigsaw.exe
	['usp10.dll', 'user32.dll', 'imm32.dll', 'rpcrt4.dll', 'lpk.dll', 'clusapi.dll', 'advapi32.dll', 'cryptdll.dll', 'msvcrt.dll', 'sechost.dll', 'gdi32.dll', 'msctf.dll', 'kernel32.dll', 'apisetschema.dll', 'kernelbase.dll', 'dbghelp.dll', 'ntdll.dll'], # ransom-matsnu.com
	['mscoree.dll', 'advapi32.dll', 'msvcrt.dll', 'msvcr80.dll', 'mscorwks.dll', 'mscorjit.dll', 'profapi.dll', 'mscoreei.dll', 'gdi32.dll', 'apisetschema.dll', 'ntdll.dll', 'mscorlib.ni.dll', 'usp10.dll', 'user32.dll', 'shell32.dll', 'rpcrt4.dll', 'ole32.dll', 'cryptbase.dll', 'sechost.dll', 'imm32.dll', 'lpk.dll', 'msctf.dll', 'shlwapi.dll', 'kernel32.dll', 'kernelbase.dll', 'uxtheme.dll'], # ransom-petrwrap-2.exe
#==================================
	['mscoree.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'mscorwks.dll', 'shlwapi.dll', 'profapi.dll', 'mscoreei.dll', 'gdi32.dll', 'apisetschema.dll', 'ntdll.dll', 'mscorlib.ni.dll', 'usp10.dll', 'user32.dll', 'shell32.dll', 'rpcrt4.dll', 'ole32.dll', 'cryptbase.dll', 'msvcr80.dll', 'imm32.dll', 'lpk.dll', 'msctf.dll', 'kernel32.dll', 'kernelbase.dll', 'uxtheme.dll'], # ransom-jigsaw.exe
	['usp10.dll', 'ws2_32.dll', 'user32.dll', 'imm32.dll', 'rtutils.dll', 'lpk.dll', 'nsi.dll', 'msctf.dll', 'apisetschema.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'gdi32.dll', 'ntdll.dll', 'kernel32.dll', 'rasapi32.dll', 'rasman.dll', 'kernelbase.dll', 'rpcrt4.dll'], # ransom-locky.exe
	['mscoree.dll', 'advapi32.dll', 'msvcrt.dll', 'msvcr80.dll', 'mscorwks.dll', 'mscorjit.dll', 'profapi.dll', 'mscoreei.dll', 'gdi32.dll', 'apisetschema.dll', 'ntdll.dll', 'mscorlib.ni.dll', 'usp10.dll', 'user32.dll', 'shell32.dll', 'rpcrt4.dll', 'ole32.dll', 'cryptbase.dll', 'sechost.dll', 'imm32.dll', 'lpk.dll', 'msctf.dll', 'shlwapi.dll', 'kernel32.dll', 'kernelbase.dll', 'uxtheme.dll'], # ransom-petrwrap-2.exe
	['oleaut32.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'ntdll.dll', 'quartz.dll', 'shlwapi.dll', 'gdi32.dll', 'apisetschema.dll', 'usp10.dll', 'user32.dll', 'shell32.dll', 'rpcrt4.dll', 'ole32.dll', 'cryptbase.dll', 'clbcatq.dll', 'imm32.dll', 'lpk.dll', 'winmm.dll', 'msctf.dll', 'kernel32.dll', 'kernelbase.dll', 'uxtheme.dll'], # ransom-teslacrypt-2.exe
	['usp10.dll', 'user32.dll', 'imm32.dll', 'rpcrt4.dll', 'lpk.dll', 'msctf.dll', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'gdi32.dll', 'kernel32.dll', 'apisetschema.dll', 'kernelbase.dll', 'ntdll.dll'], # ransom-wannacry.exe
	['oleaut32.dll', 'urlmon.dll', 'odbc32.dll', 'mfc42.dll.mui', 'advapi32.dll', 'msvcrt.dll', 'sechost.dll', 'msasn1.dll', 'iertutil.dll', 'rpcrt4.dll', 'odbcint.dll.mui', 'dwmapi.dll', 'mfc42.dll', 'shlwapi.dll', 'riched32.dll', 'gdi32.dll', 'apisetschema.dll', 'ntdll.dll', 'comctl32.dll', 'windowscodecs.dll', 'user32.dll', 'shell32.dll', 'kernel32.dll', 'wininet.dll', 'msvcp60.dll', 'crypt32.dll', 'nsi.dll', 'riched20.dll', 'usp10.dll', 'ws2_32.dll', 'imm32.dll', 'lpk.dll', 'odbcint.dll', 'msctf.dll', 'ole32.dll', 'normaliz.dll', 'kernelbase.dll', 'iconcodecservice.dll', 'uxtheme.dll'], # @wanadecryptor@.exe

]


lts = [
	['satu','dua','tiga','lima'],
	['dua','tiga','empat','lima'],
	['tujuh','lima'],
	['sembilan','delapan'],
	['enam','lima']]



