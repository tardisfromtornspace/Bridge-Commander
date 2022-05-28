lsProjectDirectories = (
	"c:/TGShared/TGSequence",
	"c:/Utopia/Current/Code/AI",
	"c:/Utopia/Current/Code/Bridge",
	"c:/Utopia/Current/Code/Common",
	"c:/Utopia/Current/Code/Editor",
	"c:/Utopia/Current/Code/Effects",
	"c:/Utopia/Current/Code/Interface",
	"c:/Utopia/Current/Code/ModelPropertyEditor",
	"c:/Utopia/Current/Code/Properties",
	"c:/Utopia/Current/Code/Tactical"
	)

lsCachedActionClasses = None
lsCachedSequenceClasses = None
dCachedFiles = None

def SetProjectDirectories(lsDirs):
	global lsProjectDirectories
	lsProjectDirectories = lsDirs

def ForceRefreshCachedClasses():
	global lsCachedActionClasses, lsCachedSequenceClasses, dCachedFiles

	dChildren, dCachedFiles = FindActions(lsProjectDirectories)
	lsCachedActionClasses = GetAllChildren("TGAction", dChildren) + ["TGAction", ]
	lsCachedActionClasses.sort()
	lsCachedSequenceClasses = GetAllChildren("TGSequence", dChildren) + ["TGSequence", ]
	lsCachedSequenceClasses.sort()

def GetProjectActions():
	global lsCachedActionClasses, lsCachedSequenceClasses, dCachedFiles
	if lsCachedActionClasses == None  or  dCachedFiles == None:
		ForceRefreshCachedClasses()

	return lsCachedActionClasses, lsCachedSequenceClasses, dCachedFiles

def FindActions(lsPaths):
	# We're looking for class definitions that
	# inherit from TGAction...  Or that inherit from
	# things that inherit from TGAction.
	# Get the names of all the .h files in our directories..
	lsFileList = []
	import dircache
	for sPath in lsPaths:
		lsFiles = dircache.listdir(sPath)
		for sFile in lsFiles:
			if sFile[-2:] == ".h"  or  sFile[-2:] == ".H":
				# It's a header file..
				lsFileList.append(sPath + "/" + sFile)
	print "Searching %d files for TGAction classes." % len(lsFileList)

	# Ok, we have a list of all the header files in all the
	# directories we need to search.  Make a pass through the
	# files searching all the class declaractions, and save
	# the class name and what the class inherits from.
	lClassInfo = []
	for sFile in lsFileList:
		try:
			pFile = open(sFile, "r")
		except IOError:
			print "Unable to open file: " + sFile
			pFile = None

		if pFile:
			# Scan through the file...
			lClassInfo.append((sFile, SearchFileForClasses(pFile)))
			pFile.close()

	# Build the inheritance tree dictionary...
	dChildren = {}
	dFile = {}
	for sFile, lInfo in lClassInfo:
		for sClass, lsParents in lInfo:
			for sParent in lsParents:
				if dChildren.has_key(sParent):
					dChildren[sParent].append(sClass)
				else:
					dChildren[sParent] = [sClass, ]
			dFile[sClass] = sFile

	return dChildren, dFile

def GetAllChildren(sClass, dChildren):
	lsChildren = []
	if dChildren.has_key(sClass):
		lsChildren = lsChildren + dChildren[sClass]

	lsReturn = lsChildren[:]
	for sChild in lsChildren:
		lsReturn = lsReturn + GetAllChildren(sChild, dChildren)

	lsReturn.sort()
	return lsReturn

def SearchFileForClasses(pFile):
	import re
	pClassRegexp = re.compile("^class[ \t]+([A-Za-z0-9]+)[ \t]*:?[ \t]*(public[ \t]+([A-Za-z0-9]+),?)*.*\n$")

	lsClasses = []
	sLine = pFile.readline()
	while sLine:
		pMatch = pClassRegexp.search(sLine)
		if pMatch:
			# Found a class definition.  Grab the information
			# we want from it.
			sClassName = pMatch.group(1)
			
			# Unfortunately, we can't grab parent class
			# names accurately if the class inherits from
			# multiple parents.
			# Check if it inherits from anyone:
			lsParents = []
			if pMatch.group(3):
				# Yep.  Search for which classes...
				iStart = pMatch.start(2)
				sChoppedLine = sLine[iStart:]
				pParentMatch = re.match("^public[ \t]+([A-Za-z0-9]+)[ \t]*,?[ \t]*(public)?", sChoppedLine)
				while pParentMatch:
					sParent = pParentMatch.group(1)
					lsParents.append(sParent)

					if pParentMatch.group(2):
						iStart = pParentMatch.start(2)
						sChoppedLine = sChoppedLine[iStart:]
					else:
						break
					pParentMatch = re.match("^public[ \t]+([A-Za-z0-9]+)[ \t]*,?[ \t]*(public)?", sChoppedLine)

			lsClasses.append((sClassName, lsParents))

		sLine = pFile.readline()

	return lsClasses









