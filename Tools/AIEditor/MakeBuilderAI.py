###############################################################################
#	Filename:	MakeBuilderAI.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	A script to take a compound AI script and convert it to
#	a (semi-streamed) compound AI with a BuilderAI..
#	
#	Created:	5/24/2001 -	KDeus
###############################################################################

import re
import string

g_sAIBuilderBegin	= "\t######### AI Builder Begin #########"
g_sAIBuilderEnd	= "\t########## AI Builder End ##########"
g_sBuilderAIHeader = (g_sAIBuilderBegin + "\n" +
		 "## BUILDER AI\n" +
		 "##  This AI file has been mauled by the MakeBuilderAI script.\n" +
		 "##  Modify at your own risk.\n" +
		 "##  Or run MakeBuilderAI(filename, 1) to remove the BuilderAI code.\n" +
		 g_sAIBuilderEnd + "\n")

def Go(sFile, bRemoveOnly = 0):
	sOutput = sFile

	file = open(sFile, "rt")
	if not file:
		return

	lsLines = file.readlines()
	file.close()

	lsLines = ProcessLines(lsLines, bRemoveOnly)

	file = open(sOutput, "wt")
	file.writelines(lsLines)
	file.close()

def IsBuilderAI(sFile):
	# If this is a builder AI, it'll have a builder AI header...
	file = open(sFile, "rt")
	try:
		auxiliarList = string.split(g_sBuilderAIHeader, "\n")
		for sLine in auxiliarList[:-1]:
			sFileLine = string.rstrip(file.readline())
			if sLine != sFileLine:
				#print "(%s) is not (%s)" % (sLine, sFileLine)
				return 0
	except:
		auxiliarList = g_sBuilderAIHeader.split("\n")
		for sLine in auxiliarList[:-1]:
			sFileLine = file.readline().rstrip()
			if sLine != sFileLine:
				#print "(%s) is not (%s)" % (sLine, sFileLine)
				return 0

	return 1

def ProcessLines(lsLines, bRemoveOnly):
	sAIBuilderBegin	= g_sAIBuilderBegin
	sAIBuilderEnd	= g_sAIBuilderEnd
	
	# Check if there are already AI Builder lines in here.
	# If there are any, remove them.  We'll write new ones.
	pMatchBegin = re.compile(sAIBuilderBegin)
	pMatchEnd = re.compile(sAIBuilderEnd)

	bRemoving = 0
	lsOutput = []
	for sLine in lsLines:
		if pMatchBegin.search(sLine):
			# There is an AI Builder line..  Remove all these lines.
			bRemoving = 1
		elif pMatchEnd.search(sLine):
			bRemoving = 0
			continue

		if not bRemoving:
			lsOutput.append(sLine)

	if bRemoveOnly:
		return lsOutput
	lsLines = lsOutput
	

	# Find AI Creation blocks.
	pCreationBeginMatch = re.compile("^\t# Creating (.*)AI (.*) at \(.*, .*\)")
	pCreationEndMatch = re.compile("^\t# ?Done creating .*")
	lContainedMatches = (
		re.compile("^\tp[^. ]+.SetContainedAI\(p([^ )]+)\)"),
		re.compile("^\tp[^. ]+.AddAI\(p([^ ),]+)\)"),
		re.compile("^\tp[^. ]+.AddAI\(p([^ ),]+), \d+\)"),
		)
	pObjectDepMatch = re.compile("^\t# Builder AI Dependency Object \(([^) ]+)\)")
	pExtAIDepMatch = re.compile("^\t# Builder AI Dependency AI \(([^) ]+)\)")


	lCreationBlocks = []
	lsCurrentContained = []
	lsLastContained = []
	lsLastDepObjects = []
	lsCurrentDepObjects = []
	sCurrentType = ""
	sCurrentName = ""
	iCurrentStart = -1
	iLine = 0
	for sLine in lsLines:
		pBegin = pCreationBeginMatch.match(sLine)
		if pBegin:
			sCurrentType = pBegin.group(1)
			sCurrentName = pBegin.group(2)
			#print "Found match:" + str(pCreationBeginMatch.match(sLine).group())
			iCurrentStart = iLine
		elif pCreationEndMatch.match(sLine):
			lCreationBlocks.append( [sCurrentName, iCurrentStart - 1, iLine, lsCurrentContained, lsCurrentDepObjects] )
			lsLastContained = lsCurrentContained
			lsCurrentContained = []
			lsLastDepObjects = lsCurrentDepObjects
			lsCurrentDepObjects = []
			sCurrentName = ""
			sCurrentType = ""
		else:
			for pMatcher in lContainedMatches:
				pMatch = pMatcher.match(sLine)
				if pMatch:
					lsCurrentContained.append( pMatch.group(1) )
			pMatch = pObjectDepMatch.match(sLine)
			if pMatch:
				if not sCurrentName:
					# Append to the last set..
					lsLastDepObjects.append(pMatch.group(1))
				else:
					lsCurrentDepObjects.append(pMatch.group(1))

			pMatch = pExtAIDepMatch.match(sLine)
			if pMatch:
				if not sCurrentName:
					# Append an additional AI dependency to the last set.
					lsLastContained.append( pMatch.group(1) )
				else:
					lsCurrentContained.append( pMatch.group(1) )

		iLine = iLine + 1

	if not lCreationBlocks:
		return lsLines


	# Insert header info.
	lInsertInfo = [
		(0, g_sBuilderAIHeader) ]

	# Insert a BuilderAI before the first AI is created.
	sBuilderFunctionBase = "BuilderCreate"
	lsInsertText = "\tpBuilderAI = App.BuilderAI_Create(pShip, \"%s Builder\", __name__)\n" % (lCreationBlocks[len(lCreationBlocks) - 1][0])
	iFunc = 0
	for sName, iStart, iEnd, lsArgs, lsDepObjs in lCreationBlocks:
		iFunc = iFunc + 1
		lsInsertText = lsInsertText + "\tpBuilderAI.AddAIBlock(\"%s\", \"%s%d\")\n" % (sName, sBuilderFunctionBase, iFunc)
		for sArg in lsArgs:
			lsInsertText = lsInsertText + "\tpBuilderAI.AddDependency(\"%s\", \"%s\")\n" % (sName, sArg)
		for sDep in lsDepObjs:
			lsInsertText = lsInsertText + "\tpBuilderAI.AddDependencyObject(\"%s\", \"%s\", %s)\n" % (sName, sDep, sDep)
	lsInsertText = lsInsertText + "\treturn pBuilderAI # Builder Return\n"

	# Add AI Builder start/end blocks around the text to insert...
	lsInsertText = sAIBuilderBegin + "\n" + lsInsertText + sAIBuilderEnd + "\n"
	lInsertInfo.append( (lCreationBlocks[0][1], lsInsertText) )



	# Split each block into its own function...
	iBuilderFunctionNum = 0
	for iBlock in range(len( lCreationBlocks )):
		sName, iStart, iEnd, lsArgs, lsDepObjs = lCreationBlocks[iBlock]
		iBuilderFunctionNum = iBuilderFunctionNum + 1

		# Add a function definition before the AI...
		lsInsertText = "def %s%d(pShip" % (sBuilderFunctionBase, iBuilderFunctionNum)
		for sArg in lsArgs:
			lsInsertText = lsInsertText + ", p" + sArg
		for sDep in lsDepObjs:
			lsInsertText = lsInsertText + ", " + sDep
		lsInsertText = lsInsertText + "):\n"

		# Add AI Builder start/end blocks around the text to insert...
		lsInsertText = sAIBuilderBegin + "\n" + lsInsertText + sAIBuilderEnd + "\n"
		lInsertInfo.append( (iStart, lsInsertText) )

		# Add a return after the AI, before the next AI...
		lsInsertText = "\treturn p%s  # Builder Return\n" % sName

		# Add AI Builder start/end blocks around the text to insert...
		lsInsertText = sAIBuilderBegin + "\n" + lsInsertText + sAIBuilderEnd + "\n"

		# Add this after the last line before the next AI.  If there is no next AI,
		# add it at the end of the file.
		try:
			iInsertLine = lCreationBlocks[iBlock + 1][1]
		except IndexError:
			iInsertLine = -1

		lInsertInfo.append( (iInsertLine, lsInsertText) )

	# Go back and modify the data, inserting lines.
	lsOutput = []
	for iLine in range(len( lsLines )):
		sLine = lsLines[iLine]

		for iInsertLine, lsInsertText in lInsertInfo:
			if iInsertLine == iLine:
				lsOutput.append(lsInsertText)

		lsOutput.append(sLine)

	# Finally, add any -1 insert line entries...
	for iInsertLine, lsInsertText in lInsertInfo:
		if iInsertLine == -1:
			lsOutput.append(lsInsertText)

	return lsOutput
