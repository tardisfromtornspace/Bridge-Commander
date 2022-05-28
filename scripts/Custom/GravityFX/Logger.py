from bcdebug import debug
###########################################################################################################################
###########################################################################################################################
##    THE   LOGGER SCRIPT         v1.2
##			by Fernando Aluani aka USS Frontier
## License:
## 	- You can't change this file, but you may distribute it with your mod if you use it on your mod,
##	  and credit must be given to me.
#####################################################################################
##  With this script, and the LogCreator class contained in this script, you can easily make a log of what happens when 
##  your code is used in-game.
##  After creating the LogCreator obj, with a single function you add a string to the log. The LogCreator automaticaly
##  arranges the strings added by the time(hour:min:sec weekday day/month/year) when they were added. And it writes the
##  string to the text file in the same time, so even if the game suddenly crashes, you'll see what was the last line
##  called.
#########
# WARNING: after some tests, i discovered that BC's python Time module doesn't work correctly, dunno why...
#		it doesn't return the exact time, resulting that sometimes it return the same time over and over again...
#	As so, the LogCreator will try to use the TimeMeasurement script, contained in GravityFX, to get a more precise time.
###########################################################################################################################
###############################################################################################
#@@@@@@ initializing/creating the LogCreator
######
# 	- initialize: LogCreator(name, path, bIsDummy = 0) 
#     	       name --> the name of the LogCreator obj you're making, if not given, the LogCreator class will use the
#				    path as the name
#			 path --> the filepath (with the file extension) to the file in which the log will be printed
#
#			 bIsDummy --> a bool (1 for true, 0 for false), determining if this is a dummy logcreator. dummy loggers
#					  doesn't write the logged strings to the file. defaults to 0 (not dummy)
#  Example on how to use:
#	import Logger
#	pLogger = Logger.LogCreator("Mod X", "script\Custom\ModXlog.txt")
#	pLogger.LogString("just started the Mod X logger")      --- See functions below
#
# TIP: you'll probably want to make a single LogCreator obj for a single script or a single class
#################################################################################################################
#@@@@@@@ The functions of the LogCreator :
######
#	-LogString(string)
#		- This is the function you'll most probaly use only. It is used to add a string to the log. Also, the LogCreator 
#		  will automaticaly arrange the strings added by the time when they were added.
#		Arguments:
#		> string --> the string to be added to the log
#	-LogError and LogImportant (string)
#		- these functions will behave like the normal LogString, adding a line to the log. However, these 2 will add
#		  the line inside a special Error or Important tag, so that it is easier to notice in the log text file.
#	-LogException(exception, string = "")
#		- this function is to be used to log python errors. the exception arg is a python exception obj, normally
#		  with a try/except statement (check GravityFX or Galaxy Charts to see how to use this properly). Then the 
#		  LogCreator will write various lines to the log, telling the type of error, the traceback of the error, and so
#		  on.
#		  The optional string argument is a simple string line to be added before the exception lines itself.
#		  And these lines, both the optional string and the exception strings, will appear inside a Exception tag
#		  to make easier to see it in the text file.
#	-GetTime()
#		- Used internally the the LogCreator to arrange the log by time. This returns the exact time now in the form 
#		   hour:minutes:seconds of day/month/year, weekday
#	-QuitDumpEnd()
#		- This is also used internally. Called with the QUIT game event, it adds that last strings, showing when 
#		  the log ended (because the game was quitted)
#	-DumpLines(stringsList)
#		- this is the master write function, all the other Log functions use this one to write their lines to the log
#		  file.
#		  it writes each string line contained in the list of strings arg stringsList to the log text file.
######################################################################################################################
import App
import nt
import time
import string

LogCreatorsQUITlist = []
QUIThandlerCreated = 0
lCreatedLogCreatorNames = []
lCreatedLogPaths = []

class  LogCreator:
	def __init__(self, name, path, bIsDummy = 0):
		debug(__name__ + ", __init__")
		global LogCreatorsQUITlist, QUIThandlerCreated, lCreatedLogCreatorNames, lCreatedLogPaths
		if path in lCreatedLogPaths:
			name = name+"[2]"
			path = string.replace(path, ".txt", "[2].txt")
		try:
			GravFXlib = __import__('Custom.GravityFX.GravityFXlib')
			if name == None:
				ID = GravFXlib.GetUniqueID(path+" LogCreator")
			else:
				ID = GravFXlib.GetUniqueID(name+" LogCreator")
		except:
			if name == None:
				ID = path+" LogCreator"
			else:
				ID = name+" LogCreator"
		self.Name = name
		self.LCID = ID
		self.CLASS = "Log Creator"
		self.IsDummy = bIsDummy
		self.FilePath = path
		self.WasFileCreated = 0
		if name in lCreatedLogCreatorNames:
			self.WasFileCreated = 1
		self.NotQuitted = 1
		self.CurrentTime = ""
		self.DynamicTS = []
		self.WroteDTS = 0
		if QUIThandlerCreated == 0:
			pTopWindow = App.TopWindow_GetTopWindow()
			if pTopWindow:
				pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
				if pOptionsWindow:
					pOptionsWindow.AddPythonFuncHandlerForInstance(App.ET_QUIT, __name__+".LoggerQuitHandler")
					QUIThandlerCreated = 1
		lCreatedLogPaths.append(self.FilePath)
		LogCreatorsQUITlist.append(self)
	def LogString(self, s):
		debug(__name__ + ", LogString")
		l = [ "#>>>"+str(s) ]
		self.DumpLines(l)
	def AddStaticStringToDTS(self, s):
		debug(__name__ + ", AddStaticStringToDTS")
		self.DynamicTS.append(s)
	def AddVariableStringToDTS(self, s):
		debug(__name__ + ", AddVariableStringToDTS")
		self.DynamicTS.append("<DTSC>"+s)
	def ClearDynamicTS(self):
		debug(__name__ + ", ClearDynamicTS")
		self.DynamicTS = []
	def LogDynamicTS(self):
		debug(__name__ + ", LogDynamicTS")
		if self.WroteDTS == 1:
			return
		sTime = self.GetTime()	
		if self.WasFileCreated == 0:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_CREAT|nt.O_TRUNC)
			nt.write(file, "#This is the dump of the LogCreator: "+str(self)+ "\n")
			nt.write(file, "#This log file was created on: "+sTime+ "\n########################################\n")
			self.WasFileCreated = 1
			lCreatedLogCreatorNames.append(self.Name)
		else:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_APPEND)
		nt.write(file, "< ======== Dynamic TS ========= >"+ "\n")
		for sLine in self.DynamicTS:
			nt.write(file, str(sLine)+ "\n")
		nt.write(file, "< ========== END DTS ========== >"+ "\n")
		nt.close(file)
		self.WroteDTS = 1
		return
	def LogError(self, s):
		debug(__name__ + ", LogError")
		l = []
		l.append("< --------------------------------------- >")
		l.append("<----------------- ERROR ----------------->")
		l.append("-----> "+str(s) )
		l.append("<--------------- END ERROR --------------->")
		l.append("< --------------------------------------- >")
		self.DumpLines(l)
	def LogImportant(self, s):
		debug(__name__ + ", LogImportant")
		l = []
		l.append("< =========================================== >")
		l.append("<================= IMPORTANT =================>")
		l.append("-----> "+str(s) )
		l.append("<=============== END IMPORTANT ===============>")
		l.append("< =========================================== >")
		self.DumpLines(l)
	def LogException(self, et, s = ""):
		debug(__name__ + ", LogException")
		l = []
		l.append("< ------------------------------------------- >")
		l.append("<----------------- EXCEPTION ----------------->")
		if s != "":
			l.append( "-----> "+str(s) )
		l.append( "Traceback of Error: "+str(et[0])+": "+str(et[1]) )
		if et[2]:
			tl = GetTracebackList(et[2])
		else:
			tl = []
		for tline in tl:
			sline = "Script: \""+str(tline[0])+"\", Line "+str(tline[1])+", in the function \""+str(tline[2])+"\"."
			l.append( sline )
		l.append("<--------------- END EXCEPTION --------------->")
		l.append("< ------------------------------------------- >")
		self.DumpLines(l)
	def DumpLines(self, lStrings):
		debug(__name__ + ", DumpLines")
		global lCreatedLogCreatorNames
		if self.IsDummy == 1:
			return
		if len(lStrings) <= 0:
			return

		sTime = self.GetTime()
		bAddTimeStamp = 0
		if sTime != self.CurrentTime:
			bAddTimeStamp = 1
			self.CurrentTime = sTime
		
		if self.WasFileCreated == 0:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_CREAT|nt.O_TRUNC)
			nt.write(file, "#This is the dump of the LogCreator: "+str(self)+ "\n")
			nt.write(file, "#This log file was created on: "+sTime+ "\n########################################\n")
			self.WasFileCreated = 1
			lCreatedLogCreatorNames.append(self.Name)
		else:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_APPEND)

		if bAddTimeStamp == 1:
			nt.write(file, "## -------------------- ##"+ "\n")
			nt.write(file, "####################\n#######>>>"+str(sTime)+ "\n")
		for sLine in lStrings:
			nt.write(file, str(sLine)+ "\n")
		nt.close(file)

	def GetTime(self):
		debug(__name__ + ", GetTime")
		try:
			Time = __import__('Custom.Autoload.TimeMeasurement')
			return Time.Clock.GetTimeString()
		except:
			return time.asctime(time.localtime(time.time()))
	def QuitDumpEnd(self):
		debug(__name__ + ", QuitDumpEnd")
		if self.IsDummy == 1:
			return
		if self.WasFileCreated and self.NotQuitted:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_APPEND)
			nt.write(file, "########################################\n# "+self.GetTime()+"\n#Ending of log dump - User is quiting the game\n########################################\n")
			nt.close(file)
			self.NotQuitted = 0
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+self.LCID+">"

###################################################################################################
# The Dummy Logger
#  - Since the LogCreator class can be set as dummy - that is, it won't log anything - This class doesn't really need to
#    be here, except for backward compatibility with some mods that are using Logger, and this class.
#    This can be used alternatively to make a dummy logger, incase your script creates or not a logger based on some
#    setting but your code is using the logger. So if the logger won't be created, just set it as this type of logger
#    so that your code won't require anything else than the LogCreator.LogString() lines.
#  - The difference between using this and simply setting a LogCreator as dummy is that all functions of this class
#    will not work (not return anything). While in a LogCreator set as dummy, some functions of it will still return a
#    value (like using log.GetTime()  ).
##########
# Example:
#	import Logger
#	if UserWantsLogs == 1:
#		pLogger = Logger.LogCreator("Mod X", "scripts\Custom\ModXlog.txt")
#	else:	
#		pLogger = Logger.DummyLogger()
## or you can use this instead to create a dummy logger
#	import Custom.GravityFX.Logger
#	pLogger = Logger.LogCreator("Mod X", "scripts\Custom\ModXlog.txt")
#	pLogger.IsDummy = 1
#
## then in the code that will be logged just use***
#	*code*
#	pLogger.LogString(string)
#	*code*
#####
# Note that you can also use LogError(string), LogImportant(string) and LogException(exception, string =None)
###################################################################################################
class DummyLogger:
	def __init__(self):
		debug(__name__ + ", __init__")
		self.CLASS = "Dummy Log Creator"
		self.IsDummy = 1
	def LogString(self, string):
		debug(__name__ + ", LogString")
		pass
	def AddStaticStringToDTS(self, s):
		debug(__name__ + ", AddStaticStringToDTS")
		pass
	def AddVariableStringToDTS(self, s):
		debug(__name__ + ", AddVariableStringToDTS")
		pass
	def ClearDynamicTS(self):
		debug(__name__ + ", ClearDynamicTS")
		pass
	def LogDynamicTS(self):
		debug(__name__ + ", LogDynamicTS")
		pass
	def LogError(self, string):
		debug(__name__ + ", LogError")
		pass
	def LogImportant(self, string):
		debug(__name__ + ", LogImportant")
		pass
	def LogException(self, et, string = ""):
		debug(__name__ + ", LogException")
		pass
	def DumpLines(self, lStrings):
		debug(__name__ + ", DumpLines")
		pass
	def QuitDumpEnd(self):
		debug(__name__ + ", QuitDumpEnd")
		pass
	def GetTime(self):
		debug(__name__ + ", GetTime")
		pass


###################################################################################################
# LoggerQuitHandler
# - This is the handler for the game quit event, to print all logs.
#   Don't use it, don't mess with it.
###################################################################################################
def LoggerQuitHandler(pObject, pEvent):
	debug(__name__ + ", LoggerQuitHandler")
	global LogCreatorsQUITlist
	for LC in LogCreatorsQUITlist:
		LC.QuitDumpEnd()
	pObject.CallNextHandler(pEvent)

#######################################################
# I made this function based on the function "extract_tb" from the traceback module i found in my BC directory,
# that module isn't from stock BC, so i assume a mod has put it there, but i do not know which one...
# So i would like to thank and credit the person that made that module (because it is diferent than the traceback module 
# from python 2.4) for this function.
###
# the next function, "tb_lineno" is also from the module i mentioned, so i again thank and credit the person who did it.
# The next function is used by this function, and this function is used by LogCreator.LogException to get the traceback
# strings (script, line number, function name, line) from the given traceback object.
####################################################
def GetTracebackList(tb, limit = None):
	debug(__name__ + ", GetTracebackList")
	import sys
	if limit is None:
		if hasattr(sys, 'tracebacklimit'):
			limit = sys.tracebacklimit
	list = []
	n = 0
	while tb is not None and (limit is None or n < limit):
		f = tb.tb_frame
		lineno = tb_lineno(tb)
		co = f.f_code
		filename = co.co_filename
		name = co.co_name
		list.append((filename, lineno, name))
		tb = tb.tb_next
		n = n+1
	return list

#########
## I got this function from a module called "traceback" that i found in my BC directory, the following comment is what was
## commented above the function in that module
#####
# Calculate the correct line number of the traceback given in tb (even
# with -O on).
# Coded by Marc-Andre Lemburg from the example of PyCode_Addr2Line()
# in compile.c.
# Revised version by Jim Hugunin to work with JPython too.
#########
def tb_lineno(tb):
	debug(__name__ + ", tb_lineno")
	c = tb.tb_frame.f_code
	if not hasattr(c, 'co_lnotab'):
		return tb.tb_lineno
	tab = c.co_lnotab
	line = c.co_firstlineno
	stopat = tb.tb_lasti
	addr = 0
	for i in range(0, len(tab), 2):
		addr = addr + ord(tab[i])
		if addr > stopat:
			break
		line = line + ord(tab[i+1])
	return line