from bcdebug import debug
import App
import MissionLib

from Custom.AdvancedTechnologies.Data.ATP_Tools   import *
from Custom.AdvancedTechnologies.Data.ATP_Config  import *

DEFAULT_INTENSITY=0.7
DRAINER_WEAPON=0
LIFE_SUPPORT=1
ACTION=0
TYPE=1
LIGHT=0
INTENSITY=1

ActionDict={}
g_DrainerActive=FALSE

g_dNameToCharacter = {}
g_AnimationModes = {}
g_sLines = []
g_Database = None

g_dAnimationModes = { 	'Speak'	:		App.CharacterAction.AT_SPEAK_LINE,		
			'Talk' :		App.CharacterAction.AT_SAY_LINE,
			'TalkAfterTurn' :	App.CharacterAction.AT_SAY_LINE_AFTER_TURN 	}

g_dNameToCharacterName = { 	'Helm' : 	'Kiska',
				'XO' : 		'Saffi',
				'Engineer' : 	'Brex',
				'Tactical' : 	'Felix',
				'Science' : 	'Miguel'
			 }
				


def Initialise():
	debug(__name__ + ", Initialise")
	global g_dNameToCharacter ,g_DrainerActive, g_Database , g_sLines , g_AnimationModes

	pBridge  = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))

	g_dNameToCharacter = { 	"Helm":		App.CharacterClass_GetObject(pBridge, "Helm"),
				"XO":		App.CharacterClass_GetObject(pBridge, "XO"),
				"Engineer":	App.CharacterClass_GetObject(pBridge, "Engineer"),
				"Science":	App.CharacterClass_GetObject(pBridge, "Science"),
				"Tactical":	App.CharacterClass_GetObject(pBridge, "Tactical")	}	
	
	g_sLines =[	"TargetImpulseDisabled",
			"SelfLifeSupportDisabled",
			"SelfWarpDisabled",
			"SelfSensorsDisabled",
			"SelfTorpedoesDisabled",
			"SelfShieldsOnline",
			"SelfTractorDisabled",
			"TargetWarpDisabled",
			"TargetTractorDisabled",
			"SelfWarpOnline",
			"TargetPhasersDisabled",
			"SelfPowerDisabled",
			"SelfLifeSupportOnline",
			"TargetSensorsDisabled",
			"SelfSensorsOnline",
			"SelfPhasersDisabled",
			"SelfTractorsFire",
			"SelfImpulseOnline",	
			"SelfImpulseDisabled",
			"SelfShieldsDisabled",
			"TargetTorpedoesDisabled",
			"TargetShieldsDisabled",
			"TargetPowerDisabled",
			"SelfTractorsStop",
			"Dock_Init",
			"Dock_ACK"			]



	
	## Settings
	pGame = App.Game_GetCurrentGame()
	g_Database = App.g_kLocalizationManager.Load("scripts/Custom/AdvancedTechnologies/Data/BridgeFX/ATP_Database.tgl")
	g_DrainerActive = FALSE	
	
	# Loop through all voice lines that we want to preload, and load them.
	for sLine in g_sLines:
		pGame.LoadDatabaseSoundInGroup(g_Database, sLine, "BridgeGeneric")

	## Unload the database:
	App.g_kLocalizationManager.Unload(g_Database)	

	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")

	#Recreate the main light
	pLight = pSet.GetLight("ambientlight1")
	if not pLight:
		pSet.CreateAmbientLight(1.000000, 1.000000, 1.000000, 0.7000000, "ambientlight1")
		pLight = pSet.GetLight("ambientlight1")
		pLight.UnilluminateEntireSet()
		
	#Remove the blueish light if present
	pLight = pSet.GetLight("ATPLight_"+str(LIFE_SUPPORT))
	if pLight:
		pSet.DeleteLightFromSet("ATPLight_"+str(LIFE_SUPPORT))

	pLight = pSet.GetLight("ATPLight_"+str(DRAINER_WEAPON))
	if pLight:
		pSet.DeleteLightFromSet("ATPLight_"+str(DRAINER_WEAPON))

	
	#Reset the LCARS
	if pBridgeObject:
		pBridgeObject.TurnLCARsOn()


	#Abort all smoke actions
	global ActionDict
	for ID in ActionDict.keys():
		pAction=ActionDict[ID][ACTION]
		if pAction:
			pAction.Abort()
		
	ActionDict={}


def MakeCharacterSay(pCharName,pTextRef,sMode = 'Speak',bTurnBack = 1):
	debug(__name__ + ", MakeCharacterSay")
	return

	##  App.CharacterAction_Create(pCharacter, ActionType, "DetailString", "To", bTurnBack, pDatabase)
	##	AT_SAY_LINE_AFTER_TURN        - similar to AT_SAY_LINE, but the character waits until they are done turning before starting to talk

	pChar = g_dNameToCharacter[pCharName]
	iMode = g_dAnimationModes[sMode]
	
	## Find the lines
	if g_sLines.count(pTextRef) == 1:
		pAction = App.CharacterAction_Create(pChar, iMode , pTextRef , 'Captain' , bTurnBack , g_Database)
	else:
		pAction = App.CharacterAction_Create(pChar, iMode , pTextRef , 'Captain' , bTurnBack )

	## Queue up
	import MissionLib
	MissionLib.QueueActionToPlay(pAction)

def MakeCharacterSayYes(pCharName,sMode = 'Speak',bTurnBack = 1):
	debug(__name__ + ", MakeCharacterSayYes")
	return
	sEffCharName = g_dNameToCharacterName[pCharName]
	pTextRef = sEffCharName + 'Yes' + str(App.g_kSystemWrapper.GetRandomNumber(4)+1)	
	MakeCharacterSay(pCharName,pTextRef,sMode,bTurnBack)		
			

def CreateDrainEffect(fDuration=10000):
	debug(__name__ + ", CreateDrainEffect")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")
	if (pBridgeObject):
		#Check if we we already hit, if so stop
		if g_DrainerActive:
			return

		#Shut the consoles down
		pBridgeObject.TurnLCARsOff()
		pSet.SetGlowIntensity(0.0)
		
		#Create long and persistent smoke
		for i in range (12):
			CreateSmoke(fDuration,DRAINER_WEAPON)
			CreateSpark(fDuration,DRAINER_WEAPON)

		#Remove the main light
		pLight = pSet.GetLight("ambientlight1")
		if pLight:
			pSet.DeleteLightFromSet("ambientlight1")
		
		#Add a new blueish light if not present
		pLight = pSet.GetLight("ATPLight_"+str(DRAINER_WEAPON))
		if not pLight:
			pSet.CreateAmbientLight(23.0/255.0,100.0/255.0,193.0/255.0,150.0/255.0,"ATPLight_"+str(DRAINER_WEAPON))
	  		

		#Mark the drainer mode as active
		global g_DrainerActive
		g_DrainerActive=TRUE


def EndDrainEffect():
	#No end for it forseen
	debug(__name__ + ", EndDrainEffect")
	pass


def CreateIonEffect():
	debug(__name__ + ", CreateIonEffect")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject(pSet, "bridge")
	if (pBridgeObject):
		#Just flicker our LCARS a bit
		pBridgeObject.FlickerLCARs(1.0)


def EndIonEffect():
	#No need to end it
	debug(__name__ + ", EndIonEffect")
	pass


def CreateLifeSupportEffect(fDuration=120.0):
	debug(__name__ + ", CreateLifeSupportEffect")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")
	if (pBridgeObject):
		#If the light already exist there is a problem and we abort
		pLight = pSet.GetLight("ATPLight_"+str(LIFE_SUPPORT))
		if pLight:
			return

		global g_DrainerActive
		if g_DrainerActive:
			return
		
		#Remove the main light if present
		pLight = pSet.GetLight("ambientlight1")
		if pLight:
			pSet.DeleteLightFromSet("ambientlight1")

		#Creates a blueish light
		pSet.CreateAmbientLight(23.0/255.0,100.0/255.0,193.0/255.0,189.0/255.0, "ATPLight_"+str(LIFE_SUPPORT))
		
		#Some effects
		pBridgeObject.FlickerLCARs(120.0)
		pSet.SetGlowIntensity(0.0)
		for i in range (5):
			CreateSmoke(fDuration,LIFE_SUPPORT)
			
		
def EndLifeSupportEffect():
	debug(__name__ + ", EndLifeSupportEffect")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")
	if (pBridgeObject):
		#Normal lights
		pBridgeObject.TurnLCARsOn()
		
		#Recreate the main light if no other process if busy
		if not g_DrainerActive:			
			pLight = pSet.GetLight("ambientlight1")
			if not pLight:
				pSet.CreateAmbientLight(1.000000, 1.000000, 1.000000, 0.7000000, "ambientlight1")
				pLight = pSet.GetLight("ambientlight1")
				pLight.UnilluminateEntireSet()
		
		#Remove the blueish light if present
		pLight = pSet.GetLight("ATPLight_"+str(LIFE_SUPPORT))
		if pLight:
			pSet.DeleteLightFromSet("ATPLight_"+str(LIFE_SUPPORT))

		#Abort all smoke created by the life support effect
		global ActionDict
		for ID in ActionDict.keys():
			pAction=ActionDict[ID][ACTION]
			if pAction:
				if ActionDict[ID][TYPE]==LIFE_SUPPORT:
					pAction.Abort()
			

def CreateLifeSupportDeathEffect():
	debug(__name__ + ", CreateLifeSupportDeathEffect")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")
	if (pBridgeObject):
		#Totally dark
		pBridgeObject.TurnLCARsOff()
		
		#Remove the main & blueish light
		pLight = pSet.GetLight("ambientlight1")
		if pLight:
			pSet.DeleteLightFromSet("ambientlight1")
		pLight = pSet.GetLight("ATPLight_"+str(LIFE_SUPPORT))
		if pLight:
			pSet.DeleteLightFromSet("ATPLight_"+str(LIFE_SUPPORT))

		#I hope it is quite dark now and let them scream!!!!!!!!!
		App.g_kSoundManager.GetSound("ATP_DeathBrex").Play()
		App.g_kSoundManager.GetSound("ATP_DeathSaffi").Play()
		App.g_kSoundManager.GetSound("ATP_DeathMiguel").Play()
		App.g_kSoundManager.GetSound("ATP_DeathKiska").Play()
		App.g_kSoundManager.GetSound("ATP_DeathFelix").Play()

	
def CreateSmoke (fDuration,iVal):
	# create smoke
	debug(__name__ + ", CreateSmoke")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")
	if (pBridgeObject):
		pAction = App.BridgeEffectAction_CreateSmoke (fDuration, 1.5, 0.01, pBridgeObject, None, "data/sphere.tga")
		pController = pAction.GetController ()

		# Setup some default values for velocity, colors and alpha
		# Time zero.
		pController.AddColorKey (0.0, 0.8, 0.8, 0.8)
		pController.AddAlphaKey (0.0, 0.75)
		pController.AddSizeKey (0.0, 2.5)

		# End of life.
		pController.AddAlphaKey (1.0, 0.0)
		pController.AddSizeKey (1.0, 20.0)
		pController.SetEmitVelocity (40)
		pController.SetAngleVariance (20)
		
		global ActionDict
		ActionDict[pAction.GetObjID()]=pAction,iVal
		pAction.Play ()


def CreateSpark (fDuration,iVal):
	# create spark
	debug(__name__ + ", CreateSpark")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")

	if (pBridgeObject):
		pAction = App.BridgeEffectAction_CreateSparks (fDuration, fDuration - 0.005 * 40, 0.005, pBridgeObject, None, "data/spark.tga")
		pController = pAction.GetSparkController ()

		# Setup some default values for velocity, colors and alpha
		pController.AddColorKey (0.0, 1.0, 1.0, 1.0)
		pController.AddColorKey (0.4, 1.0, 1.0, 0.6)
		pController.AddColorKey (1.0, 1.0, 0.7, 0.7)
		
		pController.AddAlphaKey (0.0, 1.0)
		pController.AddAlphaKey (0.95, 1.0)
		pController.AddAlphaKey (1.0, 0.0)

		pController.AddSizeKey (0.0, 0.35)

		pController.SetEmitVelocity (100.0)
		pController.SetGravity (0.0, 0.0, -250.0)
		pController.SetTailLength (5.0)

		pcHardpointName = pAction.GetHardpointName ()

		pBridgeObject.DoCrewReactions (pcHardpointName)
		pBridgeObject.FlickerLCARs(3.0)

		global ActionDict
		ActionDict[pAction.GetObjID()]=pAction,iVal
		pAction.Play ()
	return


g_lsSparks = ( "ConsoleExplosion1", "ConsoleExplosion2","ConsoleExplosion3", "ConsoleExplosion4","ConsoleExplosion5", "ConsoleExplosion6", "ConsoleExplosion7","ConsoleExplosion8" )
