# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# PATCH-SlipstreamModuleLoadFlash&Sound.py
# This patch was made by Alex SL Gato with permission from USS Sovereign, so as to allow flash and sound customizations from SlipstreamModule to work properly for stuff like GalaxyCharts. Slipstream Module remains ALL RIGHTS RESERVED, by USS Sovereign.
# GC is ALL Rights Reserved by USS Frontier, but since GC supports Plugins it is fair to release a new TravellingMethod or patch old ones as long as the files remain unmodified.
# Please note that this file requires:
# - USS Sovereign's Slipstream Module, as this file's purpose revolves around it.
# 18th April 2025
# Version 0.21

# Imports
import App
import Foundation
import MissionLib
import Custom.GravityFX.GravityFXlib

from bcdebug import debug
import traceback

myDependingTravelModule = None # The module we load.
myDependingTravelModulePath = "Custom.Slipstream.SlipstreamModule" # From where we load the module.
VERSION = '20252814' # Versions before this one will be patched
# GFX Folder
GFX = 'scripts/Custom/Slipstream/GFX/'

shipsIDDict = {} # A list of

try:
	myDependingTravelModuleAux = __import__(myDependingTravelModulePath)
	if myDependingTravelModuleAux != None and hasattr(myDependingTravelModuleAux, "VERSION") and hasattr(myDependingTravelModuleAux, "sSlipstreamList") and myDependingTravelModuleAux.VERSION < VERSION:
		myDependingTravelModule = myDependingTravelModuleAux
	else:
		print str(__name__) + ": the ", myDependingTravelModuleLibPath, " should be already up-to-date."
except:
	print str(__name__) + ": no ", myDependingTravelModuleLibPath, " to patch."
	traceback.print_exc()

myDependingTravelModuleLib = None # The module we load.
myDependingTravelModuleLibPath = "Custom.Slipstream.Libs.LoadFlash" # From where we load the module.
try:
	myDependingTravelModuleLibAux = __import__(myDependingTravelModuleLibPath)
	if myDependingTravelModuleLibAux != None and hasattr(myDependingTravelModuleLibAux, "StartGFX") and hasattr(myDependingTravelModuleLibAux, "CreateGFX") and hasattr(myDependingTravelModuleLibAux, "GetTexture"):
		myDependingTravelModuleLib = myDependingTravelModuleLibAux
	else:
		print str(__name__) + ": Error, you are missing a correct ", myDependingTravelModuleLibPath
except:
	print str(__name__) + ": Error, you are missing ", myDependingTravelModuleLibPath
	traceback.print_exc()


def GetWellShipFromID(pShipID):
	try:
		pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
		if not pShip or pShip.IsDead() or pShip.IsDying():
			return None
		return pShip
	except:
		traceback.print_exc()

	return None


# An aux class and its instance.
class ListenerFixClass:
	def __init__(self, name):
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

	def AnObjectDying(self, pEvent):
		try:
			AnObjectDying(self, pEvent)
		except:
			traceback.print_exc()
		return 0

	def BeginListening(self):
		self.StopListening()
		App.g_kEventManager.AddBroadcastPythonMethodHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "PlayReload")

	def StopListening(self):
		App.g_kEventManager.RemoveBroadcastHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "PlayReload")

	def CallNextHandler(self, pEvent):
		return

	def PlayReload(self, pEvent):
		PlayReload(self, pEvent)
		return 0

basicListener = ListenerFixClass("SlipstreamGC is listening")
basicListener.BeginListening()

def clearShipSoundInfo(pShipID):
	try:
		App.g_kSoundManager.DeleteSound("Enter Slipstream AI"+str(pShipID))
	except:
		traceback.print_exc()
	try:
		App.g_kSoundManager.DeleteSound("Exit Slipstream AI"+str(pShipID))
	except:
		traceback.print_exc()
	global shipsIDDict
	if shipsIDDict.has_key(pShipID):
		del shipsIDDict[pShipID]

# An aux function
def PlayReload(TGObject, pEvent):
	debug(__name__ + ", PlayReload")
		
	global shipsIDDict
	
	tempDict = {}
	for aKey in shipsIDDict.keys():
		tempDict[aKey] = shipsIDDict[aKey]

	for pShipID in tempDict.keys():	
		clearShipSoundInfo(pShipID)

	del tempDict

	#basicListener.StopListening()

	return 0

def ObjectDestroyed(TGObject, pEvent):
	debug(__name__ + ", ObjectDestroyed")

	kShip = App.ShipClass_Cast(pEvent.GetDestination())
	if kShip and hasattr(kShip, "GetObjID"):
		pShipID = kShip.GetObjID()
		if pShipID != None and pShipID != App.NULL_ID:
			pShip = App.ShipClass_GetObjectByID(None, pShipID)
			if pShip:
				clearShipSoundInfo(pShipID)	

	TGObject.CallNextHandler(pEvent)
	return 0

def pPlayerCleanUpRel(pShip, go = "Enter"):
	try:
		App.g_kSoundManager.DeleteSound(go)
	except:
		traceback.print_exc()
	#basicListener.BeginListening()

def shipAIListenExplode(pShip, pShipID, go = "Enter"):
	try:
		App.g_kSoundManager.DeleteSound(str(go) + " Slipstream AI"+str(pShipID))
	except:
		traceback.print_exc()
	try:
		global shipsIDDict
		shipsIDDict[pShipID] = 1
		pShip.RemoveHandlerForInstance(App.ET_OBJECT_EXPLODING, __name__ + ".ObjectDestroyed")
		pShip.AddPythonFuncHandlerForInstance(App.ET_OBJECT_EXPLODING, __name__ + ".ObjectDestroyed")
	except:
		traceback.print_exc()


if myDependingTravelModule != None and myDependingTravelModuleLib != None:
	try:
		from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import SlipstreamConfiguration
		oldStartGFX = myDependingTravelModuleLib.StartGFX
		oldCreateGFX = myDependingTravelModuleLib.CreateGFX
		oldGetTexture = myDependingTravelModuleLib.GetTexture

		oldEnteringFlash = myDependingTravelModule.EnteringFlash
		oldExitingFlash = myDependingTravelModule.ExitingFlash

		# Entering sound
		def EnteringFlash(pAction, pShipID = None):
			# Check for custom sounds
			pShip = None
			pPlayer = MissionLib.GetPlayer()
			if pShipID != None:
				pShip = GetWellShipFromID(pShipID)
			else:
				pShip = pPlayer

			if not pShip or not pPlayer:
				return 0

			# Multiple sounds called "Enter", then calling "Enter" globally... that could cause some issues if multiple different "Enter" sounds are supposed to be happening at the same time.
			if pShipID == None or (pPlayer != None and pShipID == pPlayer.GetObjID()):
				pPlayerCleanUpRel(pShip, "Enter")
				return oldEnteringFlash(pAction)

			pSSet = pShip.GetContainingSet()
			pPSet = pPlayer.GetContainingSet()
			if pSSet is None or pPSet is None:
				return 0

			if hasattr(pSSet, "GetObjID") and hasattr(pPSet, "GetObjID"):
				pSID = pSSet.GetObjID()
				pPID = pPSet.GetObjID()
				if pSID != pPID:		 
					return 0

			shipAIListenExplode(pShip, pShipID, "Enter")

			pModule = __import__(pShip.GetScript())

			pEnterSound = None
			# Is there a customization for this ship available?
			if hasattr(pModule, "SlipstreamCustomizations"):
				pCustomization = pModule.SlipstreamCustomizations()

				# Customization exists, but does the sound entry exist?!
				if pCustomization.has_key('EntrySound'):
					pSound = "scripts/Custom/Slipstream/SFX/" + pCustomization['EntrySound']

					pEnterSound = App.TGSound_Create(pSound, "Enter Slipstream AI"+str(pShipID), 0)
					pEnterSound.SetSFX(0) 
					pEnterSound.SetInterface(1)

				# No sound entry found
				else:
					pEnterSound = App.TGSound_Create("scripts/Custom/Slipstream/SFX/enterslipstream.wav", "Enter Slipstream AI"+str(pShipID), 0)
					pEnterSound.SetSFX(0) 
					pEnterSound.SetInterface(1)

			# No customizations of any kind available for this ship.
			else:
				pEnterSound = App.TGSound_Create("scripts/Custom/Slipstream/SFX/enterslipstream.wav", "Enter Slipstream AI"+str(pShipID), 0)
				pEnterSound.SetSFX(0) 
				pEnterSound.SetInterface(1)

			if pEnterSound != None:
				App.g_kSoundManager.PlaySound("Enter Slipstream AI"+str(pShipID))
				#pEnterSound.Play()

			return 0

		myDependingTravelModule.EnteringFlash = EnteringFlash

		# Exiting sound
		def ExitingFlash(pAction, pShipID = None):
			# Check for custom sounds
			pShip = None
			pPlayer = MissionLib.GetPlayer()
			if pShipID != None:
				pShip = GetWellShipFromID(pShipID)
			else:
				pShip = pPlayer

			if not pShip or not pPlayer:
				return 0

			# Multiple sounds called "Exit", then calling "Exit" globally... that could cause some issues if multiple different "Exit" sounds are supposed to be happening at the same time.
			if pShipID == None or (pPlayer != None and pShipID == pPlayer.GetObjID()):
				pPlayerCleanUpRel(pShip, "Exit")
				return oldExitingFlash(pAction)

			pSSet = pShip.GetContainingSet()
			pPSet = pPlayer.GetContainingSet()
			if pSSet is None or pPSet is None:
				return 0

			if hasattr(pSSet, "GetObjID") and hasattr(pPSet, "GetObjID"):
				pSID = pSSet.GetObjID()
				pPID = pPSet.GetObjID()
				if pSID != pPID:
					return 0

			shipAIListenExplode(pShip, pShipID, "Exit")
			
			pModule = __import__(pShip.GetScript())

			pExitSound = None
			# Is there a customization for this ship available?
			if hasattr(pModule, "SlipstreamCustomizations"):
				pCustomization = pModule.SlipstreamCustomizations()
            
				# Customization exists, but does the sound entry exist?!
				if pCustomization.has_key('ExitSound'):
					pSound = "scripts/Custom/Slipstream/SFX/" + pCustomization['ExitSound']

					pExitSound = App.TGSound_Create(pSound, "Exit Slipstream AI"+str(pShipID), 0)
					pExitSound.SetSFX(0) 
					pExitSound.SetInterface(1)

				# No sound entry found
				else:
					pExitSound = App.TGSound_Create("scripts/Custom/Slipstream/SFX/exitslipstream.wav", "Exit Slipstream AI"+str(pShipID), 0)
					pExitSound.SetSFX(0) 
					pExitSound.SetInterface(1)

			# No customizations of any kind available for this ship.
			else:
				pExitSound = App.TGSound_Create("scripts/Custom/Slipstream/SFX/exitslipstream.wav", "Exit Slipstream AI"+str(pShipID), 0)
				pExitSound.SetSFX(0) 
				pExitSound.SetInterface(1)

			if pExitSound != None:
				App.g_kSoundManager.PlaySound("Exit Slipstream AI"+str(pShipID))
				#pExitSound.Play()

			return 0

		myDependingTravelModule.ExitingFlash = ExitingFlash

		# Load the GFX animation
		def StartGFX(pShipID = None):
			pShip = None
			pPlayer = MissionLib.GetPlayer()
			if pShipID != None:
				pShip = GetWellShipFromID(pShipID)
			else:
				pShip = pPlayer

			if not pShip:
				return 0

			if pShipID == None or (pPlayer != None and pShipID == pPlayer.GetObjID()):
				return oldStartGFX()

			pModule = __import__(pShip.GetScript())

			# Is there a customization for this ship available?
			if hasattr(pModule, "SlipstreamCustomizations"):
				pCustomization = pModule.SlipstreamCustomizations()
                    
				# Customization exists, but does the flash entry exist?
				if pCustomization.has_key('FlashAnimation'):
					# Yes it does exist!
					pFlash = "scripts/Custom/Slipstream/GFX/" + pCustomization['FlashAnimation']
                        
					myDependingTravelModuleLib.LoadGFX(4, 4, pFlash)
				else:
					# There doesn't seem to be an entry of a custom flash for this ship so check for user defined ones
					reload(SlipstreamConfiguration)
                        
					if SlipstreamConfiguration.FlashGFX == 'Default':
						myDependingTravelModuleLib.LoadGFX(4, 4, GFX + "SlipstreamFlash.tga")
					else:
						pFlash = "scripts/Custom/Slipstream/GFX/" + SlipstreamConfiguration.FlashGFX
						myDependingTravelModuleLib.LoadGFX(4, 4, pFlash)

			# No customizations available for this ship, now checking for user defined stuff
			else:
				reload(SlipstreamConfiguration)
                        
				if SlipstreamConfiguration.FlashGFX == 'Default':
					myDependingTravelModuleLib.LoadGFX(4, 4, GFX + "SlipstreamFlash.tga")
				else:
					pFlash = "scripts/Custom/Slipstream/GFX/" + SlipstreamConfiguration.FlashGFX
					myDependingTravelModuleLib.LoadGFX(4, 4, pFlash)

		myDependingTravelModuleLib.StartGFX = StartGFX

		# Returns texture filename
		def GetTexture(pShip = None):

			if pShip == None:
				pShip = MissionLib.GetPlayer()

			pModule = __import__(pShip.GetScript())

			# Is there a customization for this ship available?
			if hasattr(pModule, "SlipstreamCustomizations"):
				pCustomization = pModule.SlipstreamCustomizations()
                    
				# Customization exists, but does the flash entry exist?
				if pCustomization.has_key('FlashAnimation'):
					# Yes it does exist!
					strFile = GFX + pCustomization['FlashAnimation']
				else:
					# There doesn't seem to be an entry of a custom flash for this ship
					reload(SlipstreamConfiguration)
                        
					if SlipstreamConfiguration.FlashGFX == 'Default':
						strFile = GFX + "SlipstreamFlash.tga"
					else:
						strFile = GFX + SlipstreamConfiguration.FlashGFX

			# No customizations available for this ship
			else:
				reload(SlipstreamConfiguration)

				if SlipstreamConfiguration.FlashGFX == 'Default':
					strFile = GFX + "SlipstreamFlash.tga"
				else:
					strFile = GFX + SlipstreamConfiguration.FlashGFX

			return strFile

		# Create flash effect on a ship
		def CreateGFX(pShip):
			pAttachTo = pShip.GetNode()
			fSize = pShip.GetRadius() * 10
			pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

			sFile = GetTexture(pShip)
			fLifeTime = 1
			fRed = 255.0
			fGreen = 255.0
			fBlue = 255.0
			fBrightness = 0.8
			fSpeed = 1
       
			pEffect = App.AnimTSParticleController_Create()
			pEffect.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
			pEffect.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
			pEffect.AddAlphaKey(0.0, 1.0)
			pEffect.AddAlphaKey(1.0, 1.0)
			pEffect.AddSizeKey(0.0, fSize)
			pEffect.AddSizeKey(1.0, fSize)
		
			pEffect.SetEmitLife(fSpeed)
			pEffect.SetEmitFrequency(1)
			pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
			pEffect.SetInheritsVelocity(0)
			pEffect.SetDetachEmitObject(0)
			pEffect.CreateTarget(sFile)
			pEffect.SetTargetAlphaBlendModes(0, 7)
			pEffect.SetEmitFromObject(pEmitFrom)
			pEffect.AttachEffect(pAttachTo)
			fEffect = App.EffectAction_Create(pEffect)
			if fEffect != None:
				pSequence = App.TGSequence_Create()	
				pSequence.AddAction(fEffect)
				pSequence.Play ()
		
			return

		myDependingTravelModuleLib.GetTexture = GetTexture
		myDependingTravelModuleLib.CreateGFX = CreateGFX

		print str(__name__) + ": patched " + str(myDependingTravelModulePath) + " for AI GalaxyCharts Customization."

	except:
		print str(__name__) + ": Error while patching " + str(myDependingTravelModulePath)
		traceback.print_exc()
