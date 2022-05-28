#!/usr/bin/python
if __name__ == '__main__':
	# AIEditor needs to be imported, not execfile'd, as appears to
	# be the default when python.exe opens it (from double-clicking).
	import AIEditor
	AIEditor.Go()
	import sys
	sys.exit()

from Tkinter import *
import CanvasUtils
import re
import string
import os
import os.path

sSeparationBlock = "\t#########################################\n"
sBaseTitle = "AI Editor"

# For processing configuration data:
def ProcessConfigData(sKeyword, sData):
	dKeyFuncMap = {
		"ScriptsPath"	: SetScriptsPath,
		"ConditionPath"		: SetConditionPath,
		"PlainAIPath"		: SetPlainAIPath,
		"ActionPaths"		: SetActionPaths,
		"AdvancedFeatures"	: SetAdvancedFeatures,
		"AILoadPath" : SetAILoadPath,
		"CompoundPath" : SetCompoundPath }

	try:
		pFunc = dKeyFuncMap[sKeyword]
	except KeyError:
		print "Unrecognized key: " + pFunc
		return

	pFunc(sData)

def SetScriptsPath(sData):
	global g_sScriptsPath
	g_sScriptsPath = os.path.abspath(sData)

def GetScriptsPath():
	return g_sScriptsPath

def SetConditionPath(sData):
	global g_sConditionsDir
	g_sConditionsDir = sData

def GetConditionPath():
	return g_sConditionsDir

def SetPlainAIPath(sData):
	global g_sPlainAIDir
	g_sPlainAIDir = sData

def GetPlainAIPath():
	return g_sPlainAIDir

def SetActionPaths(sData):
	lsPaths = string.split(sData, ",")

	import ActionUtils
	ActionUtils.SetProjectDirectories( lsPaths )

def SetAdvancedFeatures(sData):
	global g_bAdvancedFeatures
	g_bAdvancedFeatures = int(sData)

def GetAdvancedFeatures():
	return g_bAdvancedFeatures

def SetAILoadPath(sData):
	global g_sAILoadPath
	g_sAILoadPath = sData

def GetAILoadPath():
	return g_sAILoadPath

def SetCompoundPath(sData):
	global g_sCompoundPath
	g_sCompoundPath = sData

def GetCompoundPath():
	global g_sCompoundPath
	return g_sCompoundPath

def Initialize():
	# Set default config values.
	sBCMain = "../.."
	SetScriptsPath(sBCMain + "/scripts")
	SetConditionPath(sBCMain + "/scripts/Conditions")
	SetPlainAIPath(sBCMain + "/scripts/AI/PlainAI")
	SetActionPaths(
		sBCMain + "/scripts/AI," +
		sBCMain + "/scripts/Bridge," +
		sBCMain + "/scripts/Tactical" )
	SetAdvancedFeatures(0)
	SetAILoadPath(sBCMain + "/scripts")
	SetCompoundPath(sBCMain + "/scripts/AI/Compound")

	# Whether or not the current AI is a Builder AI.
	global g_bIsBuilderAI
	g_bIsBuilderAI = IntVar()
	g_bIsBuilderAI.set(0)

	# Read in our starting paths, and our various search paths,
	# from our config file.
	try:
		pFile = open("AIEditor.cfg", "r")
	except IOError:

		pFile = None

	if pFile:
		sLine = pFile.readline()
		while sLine:
			iKeywordEnd = string.find(sLine, "=")
			if iKeywordEnd > 0:
				sKeyword = string.strip( sLine[:iKeywordEnd] )
				sData = string.strip( sLine[(iKeywordEnd + 1):] )

				print "Found config pair: [%s:%s]" % (sKeyword, sData)

				ProcessConfigData(sKeyword, sData)
	
			sLine = pFile.readline()
		pFile.close()

class AIMenus(Frame):
	"Basic menus for accessing basic functionality."
	def __init__(self, parent, pOutput, **kw):
		# Base class init
		apply(Frame.__init__, (self, parent), kw)

		self.pOutput = pOutput

		# Add our main menu items:
		pFileMenu = Menubutton(self, text="File", relief="raised", underline=0)
		pFileMenu.pack(side=LEFT, anchor=NW)
		pFileMenu.menu = Menu(pFileMenu)

		pFileMenu.menu.add_command(label="Load AI", underline=0, command=self.LoadAI)
		pFileMenu.menu.add_command(label="Save AI", underline=0, command=self.SaveAI)
		pFileMenu.menu.add("separator")
		pFileMenu.menu.add_command(label="Clear All", underline=0, command=self.ClearAll)
		pFileMenu.menu.add_command(label="QUIT", underline=0, command=parent.quit) #destroy)
		pFileMenu["menu"] = pFileMenu.menu

		# Create AI... options:
		pAIMenu = Menubutton(self, text="Create AI", relief='raised', underline=0)
		pAIMenu.pack(side=LEFT, anchor=NW)
		pAIMenu.menu = Menu(pAIMenu)

		# Add the standard AI types.
		lNameClassMap = ( ("Conditional",	ConditionalAIEntity),
	                         ("Scripted (Plain)",	PlainAIEntity),
		                 ("Preprocessing",	PreprocessingAIEntity),
		                 ("Priority List",	PriorityListAIEntity),
		                 ("Sequence",		SequenceAIEntity),
		                 ("Random",		RandomAIEntity),
		                 ("(compound)",		CompoundAIEntity) )
		for sName, cType in lNameClassMap:
			pAIMenu.menu.add_command(label=sName, command=lambda self=self, cType=cType: self.pOutput.AddEntity(cType))

		# Add the AI's under the "Special" cascade...
		pSpecialCascade = Menu(pAIMenu.menu)
		pSpecialCascade.add_command(label="Fire Preprocess", command=self.CreateFirePreprocess)
		pSpecialCascade.add_command(label="Tractor Beam Docking Preprocess", command = self.CreateTractorDockingPreprocess)
		pSpecialCascade.add_command(label="Select Target Preprocess", command=self.CreateSelectTargetPreprocess)
		pSpecialCascade.add_command(label="Avoid Obstacles Preprocess", command=self.CreateAvoidCollisionsPreprocess)
		pSpecialCascade.add_command(label="Alert Level Preprocess", command=self.CreateAlertLevelPreprocess)
		pSpecialCascade.add_command(label="Cloaking Preprocess", command=self.CreateCloakPreprocess)
		pSpecialCascade.add_command(label="Starbase Attack AI", command=self.CreateStarbaseAttack)
		pSpecialCascade.add_command(label="Felix Report", command=self.CreateFelixReport)
		pSpecialCascade.add_command(label="AI Status Update", command=self.CreateAIStatusUpdate)

		pAIMenu.menu.add("separator")
		pAIMenu.menu.add_cascade(label="Special", underline=0, menu=pSpecialCascade)

		pAIMenu["menu"] = pAIMenu.menu

		# Create the "Advanced" menu.
		self.pAdvancedBool = IntVar()
		pAdvancedMenu = Menubutton(self, text="Advanced", relief="raised", underline=0)
		pAdvancedMenu.pack(side=LEFT, anchor=NW)
		pAdvancedMenu.menu = Menu(pAdvancedMenu)

		pAdvancedMenu.menu.add_command(label="Edit Pre-AI save text", command=self.EditPrefixText)
		pAdvancedMenu.menu.add_checkbutton(label="AI Distributes Building", variable = g_bIsBuilderAI, onvalue=1, offvalue=0)
		pAdvancedMenu.menu.add_checkbutton(label="Advanced Features", command=self.SetAdvancedFeatures, variable = self.pAdvancedBool, onvalue=1, offvalue=0)
		self.pAdvancedBool.set(GetAdvancedFeatures())

		pAdvancedMenu["menu"] = pAdvancedMenu.menu

		# Create Action...  menu:
		#self.SetupActionMenu()


		# Done.

	def SetupActionMenu(self):
		# Create the top button.
		pActionMenu = Menubutton(self, text="Create Action", relief="raised", underline = 8)
		pActionMenu.pack(side=LEFT, anchor=NW)
		pActionMenu.menu = Menu(pActionMenu)

		# Load all the action types...
		import ActionUtils
		lsActions, lsSequences, dFiles = ActionUtils.GetProjectActions()
		
		# Add buttons...
		for sAction in lsActions:
			if not (sAction in lsSequences):
				pActionMenu.menu.add_command(label=sAction, command=lambda self=self, sClass=sAction: self.CreateAction(sClass))

		pSequenceCascade = Menu(pActionMenu.menu)
		for sSequence in lsSequences:
			pSequenceCascade.add_command(label=sSequence, command=lambda self=self, sClass=sSequence: self.CreateAction(sClass))
			
		pActionMenu.menu.add_cascade(label="Sequences", underline=0, menu=pSequenceCascade)

		pActionMenu["menu"] = pActionMenu.menu

	# Button handlers:
	def LoadAI(self, event = None):
		LoadDialog(self, self.pOutput, GetAILoadPath(), SetAILoadPath)
	
	def SaveAI(self, event = None):
		SaveDialog(self, self.pOutput, self.pOutput.GetFilename(), GetAILoadPath(), SetAILoadPath)

	def ClearAll(self):
		self.pOutput.SetFilename("")
		self.pOutput.ClearAllEntities()

	def EditPrefixText(self):
		import ConfigUtils
		ConfigUtils.EditTextDialog(self.pOutput, self.SetPrefixText, self.pOutput.lpExtraFileInfo[0])

	def SetPrefixText(self, sText):
		self.pOutput.lpExtraFileInfo[0] = sText

	def SetAdvancedFeatures(self):
		# Get the current state of the "Advanced Features" menu button.
		bState = self.pAdvancedBool.get()

		SetAdvancedFeatures(bState)

	# Actions..
	def CreateAction(self, sActionClass):
		import ConfigUtils
		import ActionEntities

		#print "Create action:" + sActionClass
		pClass = ActionEntities.GetEntityClass(sActionClass)
		pEntity = self.pOutput.AddEntity(pClass)

	# Special AI's:
	def CreateFirePreprocess(self):
		# Create the entity...
		pEntity = self.pOutput.AddEntity( PreprocessingAIEntity )

		# Setup the special fields for a firing preprocess...
		pEntity.SetName("Fire")
		pEntity.lsSetup = [
			"import AI.Preprocessors",
			"pFireScript = AI.Preprocessors.FireScript(sInitialTarget)",
			"for pSystem in [ pShip.GetTorpedoSystem(), pShip.GetPhaserSystem(), pShip.GetPulseWeaponSystem() ]:",
			"\tif pSystem:",
			"\t\tpFireScript.AddWeaponSystem( pSystem )" ]
		pEntity.sMethod = "pFireScript.Update"

	def CreateTractorDockingPreprocess(self):
		# Create the entity...
		pEntity = self.pOutput.AddEntity( PreprocessingAIEntity )

		# Setup the special fields for a firing/tractoring preprocess...
		pEntity.SetName("TractorDocking")
		pEntity.lsSetup = [
			"import AI.Preprocessors",
			"pTractorScript = AI.Preprocessors.FireScript(sInitialTarget)",
			"pTractorScript.AddTractorBeam(pShip, App.TractorBeamSystem.TBS_DOCK_STAGE_1)" ]
		pEntity.sMethod = "pTractorScript.Update"

	def CreateSelectTargetPreprocess(self):
		# Create the entity...
		pEntity = self.pOutput.AddEntity( PreprocessingAIEntity )

		# Setup the special fields for a Select Target preprocess...
		pEntity.SetName("SelectTarget")
		pEntity.lsSetup = [
			"import AI.Preprocessors",
			"pSelectionPreprocess = AI.Preprocessors.SelectTarget(pAllTargetsGroup)",
			"pSelectionPreprocess.ForceCurrentTargetString(sInitialTarget)" ]
		pEntity.sMethod = "pSelectionPreprocess.Update"

	def CreateAvoidCollisionsPreprocess(self):
		# Create the entity...
		pEntity = self.pOutput.AddEntity( PreprocessingAIEntity )

		# Setup the special fields for an Avoid Obstacles preprocess...
		pEntity.SetName("AvoidObstacles")
		pEntity.lsSetup = [
			"import AI.Preprocessors",
			"pScript = AI.Preprocessors.AvoidObstacles()" ]
		pEntity.sMethod = "pScript.Update"

	def CreateAlertLevelPreprocess(self):
		# Create the entity...
		pEntity = self.pOutput.AddEntity( PreprocessingAIEntity )

		# Setup the special fields for an Avoid Obstacles preprocess...
		pEntity.SetName("AlertLevel")
		pEntity.lsSetup = [
			"import AI.Preprocessors",
			"pScript = AI.Preprocessors.AlertLevel(App.ShipClass.RED_ALERT)" ]
		pEntity.sMethod = "pScript.Update"

	def CreateCloakPreprocess(self):
		# Create the entity...
		pEntity = self.pOutput.AddEntity( PreprocessingAIEntity )

		# Setup the special fields for an Avoid Obstacles preprocess...
		pEntity.SetName("Cloak")
		pEntity.lsSetup = [
			"import AI.Preprocessors",
			"pScript = AI.Preprocessors.CloakShip(1)" ]
		pEntity.sMethod = "pScript.Update"

	def CreateStarbaseAttack(self):
		# Create the entity...
		pEntity = self.pOutput.AddEntity( CompoundAIEntity )

		# Setup the special fields for a Starbase Attack AI.
		pEntity.SetName("StarbaseAttack")
		pEntity.sModule = "AI.Compound.StarbaseAttack"
		pEntity.sFunction = "CreateAI"
		pEntity.sArgs = "pShip, \"target1\", \"target2\", ..."

	def CreateFelixReport(self):
		# Create the entity...
		pEntity = self.pOutput.AddEntity( PreprocessingAIEntity )

		# Setup the special fields for a Felix Report AI.
		pEntity.SetName("FelixReport")
		pEntity.lsSetup = [
			"import AI.Preprocessors",
			"pPreprocess = AI.Preprocessors.FelixReportStatus()" ]
		pEntity.sMethod = "pPreprocess.Update"
		
	def CreateAIStatusUpdate(self):
		from tkSimpleDialog import askstring
		sDesc = askstring("AI Status Update", "Enter new AI status:")
		# Create the entity...
		pEntity = self.pOutput.AddEntity( PreprocessingAIEntity )

		# Setup the special fields for a Felix Report AI.
		pEntity.SetName("AttackStatus_" + str(sDesc))
		pEntity.lsSetup = [
			"import AI.Preprocessors",
			"pPreprocess = AI.Preprocessors.UpdateAIStatus(\"AttackStatus_%s\")" % str(sDesc) ]
		pEntity.sMethod = "pPreprocess.Update"


class FileDialog(Toplevel):
	def __init__(self, parent, sStartPath = None):
		# Initialization...
		Toplevel.__init__(self, parent)
		self.sParentDirName = "<parent directory>"

		self.focus_set()

		# Create a little window for browsing files and directories.
		self.sFilename = StringVar()
		self.sCWD = StringVar()
		pFrame = Frame(self)
		pFrame.pack(side=TOP, anchor=NW, fill=X, expand=NO)
		Label(pFrame, textvariable=self.sCWD).pack(side=LEFT)
		if sStartPath is None:
			sStartPath = os.getcwd()
		self.sCWD.set( os.path.abspath(sStartPath) )

		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=BOTH, expand=YES)
		self.pFileFrame = Frame(pFrame)
		self.pDirectoryFrame = Frame(pFrame)
		self.SetupFileFrames()
		self.UpdateFileFrames()
		self.pFileFrame.pack(side=LEFT, fill=BOTH, expand=YES)
		self.pDirectoryFrame.pack(side=RIGHT, fill=BOTH, expand=YES)

		self.bind("<Escape>", lambda pEvent, self=self: self.destroy())

	def SetupFileFrames(self):
		import Pmw
		Label(self.pFileFrame, text="Files:").pack(side=TOP, anchor=W)
		self.pFileList = Pmw.ScrolledListBox( self.pFileFrame, hscrollmode='none', selectioncommand=self.FileSelected, dblclickcommand=self.FileDoubleClicked )
		self.pFileList.pack(fill=BOTH, expand=YES, side=TOP)
		
		Label(self.pDirectoryFrame, text="Directories:").pack(side=TOP, anchor=W)
		self.pDirectoryList = Pmw.ScrolledListBox( self.pDirectoryFrame, hscrollmode='none', dblclickcommand=self.DirectoryDoubleClicked )
		self.pDirectoryList.pack(fill=BOTH, expand=YES, side=TOP)

	def UpdateFileFrames(self):
		# Get the list of files in the "current" directory.
		lsAllFiles = os.listdir( self.sCWD.get() )

		# Split the files into files and directories...
		lsFiles = []
		lsDirectory = []
		for sFile in lsAllFiles:
			if os.path.isdir( os.path.join(self.sCWD.get(), sFile) ):
				lsDirectory.append(sFile)
			else:
				# It's a file.  We only want files that
				# end in ".py"
				if len(sFile) >= 3  and  sFile[-3:] == ".py":
					lsFiles.append(sFile)

		# The lists should be sorted...
		lsFiles.sort()
		lsDirectory.sort()

		# Update our display of the current files and directories.
		self.UpdateFileList(lsFiles)
		self.UpdateDirectoryList(lsDirectory)

	def UpdateFileList(self, lsFiles):
		# Create new entries for the files.
		self.pFileList.setlist(lsFiles)

	def UpdateDirectoryList(self, lsDirectories):
		# Create new entries for the files.
		# First entry always needs to be the parent directory
		self.pDirectoryList.setlist([self.sParentDirName] + lsDirectories)

	def FileSelected(self):
		# Get the name of the file...
		lsSelection = self.pFileList.getcurselection()
		if lsSelection:
			sFile = lsSelection[0]

			# Update the name of the file in the entry box...
			self.sFilename.set(sFile)

	def FileDoubleClicked(self):
		# Get the name of the file...
		lsSelection = self.pFileList.getcurselection()
		if lsSelection:
			sFile = lsSelection[0]

			# Update the name of the file in the entry box...
			self.sFilename.set(sFile)

	def DirectoryDoubleClicked(self):
		# Get the name of the directory...
		lsSelection = self.pDirectoryList.getcurselection()
		if lsSelection:
			sDirectory = lsSelection[0]

			# If it's the parent directory string, this means the user wants to go
			# up one level in the directory tree...
			if sDirectory == self.sParentDirName:
				# Up we go...
				sNewDir, sExtra = os.path.split( self.sCWD.get() )
			else:
				# Down we go, into the directory tree...
				sNewDir = os.path.join( self.sCWD.get(), sDirectory )

			if os.path.exists(sNewDir):
				self.ChangeDirectory(sNewDir)

	def ChangeDirectory(self, sNewDir):
       			self.sCWD.set( os.path.abspath(sNewDir) )

			# Now that we're in a new directory, we need to update the file lists...
			self.UpdateFileFrames()


class SaveDialog(FileDialog):
	"*sigh*"
	def __init__(self, parent, pOutput, sGuessedFilename, sStartPath, pSetPathFunction):
		FileDialog.__init__(self, parent, sStartPath)
		self.pSetPathFunction = pSetPathFunction

		# Add an informative label
		self.title("Save File")

		self.pOutput = pOutput

		# Save button on the bottom...
		Button(self, text="Save", command=self.Save).pack(side=BOTTOM, pady=5)

		self.sFilename.set(sGuessedFilename)

		# Create an entry for the name of the function
		# this will be saved in.
		pFrame = Frame(self)
		pFrame.pack(side=BOTTOM)
		Label(pFrame, text="Function name:").pack(side=LEFT, padx=5)
		self.sFunctionName = StringVar()
		self.pEntry = Entry(pFrame, textvariable=self.sFunctionName, width=30)
		self.pEntry.pack(side=LEFT, padx=5, fill=X)
		self.sFunctionName.set("CreateAI")

		# Create an entry for the filename.
		pFrame = Frame(self)
		pFrame.pack(side=BOTTOM, fill=X)
		Label(pFrame, text="Enter filename:").pack(side=LEFT, padx=5)
		self.pEntry = Entry(pFrame, textvariable=self.sFilename, width=30)
		self.pEntry.pack(side=LEFT, padx=5, fill=X)

		self.pEntry.bind("<Return>", lambda pEvent, self=self: self.Save())

	def FileDoubleClicked(self):
		# Parent class first...
		FileDialog.FileDoubleClicked(self)

		# Save.
		self.Save()

	def Save(self):
		# Save the path..
		self.pSetPathFunction(self.sCWD.get())

		# If the filename doesn't have a .py at the end, add one:
		sFilename = os.path.join( self.sCWD.get(), self.sFilename.get() )
		if len(sFilename) > 0:
			# Check if it has a .py in it:
			if string.find(sFilename, ".py") == -1:
				# Couldn't find it.  Add it.
				sFilename = sFilename + ".py"
			
			# Save under this filename.
			pFile = open(sFilename, "w")
			self.pOutput.Save(pFile, self.sFunctionName.get())
			pFile.close()

			# If this should be a builder AI, make it into one.
			if g_bIsBuilderAI.get():
				import MakeBuilderAI
				MakeBuilderAI.Go(sFilename)

			self.pOutput.SetFilename(self.sFilename.get())

		self.destroy()

class LoadDialog(FileDialog):
	def __init__(self, parent, pOutput, sStartPath, pSetPathFunction):
		FileDialog.__init__(self, parent, sStartPath)
		self.pSetPathFunction = pSetPathFunction

		# Add an informative label
		self.title("Load File")

		self.pOutput = pOutput

		Button(self, text="Load", command=self.Load).pack(side=BOTTOM, pady=5)

		pFrame = Frame(self)
		pFrame.pack(side=BOTTOM, fill=X)
		Label(pFrame, text="Enter filename:").pack(side=LEFT, padx=5)
		pEntry = Entry(pFrame, width=40, textvariable=self.sFilename)
		pEntry.pack(side=LEFT, padx=5, fill=X, expand=YES)

		pEntry.bind("<Return>", lambda pEvent, self=self: self.Load())

	def FileDoubleClicked(self):
		# Parent class first...
		FileDialog.FileDoubleClicked(self)

		# Save.
		self.Load()

	def Load(self):
		# Save the path..
		self.pSetPathFunction(self.sCWD.get())

		# If the filename doesn't have a .py at the end, add one:
		sFilename = os.path.join( self.sCWD.get(), self.sFilename.get() )
		if string.find(sFilename, ".py") == -1:
			# Couldn't find it.  Add it.
			sFilename = sFilename + ".py"

		# Check if the file is a Builder AI.  If so,
		# save a flag so we know to add the code again
		# when we save it.  (We'll strip out the builder
		# code when we load the file).
		import MakeBuilderAI
		g_bIsBuilderAI.set( MakeBuilderAI.IsBuilderAI(sFilename) )

		# Read in the file and pass the text along to the Output window,
		# so it can deal with it.
		pFile = open(sFilename, "r")
		if(pFile):
			lsFileText = []
			sLine = pFile.readline()
			while sLine:
				lsFileText.append(sLine)
				sLine = pFile.readline()

			# Done reading it in.
			pFile.close()

			# If it's a builder AI, strip its builderness.
			if g_bIsBuilderAI.get():
				lsFileText = MakeBuilderAI.ProcessLines(lsFileText, 1)

			# Pass the file along and close it.
			self.pOutput.Load(lsFileText)
			self.pOutput.SetFilename(self.sFilename.get())
		else:
			print "Error opening file " + sFilename
		
		self.destroy()

class SelectFileDialog(FileDialog):
	def __init__(self, parent, sPath, pOutputFunction, pSetPathFunction):
		FileDialog.__init__(self, parent, sPath)
		self.pSetPathFunction = pSetPathFunction

		# Add an informative label
		self.title("Select File")

		self.pOutputFunc = pOutputFunction

		# Save button on the bottom...
		Button(self, text="Select", command=self.Select).pack(side=BOTTOM, pady=5)

		self.sFilename.set("")

		# Create an entry for the filename.
		pFrame = Frame(self)
		pFrame.pack(side=BOTTOM, fill=X)
		Label(pFrame, text="Enter filename:").pack(side=LEFT, padx=5)
		self.pEntry = Entry(pFrame, textvariable=self.sFilename, width=30)
		self.pEntry.pack(side=LEFT, padx=5, fill=X, expand=YES)

		self.pEntry.bind("<Return>", lambda pEvent, self=self: self.Select())

	def FileDoubleClicked(self):
		# Parent class first...
		FileDialog.FileDoubleClicked(self)

		# Select this file.
		self.Select()

	def Select(self):
		# Save the path..
		self.pSetPathFunction(self.sCWD.get())

		# Get the filename..
		sFilename = os.path.join( self.sCWD.get(), self.sFilename.get() )
		#print "Selected " + str(sFilename)
		if len(sFilename) > 0:
			# Check if it has a .py in it:
			if string.find(sFilename, ".py") == -1:
				# Couldn't find it.  Add it.
				sFilename = sFilename + ".py"

			# Call the output function, passing it this filename.
			self.pOutputFunc(sFilename)

			self.destroy()

class Output(Canvas):
	"The main output window which displays the AI"
	"that's currently being setup."
	def __init__(self, parent, width=600, height=400, **kw):
		# Base class init
		kw['width'] = width
		kw['height'] = height
		apply(Canvas.__init__, (self, parent), kw)

		# Setup our list of entities
		self.lEntities = []
		
		# Info for saving out our file.
		self.lpExtraFileInfo = ["import App\n\ndef CreateAI(pShip):\n"]
		
		# A counter for unique tag names...
		self.sNextUniqueTagPrefix = "Tag"
		self.iNextUniqueTagNumber = 0

		# The load/save dialogs may use us for storage of a filename...
		self.sFilename = ""

	def AddEntity(self, cEntity):
		pEntity = cEntity(self)
		self.AddEntityDirect(pEntity)
		return pEntity

	def AddEntityDirect(self, pEntity):
		self.lEntities.append(pEntity)

	def RemoveEntity(self, pEntity):
		pEntity.Delete()
		self.lEntities.remove(pEntity)

	def SetFilename(self, sFilename):
		self.sFilename = sFilename
		if sFilename:
			root.title(sBaseTitle + " (%s)" % sFilename)
		else:
			root.title(sBaseTitle)

	def GetFilename(self):
		return self.sFilename

	def ClearAllEntities(self):
		while len(self.lEntities):
			self.RemoveEntity( self.lEntities[0] )
		
		self.lpExtraFileInfo = ["import App\n\ndef CreateAI(pShip):\n"]

	def GetEntityByName(self, sName):
		for pEntity in self.lEntities:
			if pEntity.GetName() == sName:
				return pEntity
		
		return None

	def GetEntityAt(self, x, y):
		"Get an entity that's at the specified screen location."
		"If there isn't one, this returns None"
		# Look through our entities...
		for pEntity in self.lEntities:
			# Get the bounding box for this entity...
			box = self.bbox(pEntity.GetMainTag())
			
			# Check if the point is inside this box:
			if (x >= box[0]) and (x <= box[2]):
				if (y >= box[1]) and (y <= box[3]):
					# Found a match.
					return pEntity
		
		# No match
		return None

	def GetUniqueTag(self):
		sTag = self.sNextUniqueTagPrefix + str(self.iNextUniqueTagNumber)
		self.iNextUniqueTagNumber = self.iNextUniqueTagNumber + 1
		return sTag

	def Load(self, lsFileText):
		# Clear any existing AI.
		self.ClearAllEntities()

		# There's a specialized class for doing this..  I don't
		# want to include all the code here.
		pFileLoader = FileLoader(self)
		self.lpExtraFileInfo = pFileLoader.Process(lsFileText)

	def Save(self, pFile, sFunctionName):
		# Save any text that was at the beginning of the file..
		pFile.write( self.lpExtraFileInfo[0] )

		# Now loop through all the AI's, and save them.
		for pEntity in self.lEntities:
			# Only directly save AI's that aren't
			# contained by other AI's.  The contained
			# AI's will be saved by the containing ones.
			if not pEntity.GetContainingEntity():
				pEntity.Save(pFile)
				
				# Add a return statement after this
				# AI.
				pFile.write("\treturn p%s\n" % pEntity.GetName())

class Entity(CanvasUtils.DraggableCanvasIcon):
	"Something that deals with a visible representation of"
	"an object, in the Output window."
	def __init__(self, pOutput, sName, sMainColor = "black"):
		# Base class init...
		CanvasUtils.DraggableCanvasIcon.__init__(self, pOutput)

		# Basic variable setup
		self.pOutput = pOutput
		self.pCanvas = pOutput
		self.pContainingEntity = None
		self.sMainColor = sMainColor
		self.sPostEntitySaveText = ""

		# Set our name..
		self.sText = None
		self.SetName(sName)

		# Bind mouse button 1 to drag us...
		self.pCanvas.tag_bind(self.GetMainTag(), "<Button-1>", self.DragButtonDown)
		self.pCanvas.tag_bind(self.GetMainTag(), "<ButtonRelease-1>", self.DragButtonUp)
		self.pCanvas.tag_bind(self.GetMainTag(), "<B1-Motion>", self.DragButtonDragged)
		# And the right mouse button to open the Configure menu.
		self.pCanvas.tag_bind(self.GetMainTag(), "<Button-3>", self.Configure)

	def Delete(self):
		if self.GetContainingEntity():
			self.GetContainingEntity().RemoveContainedEntity(self)

		# Remove any graphics based on our main tag (derived
		# classes will need to clean up any graphics they create
		# under different tags).
		self.pCanvas.delete(self.GetMainTag())

	def SetPostEntitySaveText(self, sText):
		self.sPostEntitySaveText = sText

	def GetAttachPoint(self):
		box = self.pCanvas.bbox(self.GetMainTag())
		return (box[0], (box[1] + box[3]) / 2)

	def Redraw(self):
		# Nothing to do but our base class Redraw...
		CanvasUtils.DraggableCanvasIcon.Redraw(self)

	def SetName(self, sName):
		# Remove any whitespace from sName
		sName = string.replace(sName, " ", "_")

		# Make sure that name isn't in use (unless it's our name):
		if sName != self.sText:
			sTest = sName
			iCount = 2
			while self.pOutput.GetEntityByName(sTest) or len(self.pCanvas.find_withtag(sTest)):
				sTest = "%s_%d" % (sName, iCount)
				iCount = iCount + 1

			self.sText = sTest

		# Change the text label for this entity, if it exists.		
		try:
			self.pCanvas.itemconfigure(self.iText, text=self.sText)
		except AttributeError:
			pass

	def GetName(self):
		return self.sText

	def CanBeContainedBy(self, pEntity):
		return 0

	def SetContainingEntity(self, pEntity):
		pContaining = self.pContainingEntity
		self.pContainingEntity = None
		if pContaining:
			pContaining.RemoveContainedEntity(self)

		self.pContainingEntity = pEntity

	def GetContainingEntity(self):
		return self.pContainingEntity

	def MoveTo(self, iXPos, iYPos):
		# Base class first, to actually move us...
		CanvasUtils.DraggableCanvasIcon.MoveTo(self, iXPos, iYPos)

		# If there's an Entity that contains us, it may need to be
		# redrawn...
		if self.GetContainingEntity():
			self.GetContainingEntity().Redraw()

	def CreateCopy(self):
		return None

	def InitializeCopy(self, pCopy):
		pCopy.SetName( self.GetName() )
		pass

	def Configure(self, event):
		print "Configuration of this item not yet implemented."
	
	def Load(self, lsCreationText):
		print "Load not implemented yet for %s" % self.GetName()
	
	def Save(self, pFile):
		print "Save not implemented for %s" % self.GetName()


class AIEntity(Entity):
	"Something that deals with a visible representation of"
	"an AI object, in the Output window."
	def __init__(self, pOutput, sName, sMainColor = "black"):
		# Base class init...
		Entity.__init__(self, pOutput, sName, sMainColor)

		# Basic variable setup
		self.iWidth = 80
		self.iHeight = 30

		# Set our Interruptable flag.  This is on by default.
		self.bInterruptable = 1

		# Create our graphics...
		self.CreateGraphics()


	def CreateGraphics(self):
		# Create our rectangle and our text, and associate
		# them with our tag...
		self.iRect = self.pCanvas.create_rectangle(self.vPos[0], self.vPos[1], self.vPos[0] + self.iWidth, self.vPos[1] + self.iHeight, outline=self.sMainColor, fill="white", tags=(self.GetMainTag(), ))
		self.iText = self.pCanvas.create_text(self.vPos[0] + (self.iWidth / 2), self.vPos[1] + (self.iHeight / 2), justify=CENTER, width=self.iWidth - 6, text=self.sText, tags=(self.GetMainTag(), ))

	def CanBeContainedBy(self, pEntity):
		# As an AIEntity, we can be contained only by other
		# AIEntities.
		return isinstance(pEntity, AIEntity)

	def Load(self, lsCreationText):
		# Look for a SetInterruptable function call, and set
		# our bInterruptable flag from that.
		pSearch = re.compile("p%s\\.SetInterruptable\\(([01])\\)\n" % self.GetName())
		for sLine in lsCreationText:
			pMatch = pSearch.search(sLine)
			if pMatch:
				self.bInterruptable = int(pMatch.group(1))
				break
	
	def Save(self, pFile):
		pFile.write("\tp%s.SetInterruptable(%d)\n" % (self.GetName(), self.bInterruptable))

	def InitializeCopy(self, pCopy):
		# Parent class first
		Entity.InitializeCopy(self, pCopy)

		pCopy.bInterruptable = self.bInterruptable



class ContainingAIEntity(AIEntity):
	"An AI entity that can contain another AI entity."
	def __init__(self, pOutput, sName, ContainBoxOutline="red", ContainBoxFill="gray"):
		self.kContainBoxOutline = ContainBoxOutline
		self.kContainBoxFill = ContainBoxFill

		# Base class init
		AIEntity.__init__(self, pOutput, sName, ContainBoxOutline)

		# Clicking on iTopBox has a different effect...
		self.vLastTopPos = None
		self.pCanvas.tag_bind(self.iTopBox, "<Button-3>", self.TopClicked)
		self.pCanvas.tag_bind(self.iTopBox, "<ButtonRelease-3>", self.TopReleased)
		self.pCanvas.tag_bind(self.iTopBox, "<B3-Motion>", self.TopDragged)

		self.pContainedEntity = None

	def Delete(self):
		# Parent class delete...
		AIEntity.Delete(self)		

		# Detach ourselves from our child, if we have one..
		self.SetContainedEntity(None)

		# Delete things that don't fall under our normal tag.
		self.pCanvas.delete(self.iTopBox)
		self.pCanvas.delete(self.iContainedLine)

	def CreateGraphics(self):
		# Parent class first...
		AIEntity.CreateGraphics(self)
		self.iTopBox = self.pCanvas.create_rectangle(self.vPos[0] + (self.iWidth / 2) - 10, self.vPos[1] - 10, self.vPos[0] + (self.iWidth / 2) + 10, self.vPos[1], outline=self.kContainBoxOutline, fill=self.kContainBoxFill)
		self.iContainedLine = self.pCanvas.create_line(self.vPos[0] + (self.iWidth / 2), self.vPos[1] - 5, self.vPos[0] + (self.iWidth / 2), self.vPos[1] - 5, fill=self.kContainBoxOutline)

	def Redraw(self):
		# Parent class first...
		# Only need to redraw things that don't have
		# our special tag.
		self.pCanvas.coords(self.iTopBox, self.vPos[0] + (self.iWidth / 2) - 10, self.vPos[1] - 10, self.vPos[0] + (self.iWidth / 2) + 10, self.vPos[1])
		self.UpdateContainedLine()

	def TopClicked(self, event):
		self.vLastTopPos = (event.x, event.y)
		self.pCanvas.grab_set()
		
		self.iDragLine = self.pCanvas.create_line(self.vPos[0] + (self.iWidth / 2), self.vPos[1] - 5, event.x, event.y, fill="red")
	
	def TopReleased(self, event):
		self.vLastTopPos = None
		self.pCanvas.grab_release()

		# Get rid of the drag line...
		self.pCanvas.delete(self.iDragLine)

		# Check if we've been dragged to something else.
		pEntity = self.pOutput.GetEntityAt(event.x, event.y)
		if pEntity  and  (pEntity != self):
			# Yep.
			# This thing is now our Contained AI.
			self.SetContainedEntity(pEntity)
	
	def TopDragged(self, event):
		if self.vLastTopPos:
			self.pCanvas.coords(self.iDragLine, self.vPos[0] + (self.iWidth / 2), self.vPos[1] - 5, event.x, event.y)
			
			self.vLastDragPos = (event.x, event.y)

	def SetContainedEntity(self, pEntity):
		# Clear our old contained AI
		if self.GetContainedEntity():
			pAI = self.GetContainedEntity()
			self.pContainedEntity = None

			pAI.SetContainingEntity(None)

		# Set our new contained AI, if we can
		if pEntity:
			if pEntity.CanBeContainedBy(self):
				self.pContainedEntity = pEntity
				self.pContainedEntity.SetContainingEntity(self)

		# Draw a line to our contained entity.
		self.UpdateContainedLine()

	def GetContainedEntity(self):
		return self.pContainedEntity

	def RemoveContainedEntity(self, pEntity):
		self.SetContainedEntity(None)

		# Draw a line to our contained entity.
		self.UpdateContainedLine()
	
	def UpdateContainedLine(self):
		vStart = ( self.vPos[0] + (self.iWidth / 2), self.vPos[1] - 5 )
		if self.GetContainedEntity():
			vEnd = self.GetContainedEntity().GetAttachPoint()
		else:
			vEnd = vStart
		
		self.pCanvas.coords(self.iContainedLine, vStart[0], vStart[1], vEnd[0], vEnd[1])


def GrabLinesBetween(sStartString, sEndString, lsText):
	"Return a list of the lines between the given"
	"starting and ending lines, in lsText."
	# Search for the start line:
	iStartGrabbing = None
	for iLine in range(len(lsText)):
		if lsText[iLine] == sStartString:
			iStartGrabbing = iLine + 1
			break
	
	lsGrabbed = []
	if iStartGrabbing is not None:
		for iLine in range(iStartGrabbing, len(lsText)):
			if lsText[iLine] == sEndString:
				break
			# Grab this line...
			lsGrabbed.append(lsText[iLine])
	
	return lsGrabbed
			
class ConditionalAIEntity(ContainingAIEntity):
	def __init__(self, pOutput):
		# Base class init
		ContainingAIEntity.__init__(self, pOutput, "Conditional")

		# Custom AI params:
		self.lConditions = []
		self.lsEvalFunc = []

	def AddCondition(self, pCondition):
		if pCondition:
			self.lConditions.append(pCondition)

	def RemoveCondition(self, pCondition):
		self.lConditions.remove(pCondition)

	def Load(self, lsCreationText):
		# Parent class load,.
		ContainingAIEntity.Load(self, lsCreationText)

		# Look for the block that contains our conditions.
		# this is between the comments:
		# "## Conditions:\n" and "## Evaluation function:\n"
		sStartString = "## Conditions:\n"
		sEndString = "## Evaluation function:\n"
		lsConditions = GrabLinesBetween(sStartString, sEndString, lsCreationText)

		# Create our conditions...
		self.LoadConditions(lsConditions)
		
		# Grab our evaluation function:
		sStartString = sEndString
		sEndString = "## The ConditionalAI:\n"
		lsEvalFunc = GrabLinesBetween(sStartString, sEndString, lsCreationText)

		# And setup our evaluation function
		self.LoadEvalFunc(lsEvalFunc)
		
		# Grab the SetContainedEntity line, so we know the name of
		# the AI we'll contain...
		matchstr = re.compile("p(.*)\.SetContainedAI\(p(.*)\)\n")
		for sLine in lsCreationText:
			match = matchstr.search(sLine)
			if match:
				# Get the name of the contained AI...
				sContainedName = match.group(2)
				
				# Get the AI entity by this name...
				pEntity = self.pOutput.GetEntityByName(sContainedName)
				
				self.SetContainedEntity(pEntity)
		
		# Done.
	
	def LoadConditions(self, lsConditions):
		while len(lsConditions):
			pCondition = Condition(None, None, None)
			lsConditions = pCondition.Load(lsConditions)

			self.AddCondition(pCondition)

	def LoadEvalFunc(self, lsEvalFunc):
		# Ignore the lines we always generate:
		matches = []
		matches.append( re.compile("^def EvalFunc\(.*\):\n$") )
		matches.append( re.compile("^\tACTIVE = App.ArtificialIntelligence.US_ACTIVE\n$") )
		matches.append( re.compile("^\tDORMANT = App.ArtificialIntelligence.US_DORMANT\n$") )
		matches.append( re.compile("^\tDONE = App.ArtificialIntelligence.US_DONE\n$") )
		iLastMatch = -1
		for iLine in range( len(lsEvalFunc) ):
			sLine = lsEvalFunc[iLine]
			for pRegExp in matches:
				match = pRegExp.search(sLine)
				if match:
					iLastMatch = iLine

		# First line of the eval func is just our "def EvalFunc(...):" line.
		# We'll ignore it.
		# We want the remaining lines, without their leading \t's, and
		# their ending \n's:
		self.lsEvalFunc = []
		if len(lsEvalFunc):
			for sLine in lsEvalFunc[(iLastMatch + 1):]:
				if sLine[0] == "\t":
					sLine = sLine[1:]

				self.lsEvalFunc.append(sLine[:-1])

	def Save(self, pFile):
		# First step in saving is to create the AI we contain...
		if self.GetContainedEntity():
			self.GetContainedEntity().Save(pFile)
		else:
			print "WARNING: Conditional AI \"%s\" has no contained AI" % self.GetName()

		# Next, output the comments that surround our creation:
		pFile.write(sSeparationBlock)
		pFile.write("\t# Creating ConditionalAI %s at (%d, %d)\n" % (self.GetName(), self.vPos[0], self.vPos[1]))

		# Create our conditions.
		if len(self.lConditions):
			pFile.write("\t## Conditions:\n")
			for pCondition in self.lConditions:
				pCondition.Save(pFile)
		else:
			print "WARNING: Conditional AI \"%s\" has no conditions" % self.GetName()
		
		# Create our evaluation function.
		pFile.write("\t## Evaluation function:\n")
		if len(self.lsEvalFunc):
			pFile.write("\tdef EvalFunc(")
			sPrepend = ""
			for pCondition in self.lConditions:
				pFile.write("%sb%s" % (sPrepend, pCondition.GetName()))
				sPrepend = ", "
			pFile.write("):\n")
			pFile.write("\t\tACTIVE = App.ArtificialIntelligence.US_ACTIVE\n")
			pFile.write("\t\tDORMANT = App.ArtificialIntelligence.US_DORMANT\n")
			pFile.write("\t\tDONE = App.ArtificialIntelligence.US_DONE\n")

			for sLine in self.lsEvalFunc:
				pFile.write("\t\t%s\n" % sLine)
		else:
			print "WARNING: Conditional AI \"%s\" has no evaluation function" % self.GetName()

		# Create ourselves:
		pFile.write("\t## The ConditionalAI:\n")
		pFile.write("\tp%s = App.ConditionalAI_Create(pShip, \"%s\")\n" % (self.GetName(), self.GetName()))

		# Parent class save.
		ContainingAIEntity.Save(self, pFile)

		# Set our contained AI:
		if self.GetContainedEntity():
			pFile.write("\tp%s.SetContainedAI(p%s)\n" % (self.GetName(), self.GetContainedEntity().GetName()))

		# Add our conditions:
		for pCondition in self.lConditions:
			pFile.write("\tp%s.AddCondition(p%s)\n" % (self.GetName(), pCondition.GetName()))

		# Set our evaluation function:
		pFile.write("\tp%s.SetEvaluationFunction(EvalFunc)\n" % self.GetName())

		# We're done
		pFile.write("\t# Done creating ConditionalAI %s\n" % self.GetName())
		pFile.write(sSeparationBlock)

		# Write any text that should appear after this AI.
		pFile.write(self.sPostEntitySaveText)


	def CreateCopy(self):
		pCopy = ConditionalAIEntity(self.pOutput)
		self.InitializeCopy(pCopy)
		return pCopy

	def InitializeCopy(self, pCopy):
		# Parent class first.
		ContainingAIEntity.InitializeCopy(self, pCopy)

		# Copy the conditions
		for pCondition in self.lConditions:
			pCopy.AddCondition( pCondition.CreateCopy() )
		for sLine in self.lsEvalFunc:
			pCopy.lsEvalFunc.append(sLine[:])

	def Configure(self, event = None):
		ConditionalAIConfigurationDialog(self.pOutput, self)

from ConfigUtils import ConfigurationDialog

class ConditionalAIConfigurationDialog(ConfigurationDialog):
	def __init__(self, pOutput, pAI):
		# Base class init
		ConfigurationDialog.__init__(self, pOutput, pAI, EditPostAIText=GetAdvancedFeatures())

		# Set a nice title.
		self.title("ConditionalAI(%s) config" % self.pAI.GetName())

		# Create things for adding conditions
		pFrame = Frame(self)
		pFrame.pack(side=TOP, anchor=W, pady=2, fill=X)
		Label(pFrame, text="Conditions:").pack(side=LEFT)
		Button(pFrame, text="Add Condition", command=self.AddCondition).pack(side=RIGHT)
		self.pConditionFrame = Frame(self)
		self.pConditionFrame.pack(side=TOP, anchor=W, pady=2)
		self.lConditionButtons = []
		
		# Create things for specifying the evaluation function
		pFrame = Frame(self)
		pFrame.pack(side=TOP, anchor=W, pady=2)
		self.pEvalFuncLabel = Label(pFrame, text="def EvalFunc():")
		self.pEvalFuncLabel.pack(side=TOP, anchor=NW)
		self.pEvalFuncText = Text(pFrame, height=8, width=80)
		self.pEvalFuncText.pack(side=TOP, fill=BOTH, anchor=NW)
		# Fill the text entry box with our existing text...
		for sLine in self.pAI.lsEvalFunc:
			self.pEvalFuncText.insert(END, sLine + "\n")

		# Update the info we display about our conditions.
		self.UpdateConditionInfo()

	def Apply(self):
		# Copy our EvalFunc lines into the AI.
		# They need to be split by \n's, first...
		lsSplit = string.split(self.pEvalFuncText.get(0.0, END), "\n")
		lsEvalFunc = []
		for sLine in lsSplit:
			if len(sLine):
				lsEvalFunc.append(sLine)
		
		self.pAI.lsEvalFunc = lsEvalFunc
		
		# Parent class Apply.
		ConfigurationDialog.Apply(self)

	def AddCondition(self):
		AddConditionDialog(self.pOutput, self, self.pAI)

	def UpdateConditionInfo(self):
		# Remove our old condition labels:
		for pButton in self.lConditionButtons:
			pButton.destroy()
		self.lConditionButtons = []
		
		sParams = ""
		sPrepend = ""
		for pCondition in self.pAI.lConditions:
			# Build our string for the evalfunc parameters
			sParams = sParams + sPrepend + "b" + pCondition.GetName()
			sPrepend = ", "
			
			# Rebuild the list of buttons we have for our
			# conditions.
			func = lambda self=self, pCondition=pCondition: self.EditCondition( pCondition.GetName() )
			pButton = Button(self.pConditionFrame, text=pCondition.GetName(), command=func)
			pButton.pack(side=TOP, anchor=W)
			self.lConditionButtons.append( pButton )
		
		# Update our "def EvalFunc(...)" string:
		self.pEvalFuncLabel['text'] = "def EvalFunc(%s):" % sParams
	
	def EditCondition(self, sName):
		# Find the condition...
		for lCondition in self.pAI.lConditions:
			if lCondition.GetName() == sName:
				EditConditionDialog(self.pOutput, self, self.pAI, lCondition)
				break

class AddConditionDialog(Toplevel):
	def __init__(self, pOutput, pConfigDialog, pAI):
		# Parent class init
		Toplevel.__init__(self, pOutput)

		self.focus_set()

		self.pOutput = pOutput
		self.pConfigDialog = pConfigDialog
		self.pAI = pAI

		# Add an informative label
		self.title("Add Condition to %s" % self.pAI.GetName())

		# Let the user specify the condition name:
		pFrame = Frame(self)
		pFrame.pack(side=TOP, anchor=W)
		Label(pFrame, text="Condition name:").pack(side=LEFT)
		self.pNameVar = StringVar()
		pNameEntry = Entry(pFrame, width=40, textvariable = self.pNameVar)
		pNameEntry.pack(side=LEFT)
		pNameEntry.bind("<KeyPress>", self.EntryKey)

		# The condition's class
		pFrame = Frame(self)
		pFrame.pack(side=TOP, anchor=NW)
		Label(pFrame, text="Condition class:").pack(side=TOP)
		pButtonFrames = ( Frame(pFrame), Frame(pFrame) )
		pButtonFrames[0].pack(side=LEFT, fill=Y, anchor=N)
		pButtonFrames[1].pack(side=RIGHT, fill=Y, anchor=N)
		lsAvailable = self.GetAvailableConditions()
		self.pRadioVar = IntVar()
		for iIndex  in range( len(lsAvailable) ):
			pRadio = Radiobutton(pButtonFrames[iIndex * 2 / len(lsAvailable)], text=lsAvailable[iIndex], variable=self.pRadioVar, value = iIndex, command=lambda self=self, iIndex=iIndex: self.SelectClass(iIndex))
			pRadio.pack(side=TOP, anchor=W)

		# Let the user specify params:
		pFrame = Frame(self)
		pFrame.pack(side=TOP, anchor=W)
		self.pParamLabel = Label(pFrame, text="Parameters:")
		self.pParamLabel.pack(side=TOP, anchor=W)
		self.pParamVar = StringVar()
		Entry(pFrame, width=50, textvariable = self.pParamVar).pack(side=TOP, anchor=W)

		# And confirmation buttons
		self.pButtonFrame = Frame(self)
		self.pButtonFrame.pack(side=TOP, fill=X)
		Button(self.pButtonFrame, text="Ok", command=self.Ok).pack(side=LEFT)
		Button(self.pButtonFrame, text="Cancel", command=self.destroy).pack(side=RIGHT)

		# Start out by selecting the first class, if none is selected.
		self.SelectClass(0)

	def EntryKey(self, event):
		# Check if the character is one of the characters
		# we'll allow in a name.  If not, we need to return
		# "break", so the event isn't propogated any further.
		if -1 == string.find(string.digits + string.letters, event.keysym):
			# Didn't find it.  Check for special keys.
			if not (event.keysym in ( "BackSpace", "Tab", "Left", "Right", "Home", "End" )):
				# It's not a special key.  Don't propogate
				# this event.
				return "break"

	def GetAvailableConditions(self):
		import dircache
		lsDir = dircache.listdir(GetConditionPath())
		matchstr = re.compile("^([A-Za-z].+)\.py$")
		lsAvailable = []
		for sEntry in lsDir:
			match = matchstr.search(sEntry)
			if match:
				lsAvailable.append(match.group(1))

		return lsAvailable

	def SelectClass(self, iIndex):
		# Update the parameter info.
		self.pParamLabel['text'] = "Parameters: " + self.GetConditionParams( self.GetSelectedClassName() )

	def GetSelectedClassName(self):
		lsClasses = self.GetAvailableConditions()
		iSelection = self.pRadioVar.get()
		
		return lsClasses[iSelection]

	def GetConditionParams(self, sCondition):
		sParams = ""
		# Open up the condition
		pFile = open(GetConditionPath() + "/" + sCondition + ".py", "r")
		# Look for the __init__ function.
		matchstr = re.compile("def +__init__\(self, \w+, (.*)\):\n$")
		line = pFile.readline()
		while line:
			match = matchstr.search(line)
			if match:
				# Found it.  Grab the params.
				sParams = match.group(1)
				break
			line = pFile.readline()
		pFile.close()
		
		return sParams

	def Ok(self):
		"Ok, the user is happy with the values entered."
		"Create a condition and add it to our AI."
		# Create the condition.
		pCondition = Condition(self.pNameVar.get(), self.GetSelectedClassName(), self.pParamVar.get())

		# Add it to the AI.
		self.pAI.AddCondition(pCondition)
		self.pConfigDialog.UpdateConditionInfo()
		
		# We're done.
		self.destroy()

class EditConditionDialog(AddConditionDialog):
	def __init__(self, pOutput, pConfigDialog, pAI, pCondition):
		# Parent class init
		AddConditionDialog.__init__(self, pOutput, pConfigDialog, pAI)

		self.pCondition = pCondition

		# Change the title..
		self.title("Edit Condition " + pCondition.GetName())

		# Add a button to delete this condition
		Button(self.pButtonFrame, text="Delete", command=self.Delete).pack()

		# Update the information we already know.
		self.pNameVar.set( self.pCondition.GetName() )
		self.pParamVar.set( self.pCondition.sParams )

		# Set our class to be selected.
		lsConditions = self.GetAvailableConditions()
		for iIndex in range( len(lsConditions) ):
			if lsConditions[iIndex] == self.pCondition.sClass:
				self.pRadioVar.set(iIndex)
				self.SelectClass(iIndex)
				break

	def Ok(self):
		self.pCondition.sName = self.pNameVar.get()
		self.pCondition.sClass = self.GetSelectedClassName()
		self.pCondition.sParams = self.pParamVar.get()

		self.pConfigDialog.UpdateConditionInfo()

		self.destroy()

	def Delete(self):
		# Tell our AI to remove this condition.
		self.pAI.RemoveCondition(self.pCondition)

		self.pConfigDialog.UpdateConditionInfo()
		
		self.destroy()

class Condition:
	def __init__(self, sName, sClass, sParams):
		self.sName = sName
		self.sClass = sClass
		self.sParams = sParams
	
	def GetName(self):
		return self.sName

	def Load(self, lsConditions):
		# We need to grab the first few lines of text from the
		# passed-in text block.  These lines will define us.
		iNextUnusedLine = 0

		# Since the API changed for ConditionScript_Create, we need to recognize
		# and load both versions (until all the AI scripts can be converted to
		# the new version).
		# Check which version this is...
		if re.search("^from AI\.Conditions import (.*)\n$", lsConditions[1]):
			# This is an old version.  Load the info we need.
			sName = re.search("^#### Condition (.*)\n$", lsConditions[0]).group(1)
			sModule = re.search("^from AI\.Conditions import (.*)\n$", lsConditions[1]).group(1)
			# ConditionScript_Create line isn't used.
			pMethodMatch = re.search("^p(%s)?Script = %s.%s\(p(([^,]*, (.*))|(.*))\)\n$" % (sName, sModule, sModule), lsConditions[3])
			sArgs = pMethodMatch.group(4)
			if not sArgs:
				sArgs = ""
			iNextUnusedLine = 5
		else:
			# This is the new version, using the new API.  Load the info
			# we need.
			sName = re.search("^#### Condition (.*)\n$", lsConditions[0]).group(1)
			test = re.search("^p%s = App.ConditionScript_Create\(\"Conditions\.([^\"]+)\", \"([^\"]+)\"(, )?(.*)\)\n$" % sName, lsConditions[1])
			bDebugLine = False
			if not test:
				test = re.search("^p%s = App.ConditionScript_Create\(\"Conditions\.([^\"]+)\", \"([^\"]+)\"(, )?(.*)\)\n$" % sName, lsConditions[2])
				bDebugLine = True
			sModule, sClass, sArgs = test.group(1,2,4)
			if sModule != sClass:
				print("Unusual Condition: Module(%s), Class(%s)" % (sModule, sClass))

			if not sArgs:
				sArgs = ""

			if bDebugLine:
				iNextUnusedLine = 3
			else:
				iNextUnusedLine = 2

		self.sName = sName
		self.sClass = sModule
		self.sParams = sArgs

		# Return all the lines we didn't use, loading this condition.		
		return lsConditions[iNextUnusedLine:]

	def Save(self, pFile):
		pFile.write("\t#### Condition %s\n" % self.sName)
		sOutputArgs = ""
		if self.sParams:
			sOutputArgs = ", " + self.sParams
		pFile.write("\tp%s = App.ConditionScript_Create(\"Conditions.%s\", \"%s\"%s)\n" % (self.sName, self.sClass, self.sClass, sOutputArgs))

	def CreateCopy(self):
		pCopy = Condition(self.sName[:], self.sClass[:], self.sParams[:])
		self.InitializeCopy(pCopy)
		return pCopy

	def InitializeCopy(self, pCopy):
		pass

class PlainAIEntity(AIEntity):
	def __init__(self, pOutput):
		# Base class init
		AIEntity.__init__(self, pOutput, "Scripted")
		
		# Setup member vars:
		self.sScriptName = ""
		self.lsScriptSetup = []
	
	def Load(self, lsCreationText):
		# Parent class load..
		AIEntity.Load(self, lsCreationText)

		# Look for our SetScriptModule line, and grab our script
		# name from that.
		matchstr = re.compile("^p(.*)\.SetScriptModule\(\"(.*)\"\)\n$")
		for sLine in lsCreationText:
			match = matchstr.search(sLine)
			if match:
				self.sScriptName = match.group(2)
				break
		
		# If we have a GetScriptInstance line, that means we
		# have additional script function calls, for setup.
		# Look for the GetScriptInstance line....
		matchstr = re.compile("^pScript = p(.*)\.GetScriptInstance\(\)\n$")
		lsFunctionLines = []
		for iLine in range(len(lsCreationText)):
			if matchstr.search(lsCreationText[iLine]):
				# Found a match.  Lines following this one
				# should be function calls..
				lsFunctionLines = lsCreationText[(iLine+1):]
		
		# Cycle through all the lines that call functions on our
		# script, and grab the functions and args they're using.
		self.lsScriptSetup = []
		matchstr = re.compile("^pScript\.(.*)\n$")
		for sLine in lsFunctionLines:
			match = matchstr.search(sLine)
			if match:
				# Yep, it seems to follow this format.
				# Grab the function call...
				self.lsScriptSetup.append( match.group(1) )

	def Save(self, pFile):
		# Output the comments that surround our creation:
		pFile.write(sSeparationBlock)
		pFile.write("\t# Creating PlainAI %s at (%d, %d)\n" % (self.GetName(), self.vPos[0], self.vPos[1]))

		# Create our AI
		pFile.write("\tp%s = App.PlainAI_Create(pShip, \"%s\")\n" % (self.GetName(), self.GetName()))
		if len(self.sScriptName):
			pFile.write("\tp%s.SetScriptModule(\"%s\")\n" % (self.GetName(), self.sScriptName))
		else:
			print "WARNING: No script module set for " + self.GetName()

		# Parent class save..
		AIEntity.Save(self, pFile)

		# Do all the script setup for this AI
		if len(self.lsScriptSetup):
			pFile.write("\tpScript = p%s.GetScriptInstance()\n" % self.GetName())
			for sSetup in self.lsScriptSetup:
				pFile.write("\tpScript.%s\n" % sSetup)

		# We're done.
		pFile.write("\t# Done creating PlainAI %s\n" % self.GetName())
		pFile.write(sSeparationBlock)

		# Write any text that should appear after this AI.
		pFile.write(self.sPostEntitySaveText)

	def CreateCopy(self):
		pCopy = PlainAIEntity(self.pOutput)
		self.InitializeCopy(pCopy)
		return pCopy

	def InitializeCopy(self, pCopy):
		# Parent class first.
		AIEntity.InitializeCopy(self, pCopy)

		# Copy our script info.
		pCopy.sScriptName = self.sScriptName[:]
		for sLine in self.lsScriptSetup:
			pCopy.lsScriptSetup.append( sLine[:] )

	def Configure(self, event):
		PlainAIConfigurationDialog(self.pOutput, self)

class PlainAIConfigurationDialog(ConfigurationDialog):
	def __init__(self, pOutput, pAI):
		# Base class init
		ConfigurationDialog.__init__(self, pOutput, pAI, EditPostAIText=GetAdvancedFeatures())

		# Set a nice title.
		self.title("PlainAI(%s) config" % self.pAI.GetName())

		# Get a list of the script modules that this
		# can choose from...
		lsScriptModules = self.GetAvailableModules()
		self.sCurrentModule = self.pAI.sScriptName
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=NW)
		Label(pFrame, text="Script module:").pack(side=LEFT)
		lRadioFrames = ( Frame(pFrame), Frame(pFrame) )
		pRadioFrameLeft, pRadioFrameRight = lRadioFrames
		pRadioFrameLeft.pack(side=LEFT, fill=Y, anchor=N)
		pRadioFrameRight.pack(side=RIGHT, fill=Y, anchor=N)
		self.pModuleVar = IntVar()
		for iIndex in range( len(lsScriptModules) ):
			sModule = lsScriptModules[iIndex]
			pRadio = Radiobutton(lRadioFrames[iIndex * 2 / len(lsScriptModules)], text=sModule, variable = self.pModuleVar, value=iIndex+1, command=lambda self=self, iIndex=iIndex: self.SelectModule(iIndex))
			pRadio.pack(side=TOP, anchor=W)

		self.pFunctionFrame = Frame(self)
		self.pFunctionFrame.pack(side=TOP, fill=X, anchor=W)
		Label(self.pFunctionFrame, text="Available setup functions:").pack(side=TOP, anchor=W)
		self.lpFunctionInfo = []

		# Copy the script setup entries from the AI.
		self.lsScriptSetupEntries = []
		for sEntry in self.pAI.lsScriptSetup:
			self.lsScriptSetupEntries.append(sEntry[:])

		# Update our radio buttons, now that all our necessary
		# variables have been created.
		self.UpdateModule()

	def __del__(self):
		print "PlainAIConfig del."
		ConfigurationDialog.__del__(self)

	def GetAvailableModules(self):
		import dircache
		lsDir = dircache.listdir(GetPlainAIPath())
		matchstr = re.compile("^([A-Za-z0-9]+)\.py$")
		lsAvailable = []
		for sEntry in lsDir:
			match = matchstr.search(sEntry)
			if match:
				sMatch = match.group(1)

				# Search the file for special flags indicating
				# that it's not a valid AI to include in the editor.
				if GetAdvancedFeatures()  or  self.IsValidAIFile(sMatch + ".py"):
					lsAvailable.append(sMatch)
		
		return lsAvailable

	def IsValidAIFile(self, sFilename):
		sFullFilename = os.path.normpath( os.path.join(GetPlainAIPath(), sFilename) )

		file = open(sFullFilename, "rt")
		if file:
			matchflags = re.compile("^# AIEditor flags: (.*)")
			for line in file.readlines():
				match = matchflags.search(line)
				if match and match.group(1):
					# Found AI flags..  NOTINLIST flag excludes
					# the AI from being valid.
					for sFlag in string.split(match.group(1), " "):
						if sFlag == "NOTINLIST":
							return 0
		file.close()
		
		# Must be valid.
		return 1

	def GetSetupFunctions(self, sModule):
		lsFunctions = []
		lFunctionsWithInfo = []
		# Open up the module...
		pFile = open(GetPlainAIPath() + "/" + sModule + ".py")
		if pFile:
			# Read through the file, looking for
			# functions in the class...
			pFunctionMatch = re.compile("^\tdef ([A-Za-z0-9]+)\(self, (.*)\): #AISetup\n$")
			pRequiredParamsLine = re.compile("^\t\tself.SetRequiredParams\(")

			sRequiredParamsLine = None
			iNeedParens = 0
			sLine = pFile.readline()
			while sLine:
				pMatch = pFunctionMatch.search(sLine)
				if pMatch:
					# Found a match.  Add it to the list.
					lsFunctions.append([pMatch.group(1), pMatch.group(2)])
				if iNeedParens > 0:
					sRequiredParamsLine = sRequiredParamsLine + string.split(sLine[:-1], "#")[0]
					iNeedParens = iNeedParens + string.count(sLine, "(")
					iNeedParens = iNeedParens - string.count(sLine, ")")
				elif (sRequiredParamsLine is None)  and  pRequiredParamsLine.search(sLine):
					# Found the start of a SetRequiredParams line.
					# Start counting the number of open and close parens.
					# Stop grabbing lines when we get the last close paren.
					sRequiredParamsLine = string.split(sLine[:-1], "#")[0]
					iNeedParens = string.count(sLine, "(")
					iNeedParens = iNeedParens - string.count(sLine, ")")

				sLine = pFile.readline()
			pFile.close()

			# Parse required params.
			lsRequiredParams = []
			pRequiredInfoMatch = re.compile("\t\t" + r"self.SetRequiredParams\((\s*\(\s*\"([^\"]+)\",\s+\"([^\"]+)\"\s*\),?)+\s*\)")
			while 1:			
				match = pRequiredInfoMatch.search(sRequiredParamsLine)
				if not match:
					break

				lsRequiredParams.append(match.group(3))

				#print "Matched:\n%s\n%s\n%s" % match.group(1,2,3)
				sRequiredParamsLine = sRequiredParamsLine[:match.start(1)] + sRequiredParamsLine[match.end(1):]

			for sFunc, sArgs in lsFunctions:
				iRequired = 0
				for sRequiredParam in lsRequiredParams:
					if sFunc == sRequiredParam:
						iRequired = 1
						break
				lFunctionsWithInfo.append((sFunc, sArgs, iRequired))

		return lFunctionsWithInfo

	def UpdateModule(self):
		"Update the radio buttons to correctly reflect the"
		"currently selected module."
		# Look through the available modules...
		lsScriptModules = self.GetAvailableModules()
		for iIndex in range( len(lsScriptModules) ):
			# Check for one that matches our AI's listed
			# module.
			sModule = lsScriptModules[iIndex]
			if self.pAI.sScriptName == sModule:
				# Found it.  Set and update...
				self.pModuleVar.set(iIndex+1)
				self.SelectModule(iIndex)

	def SelectModule(self, iIndex):
		lsModules = self.GetAvailableModules()
		self.sCurrentModule = lsModules[iIndex]
		
		# Fill in the function info in the function frame,
		# letting the user know what functions are available.
		self.UpdateSetupFunctions( self.sCurrentModule )

	def UpdateSetupFunctions(self, sModule):
		# Remove our old functions...
		for pEntry, iEnabled, sFunction, sParamEntry, sDefaultParams, pEntryField in self.lpFunctionInfo:
			pEntry.destroy()
		self.lpFunctionInfo = []
		
		# Add the updated functions...
		lsFunctions = self.GetSetupFunctions(sModule)
		for sFunction, sParams, iRequired in lsFunctions:
			iEnabled = IntVar()
			sParamEntry = StringVar()

			sColor = ("black", "red")[iRequired]

			pFunctionFrame = Frame(self.pFunctionFrame)
			pFunctionFrame.pack(side=TOP, anchor=W, fill=X, expand=YES)
			Checkbutton(pFunctionFrame, text=sFunction, foreground=sColor, variable=iEnabled, command=lambda self=self, sFunction=sFunction : self.FunctionToggle(sFunction)).pack(side=LEFT)
			Label(pFunctionFrame, text="(").pack(side=LEFT)
			pEntryField = Entry(pFunctionFrame, width=60, textvariable = sParamEntry)
			pEntryField.pack(side=LEFT, fill=X, expand=YES)
			Label(pFunctionFrame, text=")").pack(side=LEFT)

			self.lpFunctionInfo.append((pFunctionFrame, iEnabled, sFunction, sParamEntry, sParams, pEntryField))

			# Check if this function should be enabled.  It should
			# be enabled if we have info on this function in the
			# lsScriptSetupEntries member.
			iEnabled.set(0)
			for sSetupEntry in self.lsScriptSetupEntries:
				# Check if the beginning of this entry matches
				# the function name.
				if sSetupEntry[:len(sFunction)] == sFunction:
					iEnabled.set(1)
					sParamEntry.set(sSetupEntry[len(sFunction + "("):-1])

			# If it's not enabled, set its text to the parameters
			# for the function.
			if not iEnabled.get():
				sParamEntry.set(sParams)
				pEntryField["state"] = DISABLED
				pEntryField["foreground"] = "gray"

	def FunctionToggle(self, sToggleFunction):
		# Find this function, and all its info...
		for pEntry, iEnabled, sFunction, sParamEntry, sDefaultParams, pEntryField in self.lpFunctionInfo:
			if sFunction == sToggleFunction:
				# This is the one.
				if iEnabled.get():
					pEntryField["state"] = NORMAL
					pEntryField["foreground"] = "black"
				else:
					pEntryField["state"] = DISABLED
					pEntryField["foreground"] = "gray"
					sParamEntry.set(sDefaultParams)

				break

	def Apply(self):
		# Copy our script module name to the AI
		self.pAI.sScriptName = self.sCurrentModule

		# Copy our script setup lines to the AI
		lsScriptSetup = []
		for pEntry, iEnabled, sFunction, sParamEntry, sDefaultParams, pEntryField in self.lpFunctionInfo:
			if iEnabled.get():
				sSetup = sFunction + "(" + sParamEntry.get() + ")"
				lsScriptSetup.append(sSetup)

		self.pAI.lsScriptSetup = lsScriptSetup

		# Parent class Apply.
		ConfigurationDialog.Apply(self)

class PreprocessingAIEntity(ContainingAIEntity):
	def __init__(self, pOutput):
		# Base class init
		ContainingAIEntity.__init__(self, pOutput, "Preprocessing", ContainBoxOutline = "green", ContainBoxFill="lightgray")

		# Custom AI params:
		self.lsSetup = []
		self.sFunction = ""
		self.sMethod = ""

	def Load(self, lsCreationText):
		# Parent class load..
		ContainingAIEntity.Load(self, lsCreationText)

		# Grab any pre-creation setup:
		sStartLine = "## Setup:\n"
		sEndLine = "## The PreprocessingAI:\n"
		lsSetup = GrabLinesBetween(sStartLine, sEndLine, lsCreationText)
		self.LoadSetupScript(lsSetup)

		# Look for a SetPreprocessingFunction line...
		matchstr = re.compile("^p(.*)\.SetPreprocessingFunction\((.*)\)\n$")
		for sLine in lsCreationText:
			match = matchstr.search(sLine)
			if match:
				self.sFunction = match.group(2)

		# Look for a SetPreprocessingMethod line...
		matchstr = re.compile("^p(.*)\.SetPreprocessingMethod\((.*), \"(.*)\"\)\n$")
		for sLine in lsCreationText:
			match = matchstr.search(sLine)
			if match:
				self.sMethod = "%s.%s" % match.group(2,3)

		# Look for a SetContainedAI line...
		matchstr = re.compile("^p(.*)\.SetContainedAI\(p(.*)\)\n$")
		for sLine in lsCreationText:
			match = matchstr.search(sLine)
			if match:
				# Get the name of the contained AI...
				sContainedName = match.group(2)
				
				# Get the AI entity by this name...
				pEntity = self.pOutput.GetEntityByName(sContainedName)
				
				self.SetContainedEntity(pEntity)
		
		# Done.

	def LoadSetupScript(self, lsSetupLines):
		# These lines go straight into our lsSetup variable,
		# once we strip the ending \n's
		self.lsSetup = []
		for sLine in lsSetupLines:
			self.lsSetup.append( sLine[:-1] )

	def Save(self, pFile):
		# First step in saving is to create the AI we contain...
		if self.GetContainedEntity():
			self.GetContainedEntity().Save(pFile)
		else:
			print "WARNING: Preprocessing AI \"%s\" has no contained AI" % self.GetName()

		# Next, output the comments that surround our creation:
		pFile.write(sSeparationBlock)
		pFile.write("\t# Creating PreprocessingAI %s at (%d, %d)\n" % (self.GetName(), self.vPos[0], self.vPos[1]))

		# Do our pre-creation setup:
		if len(self.lsSetup):
			pFile.write("\t## Setup:\n")

			for sLine in self.lsSetup:
				pFile.write("\t%s\n" % sLine)
		else:
			print "WARNING: Preprocessing AI \"%s\" has setup" % self.GetName()

		# Create ourselves:
		pFile.write("\t## The PreprocessingAI:\n")
		pFile.write("\tp%s = App.PreprocessingAI_Create(pShip, \"%s\")\n" % (self.GetName(), self.GetName()))

		# Parent class save..
		ContainingAIEntity.Save(self, pFile)

		if len(self.sFunction) or len(self.sMethod):
			# Set our preprocessing function, if any:
			if len(self.sFunction):
				pFile.write("\tp%s.SetPreprocessingFunction(%s)\n" % (self.GetName(), self.sFunction))

			# Set our preprocessing method, if any:
			if len(self.sMethod):
				sSplitString = string.split(self.sMethod, ".")
				sInstance = sSplitString[0]
				sMethod = sSplitString[1]
				pFile.write("\tp%s.SetPreprocessingMethod(%s, \"%s\")\n" % (self.GetName(), sInstance, sMethod))
		else:
			print "WARNING: No preprocessing function or method setup for " + self.GetName()

		# Save which AI we contain:
		if self.GetContainedEntity():
			pFile.write("\tp%s.SetContainedAI(p%s)\n" % (self.GetName(), self.GetContainedEntity().GetName()))

		# We're done
		pFile.write("\t# Done creating PreprocessingAI %s\n" % self.GetName())
		pFile.write(sSeparationBlock)

		# Write any text that should appear after this AI.
		pFile.write(self.sPostEntitySaveText)

	def CreateCopy(self):
		pCopy = PreprocessingAIEntity(self.pOutput)
		self.InitializeCopy(pCopy)
		return pCopy

	def InitializeCopy(self, pCopy):
		# Parent class first.
		ContainingAIEntity.InitializeCopy(self, pCopy)

		# Copy our script info.
		for sLine in self.lsSetup:
			pCopy.lsSetup.append( sLine[:] )
		pCopy.sFunction = self.sFunction[:]
		pCopy.sMethod = self.sMethod[:]

	def Configure(self, event = None):
		PreprocessingAIConfigurationDialog(self.pOutput, self)

class PreprocessingAIConfigurationDialog(ConfigurationDialog):
	def __init__(self, pOutput, pAI):
		# Base class init
		ConfigurationDialog.__init__(self, pOutput, pAI, EditPostAIText=GetAdvancedFeatures())

		# Set a nice title.
		self.title("PreprocessingAI(%s) config" % self.pAI.GetName())

		# Let the user specify code to set things up.
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=NW)
		Label(pFrame, text="Setup code:").pack(side=TOP)
		self.pSetupText = Text(pFrame, width=80, height=8)
		self.pSetupText.pack(side=TOP, anchor=NW, fill=BOTH)
		# Fill the setup text box with whatever setup text we have.
		for sLine in self.pAI.lsSetup:
			self.pSetupText.insert(END, sLine + "\n")

		# Let the user specify a preprocessing function:
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=W)
		Label(pFrame, text="Function:").pack(side=LEFT)
		sVar = StringVar()
		self.pFunctionEntry = Entry(pFrame, width=30, textvariable=sVar)
		self.pFunctionEntry.pack(side=LEFT)
		sVar.set( self.pAI.sFunction )

		# Let the user specify a preprocessing method:
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=W)
		Label(pFrame, text="Method (Instance.Method):").pack(side=LEFT)
		sVar = StringVar()
		self.pMethodEntry = Entry(pFrame, width=40, textvariable=sVar)
		self.pMethodEntry.pack(side=LEFT)
		sVar.set( self.pAI.sMethod )

	def Apply(self):
		# Copy our script setup lines to the AI
		lsSplit = string.split(self.pSetupText.get(0.0, END), "\n")
		lsSetup = []
		for sLine in lsSplit:
			if len(sLine):
				lsSetup.append(sLine)

		self.pAI.lsSetup = lsSetup

		# Copy our function name to the AI
		self.pAI.sFunction = self.pFunctionEntry.get()
		
		# Copy our method name to the AI
		self.pAI.sMethod = self.pMethodEntry.get()

		# Parent class Apply.
		ConfigurationDialog.Apply(self)

class AIEntityWithSequenceBlock(AIEntity):
	def __init__(self, pOutput, sName, SequenceBlockLineColor="blue"):
		# Base class init
		AIEntity.__init__(self, pOutput, sName, SequenceBlockLineColor)

		self.pSequenceBlock = SequenceBlock(pOutput, self, ParentLineColor=SequenceBlockLineColor)

	def Delete(self):
		# Need to delete our sequence block:
		self.pSequenceBlock.Delete()
		self.pSequenceBlock = None
		
		# Parent class delete...
		AIEntity.Delete(self)

	def LoadSequenceBlock(self, lsCreationText):
		# Look for the group of AddAI calls, and grab the names of
		# the AI's that we're adding.
		matchstr = re.compile("^p(.*)\.AddAI\(p([A-Za-z0-9_]+)(, [0-9]+)?\)\n$")
		lsAddEntities = []
		for sLine in lsCreationText:
			match = matchstr.search(sLine)
			if match:
				sName = match.group(2)
				pEntity = self.pOutput.GetEntityByName(sName)
				if pEntity:
					lsAddEntities.append(pEntity)
		
		# Ok, we have the list of entities in the priority list (in order).
		# Setup our sequence block to handle this many entities, then
		# set it to contain these.
		if len(lsAddEntities) > 0:
			self.pSequenceBlock.Resize(len(lsAddEntities))
			
			for iEntity in range( len(lsAddEntities) ):
				self.pSequenceBlock.SetContainedEntity(iEntity, lsAddEntities[iEntity])

		# Look for a comment about where the sequence block should
		# be positioned...
		matchstr = re.compile("^# SeqBlock is at \((.*), (.*)\)\n$")
		for sLine in lsCreationText:
			match = matchstr.search(sLine)
			if match:
				iXPos = string.atoi( match.group(1) )
				iYPos = string.atoi( match.group(2) )
				
				self.pSequenceBlock.MoveTo(iXPos, iYPos)

	def SaveSequenceBlock(self, pFile):
		# Save a comment about where the sequence block is.
		pFile.write("\t# SeqBlock is at (%d, %d)\n" % (self.pSequenceBlock.vPos[0], self.pSequenceBlock.vPos[1]))

		# Save the contents of the sequence block, in a bunch
		# of AddAI function calls.
		for sName in self.pSequenceBlock.GetNameList():
			pFile.write("\tp%s.AddAI(p%s)\n" % (self.GetName(), sName))

	def GetBlockAttachPoint(self):
		box = self.pCanvas.bbox(self.GetMainTag())
		return ( box[2], (box[1] + box[3]) / 2 )

	def MoveTo(self, x, y):
		# Parent MoveTo
		AIEntity.MoveTo(self, x, y)
		
		# Update our sequence block...
		self.pSequenceBlock.Redraw()

	def InitializeCopy(self, pCopy):
		# Parent class first.
		AIEntity.InitializeCopy(self, pCopy)

		# Copy the # of items in the sequence block.
		pCopy.pSequenceBlock.Resize( self.pSequenceBlock.iNumBlocks )


class PriorityListAIEntity(AIEntityWithSequenceBlock):
	def __init__(self, pOutput):
		# Base class init
		AIEntityWithSequenceBlock.__init__(self, pOutput, "PriorityList", SequenceBlockLineColor="orange")
	
	def Load(self, lsCreationText):
		# Parent class load..
		AIEntityWithSequenceBlock.Load(self, lsCreationText)

		self.LoadSequenceBlock(lsCreationText)

	def Save(self, pFile):
		# First, we need to setup all the AI's we contain.
		for pAI in self.pSequenceBlock.GetAIList():
			if pAI:
				pAI.Save(pFile)

		# Output the comments that surround our creation:
		pFile.write(sSeparationBlock)
		pFile.write("\t# Creating PriorityListAI %s at (%d, %d)\n" % (self.GetName(), self.vPos[0], self.vPos[1]))

		# Create our AI
		pFile.write("\tp%s = App.PriorityListAI_Create(pShip, \"%s\")\n" % (self.GetName(), self.GetName()))

		# Parent class save..
		AIEntityWithSequenceBlock.Save(self, pFile)

		# Add all our contained AI's.
		self.SaveSequenceBlock(pFile)

		# We're done.
		pFile.write("\t# Done creating PriorityListAI %s\n" % self.GetName())
		pFile.write(sSeparationBlock)

		# Write any text that should appear after this AI.
		pFile.write(self.sPostEntitySaveText)

	def SaveSequenceBlock(self, pFile):
		# Save a comment about where the sequence block is.
		pFile.write("\t# SeqBlock is at (%d, %d)\n" % (self.pSequenceBlock.vPos[0], self.pSequenceBlock.vPos[1]))

		# Save the contents of the sequence block, in a bunch
		# of AddAI function calls.
		for iIndex in range( len(self.pSequenceBlock.GetNameList()) ):
			pFile.write("\tp%s.AddAI(p%s, %d)\n" % (self.GetName(), self.pSequenceBlock.GetNameList()[iIndex], iIndex+1))


	def CreateCopy(self):
		pCopy = PriorityListAIEntity(self.pOutput)
		self.InitializeCopy(pCopy)
		return pCopy

	def InitializeCopy(self, pCopy):
		# Parent class first.
		AIEntityWithSequenceBlock.InitializeCopy(self, pCopy)

	def Configure(self, event):
		PriorityListAIConfigurationDialog(self.pOutput, self)

class PriorityListAIConfigurationDialog(ConfigurationDialog):
	def __init__(self, pOutput, pAI):
		# Base class init
		ConfigurationDialog.__init__(self, pOutput, pAI, EditPostAIText=GetAdvancedFeatures())

		# Set a nice title.
		self.title("PriorityListAI(%s) config" % self.pAI.GetName())

		# Setup the number of items in the sequence.
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=W)
		Label(pFrame, text="Number of AI's:").pack(side=LEFT)
		self.iNumContainedVar = IntVar()
		Entry(pFrame, width=5, textvariable=self.iNumContainedVar).pack(side=LEFT)
		self.iNumContainedVar.set( self.pAI.pSequenceBlock.iNumBlocks )

	def Apply(self):
		# Set our number of contained AI's, if it's valid.
		iNum = self.iNumContainedVar.get()
		if iNum < 1:
			iNum = 1
		elif iNum > 50:
			iNum = 50
		self.pAI.pSequenceBlock.Resize(iNum)

		# Parent class Apply.
		ConfigurationDialog.Apply(self)

class SequenceAIEntity(AIEntityWithSequenceBlock):
	def __init__(self, pOutput):
		# Base class init
		AIEntityWithSequenceBlock.__init__(self, pOutput, "Sequence", SequenceBlockLineColor="blue")

		# Setup member vars:
		self.iLoopCount = 1
		self.bResetIfInterrupted = 1
		self.bDoubleCheckAllDone = 0
		self.bSkipDormant = 0

		self.lSetupFuncs = [ ( "SetLoopCount",
				       "Loop count (-1=infinite):",
				       self.SetLoopCount,
				       self.GetLoopCount ),
				     ( "SetResetIfInterrupted",
				       "Reset if interrupted",
				       self.SetResetIfInterrupted,
				       self.GetResetIfInterrupted ),
				     ( "SetDoubleCheckAllDone",
				       "Double check all done",
				       self.SetDoubleCheckAllDone,
				       self.GetDoubleCheckAllDone ),
				     ( "SetSkipDormant",
				       "Skip dormant AI's",
				       self.SetSkipDormant,
				       self.GetSkipDormant ) ]

	def SetLoopCount(self, iCount):
		self.iLoopCount = iCount
	def GetLoopCount(self):
		return self.iLoopCount
		
	def SetResetIfInterrupted(self, bFlag):
		self.bResetIfInterrupted = bFlag
	def GetResetIfInterrupted(self):
		return self.bResetIfInterrupted
		
	def SetDoubleCheckAllDone(self, bFlag):
		self.bDoubleCheckAllDone = bFlag
	def GetDoubleCheckAllDone(self):
		return self.bDoubleCheckAllDone

	def SetSkipDormant(self, bFlag):
		self.bSkipDormant = bFlag
	def GetSkipDormant(self):
		return self.bSkipDormant

	def Load(self, lsCreationText):
		# Parent class load.
		AIEntityWithSequenceBlock.Load(self, lsCreationText)

		# Find the calls to the functions that setup our parameters.
		# Set the appropriate variables...
		for sName, lUnused, pSetFunc, pReadFunc in self.lSetupFuncs:
			matchstr = re.compile("^p(.*)\.%s\((.*)\)\n$" % sName)
			for sLine in lsCreationText:
				match = matchstr.search(sLine)
				if match:
					# Found it.  Call the function with the
					# (numeric) value we found.
					iValue = string.atoi( match.group(2) )
					pSetFunc(iValue)

		self.LoadSequenceBlock(lsCreationText)

	def Save(self, pFile):
		# First, we need to setup all the AI's we contain.
		for pAI in self.pSequenceBlock.GetAIList():
			if pAI:
				pAI.Save(pFile)

		# Output the comments that surround our creation:
		pFile.write(sSeparationBlock)
		pFile.write("\t# Creating SequenceAI %s at (%d, %d)\n" % (self.GetName(), self.vPos[0], self.vPos[1]))

		# Create our AI
		pFile.write("\tp%s = App.SequenceAI_Create(pShip, \"%s\")\n" % (self.GetName(), self.GetName()))

		# Parent class save..
		AIEntityWithSequenceBlock.Save(self, pFile)

		# Do all the setup for this AI
		for sFunc, lUnused, pSetFunc, pGetFunc in self.lSetupFuncs:
			pFile.write("\tp%s.%s(%s)\n" % (self.GetName(), sFunc, pGetFunc()))

		# Add all our contained AI's.
		self.SaveSequenceBlock(pFile)

		# We're done.
		pFile.write("\t# Done creating SequenceAI %s\n" % self.GetName())
		pFile.write(sSeparationBlock)

		# Write any text that should appear after this AI.
		pFile.write(self.sPostEntitySaveText)

	def CreateCopy(self):
		pCopy = SequenceAIEntity(self.pOutput)
		self.InitializeCopy(pCopy)
		return pCopy

	def InitializeCopy(self, pCopy):
		# Parent class first.
		AIEntityWithSequenceBlock.InitializeCopy(self, pCopy)

		# Copy our config info.
		pCopy.iLoopCount = self.iLoopCount
		pCopy.bResetIfInterrupted = self.bResetIfInterrupted
		pCopy.bDoubleCheckAllDone = self.bDoubleCheckAllDone
		pCopy.bSkipDormant = self.bSkipDormant

	def Configure(self, event):
		SequenceAIConfigurationDialog(self.pOutput, self)

class SequenceAIConfigurationDialog(ConfigurationDialog):
	def __init__(self, pOutput, pAI):
		# Base class init
		ConfigurationDialog.__init__(self, pOutput, pAI, EditPostAIText=GetAdvancedFeatures())

		# Set a nice title.
		self.title("SequenceAI(%s) config" % self.pAI.GetName())

		# Setup the number of items in the sequence.
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=W)
		Label(pFrame, text="Number of AI's:").pack(side=LEFT)
		self.iNumContainedVar = IntVar()
		Entry(pFrame, width=5, textvariable=self.iNumContainedVar).pack(side=LEFT)
		self.iNumContainedVar.set( self.pAI.pSequenceBlock.iNumBlocks )

		# Loopcount:
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=W)
		Label(pFrame, text=self.pAI.lSetupFuncs[0][1]).pack(side=LEFT)
		self.iLoopVal = IntVar()
		Entry(pFrame, width=5, textvariable=self.iLoopVal).pack(side=LEFT)
		self.iLoopVal.set( self.pAI.iLoopCount )

		# Flags:
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=W)
		self.bReset = IntVar()
		Checkbutton(pFrame, text=self.pAI.lSetupFuncs[1][1], variable=self.bReset).pack(side=TOP)
		self.bReset.set(self.pAI.bResetIfInterrupted)
		self.bDouble = IntVar()
		Checkbutton(pFrame, text=self.pAI.lSetupFuncs[2][1], variable=self.bDouble).pack(side=TOP)
		self.bDouble.set(self.pAI.bDoubleCheckAllDone)
		self.bSkipDormant = IntVar()
		Checkbutton(pFrame, text=self.pAI.lSetupFuncs[3][1], variable=self.bSkipDormant).pack(side=TOP)
		self.bSkipDormant.set(self.pAI.bSkipDormant)

	def Apply(self):
		# Set our number of contained AI's, if it's valid.
		iNum = self.iNumContainedVar.get()
		if iNum < 1:
			iNum = 1
		elif iNum > 50:
			iNum = 50
		self.pAI.pSequenceBlock.Resize(iNum)

		# Set our loop count
		self.pAI.iLoopCount = self.iLoopVal.get()

		# Set our flags:
		self.pAI.bResetIfInterrupted = self.bReset.get()
		self.pAI.bDoubleCheckAllDone = self.bDouble.get()
		self.pAI.bSkipDormant = self.bSkipDormant.get()

		# Parent class Apply.
		ConfigurationDialog.Apply(self)

class RandomAIEntity(AIEntityWithSequenceBlock):
	def __init__(self, pOutput):
		# Base class init
		AIEntityWithSequenceBlock.__init__(self, pOutput, "Random", SequenceBlockLineColor="darkgreen")

	def Load(self, lsCreationText):
		# Parent class load..
		AIEntityWithSequenceBlock.Load(self, lsCreationText)

		# Not much to do...
		self.LoadSequenceBlock(lsCreationText)

	def Save(self, pFile):
		# First, we need to setup all the AI's we contain.
		for pAI in self.pSequenceBlock.GetAIList():
			if pAI:
				pAI.Save(pFile)

		# Output the comments that surround our creation:
		pFile.write(sSeparationBlock)
		pFile.write("\t# Creating RandomAI %s at (%d, %d)\n" % (self.GetName(), self.vPos[0], self.vPos[1]))

		# Create our AI
		pFile.write("\tp%s = App.RandomAI_Create(pShip, \"%s\")\n" % (self.GetName(), self.GetName()))

		# Parent class save..
		AIEntityWithSequenceBlock.Save(self, pFile)

		# Add all our contained AI's.
		self.SaveSequenceBlock(pFile)

		# We're done.
		pFile.write("\t# Done creating RandomAI %s\n" % self.GetName())
		pFile.write(sSeparationBlock)

		# Write any text that should appear after this AI.
		pFile.write(self.sPostEntitySaveText)

	def CreateCopy(self):
		pCopy = RandomAIEntity(self.pOutput)
		self.InitializeCopy(pCopy)
		return pCopy

	def InitializeCopy(self, pCopy):
		# Parent class first.
		AIEntityWithSequenceBlock.InitializeCopy(self, pCopy)

	def Configure(self, event):
		RandomAIConfigurationDialog(self.pOutput, self)

class RandomAIConfigurationDialog(ConfigurationDialog):
	def __init__(self, pOutput, pAI):
		# Base class init
		ConfigurationDialog.__init__(self, pOutput, pAI, EditPostAIText=GetAdvancedFeatures())

		# Set a nice title.
		self.title("RandomAI(%s) config" % self.pAI.GetName())

		# Setup the number of items in the sequence.
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=W)
		Label(pFrame, text="Number of AI's:").pack(side=LEFT)
		self.iNumContainedVar = IntVar()
		Entry(pFrame, width=5, textvariable=self.iNumContainedVar).pack(side=LEFT)
		self.iNumContainedVar.set( self.pAI.pSequenceBlock.iNumBlocks )

	def Apply(self):
		# Set our number of contained AI's, if it's valid.
		iNum = self.iNumContainedVar.get()
		if iNum < 1:
			iNum = 1
		elif iNum > 50:
			iNum = 50
		self.pAI.pSequenceBlock.Resize(iNum)

		# Parent class Apply.
		ConfigurationDialog.Apply(self)


class SequenceBlock(CanvasUtils.DraggableCanvasIcon):
	"A line of blocks that can contain AI objects."
	def __init__(self, pOutput, pParentAI, posx=100, posy=80, ParentLineColor="blue"):
		# Parent class init...
		CanvasUtils.DraggableCanvasIcon.__init__(self, pOutput, posx, posy)
		# Setup member vars
		self.pOutput = pOutput
		self.pCanvas = pOutput
		self.iNumBlocks = 1
		self.pParentAI = pParentAI
		self.kParentLineColor = ParentLineColor

		self.iBoxWidth = 16
		self.iBoxHeight = 16

		self.lContainedEntities = range(self.iNumBlocks)
		for i in range(self.iNumBlocks):
			self.lContainedEntities[i] = None

		# Setup our graphical bits.
		self.liContainedLines = []
		self.iParentLine = None
		self.liBoxes = []
		self.CreateGraphics()

		# Setup our event handlers
		self.vLastDragPos = None
		self.pCanvas.tag_bind(self.GetMainTag(), "<Button-1>", self.DragButtonDown)
		self.pCanvas.tag_bind(self.GetMainTag(), "<ButtonRelease-1>", self.DragButtonUp)
		self.pCanvas.tag_bind(self.GetMainTag(), "<B1-Motion>", self.DragButtonDragged)
		self.pCanvas.tag_bind(self.GetMainTag(), "<Button-3>", self.ConnectButtonDown)
		self.pCanvas.tag_bind(self.GetMainTag(), "<ButtonRelease-3>", self.ConnectButtonUp)
		self.pCanvas.tag_bind(self.GetMainTag(), "<B3-Motion>", self.ConnectButtonDrag)

	def Delete(self):
		# Delete all our graphical bits:

		# Remove our old lines:
		for iLine in self.liContainedLines:
			self.pCanvas.delete(iLine)
		# Remove our parent line
		self.pCanvas.delete(self.iParentLine)
		# Remove our boxes.
		self.pCanvas.delete(self.GetMainTag())
		
		# Uncontain our contained AI's.
		for pAI in self.lContainedEntities:
			if pAI:
				pAI.SetContainingEntity(None)

	def Resize(self, iNewSize):
		# Add to our contained AI list, if we're growing...
		if iNewSize > self.iNumBlocks:
			for i in range(iNewSize - self.iNumBlocks):
				self.lContainedEntities.append(None)
		elif iNewSize < self.iNumBlocks:
			# If we have contained AI's in the blocks that
			# are being deleted, tell them they're no longer
			# contained.
			for iIndex in range(iNewSize, self.iNumBlocks):
				if self.lContainedEntities[iIndex]:
					self.lContainedEntities[iIndex].SetContainingEntity(None)
					self.lContainedEntities[iIndex] = None

			self.lContainedEntities = self.lContainedEntities[:iNewSize]

		# Resize ourselves...
		self.iNumBlocks = iNewSize
		self.CreateGraphics()
		self.Redraw()

	def CreateGraphics(self):
		# Parent class...
		CanvasUtils.DraggableCanvasIcon.CreateGraphics(self)
		
		# Setup our lines and boxes...
		self.SetupContainedLines()
		self.SetupBoxes()

		# Setup our parent line
		if self.iParentLine is not None:
			self.pCanvas.delete(self.iParentLine)
		vAttach = self.pParentAI.GetBlockAttachPoint()
		vStart = self.GetParentLineStart()
		self.iParentLine = self.pCanvas.create_line(vStart[0], vStart[1], vAttach[0], vAttach[1], fill=self.kParentLineColor)

	def SetupContainedLines(self):
		# Remove our old lines:
		for iLine in self.liContainedLines:
			self.pCanvas.delete(iLine)

		# Setup new ones.
		self.liContainedLines = []
		for i in range(self.iNumBlocks):
			vStart = self.GetLineStart(i)
			iLine = self.pCanvas.create_line(vStart[0], vStart[1], vStart[0], vStart[1], fill=self.kParentLineColor)
			self.liContainedLines.append(iLine)

	def SetupBoxes(self):
		# Remove our old boxes:
		self.pCanvas.delete(self.GetMainTag())

		# Setup new ones
		self.liBoxes = []
		for i in range(self.iNumBlocks):
			vCoords = self.GetBoxCoords(i)
			iBox = self.pCanvas.create_rectangle(vCoords[0], vCoords[1], vCoords[2], vCoords[3], tag=self.GetMainTag(), outline=self.kParentLineColor, fill="white")
			self.liBoxes.append(iBox)

			vCenter = ((vCoords[0] + vCoords[2]) / 2, (vCoords[1] + vCoords[3]) / 2)
			self.pCanvas.create_text(vCenter[0], vCenter[1], text=str(i+1), tag=self.GetMainTag())

	def GetParentLineStart(self):
		return (self.vPos[0], self.vPos[1] + (self.iBoxHeight / 2))

	def GetLineStart(self, iIndex):
		return (self.vPos[0] + (self.iBoxWidth * iIndex) + (self.iBoxWidth / 2),
		        self.vPos[1] + (self.iBoxHeight / 2))

	def GetBoxCoords(self, iIndex):
		xAdj = self.vPos[0] + (self.iBoxWidth * iIndex)
		yAdj = self.vPos[1]
		return ( xAdj, yAdj,
		         xAdj + self.iBoxWidth, yAdj + self.iBoxHeight)

	def MoveTo(self, iXPos, iYPos):
		# Find the difference between our current position and the new position.
		vDiff = (iXPos - self.vPos[0], iYPos - self.vPos[1])
		self.vPos = [iXPos, iYPos]
		self.pCanvas.move(self.GetMainTag(), vDiff[0], vDiff[1])
		self.Redraw()

	def GetIndexAt(self, vPos):
		iIndex = None
		xDiff = vPos[0] - self.vPos[0]
		if xDiff >= 0:
			iIndex = (xDiff / self.iBoxWidth)
			if iIndex > self.iNumBlocks:
				iIndex = None
		
		return iIndex

	def ConnectButtonDown(self, event):
		# Create a temporary line for connecting to an object
		vPos = (event.x, event.y)
		self.iConnectIndex = self.GetIndexAt(vPos)
		vStart = self.GetLineStart( self.iConnectIndex )
		self.iConnectLine = self.pCanvas.create_line(vStart[0], vStart[1], event.x, event.y)
		self.pCanvas.grab_set()

	def ConnectButtonUp(self, event):
		# Remove our temporary line.
		self.pCanvas.delete(self.iConnectLine)
		
		# Check if we released on an AI.  If so, we want to contain
		# that AI now.
		pEntity = self.pOutput.GetEntityAt(event.x, event.y)
		if pEntity  and  (pEntity != self):
			# Got one.  Contain it.
			self.SetContainedEntity(self.iConnectIndex, pEntity)
			self.Redraw()

		self.pCanvas.grab_release()

	def ConnectButtonDrag(self, event):
		# Reposition our connect line
		vStart = self.GetLineStart( self.iConnectIndex )
		self.pCanvas.coords(self.iConnectLine, vStart[0], vStart[1], event.x, event.y)

	def GetNameList(self):
		# Get a list of the names of all the AI's we contain.
		lsNames = []
		for pAI in self.lContainedEntities:
			if pAI:
				lsNames.append(pAI.GetName())
		
		return lsNames

	def GetAIList(self):
		lAIs = []
		for pAI in self.lContainedEntities:
			if pAI:
				lAIs.append(pAI)
		return lAIs

	def SetContainedEntity(self, iIndex, pEntity):
		# If we had an old contained AI here, let it know it's
		# no longer contained here.
		pContained = self.lContainedEntities[iIndex]
		self.lContainedEntities[iIndex] = None
		if pContained:
			pContained.SetContainingEntity(None)
		
		# Set this slot to contain the new AI, if we can.
		if pEntity:
			if pEntity.CanBeContainedBy(self.pParentAI):
				pEntity.SetContainingEntity(self)
				self.lContainedEntities[iIndex] = pEntity

	def RemoveContainedEntity(self, pEntity):
		bRedraw = 0
		for i in range(self.iNumBlocks):
			if self.lContainedEntities[i] == pEntity:
				# Found the match.  Remove it.
				self.SetContainedEntity(i, None)

				# We need to redraw ourselves.
				bRedraw = 1
		
		if bRedraw:
			self.Redraw()

	def Redraw(self):
		# More like reposition, for us...
		# Reposition our lines:
		for i in range(self.iNumBlocks):
			vStart = self.GetLineStart(i)
			vEnd = vStart
			if self.lContainedEntities[i]:
				vEnd = self.lContainedEntities[i].GetAttachPoint()
			
			self.pCanvas.coords(self.liContainedLines[i], vStart[0], vStart[1], vEnd[0], vEnd[1])

		# Reposition our line to our parent.
		vAttach = self.pParentAI.GetBlockAttachPoint()
		vStart = self.GetParentLineStart()
		self.pCanvas.coords(self.iParentLine, vStart[0], vStart[1], vAttach[0], vAttach[1])

class CompoundAIEntity(AIEntity):
	def __init__(self, pOutput):
		# Base class init
		AIEntity.__init__(self, pOutput, "Compound", "purple")
		
		# Setup member vars:
		self.sModule = ""
		self.sFunction = "CreateAI"
		self.sArgs = ""
		self.lFlags = []

	def Load(self, lsCreationText):
		# Look for our "import ..." line, and grab our module
		# name from that.
		matchstr = re.compile("^import (.*)\n$")

		for sLine in lsCreationText:
			match = matchstr.search(sLine)
			if match:
				self.sModule = match.group(1)
				break

		# Look for the function call that gets our AI, and
		# grab the function name and args from that.
		matchstr = re.compile("^p(.*) = %s\.([a-zA-Z0-9_]+)\((.*)\)\n$" % self.sModule)
		for sLine in lsCreationText:
			match = matchstr.search(sLine)
			if match:
				self.sFunction = match.group(2)
				self.sArgs = match.group(3)
				break
		if self.sArgs is None:
			self.sArgs = ""

		# Pull the flags out of the arguments.
		pFlagMatch = re.compile(r"(, )?(\w+)\s*=\s*([-0-9.]+)")
		while 1:
			match = pFlagMatch.search(self.sArgs)
			if match is None:
				break

			# Grab this flag.
			sFlag, sValue = match.group(2,3)
			self.lFlags.append( (sFlag, sValue) )

			self.sArgs = self.sArgs[:match.start()] + self.sArgs[match.end():]

			# sArgs might start with ", " now.  Fix that...
			if len(self.sArgs) >= 2 and self.sArgs[:2] == ", ":
				self.sArgs = self.sArgs[2:]

	def Save(self, pFile):
		# Output the comments that surround our creation:
		pFile.write(sSeparationBlock)
		pFile.write("\t# Creating CompoundAI %s at (%d, %d)\n" % (self.GetName(), self.vPos[0], self.vPos[1]))

		# Import our module
		pFile.write("\timport %s\n" % self.sModule)

		# Add our flags into the arguments
		sArgs = self.sArgs[:]
		if sArgs:
			sPrefix = ", "
		else:
			sPrefix = ""
		for sFlag, sValue in self.lFlags:
			sArgs = sArgs + sPrefix + "%s = %s" % (sFlag, sValue)
			sPrefix = ", "

		# Create our AI
		pFile.write("\tp%s = %s.%s(%s)\n" % (self.GetName(), self.sModule, self.sFunction, sArgs))

		# We're done.
		pFile.write("\t# Done creating CompoundAI %s\n" % self.GetName())
		pFile.write(sSeparationBlock)

		# Write any text that should appear after this AI.
		pFile.write(self.sPostEntitySaveText)

	def CreateCopy(self):
		pCopy = CompoundAIEntity(self.pOutput)
		self.InitializeCopy(pCopy)
		return pCopy

	def InitializeCopy(self, pCopy):
		# Parent class first.
		AIEntity.InitializeCopy(self, pCopy)

		# Copy our config info.
		pCopy.sModule = self.sModule
		pCopy.sFunction = self.sFunction
		pCopy.sArgs = self.sArgs

	def Configure(self, event):
		CompoundAIConfigurationDialog(self.pOutput, self)

class CompoundAIConfigurationDialog(ConfigurationDialog):
	class FlagConfig(Frame):
		def __init__(self, pParent, pConfigDialog, pAI, lSettings, text="", **kw):
			apply(Frame.__init__, (self, pParent), kw)
			self.pConfigDialog = pConfigDialog
			self.bEnabled = IntVar()
			self.sName = text
			self.sEnabledColor = "black"
			self.sDisabledColor = "black"

			self.pFlagConfigCheckbutton = Checkbutton(self, text=self.sName, variable = self.bEnabled, command=self.FlagCheckChanged)
			self.pFlagConfigCheckbutton.pack(side=LEFT)

		def IsEnabled(self):
			return self.bEnabled.get()

		def Enable(self):
			self.bEnabled.set(1)

		def GetName(self):
			return self.sName

		def GetValue(self):
			return None

		def SetColors(self, sEnabled, sDisabled):
			self.sEnabledColor = sEnabled
			self.sDisabledColor = sDisabled

			self.UpdateColors()

		def GetColor(self):
			if self.IsEnabled():
				return self.sEnabledColor
			return self.sDisabledColor

		def UpdateColors(self):
			self.pFlagConfigCheckbutton["foreground"] = self.GetColor()

	class OnOffConfig(FlagConfig):
		def __init__(self, pParent, pConfigDialog, pAI, lSettings, **kw):
			apply(CompoundAIConfigurationDialog.FlagConfig.__init__, (self, pParent, pConfigDialog, pAI, lSettings), kw)
			self.bOnOff = IntVar()

			self.pOnRadio = Radiobutton(self, text="On", variable=self.bOnOff, value = 1)
			self.pOnRadio.pack(side=RIGHT)
			self.pOffRadio = Radiobutton(self, text="Off", variable=self.bOnOff, value = 0)
			self.pOffRadio.pack(side=RIGHT)

			# Check if the AI has information about this flag.
			for sAIFlag, iValue in pAI.lFlags:
				if sAIFlag == self.sName:
					self.Enable()
					self.bOnOff.set( int(iValue) )

			self.FlagCheckChanged()

		def FlagCheckChanged(self):
			# If we're checked, enable the OnOff radio buttons.  If
			# we're not checked, disable them.
			if self.IsEnabled():
				self.pOnRadio["state"] = NORMAL
				self.pOffRadio["state"] = NORMAL
			else:
				self.pOnRadio["state"] = DISABLED
				self.pOffRadio["state"] = DISABLED

			self.pConfigDialog.SetFlagColorsFromModule()
			self.UpdateColors()

		def GetValue(self):
			return self.bOnOff.get()

	class RangeConfig(FlagConfig):
		def __init__(self, pParent, pConfigDialog, pAI, lSettings, **kw):
			apply(CompoundAIConfigurationDialog.FlagConfig.__init__, (self, pParent, pConfigDialog, pAI, lSettings), kw)
			self.fValue = DoubleVar()

			for iIndex in range(len(lSettings)):
				if lSettings[iIndex] == "Range":
					fFrom = float(lSettings[iIndex + 1])
					fTo = float(lSettings[iIndex + 2])
			self.pScale = Scale(self, orient=HORIZONTAL, from_=fFrom, to=fTo, resolution = -1, variable=self.fValue, command=self.ValueChanged)
			self.pScale.pack(side=RIGHT, fill=X, expand=YES)

			# Check if the AI has information about this flag.
			for sAIFlag, fValue in pAI.lFlags:
				if sAIFlag == self.sName:
					self.Enable()
					self.fValue.set( float(fValue) )

			self.FlagCheckChanged()

		def ValueChanged(self, fValue):
			self.pConfigDialog.SetFlagColorsFromModule()

		def FlagCheckChanged(self):
			# If we're checked, enable the slider.
			if self.IsEnabled():
				self.pScale["state"] = NORMAL
				self.pScale["foreground"] = "black"
			else:
				self.pScale["state"] = DISABLED
				self.pScale["foreground"] = "gray"

			self.pConfigDialog.SetFlagColorsFromModule()
			self.UpdateColors()

		def GetValue(self):
			return self.fValue.get()

	def __init__(self, pOutput, pAI):
		# Base class init
		ConfigurationDialog.__init__(self, pOutput, pAI, EditPostAIText=GetAdvancedFeatures())

		# Set a nice title.
		self.title("CompoundAI(%s) config" % self.pAI.GetName())

		# Let the user set the module name:
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=NW)
		Label(pFrame, text="Module:").pack(side=LEFT)
		self.sModuleVar = StringVar()
		self.pModuleEntry = Entry(pFrame, width=40, textvariable=self.sModuleVar)
		self.pModuleEntry.pack(side=LEFT, fill=X, expand=YES)
		self.sModuleVar.set( self.pAI.sModule )
		Button(pFrame, text="Select File", command=self.SelectModule).pack(side=LEFT)

		# Let the user set the function name:
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=NW)
		Label(pFrame, text="Function:").pack(side=LEFT)
		sVar = StringVar()
		self.pFunctionEntry = Entry(pFrame, width=40, textvariable=sVar)
		self.pFunctionEntry.pack(side=LEFT, fill=X, expand=YES)
		sVar.set( self.pAI.sFunction )

		# Once a module has been selected, list what the args
		# should be:
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=NW)
		Label(pFrame, text="Module args:").pack(side=LEFT)
		self.pModuleArgsLabel = Label(pFrame, text="(unknown)")
		self.pModuleArgsLabel.pack(side=LEFT)

		# Let the user set the arguments to the function:
		pFrame = Frame(self)
		pFrame.pack(side=TOP, fill=X, anchor=NW)
		Label(pFrame, text="Function arguments:").pack(side=LEFT)
		sVar = StringVar()
		self.pArgsEntry = Entry(pFrame, width=40, textvariable=sVar)
		self.pArgsEntry.pack(side=LEFT, fill=X, expand=YES)
		sVar.set( self.pAI.sArgs )

		# Some compound AI's have special flags that
		# can be set.  This frame will display those flags,
		# if present.
		self.pFlagOverrideFrame = Frame(self)
		self.pFlagOverrideFrame.pack(side=TOP, fill=X, anchor=NW)
		self.lFlags = []

		if self.sModuleVar.get():
			sModuleFilePath = apply(os.path.join, (GetScriptsPath(),) + tuple(string.split(self.sModuleVar.get(), "."))) + ".py"
			self.SetModule(sModuleFilePath)

	def SelectModule(self):
		# Make a file selection dialog, and have it call
		# our SetModule function when it has a file.
		SelectFileDialog(self, GetCompoundPath(), self.SetModule, SetCompoundPath)

	def SetModule(self, sFile):
		# Make the path relative to the scripts path, and
		# convert any slashes or backslashes to dots.
		sFilePath = os.path.abspath(sFile)

		#print "SetModule %s, scripts(%s)" % (sFile, GetScriptsPath())
		if sFilePath[:len(GetScriptsPath())] == GetScriptsPath():
			# It's inside the build directory.  Good.  Strip off
			# the part of it that is the build directory...
			sModule = sFilePath[len(GetScriptsPath()) + 1:]
			if len(sModule):
				# Replace all slashes with dots.
				sModule = string.replace(sModule, "/", ".")
				sModule = string.replace(sModule, "\\", ".")

				# And strip off the ".py"
				sModule = sModule[:-3]
				self.sModuleVar.set(sModule)

				# Set the pModuleArgsLabel based on this module file.
				try:
					pFile = open(sFilePath, "r")
					lsLines = pFile.readlines()
					pFile.close()
				except IOError:
					lsLines = []

				self.SetModuleArgsFromLines(lsLines)
				self.SetOverrideFlagsFromLines(lsLines)
				self.SetFlagColorsFromModule()

	def SetModuleArgsFromLines(self, lsLines):
		self.pModuleArgsLabel["text"] = "(unknown)"
		pFuncMatch = re.compile("^def %s\((.*)\):" % self.pFunctionEntry.get())
		for sLine in lsLines:
			pMatch = pFuncMatch.match(sLine)
			if pMatch:
				self.pModuleArgsLabel["text"] = pMatch.group(1)
				break

	def SetOverrideFlagsFromLines(self, lsLines):
		# Remove anything currently in the override
		# flag frame.
		for pChild in self.pFlagOverrideFrame.winfo_children():
			pChild.destroy()
		self.lFlags = []

		# Grab AI groups and group tabs..
		pGroupStartMatch = re.compile(r"^\s*# AIGroup\s*\(([^)]+)\)\s*Begin$")
		pGroupEndMatch = re.compile(r"^\s*# AIGroup\s*\(([^)]+)\)\s*End$")
		pGroupTabMatch = re.compile(r"^\s*# AIGroupTab\s*\(([^):]+):([^)]+)\)\s*(.*)$")
		pFlagMatch = re.compile(r"^\s*# AIFlag\(([^)]+)\)\s*(.*)$")

		dGroups = {}
		dTabs = {}
		lsTabs = [] # Needed to keep the tabs in order.
		dGroupDefaultTabs = {}
		lCurrentGroup = None
		sGroup = None
		for sLine in lsLines:
			# Check for group tabs.
			pMatch = pGroupTabMatch.match(string.strip(sLine))
			if pMatch:
				# Found a tab.  Save info on it.
				sTab = pMatch.group(1)
				sGroup = pMatch.group(2)
				dTabs[sTab] = sGroup
				lsTabs.append(sTab)

				# If this tab has the "default" setting for its group,
				# save that info..
				sArgs = pMatch.group(3)
				if "Default" in string.split(sArgs, " "):
					dGroupDefaultTabs[sGroup] = sTab

			# If we're in a group right now, look for flags.
			if lCurrentGroup is not None:
				# First check for a group end marker.
				pMatch = pGroupEndMatch.match(string.strip(sLine))
				if pMatch:
					if pMatch.group(1) == sGroup:
						# Done with this group.
						dGroups[sGroup] = lCurrentGroup
						sGroup = None
						lCurrentGroup = None
						continue

				pMatch = pFlagMatch.match(string.strip(sLine))
				if pMatch:
					sFlag, lSettings = (pMatch.group(1), string.split(pMatch.group(2), " "))

					# Don't include advanced flags, if advanced features aren't on.
					if ("Advanced" in lSettings) and (not GetAdvancedFeatures()):
						continue

					lCurrentGroup.append( [sFlag, lSettings] )
			else:
				# No current group.  Look for a group start marker.
				pMatch = pGroupStartMatch.match(string.strip(sLine))
				if pMatch:
					# Found the start of a group...
					sGroup = pMatch.group(1)
					lCurrentGroup = []

		if dGroups and dTabs:
			# Found group info.  Create some UI for selecting each group.
			import Pmw
			pNotebook = Pmw.NoteBook(self.pFlagOverrideFrame)
			sDefaultTab = None
			for sTab in lsTabs:
				pTab = pNotebook.add(sTab)
				# Add settings under this tab.  If this isn't the
				# default tab, change the names of the flags
				# to match the tab...
				sGroup = dTabs[sTab]
				if (not dGroupDefaultTabs.has_key(sGroup))  or  (dGroupDefaultTabs[sGroup] != sTab):
					lFlags = dGroups[ sGroup ]
					lRevisedFlags = []
					for sFlag, lSettings in lFlags:
						lRevisedFlags.append( (sTab + "_" + sFlag, lSettings) )
				else:
					lRevisedFlags = dGroups[ sGroup ]
					sDefaultTab = sTab

				self.AddFlags(pTab, lRevisedFlags)

			pNotebook.pack(fill=BOTH, expand=YES)
			pNotebook.setnaturalsize()

			# Make sure the default tab is in the foreground.
			if sDefaultTab is not None:
				pNotebook.selectpage( sDefaultTab )
				
		else:
			# No groups.  Just read normal flags.
			# Read in all the flags defined in the file, and their settings.
			lFlags = []
			for sLine in lsLines:
				match = pFlagMatch.match(string.strip(sLine))
				if match:
					sFlag, sSettings = match.group(1, 2)
					lSettings = string.split(sSettings, " ")

					# If this flag should only be available with Advanced features
					# and advanced features aren't available, skip it.
					if ("Advanced" in lSettings) and (not GetAdvancedFeatures()):
						continue

					lFlags.append( (sFlag, lSettings) )

			self.AddFlags(self.pFlagOverrideFrame, lFlags)

	def SetFlagColorsFromModule(self):
		# Get the path to our module.
		if not self.sModuleVar.get():
			return
		sFilePath = apply(os.path.join, (GetScriptsPath(),) + tuple(string.split(self.sModuleVar.get(), "."))) + ".py"

		# Import the given module, and set the colors of all our flag
		# settings based on what the module tells us to do.
		sPath, sFile = os.path.split(sFilePath)
		sPath = os.path.join(sPath, "")
		sFile, sExt = os.path.splitext(sFile)
		import imp
		try:
			pFile, sPathName, sDescription = imp.find_module(sFile, [sPath])
			pModule = imp.load_module(sFile, pFile, sFilePath, sDescription)
		except ImportError, sValue:
			#print "Error importing file for colors: (%s), (%s)" % (sPath, sFile)
			#print sValue
			return

		# Build a dictionary with the keys we have set..
		dKeys = {}
		for sFlag, pValue in self.GetFlagsFromInfo():
			dKeys[sFlag] = pValue

		# Imported the file.  Try running a GetKeyColors function in that module,
		# to get info about what colors the various flags should be.
		try:
			dKeyColors = getattr(pModule, "GetKeyColors")(dKeys)
		except Exception, sValue:
			#print "Error calling %s.GetKeyColors" % sFile
			#print sValue
			return

		# Got a set of colors for the various keys.  Set the flag colors.
		for pFlagConfig in self.lFlags:
			try:
				apply(pFlagConfig.SetColors, dKeyColors[pFlagConfig.GetName()])
			except KeyError: pass

	def AddFlags(self, pFrame, lFlags):
		bHeaderSet = 0
		for sFlag, lSettings in lFlags:
			# Create a class for handling configuration of this flag.
			for sSetting, cClass in [
				("OnOff",	CompoundAIConfigurationDialog.OnOffConfig),
				("Range",	CompoundAIConfigurationDialog.RangeConfig),
				]:

				if sSetting in lSettings:
					# Found the right class.
					if not bHeaderSet:
						Label(pFrame, text="Optional settings:").pack(side=TOP, anchor=W, fill=X, expand=YES)
						Label(pFrame, text="Blue is on at current setting", foreground="blue").pack(side=TOP, anchor=W, fill=X, expand=YES)
						Label(pFrame, text="Dark red is off at current setting", foreground="darkred").pack(side=TOP, anchor=W, fill=X, expand=YES)
						bHeaderSet = 1

					# Create an instance of the class and add it to the frame.
					pFlagConfig = cClass(pFrame, self, self.pAI, lSettings, text=sFlag)
					pFlagConfig.pack(side=TOP, anchor=W, fill=X, expand=YES)
					self.lFlags.append(pFlagConfig)
					break

	def GetFlagsFromInfo(self):
		lFlags = []
		for pFlagConfig in self.lFlags:
			if pFlagConfig.IsEnabled():
				lFlags.append( (pFlagConfig.GetName(), pFlagConfig.GetValue()) )

		return lFlags

	def Apply(self):
		# Copy our info to the AI
		self.pAI.sModule = self.sModuleVar.get()
		self.pAI.sFunction = self.pFunctionEntry.get()
		self.pAI.sArgs = self.pArgsEntry.get()
		self.pAI.lFlags = self.GetFlagsFromInfo()

		# Parent class Apply.
		ConfigurationDialog.Apply(self)

class FileLoader:
	def __init__(self, pOutput):
		self.pOutput = pOutput

	def Process(self, lsFileText):
		# Parse through the file text we've been given, finding the
		# blocks that belong to individual AI's.
		lFileBlocks, lsExtraFileInfo = self.SplitIntoCreationBlocks(lsFileText)

		# Process each block, creating AI entities for them.
		for iIndex in range( len(lFileBlocks) ):
			lsBlock = lFileBlocks[iIndex]
			lsExtra = lsExtraFileInfo[iIndex + 1]
			self.ProcessEntityBlock(lsBlock, lsExtra)
		
		return lsExtraFileInfo

	def SplitIntoCreationBlocks(self, lsFileText):
		# Since we've conveniently placed big blocks of ########'s
		# around each of the AI creations, we'll just search for those:
		bGrabbing = 0
		lBlocks = []
		lsCurrentBlock = []
		sCurrentExtra = ""
		lsExtraFileInfo = []
		pMatchReturn = re.compile("^\treturn p([a-zA-Z0-9_]+)\n$")
		for sLine in lsFileText:
			if sLine == sSeparationBlock:
				if not bGrabbing:
					# End of a pre-block extra bit...
					lsExtraFileInfo.append(sCurrentExtra)
					sCurrentExtra = ""
					
					# Start grabbing...
					bGrabbing = 1
					lsCurrentBlock = []
				else:
					bGrabbing = 0
					lBlocks.append(lsCurrentBlock)
			else:
				if bGrabbing:
					# Grab this line.  We'll strip the leading
					# \t from it, for later convenience.
					if sLine[0] == "\t":
						sLine = sLine[1:]

					lsCurrentBlock.append(sLine)
				else:
					# We're not grabbing an entity.  Add this
					# line to our extra file info...
					# We want to intercept the "return pAI"
					# statement, though, if it's after an existing AI,
					# so we can put our own in.
					if (not lBlocks)  or  (not pMatchReturn.search(sLine)):
						sCurrentExtra = sCurrentExtra + sLine

		if bGrabbing:
			# We ended in the middle of a grab.. ..somehow..
			lBlocks.append(lsCurrentBlock)
		
		# Append our last bit of extra file text to lsExtraFileInfo.
		lsExtraFileInfo.append(sCurrentExtra)
		
		return (lBlocks, lsExtraFileInfo)

	def ProcessEntityBlock(self, lsBlock, lsExtra):
		# One of the first lines we find should be a line
		# like: # Creating (.*)AI (.*)\n"
		# Search until we find this line, and use it to determine
		# what type of AI we need to make, and what name to give it.
		matchstr = re.compile("^# Creating (.*)AI (.*) at \((.*), (.*)\)\n$")
		specialmatch = re.compile("^# Creating Special: (.*)\n$")
		actionmatch = re.compile("^# CreatingAction ([^ ]+) ([^ ]+) at \((.*), (.*)\)\n$")

		sClass, sName, sSpecial, bAction = (None, None, None, 0)
		iXPos, iYPos = (50, 50)
		for iLine in range(len(lsBlock)):
			match =  matchstr.search(lsBlock[iLine])
			if match:
				# Found a match.  Pull the class name and
				# object 
				sClass, sName = match.group(1, 2)
				print "Matched %sAI: %s" % (sClass, sName)

				iXPos = string.atoi( match.group(3) )
				iYPos = string.atoi( match.group(4) )

				lsBlock = lsBlock[(iLine+1):]
				break
			# Check for special things.
			match = specialmatch.search(lsBlock[iLine])
			if match:
				# Found a match on a special object.
				sSpecial = match.group(1)
				print "Matched special: %s" % sSpecial
				break
			# Check for actions.
			match = actionmatch.search(lsBlock[iLine])
			if match:
				bAction = 1
				sClass, sName = match.group(1, 2)
				print "Matched Action %s: %s" % (sClass, sName)

				iXPos = string.atoi( match.group(3) )
				iYPos = string.atoi( match.group(4) )

				lsBlock = lsBlock[(iLine+1):]
				break

		# Remove the ending "Done" line...
		if bAction:
			sDone = "# ?Done creating %s %s\n" % (sClass, sName)
		else:
			sDone = "# ?Done creating %sAI %s\n" % (sClass, sName)

		for iLine in range(len(lsBlock)):
			if lsBlock[iLine] == sDone:
				lsBlock = lsBlock[:iLine]
				break

		if sClass:
			if bAction:
				# Create the appropriate Action entity.
				import ActionEntities
				pClass = ActionEntities.GetEntityClass(sClass)
				pEntity = self.pOutput.AddEntity(pClass)
			else:
				# Create the appropriate AI entity.
				dNameClassMatch = {
					"Conditional"	: ConditionalAIEntity,
					"Plain"		: PlainAIEntity,
					"Preprocessing"	: PreprocessingAIEntity,
					"PriorityList"	: PriorityListAIEntity,
					"Sequence"	: SequenceAIEntity,
					"Random"	: RandomAIEntity,
					"Compound"	: CompoundAIEntity }
				cClass = dNameClassMatch[sClass]
				pEntity = self.pOutput.AddEntity(cClass)

			# Tell the entity to load itself from the block
			# of entity-creating text we have.
			pEntity.SetName(sName)
			pEntity.Load(lsBlock)
			pEntity.SetPostEntitySaveText(lsExtra)

			pEntity.MoveTo(iXPos, iYPos)
		elif sClass:

			# Tell the entity to load itself from the block
			# of entity-creating text we have.
			pEntity.SetName(sName)
			pEntity.Load(lsBlock)
			pEntity.SetPostEntitySaveText(lsExtra)

			pEntity.MoveTo(iXPos, iYPos)

		elif sSpecial:
			# Not an AI entity.  Call the function to handle
			# the special block.
			dSpecialFuncMatch = { "ExternGlobals" : self.MakeExternGlobals }

			dSpecialFuncMatch[sSpecial](sName, lsBlock, lsExtra)

	def MakeExternGlobals(self, sName, lsBlock, lsExtra):
		pass

def Go():
	global root
	root = Tk()

	import Pmw
	Pmw.initialise()  # Somebody can't spell initialize?

	Initialize()

	# Add an informative label
	root.title(sBaseTitle + " (It's beautiful!!!)")

	out = Output(root)
	out.pack(side=BOTTOM, fill=BOTH, expand=YES)
	menus = AIMenus(root, out)
	menus.pack(side=TOP, fill=X, anchor=NW, expand=NO)

	root.bind("<Control-o>", menus.LoadAI)
	root.bind("<Control-l>", menus.LoadAI)
	root.bind("<Control-s>", menus.SaveAI)

	root.mainloop()
	print "Exiting editor..."
