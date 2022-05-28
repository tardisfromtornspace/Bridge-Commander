from bcdebug import debug
##########################################################################################################
#
#        SetLIB                 by Fernando Aluani, aka USS Frontier
#
#######################################################################################################
#   The Traveler system will need to create new sets for when AI ships drop out of travel.
#   So this will handle the creation of the scripts of those sets, making sure they don't already exist and so on...
###################################################################################################
import App
import nt
import Custom.GalaxyCharts.Cartographer

iIndex = 99

def GetSetForPos(vPos):
	debug(__name__ + ", GetSetForPos")
	global iIndex
	fX = vPos.x
	fY = vPos.y
	fOffset = 10.0
	pRetRegion = None
	lRegions = Custom.GalaxyCharts.Cartographer.RegionManager.GetAllRegions()
	for pRegion in lRegions:
		vRegPos = pRegion.GetLocation()
		if vRegPos != "DEFAULT":
			fMinX = vRegPos.x - fOffset
			fMaxX = vRegPos.x + fOffset
			fMinY = vRegPos.y - fOffset
			fMaxY = vRegPos.y + fOffset
			if fMinX <= fX <= fMaxX:
				if fMinY <= fY <= fMaxY:
					pRetRegion = pRegion
					break

	if pRetRegion == None:
		iIndex = iIndex + 1
		pScript = CreateSetScript("SpaceSector"+str(iIndex))
		if pScript != None:
			return pScript.Initialize()
		else:
			return None
	else:
		try:
			pScript = __import__(pRetRegion.Region)
		except:
			# very freakin weird this happening here.... Well, we'll have to return None, and the AI ship won't 
			# be able to drop out until this function return a set
			return None			
		pSet = pScript.GetSet()
		if pSet == None:
			pScript.Initialize()
			pSet = pScript.GetSet()
		return pSet

# Helper function to create the script file for a set with the given name, if it doesn't exists. 
# return is the script file
def CreateSetScript(sSetName):
	debug(__name__ + ", CreateSetScript")
	try:
		pScript = __import__('Custom.GalaxyCharts.TravelerSystems.AI_SpaceSets.'+sSetName)
	except ImportError:
		pScript = None
	if pScript == None:
		sFilePath = "scripts\Custom\GalaxyCharts\TravelerSystems\AI_SpaceSets\\"+sSetName+".py"
		file = nt.open(sFilePath, nt.O_WRONLY|nt.O_CREAT|nt.O_TRUNC)
		nt.write(file, "import App" + "\n")
		nt.write(file, "import Custom.GalaxyCharts.TravelerSystems.AISpaceSet" + "\n")
		nt.write(file, "import Custom.GalaxyCharts.Cartographer" + "\n")
		nt.write(file, "SET_NAME = \""+sSetName+"\"" + "\n")
		nt.write(file, "def Initialize():" + "\n")
		nt.write(file, "\tglobal SET_NAME" + "\n")
		nt.write(file, "\tpSet = App.SetClass_Create()" + "\n")
		nt.write(file, "\tApp.g_kSetManager.AddSet(pSet, SET_NAME)" + "\n")
		nt.write(file, "\tpSet.SetRegionModule(__name__)" + "\n")
		nt.write(file, "\tpSet.SetProximityManagerActive(1)" + "\n")
		nt.write(file, "\tCustom.GalaxyCharts.TravelerSystems.AISpaceSet.LoadPlacements(SET_NAME)" + "\n")
		nt.write(file, "\tCustom.GalaxyCharts.TravelerSystems.AISpaceSet.LoadBackdrops(pSet)" + "\n")
		nt.write(file, "\tpGrid = App.GridClass_Create()" + "\n")
		nt.write(file, "\tpSet.AddObjectToSet(pGrid, \"grid\")" + "\n")
		nt.write(file, "\tpGrid.SetHidden(1)" + "\n")
		nt.write(file, "\tCustom.GalaxyCharts.Cartographer.RegionManager.AddRegion(SET_NAME, __name__, None, None)" + "\n")
		nt.write(file, "\treturn pSet" + "\n")
		nt.write(file, "def GetSetName():" + "\n")
		nt.write(file, "\treturn SET_NAME" + "\n")
		nt.write(file, "def GetSet():" + "\n")
		nt.write(file, "\treturn App.g_kSetManager.GetSet(SET_NAME)" + "\n")
		nt.write(file, "def Terminate():" + "\n")
		nt.write(file, "\tApp.g_kSetManager.DeleteSet(SET_NAME)" + "\n")
		nt.close(file)

		try:
			pScript = __import__('Custom.GalaxyCharts.TravelerSystems.AI_SpaceSets.'+sSetName)
		except ImportError:
			pScript = None
	return pScript

###########################################################################
# 
#   Helper functions for the initialization of Sets
#
###########################################################################
def LoadPlacements(sSetName):
	debug(__name__ + ", LoadPlacements")
	vPlayer = (0.0, 0.0, 0.0)
	vLight = (-2000.0, 0.0, 0.0)

	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vLight[0], vLight[1], vLight[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.0, 1.0, 1.0, 0.4)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(vPlayer[0], vPlayer[1], vPlayer[2])
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 1.0, 0.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"


def LoadBackdrops(pSet):
	# Star Sphere "Backdrop stars"
	debug(__name__ + ", LoadBackdrops")
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258938)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049821, 0.254100, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/stars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(35000.000000)
	kThis.SetTextureHTile(22.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"