import AIEditor
from Tkinter import *

def GetEntityClass(sActionClass):
	dEntityToClass = {
		"TGScriptAction":	TGScriptActionEntity,
		"TGSequence":		ActionEntity,
		}

	if dEntityToClass.has_key(sActionClass):
		return dEntityToClass[sActionClass]

	return ActionEntity

class ActionEntity(AIEditor.Entity):
	"An entity for Sequence-based actions."
	def __init__(self, pOutput, sName="Sequence Action", sMainColor = "yellow", sTextColor = "darkgreen", sContainBoxOutline="black", sContainBoxFill="orange"):
		self.sContainBoxOutline = sContainBoxOutline
		self.sContainBoxFill = sContainBoxFill

		# Base class init...
		AIEditor.Entity.__init__(self, pOutput, sName, sMainColor)

		# Basic variable setup
		self.iWidth = 85
		self.iHeight = 35
		self.sTextColor = sTextColor
		self.bInterruptable = 1
		self.sSequenceName = None
		self.fDelay = 0.0

		# Create our graphics...
		self.CreateGraphics()

		# Clicking on iContainBox has a different effect...
		self.vLastTopPos = None
		self.pCanvas.tag_bind(self.iContainBox, "<Button-3>", self.ConnectClicked)
		self.pCanvas.tag_bind(self.iContainBox, "<ButtonRelease-3>", self.ConnectReleased)
		self.pCanvas.tag_bind(self.iContainBox, "<B3-Motion>", self.ConnectDragged)

		self.pContainedEntities = []

	def Delete(self):
		# Parent class delete...
		ActionEntity.Delete(self)		

		# Detach ourselves from our children, if we have any..
		self.RemoveContainedEntities()

	def GetContainStartLocation(self):
		box = self.pCanvas.bbox(self.GetMainTag())
		iHeight = box[3] - box[1]
		iCenterY = (box[1] + box[3]) / 2
		
		return (box[2] + iHeight / 4, iCenterY)

	def CreateGraphics(self):
		# Create our rectangle and our text, and associate
		# them with our tag...
		self.iRect = self.pCanvas.create_rectangle(self.vPos[0], self.vPos[1], self.vPos[0] + self.iWidth, self.vPos[1] + self.iHeight, outline=self.sMainColor, fill="white", tags=(self.GetMainTag(), ))
		self.iText = self.pCanvas.create_text(self.vPos[0] + (self.iWidth / 2), self.vPos[1] + (self.iHeight / 2), justify=CENTER, width=self.iWidth - 6, text=self.sText, fill=self.sTextColor, tags=(self.GetMainTag(), ))

		box = self.pCanvas.bbox(self.GetMainTag())
		iHeight = box[3] - box[1]
		iCenterY = (box[1] + box[3]) / 2

		self.iContainBox = self.pCanvas.create_polygon(box[2], box[1], box[2] + iHeight / 2, iCenterY, box[2], box[3], fill=self.sContainBoxFill, outline=self.sContainBoxOutline)

	def Redraw(self):
		# Parent class first...
		# Only need to redraw things that don't have
		# our special tag.
		box = self.pCanvas.bbox(self.GetMainTag())
		iHeight = box[3] - box[1]
		iCenterY = (box[1] + box[3]) / 2

		self.pCanvas.coords(self.iContainBox, box[2], box[1], box[2] + iHeight / 2, iCenterY, box[2], box[3])
		self.UpdateContainedLines()

	def SetSequenceName(self, sName):
		self.sSequenceName = sName

		# Gotta set the sequence name for all other entities.
		# Handle parents, and entities above us.
		self.SetSequenceNameUp(sName)
		# Handle children, and entities below us.
		self.SetSequenceNameDown(sName)

	def SetSequenceNameUp(self, sName):
		pParent = self.GetContainingEntity()
		if pParent:
			# Set the name for the parent.
			pParent.sSequenceName = sName
			# Set the name for the parent's parents.
			pParent.SetSequenceNameUp(sName)
			# Set the name for all of the parent's children
			# except us.
			for pChild in pParent.GetContainedEntities():
				if pChild != self:
					pChild.SetSequenceNameDown(sName)

	def SetSequenceNameDown(self, sName):
		# Set the name for us.
		self.sSequenceName = sName

		# Set the name for all our children.
		for pChild in self.GetContainedEntities():
			pChild.SetSequenceNameDown(sName)

	def GetSequenceName(self):
		return self.sSequenceName

	def SetDelay(self, fDelay):
		self.fDelay = fDelay

	def GetDelay(self):
		return self.fDelay

	def ConnectClicked(self, event):
		self.vLastTopPos = (event.x, event.y)
		self.pCanvas.grab_set()

		vLinePos = self.GetContainStartLocation()
		
		self.iDragLine = self.pCanvas.create_line(vLinePos[0], vLinePos[1], event.x, event.y, fill="red")

	def ConnectReleased(self, event):
		self.vLastTopPos = None
		self.pCanvas.grab_release()

		# Get rid of the drag line...
		self.pCanvas.delete(self.iDragLine)

		# Check if we've been dragged to something else.
		pEntity = self.pOutput.GetEntityAt(event.x, event.y)
		if pEntity  and  (pEntity != self):
			# Yep.
			# This thing is now our Contained entity.
			self.ToggleContainedEntity(pEntity)

	def ConnectDragged(self, event):
		if self.vLastTopPos:
			vLinePos = self.GetContainStartLocation()
			self.pCanvas.coords(self.iDragLine, vLinePos[0], vLinePos[1], event.x, event.y)
			
			self.vLastDragPos = (event.x, event.y)

	def ToggleContainedEntity(self, pEntity):
		# Do we already contain this entity?
		bAdd = 1
		for pContained, iLine in self.pContainedEntities:
			if pContained == pEntity:
				# Yep.  Remove it.
				self.RemoveContainedEntity(pEntity)
				bAdd = 0
				break

		if bAdd:
			# Gotta add this one.
			# Make sure we have a sequence name.
			if self.sSequenceName is None:
				self.sSequenceName = self.MakeUniqueSequenceName()

			# Attach a line showing that it's contained.
			vLinePos = self.GetContainStartLocation()
			vEnd = pEntity.GetAttachPoint()
			iLine = self.pCanvas.create_line(vLinePos[0], vLinePos[1], vEnd[0], vEnd[1], fill=self.sContainBoxOutline)

			# Update contained lists..
			self.pContainedEntities.append((pEntity, iLine))
			pEntity.SetContainingEntity(self)

		# Draw a line to our contained entity.
		self.UpdateContainedLines()

	def CanBeContainedBy(self, pEntity):
		# As an ActionEntity, we can be contained only by other
		# ActionEntities.
		return isinstance(pEntity, ActionEntity)

	def SetContainingEntity(self, pEntity):
		# Parent class first.
		Entity.SetContainingEntity(self, pEntity)

		# Set our sequence name to the sequence name in
		# our containing entity (None if we're contained by None).
		if pEntity:
			self.SetSequenceName( pEntity.GetSequenceName() )
		else:
			self.SetSequenceName(None)

	def GetContainedEntity(self, iIndex=0):
		return self.pContainedEntities[iIndex][0]

	def GetContainedEntities(self):
		lEntities = []
		for pContained, iLine in self.pContainedEntities:
			lEntities.append(pContained)
		return lEntities

	def RemoveContainedEntities(self):
		while len(self.pContainedEntities):
			self.RemoveContainedEntity( self.GetContainedEntity(0) )

	def RemoveContainedEntity(self, pEntity):
		for iIndex in range( len(self.pContainedEntities) ):
			pContained, iLine = self.pContainedEntities[iIndex]
			if pEntity == pContained:
				# Tell the entity it's no longer contained.
				pEntity.SetContainingEntity(None)

				# Delete the contained line..
				self.pCanvas.delete(iLine)

				# Clear the entity..
				del self.pContainedEntities[iIndex]
				break

		self.UpdateContainedLines()

	def UpdateContainedLines(self):
		vStart = self.GetContainStartLocation()

		for pEntity, iLine in self.pContainedEntities:
			vEnd = pEntity.GetAttachPoint()
			self.pCanvas.coords(iLine, vStart[0], vStart[1], vEnd[0], vEnd[1])

	def PostSetupLoad(self, lsCreationText):
		# Look for info about who we're attached after.
		import re
		import string
		pAddActionMatch = re.compile("p[^.]+\.AddAction\(p%s, ([^,]+), ([0-9.e+-]+)\)\n" % self.GetName())
		for sLine in lsCreationText:
			match = pAddActionMatch.match(sLine)
			if match:
				# Found who we're attached after, and our
				# delay value.  Set our delay value...
				self.SetDelay(float(match(2)))
				# Get the entity that contains us..
				sParent = match(1)
				if sParent != "None":
					# Strip the initial 'p'
					sParent = sParent[1:]
					# Get the entity with this name.
					# It should already exist.
					pEntity = self.pOutput.GetEntityByName(sParent)
					assert(pEntity)
					if pEntity:
						# Lots of indents.  Yaaay.
						pEntity.ToggleContainedEntity(self)
				break

	def PostSetupSave(self, pFile):
		# Save info about who we're attached after.
		pParent = self.GetContainingEntity()
		if pParent:
			# We're attached after our parent.  Write
			# out stuff to add us to our sequence, after
			# the parent.
			pFile.write("\tp%s.AddAction(p%s, p%s, %f)\n" % (self.GetSequenceName(), self.GetName(), pParent.GetName(), self.GetDelay()))
		else:
			# We're a lone action, or the start of a
			# sequence.  ...Check which..
			lChildren = self.GetContainedEntities()
			if lChildren:
				# We're the start of a sequence.  Create
				# the sequence object.
				pFile.write("\tp%s = App.TGSequence_Create()\n" % (self.GetSequenceName()))
				# Add ourselves.
				pFile.write("\tp%s.AddAction(p%s, None, %f)\n" % (self.GetSequenceName, self.GetName(), self.GetDelay()))

	def PostDoneSave(self, pFile):
		# Save our children.
		for pChild in self.GetContainedEntities():
			for pChild in lChildren:
				pChild.Save(pFile)




class TGScriptActionEntity(ActionEntity):
	"Entity for handling a TGScriptAction."
	def __init__(self, pOutput):
		# Base class init...
		ActionEntity.__init__(self, pOutput, "TGScriptAction", "orange", "red")

		# Basic variable setup.
		self.sModuleName = ""
		self.sFunctionName = ""
		self.sParams = ""

	def Load(self, lsCreationText):
		# Format for our creation function is:
		# App.TGScriptAction_Create(sModule, sFunction, ...)
		# Grab the module name, function name, and parameters from the
		# line that matches this format.
		import re
		matchstr = re.compile("^p[^ ]+ = App\.TGScriptAction_Create\(\"([^\"]+)\", \"([^\"]+)\"(, (.+))?\)\n$")

		for sLine in lsCreationText:
			match = matchstr.search(sLine)
			if match:
				self.sModuleName, self.sFunctionName, self.sParams = match.group(1,2,4)
				if self.sParams is None:
					self.sParams = ""

				break

		# Post-setup loading.
		self.PostSetupLoad()

	def Save(self, pFile):
		# Output the comments that surround our creation:
		pFile.write(AIEditor.sSeparationBlock)
		pFile.write("\t# CreatingAction TGScriptAction %s at (%d, %d)\n" % (self.GetName(), self.vPos[0], self.vPos[1]))

		# Create us..
		sParams = ""
		if self.sParams:
			sParams = ", " + self.sParams
		pFile.write("\tp%s = App.TGScriptAction_Create(\"%s\", \"%s\"%s)\n" % (self.GetName(), self.sModuleName, self.sFunctionName, sParams))

		# Save info about who we're attached after.
		self.PostSetupSave(pFile)

		# We're done.
		pFile.write("\t# Done creating TGScriptAction %s\n" % self.GetName())
		pFile.write(AIEditor.sSeparationBlock)

		for pEntity in lContained:
			pContained.Save()
			pFile.write("

		# Write any text that should appear after this entity.
		pFile.write(self.sPostEntitySaveText)

		self.PostDoneSave(pFile)

	def Configure(self, event):
		TGScriptActionConfigurationDialog(self.pOutput, self)

from ConfigUtils import ConfigurationDialog

class TGScriptActionConfigurationDialog(ConfigurationDialog):
	def __init__(self, pOutput, pEntity):
		# Base class init.
		ConfigurationDialog.__init__(self, pOutput, pEntity)

		self.lLastFunctionInfo = None
		self.sLastModule = None

		self.sFunction = pEntity.sFunctionName
		self.sParams = StringVar()
		self.sParams.set( pEntity.sParams )

		# Interface setup
		# Module name input...
		pFrame = Frame(self)
		pFrame.pack(side=TOP, anchor=W, pady=2)
		self.sModuleVar = StringVar()
		Label(pFrame, text="Module (without .py extension):").pack(side=LEFT)
		Entry(pFrame, width=40, textvariable=self.sModuleVar).pack(side=LEFT, fill=X, expand=YES)
		self.sModuleVar.set(self.pAI.sModuleName)
		Button(pFrame, text="Select File", command=self.SelectModule).pack(side=LEFT)

		# A frame for radio buttons for selecting a function from
		# the specified module.
		self.pFunctionsFrame = Frame(self)
		self.pFunctionsFrame.pack(side=TOP, pady=2, fill=BOTH, expand=YES)

		# A frame for setting up parameters to the function.
		self.pParamSetupFrame = Frame(self)
		self.pParamSetupFrame.pack(side=TOP, pady=2, fill=X, expand=YES)

		self.UpdateFunctionsFrame()

		# Function name input...
		#pFrame = Frame(self)
		#pFrame.pack(side=TOP, anchor=W, pady=2)
		#self.sFunctionVar = StringVar()
		#Label(pFrame, text="Function name:").pack(side=LEFT)
		#Entry(pFrame, width=40, textvariable=self.sFunctionVar).pack(side=LEFT)
		#self.sFunctionVar.set(self.pAI.sFunctionName)
		#self.pSelectFuncButton = Button(pFrame, text="Select Function", command=self.SelectFunction)
		#self.pSelectFuncButton.pack(side=LEFT)

	def SelectModule(self):
		import os
		# Make a file selection dialog, and have it call
		# our SetModule function when it has a file.

		# Save our cwd as the AI load dir.
		AIEditor.SetAILoadPath(os.getcwd())

		# Make the cwd our compound dir.
		os.chdir(AIEditor.GetCompoundPath())

		AIEditor.SelectFileDialog(self, self.SetModule)

	def SetModule(self, sFile):
		# Make the path relative to the build directory, and
		# convert any slashes or backslashes to dots.
		import os.path
		sFilePath = os.path.abspath(sFile)

		if sFilePath[:len(AIEditor.GetScriptsPath())] == AIEditor.GetScriptsPath():
			# It's inside the build directory.  Good.  Strip off
			# the part of it that is the build directory...
			sModule = sFilePath[len(AIEditor.GetScriptsPath()) + 1:]
			if len(sModule):
				# Replace all slashes with dots.
				import string
				sModule = string.replace(sModule, "/", ".")
				sModule = string.replace(sModule, "\\", ".")

				# And strip off the ".py"
				sModule = sModule[:-3]

				self.sModuleVar.set(sModule)

		# Save our cwd as the compound dir, and
		# restore the cwd from the AI load dir.
		AIEditor.SetCompoundPath(os.getcwd())
		os.chdir(AIEditor.GetAILoadPath())

		# Setup the functions frame with the available functions
		# in this module.
		self.UpdateFunctionsFrame()

	def UpdateFunctionsFrame(self):
		# Get rid of any old functions that are listed.
		for pChild in self.pFunctionsFrame.winfo_children():
			pChild.destroy()

		# Get the list of actions in the currently listed module.
		lActions = self.GetActionsFromModule(self.sModuleVar.get())
		iButtonNum = 1
		iSelectedFunction = IntVar()
		pInvokeMe = None
		for sFunction, sParams in lActions:
			pRadio = Radiobutton(self.pFunctionsFrame, text=sFunction, variable = iSelectedFunction, value=iButtonNum, command = lambda self=self, sFunc = sFunction : self.SelectAction(sFunc))
			pRadio.pack(side=TOP, anchor=W)

			if sFunction == self.sFunction:
				# Rrgh..  This needs to be done with
				# an after_idle call for some fucked up
				# reason.
				self.pFunctionsFrame.after_idle(lambda func=pRadio.invoke : func())

			iButtonNum = iButtonNum + 1

	def SelectAction(self, sFunction):
		print "Select Action %s" % sFunction
		self.sFunction = sFunction

		self.UpdateFunctionParamFrame()
		pass

	def UpdateFunctionParamFrame(self):
		# Remove old stuff.
		for pChild in self.pParamSetupFrame.winfo_children():
			pChild.destroy()

		# Add a label describing the function parameters:
		bPresent = 0
		lFunctions = self.GetActionsFromModule( self.sModuleVar.get() )
		for sFunction, sArgs in lFunctions:
			if sFunction == self.sFunction:
				bPresent = 1
				sText = "Function Parameters: " + str(sArgs)
				if sArgs is None:
					sText = "(No function parameters)"
				Label(self.pParamSetupFrame, text=sText).pack(side=TOP, anchor=W)
				break

		# Add an Entry, so the user can specify params.
		if bPresent:
			Entry(self.pParamSetupFrame, textvariable=self.sParams, width=60).pack(side=TOP, anchor=W, fill=X, expand=YES)

	def GetActionsFromModule(self, sModule):
		import string
		import os

		if self.sLastModule == sModule:
			return self.lLastFunctionInfo

		# In case we don't reach the end of the function, clear
		# the cached function info for now.
		self.lLastFunctionInfo = None
		self.sLastModule = sModule

		lActions = []

		# Open up the module file.
		sFilePath = AIEditor.GetScriptsPath()
		for sFragment in string.split(sModule, "."):
			sFilePath = os.path.join(sFilePath, sFragment)
		sFilePath = sFilePath + ".py"

		try:
			pFile = open(sFilePath, "rb")
		except IOError:
			return []

		import re
		# Search through the file for lines that match
		# action function declarations.
		pSearch = re.compile("^def ([^)]+)\(pAction(,\s*([^)]+))?\):")
		for sLine in pFile.readlines():
			pMatch = pSearch.match(sLine)
			if pMatch:
				lActions.append(pMatch.group(1,3))

		pFile.close()

		# Save cached values.
		self.lLastFunctionInfo = lActions

		return lActions			

	def Ok(self):
		# Set module and function name in the AI.
		self.pAI.sModuleName = self.sModuleVar.get()
		self.pAI.sFunctionName = self.sFunction
		self.pAI.sParams = self.sParams.get()

		# Base class Ok..
		ConfigurationDialog.Ok(self)



























