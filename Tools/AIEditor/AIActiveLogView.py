import socket
import select
import string
import cPickle
import Pmw
from Tkinter import *
from tkSimpleDialog import askstring

PORT = 61257

class InvalidData:
	def __init__(self):
		pass

class MainFrame(Pmw.ScrolledFrame):
	def __init__(self, root):
		Pmw.ScrolledFrame.__init__(self, root)
		self.pRoot = root

		self.bConnected = 0

		self.after_idle(self.AskHostName)

		self.lFrames = []

	def AskHostName(self):
		sHost = None

		#if -1 != string.find(string.lower(socket.gethostname()), "specialhost"):
		#	sHost = askstring("Host Name",
		#		"Enter name of host to watch (leave blank for local host):")
		#else:
		#	sHost = None

		if sHost:
			self.pHost = socket.gethostbyname(sHost)
		else:
			self.pHost = socket.gethostbyname(socket.gethostname())

		#root.title("AI Log Watcher (%s)" % sHost)
		self.TryConnect()

	def TryConnect(self):
		import time
		print "%s: Trying connection %s:%d" % (time.asctime(time.localtime(time.time())), self.pHost, PORT)
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.sock.connect(self.pHost, PORT)

			# Connected.  Start the update loop.
			print "Connected: %s" % time.asctime(time.localtime(time.time()))
			self.AddWidget(Label, text="NEW CONNECTION\n%s" % time.asctime(time.localtime(time.time())))

			self.dButtons = {}

			self.sAccumulatedData = None
			self.iAnticipatedSize = 0

			self.Update()
			return
		except:
			pass

		self.after(2000, self.TryConnect)

	def Update(self):
		import time
		#print "update " + str(time.asctime(time.localtime(time.time())))
		lReads, lWrites, lExceptions = select.select([self.sock], [], [self.sock], 0)
		if lReads:
			for readysocket in lReads:
				try:
					sData = self.sock.recv(1024 * 256)
				except:
					# Lost the connection.
					self.LostConnection()
					return

				if self.sAccumulatedData is None:
					try:
						self.iAnticipatedSize, self.sAccumulatedData = self.SplitSizeAndDataFromInput(sData)
					except InvalidData:
						print "Invalid data received."
				else:
					# Add to the accumulated data.
					self.sAccumulatedData = self.sAccumulatedData + sData

				sTree = None
				if (self.sAccumulatedData is not None):
					if len(self.sAccumulatedData) == self.iAnticipatedSize:
						sTree = self.sAccumulatedData
						self.sAccumulatedData = None
						self.iAnticipatedSize = 0
					elif len(self.sAccumulatedData) > self.iAnticipatedSize:
						#print "Read too much data (size is %d, expected %d).  Trimming..." % (len(self.sAccumulatedData), self.iAnticipatedSize)
						sTree = self.sAccumulatedData[:self.iAnticipatedSize]
						sData = self.sAccumulatedData[self.iAnticipatedSize:]

						self.sAccumulatedData = None
						self.iAnticipatedSize = 0
						try:
							self.iAnticipatedSize, self.sAccumulatedData = self.SplitSizeAndDataFromInput(sData)
						except InvalidData:
							print "Extra data is invalid: %s" % (sData[:10])

				if sTree:
					lTree = cPickle.loads(sTree)
					self.UpdateTree(lTree)
				else:
					self.LostConnection()
					return

		if lExceptions:
			# Something wrong with the socket.  Terminate
			# this connection.
			self.LostConnection()
			return

		self.after(100, self.Update)

	def SplitSizeAndDataFromInput(self, sData):
		iNumSeparator = string.find(sData, "*")
		if not iNumSeparator:
			raise InvalidData

		try:
			iSize = int(sData[:iNumSeparator])
		except ValueError:
			raise InvalidData

		return (iSize, sData[iNumSeparator + 1:])

	def LostConnection(self):
		self.sock = None

		import time
		self.AddWidget(Label, text="LOST CONNECTION\n%s" % time.asctime(time.localtime(time.time())))

		self.TryConnect()

	def UpdateTree(self, lTree):
		sName = lTree[0][1]

		print "Updating tree " + str(sName)
		if self.dButtons.has_key(sName):
			self.dButtons[sName].AddTree(lTree)
		else:
			self.dButtons[sName] = self.AddWidget(TreeButton, text=sName)
			self.dButtons[sName].AddTree(lTree)

	def AddWidget(self, pClass, **dKeywords):
		pWidget = None

		# Choose which frame to add it in.
		bAdded = 0
		for iIndex in range(len(self.lFrames)):
			iNumInFrame, pFrame = self.lFrames[iIndex]

			if iNumInFrame < 20:
				# Add a button to this frame.
				pWidget = self.AddToFrame(iIndex, pClass, dKeywords)
				bAdded = 1

		if not bAdded:
			pButtonFrame = Frame(self.interior())
			pButtonFrame.pack(side=LEFT, fill=Y)
			self.lFrames.append([0, pButtonFrame])
			pWidget = self.AddToFrame(len(self.lFrames) - 1, pClass, dKeywords)

		return pWidget

	def AddToFrame(self, iFrameNum, pClass, dKeywords):
		iNumInFrame, pFrame = self.lFrames[iFrameNum]

		self.lFrames[iFrameNum][0] = iNumInFrame + 1
		pWidget = apply(pClass, (pFrame,), dKeywords)
		pWidget.pack(side=TOP)

		return pWidget

class TreeButton(Button):
	def __init__(self, root, **dKeys):
		dKeys["command"] = self.ShowDetail
		apply(Button.__init__, (self, root,), dKeys)
		self.lTrees = []

	def AddTree(self, lTree):
		self.lTrees.append(lTree)

	def GetTrees(self):
		return self.lTrees

	def ShowDetail(self):
		# Create a window to show the detail of this tree..
		pTop = Toplevel(self)
		pTop.title(self["text"])
		DetailWindow(pTop, self, self["text"]).pack(expand=YES, fill=BOTH)

class DetailWindow(Text):
	def __init__(self, windowroot, pParent, sRootName):
		#Pmw.ScrolledText.__init__(self, windowroot, padx=10, pady=10, hscrollmode='static', vscrollmode='static')
		Text.__init__(self, windowroot)
		scroll = Scrollbar(windowroot, command=self.yview)
		self.configure(yscrollcommand=scroll.set)
		scroll.pack(side=RIGHT, fill=Y) #, expand=YES)

		self.pParent = pParent
		self.sRootName = sRootName

		self.iNumLines = 0

		self.UpdateText()

	def UpdateText(self):
		# Get the list of trees for this root.
		lTrees = self.pParent.GetTrees() #lFrameText[self.sRootName]

		iNumToSkip = self.iNumLines
		iNumLines = 0

		# Add text for the trees to the text window.
		sText = ""
		for lTree in lTrees:
			for iIndent, sTreeText in lTree:
				iNumToSkip = iNumToSkip - 1
				if iNumToSkip <= 0:
					iNumLines = iNumLines + 1
					sText = sText + ("  " * iIndent + sTreeText + "\n")

			iNumToSkip = iNumToSkip - 1
			if iNumToSkip <= 0:
				iNumLines = iNumLines + 1
				sText = sText + "\n"

		# Check if the last line of text is visible...
		try:
			sIndex = self.index(END)
			x,y = string.split(sIndex, ".")
			sIndex = "%d.%d" % (int(x) - 1, int(y))
			if self.bbox(sIndex):
				bAtEnd = 1
			else:
				bAtEnd = 0
		except:
			# Window probably doesn't exist anymore.
			return

		if iNumLines:
			self.insert(END, sText)
			if bAtEnd:
				self.see(END)

		self.iNumLines = self.iNumLines + iNumLines

		self.after(100, self.UpdateText)

def Go():
	global root
	root = Tk()
	root.title("AI Log Watcher")

	pMainFrame = MainFrame(root)
	pMainFrame.pack(fill=BOTH, expand=YES, side=BOTTOM)

	root.mainloop()

if __name__ == "__main__":
	Go()

