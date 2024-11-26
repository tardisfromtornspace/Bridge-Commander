"""
#         AnubisSuperWeaponRay
#         26th November 2024
#         Based on Turrets script, which was strongly based on SubModels.py by USS Defiant and their team, and AutoTargeting.py by USS Frontier... even if the final product of this file lacks prety much any of the features from SubModels or AutoTargeting
#################################################################################################################
# This technology makes your beams "jump" between targetted ships in range, like with Anubis Superweapon on Stargate, hence the name.
"""
"""
Sample Setup:
# This is a bit more complex than usual Technologies I make, similar to Turrets in implementation
# First, it requires to be included on the scripts/Custom/Techs folder, as usual. Remember to replace the "Ambassador" abbrev below for the proper abbrev
Foundation.ShipDef.Ambassador.dTechs = {
	"SG Anubis SuperWeapon Ray": { "Beams": ["Beam hardpoint property 1"]}
}
# "Beams" is an optional field where you include certain beam hardpoint names for checking, so only those make the beams hop. By default, when not added or left empty, it is considered all beams have this ability.

# Now, the more complex part - you need to edit the hardpoint to add an auxiliar, non-targettable, extremely fast-recharge phaser with ridiculous angle height and width but negative max charge, so once it is out of the vessel, it can target any vessel in range without too many calculations from our script part except ensuring the beam is now at the target's position and has a positive max charge. You can also add multiple ones for more effect, or strange behaviours that look like current flowing (like the Anubis Superweapon).
There's an example below for this:
#################################################
ArrayT6 = App.PhaserProperty_Create("Array 6 T")

ArrayT6.SetMaxCondition(3000.000000)
ArrayT6.SetCritical(0)
ArrayT6.SetTargetable(0)
ArrayT6.SetPrimary(1)
ArrayT6.SetPosition(0.000000, -3.350000, 4.150000)
ArrayT6.SetPosition2D(0.000000, 0.000000)
ArrayT6.SetRepairComplexity(1.000000)
ArrayT6.SetDisabledPercentage(0.560000)
ArrayT6.SetRadius(0.250000)
ArrayT6.SetDumbfire(0)
ArrayT6.SetWeaponID(0)
ArrayT6.SetGroups(0)
ArrayT6.SetDamageRadiusFactor(0.100000)
ArrayT6.SetIconNum(0)
ArrayT6.SetIconPositionX(0.000000)
ArrayT6.SetIconPositionY(0.000000)
ArrayT6.SetIconAboveShip(1)
ArrayT6.SetFireSound("Superweapon Phaser")
ArrayT6.SetMaxCharge(-1.000000)
ArrayT6.SetMaxDamage(70000.000000)
ArrayT6.SetMaxDamageDistance(100.000000)
ArrayT6.SetMinFiringCharge(1.000000)
ArrayT6.SetNormalDischargeRate(1.000000)
ArrayT6.SetRechargeRate(60.100000)
ArrayT6.SetIndicatorIconNum(0)
ArrayT6.SetIndicatorIconPositionX(0.000000)
ArrayT6.SetIndicatorIconPositionY(0.000000)
ArrayT6Forward = App.TGPoint3()
ArrayT6Forward.SetXYZ(0.000000, -1.000000, 0.000000)
ArrayT6Up = App.TGPoint3()
ArrayT6Up.SetXYZ(0.000000, 0.000000, 1.000000)
ArrayT6.SetOrientation(ArrayT6Forward, ArrayT6Up)
ArrayT6.SetWidth(0.001000)
ArrayT6.SetLength(0.001000)
ArrayT6.SetArcWidthAngles(-2.523599, 2.523599)
ArrayT6.SetArcHeightAngles(-2.523599, 2.523599)
ArrayT6.SetPhaserTextureStart(0)
ArrayT6.SetPhaserTextureEnd(0)
ArrayT6.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.874510, 0.439216, 0.000000, 1.000000)
ArrayT6.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.647059, 0.286275, 1.000000)
ArrayT6.SetInnerShellColor(kColor)
kColor.SetRGBA(0.768628, 0.768628, 0.000000, 1.000000)
ArrayT6.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
ArrayT6.SetInnerCoreColor(kColor)
ArrayT6.SetNumSides(6)
ArrayT6.SetMainRadius(0.150000)
ArrayT6.SetTaperRadius(0.000000)
ArrayT6.SetCoreScale(0.500000)
ArrayT6.SetTaperRatio(0.000000)
ArrayT6.SetTaperMinLength(1.000000)
ArrayT6.SetTaperMaxLength(1.000000)
ArrayT6.SetLengthTextureTilePerUnit(0.010000)
ArrayT6.SetPerimeterTile(1.000000)
ArrayT6.SetTextureSpeed(-0.005000)
ArrayT6.SetTextureName("data/textures/tactical/AnubisWeapon.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ArrayT6)

# Then the thing below would go on the "def LoadPropertySet(pObj)" area
	prop = App.g_kModelPropertyManager.FindByName("Array 6 T", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)

"""
#################################################################################################################
from bcdebug import debug
import traceback

import App
import FoundationTech
import loadspacehelper
import math
import MissionLib



#################################################################################################################
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.21",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#################################################################################################################



REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209

globalTurretTimer = None
bOverflow = 0
sinTurretbOverflow = 0
defaultSlice = 0.1 # In seconds

ticksPerKilometer = 225.0/40.0 # 225 is approximately 40 km, so 225/40 is the number of ticks per kilometer


# This class does control the attach and detach of the Models
class AnubisSuperWeaponRay(FoundationTech.TechDef):

	# called by FoundationTech when a ship is created
	# Prepares the ship for moving its sub parts
	def AttachShip(self, pShip, pInstance):
		debug(__name__ + ", AttachShip")
		pShip.RemoveHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".WeaponFired") #App.ET_WEAPON_HIT
		pShip.RemoveHandlerForInstance(App.ET_PHASER_STOPPED_FIRING, __name__ + ".WeaponFiredStop")
		pShip.RemoveHandlerForInstance(App.ET_TRACTOR_BEAM_STOPPED_FIRING, __name__ + ".WeaponFiredStop")
		pShip.AddPythonFuncHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".WeaponFired")
		pShip.AddPythonFuncHandlerForInstance(App.ET_PHASER_STOPPED_FIRING, __name__ + ".WeaponFiredStop")
		pShip.AddPythonFuncHandlerForInstance(App.ET_TRACTOR_BEAM_STOPPED_FIRING, __name__ + ".WeaponFiredStop")

        def DetachShip(self, iShipID, pInstance):
		debug(__name__ + ", DetachShip")
		pShip = App.ShipClass_GetObjectByID(None, iShipID)

		if pShip:
			pShip.RemoveHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".WeaponFired")
			pShip.RemoveHandlerForInstance(App.ET_PHASER_STOPPED_FIRING, __name__ + ".WeaponFiredStop")
			pShip.RemoveHandlerForInstance(App.ET_TRACTOR_BEAM_STOPPED_FIRING, __name__ + ".WeaponFiredStop")

        # Called by FoundationTech when a Ship is removed from set (eg destruction)
        def Detach(self, pInstance):
                debug(__name__ + ", Detach")
                self.TrueDetach(pInstance, pInstance.pShipID)

        def TrueDetach(self, pInstance, pShipID):
                debug(__name__ + ", TrueDetach")

                try:
                    self.DetachShip(pShipID, pInstance)
                except:
                    print "Error while e-detaching"
                    traceback.print_exc()

                pInstance.lTechs.remove(self)

oAnubisSuperWeaponRay = AnubisSuperWeaponRay("SG Anubis SuperWeapon Ray")

def MatrixMult(kFwd, kNewUp):
    debug(__name__ + ", MatrixMult")
    vAuxVx = kFwd.y * kNewUp.z - kNewUp.y * kFwd.z
    vAuxVy = kNewUp.x * kFwd.z - kFwd.x * kNewUp.z
    vAuxVz = kFwd.x * kNewUp.y - kNewUp.x * kFwd.y
    return vAuxVx, vAuxVy, vAuxVz


def MatrixDet(matrix):
    debug(__name__ + ", MatrixDet")
    secondRow = {"x": matrix[3], "y": matrix[4], "z": matrix[5]}
    ThirdRow = {"x": matrix[3], "y": matrix[4], "z": matrix[5]}
    vAuxVx, vAuxVy, vAuxVz = MatrixMult(secondRow, ThirdRow)
    return vAuxVx * matrix[0] + vAuxVy * matrix[1] + vAuxVz * matrix[2]
        
def findShipInstance(pShip):
        debug(__name__ + ", findShipInstance")
        pInstance = None
        try:
            if not pShip:
                return pInstance
            if FoundationTech.dShips.has_key(pShip.GetName()):
                pInstance = FoundationTech.dShips[pShip.GetName()]
        except:
            pass

        return pInstance

def CheckLOS(pObject1, pObject2, pObjectInBetween, pSet):
        debug(__name__ + ", CheckLOS")
        bBlockedLOS = 0

        # Get the proximity manager...
        pProxManager = pSet.GetProximityManager()

        if pProxManager:
                # Get a list of objects between pObject1 and pObject2
                kIter = pProxManager.GetLineIntersectObjects(pObject1.GetWorldLocation(), pObject2.GetWorldLocation(), 0)
                pObject = pProxManager.GetNextObject(kIter)
                while (pObject != None):
                        # Is this object the object we're looking for?
                        if pObject.GetObjID() == pObjectInBetween.GetObjID() and pObject.GetObjID() != pObject2.GetObjID() and pObject.GetObjID() != pObject1.GetObjID():
                                #print "Ok, not firing because parent ship is between us"
                                # Yep.  We're now true.
                                bBlockedLOS = 1
                                break
                        pObject = pProxManager.GetNextObject(kIter)
                pProxManager.EndObjectIteration(kIter)

        return bBlockedLOS

def WeaponSystemFiredStopAction(pShip, pSystem, pTarget=None):
        debug(__name__ + ", WeaponSystemFiredStopAction")
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "WeaponSystemFiredStopActionAux", pShip, pSystem, pTarget), 0.1) # 0.1 works
        pSeq.Play()

def WeaponSystemFiredStopActionAux(pAction, pShip, pSystem, pTarget):
       debug(__name__ + ", WeaponSystemFiredStopActionAux")
       pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
       if pShip:
           pTargetI =  App.ShipClass_GetObjectByID(None, pTarget.GetObjID())
           if pTargetI:
               pSystem.StopFiringAtTarget(pTargetI)
           else:
               pSystem.StopFiring()

       return 0

def WeaponFiredStopAction(pObject, pEvent):
        debug(__name__ + ", WeaponFiredStopAction")

        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "WeaponFiredStopActionAux", pObject, pEvent), 0.1)
        pSeq.Play()

def WeaponFiredStopActionAux(pAction, pObject, pEvent):
        debug(__name__ + ", WeaponFiredStopActionAux")
        WeaponFiredStop(pObject, pEvent)

def WeaponFiredStop(pObject, pEvent, stoppedFiring=None):
	debug(__name__ + ", WeaponFiredStop")

	#print "The pEvent destination of stopped fire is ", pEvent.GetDestination()

	pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
	pInstance = None
	if pShip:
		#print "Found ship: ", pShip.GetName()
		pInstance = findShipInstance(pShip)

        if pInstance:
		pInstanceDict = pInstance.__dict__
		if pInstanceDict.has_key("SG Anubis SuperWeapon Ray"):
			pWeaponFired = App.Weapon_Cast(pEvent.GetSource())
			if pWeaponFired == None:
				print "no weapon stopped fired obj..."
				pObject.CallNextHandler(pEvent)
				return

			pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pWeaponFired.GetTargetID()))
			if pTarget:
				pTarget = App.ShipClass_GetObjectByID(None, pTarget.GetObjID())
			if not pTarget:
				pTarget = pShip.GetTarget()
			if not pTarget:
				pObject.CallNextHandler(pEvent)
				return

			pParentFired = pWeaponFired.GetParentSubsystem()
			if pParentFired == None:
				print "no weapon stop-fire parent subsystem obj..."
				pObject.CallNextHandler(pEvent)
				return

			pPhaser = pShip.GetPhaserSystem()
			if pPhaser:
				weaponParentName = pParentFired.GetName()
				wpnSystem = App.WeaponSystem_Cast(pPhaser)
				if pPhaser.GetName() == weaponParentName:
					weaponName = pWeaponFired.GetName()
					if pInstanceDict["SG Anubis SuperWeapon Ray"].has_key("Beams") and len(pInstanceDict["SG Anubis SuperWeapon Ray"]["Beams"]) > 0:
						lBeamNames = pInstanceDict["SG Anubis SuperWeapon Ray"]["Beams"]		

						if not weaponName in lBeamNames:
							pObject.CallNextHandler(pEvent)
							return
					#else:
					#	print "SGAnubisSuperWeaponRay: I do not have beams key, I will assume all phasers have SG Anubis SuperWeapon Rays" 
					
					if pTarget:
						#wpnSystem.StopFiringAtTarget(pTarget)
						lookandUpdateSiblingTPhasers(wpnSystem, pShip, None, None, 1, 1)
						#wpnSystem.StopFiring()
                         

					wpnSystem.SetForceUpdate(1)
                                #else:
                                #        print "We have gone so far, what do you mean you don't have the system to fire???"
                        
        pObject.CallNextHandler(pEvent)


def WeaponFired(pObject, pEvent, stoppedFiring=None):
	debug(__name__ + ", WeaponFired")

	pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
	pInstance = None
	if pShip:
		pInstance = findShipInstance(pShip)

        if pInstance:
		pInstanceDict = pInstance.__dict__
		if pInstanceDict.has_key("SG Anubis SuperWeapon Ray"):
			pWeaponFired = App.Weapon_Cast(pEvent.GetSource())
			if pWeaponFired == None:
				print "no weapon stopped fired obj..."
				pObject.CallNextHandler(pEvent)
				return

			pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pWeaponFired.GetTargetID()))
			if pTarget:
				pTarget = App.ShipClass_GetObjectByID(None, pTarget.GetObjID())
			if not pTarget:
				pTarget = pShip.GetTarget()
			if not pTarget:
				pObject.CallNextHandler(pEvent)
				return

			pParentFired = pWeaponFired.GetParentSubsystem()
			if pParentFired == None:
				print "no weapon stop-fire parent subsystem obj..."
				pObject.CallNextHandler(pEvent)
				return

			pPhaser = pShip.GetPhaserSystem()
			if pPhaser:
				weaponParentName = pParentFired.GetName()
				wpnSystem = App.WeaponSystem_Cast(pPhaser)
				if wpnSystem and pPhaser.GetName() == weaponParentName:
					weaponName = pWeaponFired.GetName()
					if pInstanceDict["SG Anubis SuperWeapon Ray"].has_key("Beams") and len(pInstanceDict["SG Anubis SuperWeapon Ray"]["Beams"]) > 0:
						lBeamNames = pInstanceDict["SG Anubis SuperWeapon Ray"]["Beams"]		

						if not weaponName in lBeamNames:
							#print "SGAnubisSuperWeaponRay: cancelling, ship has SGOriBeamWeapon equipped but not for that beam..."
							pObject.CallNextHandler(pEvent)
							return
					#else:
					#	print "SGAnubisSuperWeaponRay: I do not have beams key, I will assume all phasers have SG Anubis SuperWeapon Rays" 

					numberShots = 3
					closestShips = None
					enemyShipList = MakeEnemyVisibleShipObjectList(pShip)
					if enemyShipList and len(enemyShipList) > 0: 
						closestShips = GetClosestEnemyShips(pTarget, enemyShipList, 1, pTarget.GetWorldLocation())

					#wpnSystem.StopFiringAtTarget(pTarget)
					#wpnSystem.StopFiring() # Safety check for strays due to multi-targeting

					wpnSystem.StartFiring(pTarget)

					if closestShips != None and len(closestShips) > 0:
						lookandUpdateSiblingTPhasers(wpnSystem, pShip, pTarget, closestShips[0], 0, 1, numberShots)
						wpnSystem.StartFiring(closestShips[0])
					
                                        #lookandUpdateSiblingTPhasers(wpnSystem, pShip, pTarget, None, 1, 1, numberShots)
                                        wpnSystem.SetForceUpdate(1)
                                #else:
                                #        print "We have gone so far, what do you mean you don't have the system to fire???"
                        
        pObject.CallNextHandler(pEvent)

#slightly modified MakeEnemyShipList from Mleo's FoundationTech, borrowed from AutoTargeting (as well as the function "GetClosestEnemyShips") and modified again
def DistanceCheck(pObject1, pObject2, alternateWorldLocation=None):
	if alternateWorldLocation != None:
		vDifference = alternateWorldLocation
	else:
		vDifference = pObject1.GetWorldLocation()
	vDifference.Subtract(pObject2.GetWorldLocation())

	return vDifference.Length()

def MakeEnemyVisibleShipObjectList(pShip):
	return MakeTeamVisibleShipObjectList(pShip, 1)

def MakeFriendlyVisibleShipObjectList(pShip):
	return MakeTeamVisibleShipObjectList(pShip, 0)

def MakeTeamVisibleShipObjectList(pShip, enemy):
		
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pEnemies = pMission.GetEnemyGroup()
	pFriendlies = pMission.GetFriendlyGroup()
	pNeutrals = pMission.GetNeutralGroup()
	if pFriendlies.IsNameInGroup(pShip.GetName()):
		if enemy == 0:
			pFriendlyGroup = pFriendlies
		else:
			pFriendlyGroup = pEnemies
	elif pEnemies.IsNameInGroup(pShip.GetName()):
		if enemy == 0:
			pFriendlyGroup = pEnemies
		else:
			pFriendlyGroup = pFriendlies
	else:
		pFriendlyGroup = pNeutrals
	lFriendlyShips = []
	if pFriendlyGroup != None:
		pSet = pShip.GetContainingSet()
		if pSet:
			ObjTuple = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)
			if len(ObjTuple):
				for i in ObjTuple:
					pObj = App.ShipClass_Cast(i)
					if pObj:			
						lFriendlyShips.append(pObj)

	return lFriendlyShips

def GetClosestEnemyShips(pShip, pEnemyList, iNumShips, alternateWorldLocation=None):
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	
	try:
		if pEnemyList[pEnemyList.index(pShip)]:
			pEnemyList.remove(pShip)
	except:
		pass
	
	#now to the real deal
	EnemyDistDict = {}
	for pEnemyShip in pEnemyList:
		#Define the distance and check it after checking if pShip is cloaked
		pEnemyShipCh = App.ShipClass_GetObjectByID(None, pEnemyShip.GetObjID())
		if pEnemyShip and not pEnemyShip.IsDead() and not pEnemyShip.IsDying() and not pEnemyShip.IsCloaked():
			fDistance = DistanceCheck(pShip, pEnemyShip, alternateWorldLocation)
			if 0 < fDistance:
				EnemyDistDict[fDistance] = pEnemyShip
	lDistances = EnemyDistDict.keys()
	lDistances.sort()
	iDistAmount = len(lDistances)
	lRet = []
	if iDistAmount > 0:
		if iNumShips <= iDistAmount:
			for i in range(iNumShips):
				 lRet.append(  EnemyDistDict[ lDistances[i] ]  )
		elif iNumShips > iDistAmount:
			for i in range(  iNumShips - (iNumShips - iDistAmount)  ):
				 lRet.append(  EnemyDistDict[ lDistances[i] ]  )
	return lRet

def lookandUpdateSiblingTPhasers(wpnSystem, pShip, pTurret, pTarget=None, discharge=0, phaser=1, numberShots = 2):
	debug(__name__ + ", lookandUpdateSiblingTPhasers")

	numberOfShotShips = []
	wpnSystemButPhaser = App.PhaserSystem_Cast(wpnSystem)
	itsTractor = 0
	if not wpnSystemButPhaser:
		itsTractor = 1
		wpnSystemButPhaser = App.TractorBeamSystem_Cast(wpnSystem)

	pShipNode = pShip.GetNiObject()
	pTargetNode = None
	pTargetLoc = None
	pTurretLoc = None
	pTurretRad = None
	pVec = None
	if pTarget:
		pTargetNode = pTarget.GetNiObject()
		pTargetLoc = pTarget.GetWorldLocation()

	if pTurret:
		pTurretLoc = pTurret.GetWorldLocation()
		pTurretRad = pTurret.GetRadius()

	if pTarget and pTurret:
		pVec = pTarget.GetWorldLocation()
		pVec.Subtract(pTurretLoc)
		pVec.Unitize()
		pVec.Scale(pTurretRad + 0.1)

	systemsToChoose = {}

	for i in range(wpnSystem.GetNumChildSubsystems()):
		pChild = wpnSystem.GetChildSubsystem(i)
		if (pChild != None):
			newName = pChild.GetName() + " T"
			systemsToChoose[newName] = [pChild, None]

	lTurretSys = systemsToChoose.keys()

	# We are only interested on phasers or tractors, we can do this even faster
	pEnergyWeaponSubsystem = None
	if phaser:
		pEnergyWeaponSubsystem = pShip.GetPhaserSystem()
	else:
		pEnergyWeaponSubsystem = pShip.GetTractorBeamSystem()

	if pEnergyWeaponSubsystem:
		for i in range(pEnergyWeaponSubsystem.GetNumChildSubsystems()):
			pChildM = pEnergyWeaponSubsystem.GetChildSubsystem(i)
			if pChildM.GetName() in lTurretSys: # Future TO-DO maybe add something so only 1 of the beams move? and pChildM.GetName() == weaponFired.GetName + " T":
				systemsToChoose[pChildM.GetName()][-1] = pChildM

	for i in lTurretSys:
		if systemsToChoose[i][-1] != None:
			subsystemProperty = systemsToChoose[i][-1].GetProperty()
			if pTurret and pTarget:
				childPos = pTurret.GetWorldLocation()
				childPos.Add(pVec)
				newPosition = App.TGModelUtils_WorldToLocalPoint(pShipNode, childPos)

				oldPosition = subsystemProperty.GetPosition()
				subsystemProperty.SetPosition(newPosition.x/100.0, newPosition.y/100.0, newPosition.z/100.0)
			#else:
			#	print "setting beam location to center of the ship ", systemsToChoose[i][-1].GetName()
			#	subsystemProperty.SetPosition(0.0, 0.0, 0.0)


				
			if not itsTractor and discharge != 2:
				parentSiblingBank = App.EnergyWeaponProperty_Cast(subsystemProperty)
				if discharge:
					parentSiblingBank.SetMaxCharge(-abs(parentSiblingBank.GetMaxCharge()))
				else:
					parentSiblingBank.SetMaxCharge(abs(parentSiblingBank.GetMaxCharge()))

def DeleteObjectFromSet(pSet, sObjectName):
        if not MissionLib.GetShip(sObjectName, None, 1):
                return
        pSet.DeleteObjectFromSet(sObjectName)
        
        # send clients to remove this object
        if App.g_kUtopiaModule.IsMultiplayer():
                # Now send a message to everybody else that the score was updated.
                # allocate the message.
                pMessage = App.TGMessage_Create()
                pMessage.SetGuaranteed(1)                # Yes, this is a guaranteed packet
                        
                # Setup the stream.
                kStream = App.TGBufferStream()                # Allocate a local buffer stream.
                kStream.OpenBuffer(256)                                # Open the buffer stream with a 256 byte buffer.
        
                # Write relevant data to the stream.
                # First write message type.
                kStream.WriteChar(chr(REMOVE_POINTER_FROM_SET))

                # Write the name of killed ship
                for i in range(len(sObjectName)):
                        kStream.WriteChar(sObjectName[i])
                # set the last char:
                kStream.WriteChar('\0')

                # Okay, now set the data from the buffer stream to the message
                pMessage.SetDataFromStream(kStream)

                # Send the message to everybody but me.  Use the NoMe group, which
                # is set up by the multiplayer game.
                pNetwork = App.g_kUtopiaModule.GetNetwork()
                if not App.IsNull(pNetwork):
                        if App.g_kUtopiaModule.IsHost():
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                        else:
                                pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

                # We're done.  Close the buffer.
                kStream.CloseBuffer()
        return 0


def MultiPlayerEnableCollisionWith(pObject1, pObject2, CollisionOnOff):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", MultiPlayerEnableCollisionWith")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(NO_COLLISION_MESSAGE))
        
        # send Message
        kStream.WriteInt(pObject1.GetObjID())
        kStream.WriteInt(pObject2.GetObjID())
        kStream.WriteInt(CollisionOnOff)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def MPSentReplaceModelMessage(pShip, sNewShipScript):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", MPSentReplaceModelMessage")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(REPLACE_MODEL_MSG))

        try:
                from Multiplayer.Episode.Mission4.Mission4 import dReplaceModel
                dReplaceModel[pShip.GetObjID()] = sNewShipScript
        except ImportError:
                pass

        # send Message
        kStream.WriteInt(pShip.GetObjID())
        iLen = len(sNewShipScript)
        kStream.WriteShort(iLen)
        kStream.Write(sNewShipScript, iLen)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def mp_send_settargetable(iShipID, iMode):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", mp_send_settargetable")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(SET_TARGETABLE_MSG))

        # send Message
        kStream.WriteInt(iShipID)
        kStream.WriteInt(iMode)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()
