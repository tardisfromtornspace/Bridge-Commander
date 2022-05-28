from bcdebug import debug
# NanoFXv2 Beta fixes by MLeo Daalder
# Original author: NanoByte (NanoFX itself)
#
# Bug descriptions:
# 	Cloak bug:
# 		Blinkers still visible after you cloaked (on both player and AI ships).
#		Can be exploited if you have good eyes.
#	Fix used:
#		Hide the Static and Dynamic lights when a ship cloaks
#		And remove the clock that controls the blinking
#
#	MVAM bug:
#		The static blinkers would shift 0.1 on the Y axis when (atleast) the player
#		reintegrated.
#		Untested if this also happens to AI ships, but it was never said
#	Fix used:
#		Move the static blinkers by -0.1 on teh Y axis when the player reintegrates.
#		Detecting the player reintegrating is a slight problem, since no events are
#		fired when that happens.
#		Solution to this is to attach an event listener on the reintegration button.
#		With that we hit another kink. Though not a large one.
#		It appears to be the case that CreateBlinkerFX get's called 4 times for the player
#
#	Warp when cloaked bug:
#		When you start/end warp cloaked, the ship will turn totally opaque
#		when you enter or leave the warpset.
#	Fix used:
#		When the ship get's unhidden (through HideShip function in WarpFX.py)
#		I'll check if the ship has a cloaking device and if so,
#		then I'll quickly recloak (InstantDecloak and InstantCloak) the ship
#		Though this seems to work for dropping out of warp.
#		Something else that I did/had to do was to temporarly disable the cloak sounds.
#		To fix the part of actually going to warp
#
#	Ship destroyed bug:
#		When a ship with blinkers get destroyed, the blinkers stay behind.
#	Fix used:
#		Hide the blinkers and static lights, then delete them.

import App
import Custom.NanoFXv2.NanoFX_ScriptActions
from Custom.NanoFXv2.SpecialFX.BlinkerFX import TRUE, FALSE, Blinkers, Static, GetBlinkers, RemoveBlinkers, BlinkerContainer
from Custom.NanoFXv2.SpecialFX import BlinkerFX

import Foundation

# MLeo edit: Fixing Cloak problem... part 3
dContainers = {}
# MLeo edit: Blinker Destruction... part 3
dSequences = {}

#MLeo edit: Fixing MVAM problem... part 3
lET = []

bExpectingPlayer = 0

def CreateBlinkerFX(pShip):

	# MLeo edit: if this line isn't here,
	#	then pBlinkers won't exist outside the scope of the if, or
	#	if the ship doesn't exist, then you have a problem, because
	#	then pBlinkers won't exist at all.
	debug(__name__ + ", CreateBlinkerFX")
	pBlinkers = None

	if pShip:
		pBlinkers = GetBlinkers(pShip)
	if not pBlinkers:
		return
	if pShip.GetName() == None:
		return	
	RemoveBlinkers(pShip)

	pSet = pShip.GetContainingSet()
	
	#kBlinkers = App.Waypoint_Create("Fun", pSet.GetName(), None)
	kBlinkers = App.ObjectClass_Create(None)
	#kForward = App.TGPoint3()
	#kForward.SetXYZ(0,0,1)
	#kUp = App.TGPoint3()
	#kUp.SetXYZ(0,0,1)
	kBlinkers.SetTranslateXYZ(0.0,0.0,0.0)
	kBlinkers.UpdateNodeOnly()
	kBlinkers.SetName(pShip.GetName() + "_Blinking_Lights")
	Blinkers.append(kBlinkers)
	pShip.AttachObject(kBlinkers)
	
	kStatic = App.ObjectClass_Create(None)
	#kForward = App.TGPoint3()
	#kForward.SetXYZ(0,0,1)
	#kUp = App.TGPoint3()
	#kUp.SetXYZ(0,0,1)
	kStatic.SetTranslateXYZ(0.0,0.0,0.0)
	kStatic.UpdateNodeOnly()
	kStatic.SetName(pShip.GetName() + "_Static_Lights")
	Static.append(kStatic)
	pShip.AttachObject(kStatic)
	
	sFile = "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Blinker/Blinker.tga"
	### Setup for Effect ###
	pSequence = App.TGSequence_Create()
	
	for iBlinkers in range(len(pBlinkers)):
		pBlinker = pBlinkers[iBlinkers]
		
		# MLeo edit: Blinker Destruction... Part 1
		# Add a listener for when the blinker get's destroyed
		# Or I'd like to do that, if pBlinker wasn't a property. :(
		#pBlinker.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_DESTROYED, __name__ + ".HandleBlinkerDestruction")
		
		vPos = pBlinker.GetPosition()
		pCol = pBlinker.GetColor()
		fPeriod = pBlinker.GetPeriod()
		fDuration = pBlinker.GetDuration()
		fLifeTime = 9999999
		vEmitPos = App.NiPoint3(vPos.GetX(), vPos.GetY(), vPos.GetZ())
		
		if fDuration == 0:
			fSize = pShip.GetRadius() * 0.018 * pBlinker.GetRadius()
			fDuration = 9999999
			fLifeTime = 0.1
			fPeriod = 1.0
			sType = "StaticBlinker"
			pAttachTo = kStatic.GetNode()
			pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pAttachTo)
		else:
			fSize = pShip.GetRadius() * 0.018 * pBlinker.GetRadius()
			fDuration = 9999999
			fLifeTime = 0.1
			fPeriod = 1.0
			sType = "StaticBlinker"
			pAttachTo = kBlinkers.GetNode()
			pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pAttachTo)
		
		pLight = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * 1.1, vEmitPos, fFrequency = fPeriod, fLifeTime = fLifeTime, iTiming = fDuration, sType = sType, fRed = 255.0 * pCol.GetR(), fGreen = 255.0 * pCol.GetG(), fBlue = 255.0 * pCol.GetB())
		pSequence.AddAction(pLight)
		pLight = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * 0.5, vEmitPos, fFrequency = fPeriod, fLifeTime = fLifeTime, iTiming = fDuration, sType = sType)
		pSequence.AddAction(pLight)
	
	pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "DestroyTGSequence", pSequence), 1.0)
	dSequences[pShip.GetName()] = pSequence
	pSequence.Play()
	
	## Create a container for the blinkers
	pContainer = BlinkerContainer()
	pContainer.SetNode(kBlinkers)
	
	# MLeo edit: Fixing cloak problem... part 4
	dContainers[pShip.GetName()] = pContainer
	
	# MLeo edit: Fixing cloak problem... Part 1
	pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
	pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")
	
	# MLeo edit: Fixing ship destruction problem... Part 1
	pShip.AddPythonFuncHandlerForInstance(App.ET_OBJECT_DESTROYED, __name__ + ".ShipDestruction")

	# MLeo edit: Fixing Warp problem... Part 2
	#pShip.AddPythonFuncHandlerForInstance(App.ET_ENTERED_SET, __name__ + ".ShipEnteredSet")

	# MLeo edit: Fixing MVAM reintegration problem... Part 1
	global bExpectingPlayer
	sPlayer = App.Game_GetCurrentPlayer().GetName()
	if not App.Game_GetCurrentPlayer() or App.Game_GetCurrentPlayer().GetName() != pShip.GetName():
		return
	sPlayer = App.Game_GetCurrentPlayer().GetName()

	# There is something funny here, this function get's called 4 times when a player reintegrates
	# Also, I don't know if this bug is also present with AI seperation
	if bExpectingPlayer == 4:
		# Hmm... The Y value always was -0.06
		# And all of a sudden it's -0.10...
		# Though it ounce was -2.00...
		kStatic.SetTranslateXYZ(0,-0.10,0)
		kStatic.UpdateNodeOnly()
		bExpectingPlayer = 0
	elif bExpectingPlayer != 0:
		bExpectingPlayer = bExpectingPlayer + 1
	else:
		try:
			# I actually need to get the events from the buttons themselfs...
			
			# If this fails, then we don't need to bother with the rest
			if not __import__("Custom.Sneaker.Mvam.SneakerMenuAdd"):
				return
		except:
			return

		# Get XO menu
		import Bridge.BridgeUtils
		pXOMenu = Bridge.BridgeUtils.GetBridgeMenu("XO")
		if not pXOMenu:
			return
		pMVAMMenu = pXOMenu.GetSubmenuW(App.TGString("MVAM Menu"))
		if not pMVAMMenu:
			return
		pReint = App.STButton_Cast(pMVAMMenu.GetLastChild())
		if not pReint:
			return
		pEvent = pReint.GetActivationEvent()
		if not pEvent:
			return
		if pEvent.GetEventType() not in lET:
			pXOMenu.AddPythonFuncHandlerForInstance(pEvent.GetEventType(), __name__ + ".HandleReintegration")
			lET.append(pEvent.GetEventType())

# MLeo edit: Fixing cloak problem... Part 2
def CloakHandler(pEObject, pEvent):
	debug(__name__ + ", CloakHandler")
	pShip = App.ShipClass_Cast(pEObject)
	if pShip:
		if dContainers.has_key(pShip.GetName()):
			pContainer = dContainers[pShip.GetName()]
			if pContainer:
				if not pContainer.Node.IsHidden():
					pContainer.Swap(None)
				pContainer.RemoveClock("Swap")
		for pObject in Static:
			if pObject.GetName() == pShip.GetName() + "_Static_Lights":
				pObject.SetHidden(1)
				break
	pEObject.CallNextHandler(pEvent)

def DecloakHandler(pEObject, pEvent):
	debug(__name__ + ", DecloakHandler")
	pShip = App.ShipClass_Cast(pEObject)
	if pShip:
		if dContainers.has_key(pShip.GetName()):
			pContainer = dContainers[pShip.GetName()]
			if pContainer:
				pContainer.Swap(None)
		for pObject in Static:
			if pObject.GetName() == pShip.GetName() + "_Static_Lights":
				pObject.SetHidden(0)
				break

	pEObject.CallNextHandler(pEvent)
	
# MLeo edit: Fixing MVAM problem... Part 2
def HandleReintegration(pObject, pEvent):
	debug(__name__ + ", HandleReintegration")
	global bExpectingPlayer
	bExpectingPlayer = 1
	pObject.CallNextHandler(pEvent)
	
# MLeo edit: Fixing Ship destruction problem... Part 2
def ShipDestruction(pObject, pEvent):
	debug(__name__ + ", ShipDestruction")
	if not App.ShipClass_Cast(pObject):
		print "No ship destroyed"
	sName = pObject.GetName()
	if sName:
		for oStatic in Static:
			if oStatic.GetName() == sName + "_Static_Lights":
				oStatic.SetHidden(1)
				oStatic.SetDeleteMe(1)
		if dContainers.has_key(sName):
			dContainers[sName].Node.SetHidden(1)
			try:
				dContainers[sName].DeleteContainer(None)
			except:
				print "Error deleting container"
	pObject.CallNextHandler(pEvent)

# And overwrite the original CreateBlinkerFX with our own
BlinkerFX.CreateBlinkerFX = CreateBlinkerFX

# MLeo edit: Blinker Destruction... Part 2
def HandleBlinkerDestruction(pObject, pEvent):
	debug(__name__ + ", HandleBlinkerDestruction")
	pBlinker = App.BlinkingLightProperty_Cast(pObject)
	if pBlinker:
		pBlinkers = GetBlinkers()
		i=0
		while pBlinkers[i].GetObjID() != pBlinker.GetObjID(): i = i + 1
		pShip = pBlinker.GetParentShip()
		if pShip:
			if dSequences.has_key(pShip.GetName()):
				pSequence = dSequences[pShip.GetName()]
				pAction = pSequence.GetAction(i)
				pAction.Abort()
			
	pObject.CallNextHandler(pEvent)

# MLeo edit: Fixing Warp problem... Part 1
def HideShip(pAction, iShipID, iHide):
	debug(__name__ + ", HideShip")
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), iShipID)
	if pShip:
		pShip.SetHidden(iHide)
		try:
			if iHide == FALSE and pShip.GetCloakingSubsystem().IsCloaked():
				# temporarly detach the sounds
				oCloakSound = DetachSoundDef("Cloak")
				oDecloakSound = DetachSoundDef("Uncloak")

				pShip.GetCloakingSubsystem().InstantDecloak()
				pShip.GetCloakingSubsystem().InstantCloak()

				# And attach the sounds again
				oCloakSound.AddToMutator(Foundation.MutatorDef.StockSounds)
				oDecloakSound.AddToMutator(Foundation.MutatorDef.StockSounds)
		except:
			return 0
	return 0

import Custom.NanoFXv2.WarpFX.WarpFX
# And overwrite the original HideShip with our own
Custom.NanoFXv2.WarpFX.WarpFX.HideShip = HideShip

# MLeo edit: Fixing Warp problem... Part 3
def ShipEnteredSet(pObject, pEvent):
	debug(__name__ + ", ShipEnteredSet")
	pShip = App.ShipClass_Cast(pObject)
	if pShip:
		CreateBlinkerFX(pShip)
		#HideShip(None, pShip.GetObjID(), pShip.IsHidden())
		try:
			if pShip.GetCloakingSubsystem().IsCloaked():
				# temporarly detach the sounds
				oCloakSound = DetachSoundDef("Cloak")
				oDecloakSound = DetachSoundDef("Uncloak")

				pShip.GetCloakingSubsystem().InstantDecloak()
				pShip.GetCloakingSubsystem().InstantCloak()

				# And attach the sounds again
				oCloakSound.AddToMutator(Foundation.MutatorDef.StockSounds)
				oDecloakSound.AddToMutator(Foundation.MutatorDef.StockSounds)
		except:
			pObject.CallNextHandler(pEvent)
			return
	pObject.CallNextHandler(pEvent)

def DetachSoundDef(sName):
	debug(__name__ + ", DetachSoundDef")
	oSoundDef = Foundation.MutatorDef.StockSounds.sounds[sName]
	Foundation.MutatorDef.StockSounds.elements.remove(oSoundDef)
	del Foundation.MutatorDef.StockSounds.sounds[sName]
