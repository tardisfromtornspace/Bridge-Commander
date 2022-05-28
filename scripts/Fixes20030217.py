from bcdebug import debug
import App
import sys
import Foundation


import Bridge.Characters.CommonAnimations



# CommonAnimations.py

###############################################################################
#	SetPosition()
#
#	Sets the position of any character
#
#	Args:	pCharacter	- character to set up
#
#	Return:	pSequence
###############################################################################
def SetPosition(pCharacter):
	debug(__name__ + ", SetPosition")
	kAM = App.g_kAnimationManager

	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	import Foundation
	if Foundation.BridgeSetLocation(pCharacter.GetLocation(), kAM, pSequence, pAnimNode):
		return pSequence


	# Dasher42's change - use of a hash here is appropriate, especially in lieu of a
	# lot of if checks with no else!

	# It's tempting to move this to StaticDefs but the availability of these needs to be assured.

	locations = {

		# D-Bridge Locations
		'DBHelm':		( 'data/animations/db_stand_h_m.nif', 'db_stand_h_m' ),
		'DBTactical':	( 'data/animations/db_stand_t_l.nif', 'db_stand_t_l' ),
		'DBCommander':	( 'data/animations/db_stand_c_m.nif', 'db_stand_c_m' ),
		'DBCommander1':	( 'data/animations/DB_C1toC_M.nif', 'DB_C1toC_M' ),
		'DBScience':	( 'data/animations/db_StoL1_S.nif', 'db_StoL1_S' ),
		'DBEngineer':	( 'data/animations/db_EtoL1_s.nif', 'db_EtoL1_s' ),
		'DBGuest':		( 'data/animations/Seated_P.nif', 'Seated_P' ),
		'DBL1S':		( 'data/animations/DB_L1toE_S.nif', 'DB_L1toE_S', 'pCharacter.SetHidden(1)' ),
		'DBL1M':		( 'data/animations/DB_L1toG1_M.nif', 'DB_L1toG1_M', 'pCharacter.SetHidden(1)' ),
		'DBL1L':		( 'data/animations/DB_L1toT_L.nif', 'DB_L1toT_L', 'pCharacter.SetHidden(1)' ),

		# E-Bridge Locations
		'EBHelm':		( 'data/animations/EB_stand_h_m.nif', 'EB_stand_h_m' ),
		'EBTactical':	( 'data/animations/EB_stand_t_l.nif', 'EB_stand_t_l' ),
		'EBCommander':	( 'data/animations/EB_stand_c_m.nif', 'EB_stand_c_m' ),
		'EBCommander1':	( 'data/animations/EB_C1toC_M.nif', 'EB_C1toC_M' ),
		'EBScience':	( 'data/animations/EB_stand_s_s.nif', 'EB_stand_s_s' ),
		'EBEngineer':	( 'data/animations/EB_stand_e_s.nif', 'EB_stand_e_s' ),
		'EBGuest':		( 'data/animations/EB_stand_X_m.nif', 'EB_stand_X_m' ),
		'EBL1S':		( 'data/animations/EB_L1toE_S.nif', 'EB_L1toE_S', 'pCharacter.SetHidden(1)' ),
		'EBL1M':		( 'data/animations/EB_L1toH_M.nif', 'EB_L1toH_M', 'pCharacter.SetHidden(1)' ),
		'EBL1L':		( 'data/animations/EB_L1toT_L.nif', 'EB_L1toT_L', 'pCharacter.SetHidden(1)' ),
		'EBL2M':		( 'data/animations/EB_L2toG2_M.nif', 'EB_L2toG2_M', 'pCharacter.SetHidden(1)' ),
		'EBG1M':		( 'data/animations/EB_G1toL2_M.nif', 'EB_G1toL2_M' ),
		'EBG2M':		( 'data/animations/EB_G2toL2_M.nif', 'EB_G2toL2_M' ),
		'EBG3M':		( 'data/animations/EB_G32toL1_M.nif', 'EB_G3toL1_M' ),

		# Partial Set Locations
		'CardassianSeated':	( 'data/animations/CardassianSeated01.NIF', 'CardassianSeated01' ),
		'CardassianStationSeated':	( 'data/animations/CardStationSeated01.NIF', 'CardStationSeated01' ),
		'FederationOutpostSeated':	( 'data/animations/FedOutpostSeated01.NIF', 'FederationOutpostSeated01' ),
		'FederationOutpostSeated2':	( 'data/animations/FedOutpostSeated02.NIF', 'FederationOutpostSeated02' ),
		'FederationOutpostSeated3':	( 'data/animations/FedOutpostSeated03.NIF', 'FederationOutpostSeated03' ),
		'FerengiSeated':	( 'data/animations/FerengiSeated01.NIF', 'FerengiSeated01' ),
		'GalaxyEngSeated':	( 'data/animations/GalaxyEngSeated01.NIF', 'GalaxyEngSeated01' ),
		'GalaxySeated':		( 'data/animations/GalaxySeated01.NIF', 'GalaxySeated01' ),
		'KessokSeated':		( 'data/animations/KessokSeated01.NIF', 'KessokSeated01' ),
		'KlingonSeated':	( 'data/animations/KlingonSeated01.NIF', 'KlingonSeated01' ),
		'MiscEngSeated':	( 'data/animations/MiscEng01.NIF', 'MiscEngSeated01' ),
		'MiscEngSeated2':	( 'data/animations/MiscEng02.NIF', 'MiscEngSeated02' ),
		'RomulanSeated':	( 'data/animations/RomulanSeated01.NIF', 'RomulanSeated01' ),
		'ShuttleSeated':	( 'data/animations/ShuttleSeated01.NIF', 'ShuttleSeated01' ),
		'ShuttleSeated2':	( 'data/animations/ShuttleSeated02.NIF', 'ShuttleSeated02' ),
		'SovereignEngSeated':	( 'data/animations/SovereignEngSeated01.NIF', 'SovereignEngSeated01' ),
		'SovereignSeated':	( 'data/animations/SovereignSeated01.NIF', 'SovereignSeated01' ),
		'StarbaseSeated':	( 'data/animations/StarbaseSeated01.NIF', 'StarbaseSeated01' ),
		'StarbaseSeated2':	( 'data/animations/StarbaseSeated02.NIF', 'StarbaseSeated02' ),
	}

	try:
		loc = locations[pCharacter.GetLocation()]
	except KeyError:
		return pSequence

	kAM.LoadAnimation(loc[0], loc[1])
	pSequence.AppendAction(App.TGAnimPosition_Create(pAnimNode, loc[1]))
	for i in loc[2:]:
		try:
			exec(i)
		except SyntaxError:
			errtype, errinfo, errtrace = sys.exc_info()
			import traceback
			fulltrace = traceback.print_exc(errtrace)
			if fulltrace:
				print("Traceback: %s") % (fulltrace)

	# End Dasher42's changes

	return pSequence


import LoadBridge

###############################################################################
#   Load()
#
#   Load the generic bridge by creating the bridge set then add in the specific
#   bridge model and character configurations for the bridge type specified.
#
#   Args:   sBridgeConfigScript -   The name of the script that contains
#                                   functions to create the bridge model and
#                                   configure the characters animations to that
#                                   bridge
#
#   Return: none
###############################################################################
def LoadBridge_Load(sBridgeConfigScript):
#   kDebugObj.Print("Loading the " + sBridgeConfigScript + " bridge")

	# Set up a customized Bridge
	debug(__name__ + ", LoadBridge_Load")
	Foundation.pCurrentBridge = Foundation.bridgeList[sBridgeConfigScript]

	# print 'Setting pCurrentBridge to ', Foundation.pCurrentBridge

	#
	# Check to see if there is a Set called "bridge" already.  If not, create
	# it for the first time.
	#
	pBridgeSet = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"));
	if (pBridgeSet == None):
#       kDebugObj.Print("No previous bridge")
		pBridgeSet = LoadBridge.CreateAndPopulateBridgeSet()
	else:
		# Reset all the extras..
		LoadBridge.ResetExtraLocations()

		#
		# If it already existed, check to see if the bridge set is configured
		# for what we are requesting.  If so, we're done.  Otherwise, unload
		# the previous config and load up with the new one
		#
		if (pBridgeSet.IsSameConfig(sBridgeConfigScript)):
#           kDebugObj.Print(sBridgeConfigScript + " is already loaded")
			return
		else:
			# Unload animations and sounds of the previous bridge
			pcOldBridgeConfigScript = pBridgeSet.GetConfig ()
			pOldMod = __import__("Bridge." + pcOldBridgeConfigScript)
			pOldMod.UnloadAnimations()
			pOldMod.UnloadSounds()


	# Save away the camera our viewscreen was displaying
	pCamera = None
	pViewScreen = pBridgeSet.GetViewScreen()
	if (pViewScreen != None):
		pCamera = pViewScreen.GetRemoteCam()

	#
	# Remove the old bridge model and viewscreen, if they existed
	#
	pBridgeSet.DeleteObjectFromSet("bridge")        # Remove the bridge, if it exists
	pBridgeSet.DeleteObjectFromSet("viewscreen")    # Remove viewscreen, if it exists
	pBridgeSet.DeleteCameraFromSet("maincamera")    # Remove maincamera, if it exists

	#
	# Now call the config script to create our bridge model, viewscreen
	# and to configure our characters to that bridge
	#
	pMod = __import__("Bridge." + sBridgeConfigScript)
	pMod.CreateBridgeModel(pBridgeSet)
	pMod.ConfigureCharacters(pBridgeSet)
	pMod.PreloadAnimations ()

	if (pCamera != None):                   # reset our viewscreen to its
		pViewScreen = pBridgeSet.GetViewScreen()
		pViewScreen.SetRemoteCam(pCamera)   #   previous state, if it had one
		pViewScreen.SetIsOn(1)

	pBridgeSet.SetConfig(sBridgeConfigScript)       # store our config

	import Bridge.Characters.CommonAnimations
	Bridge.Characters.CommonAnimations.PutGuestChairOut()

#   kDebugObj.Print("Done loading the " + sBridgeConfigScript + " bridge")


LoadBridge.Load = LoadBridge_Load
