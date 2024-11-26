"""
#         Starcraft Defensive Matrix
#         30th April 2024
#         Based strongly on Shields.py by the FoundationTech team (and QuickBattleAddon.corboniteReflector() in Apollo's Advanced Technologies) and Turrets.py by Alex SL Gato, and based on SubModels by USS Defiant and their team.
#################################################################################################################
# This tech gives a ship a Defensive Matrix like on Starcraft.
# Please notice that for simplicity, the Smartcast part only takes into account Hull and Warp Core conditions, in order to make it activate for lesser damage or no damage at all, adjust the primary hull disabled percentage.
# TO-DO update these intructions
# "MatrixFile": optional value, do not include to leave "StarcraftDefensiveMatrix" as default
# "MatrixScale": multiplier scale value. 0.1 with "StarcraftDefensiveMatrix" is a sphere of size equal to a Minotaur-class battlecruiser from Starcraft II. Smaller value, reduced scale.
# "PowerDrain": TBD (TO-DO supposed to be resource-intensive, if there is not enough energy then it will not activate the shield).
# "Duration": time the shield will remain active, in seconds. Default is 20.
# "Cooldown": time after deactvation before it can be reactivated again, in seconds. Default is 20.
# "Smartcast": used to decide when to activate a shield. A value of 1.5 will make it so the shield will activate is the hull or warp core are at 1.5 times their disabled value, or if the hull will be at less than 50% if the weapon 
# that has been fired hits the ship. Default is 1.5
# "Starcraft I": on Starcraft I, Defensive Matrixes were less advanced, and had a decent change ("Percentage", default 75 (75%)) of dealing leakage damage ("Leakage", default 0.5 dmg). Remove the field on your ship instance to use
# SCII mechanics.

#Sample Setup:

Foundation.ShipDef.Sovereign.dTechs = {
	"Starcraft Defensive Matrix": {
		"MatrixFile": "StarcraftDefensiveMatrix"
		"MatrixScale": 0.1,
		"PowerDrain": 100,
		"Duration": 20,
		"Cooldown": 20,
		"Smartcast": 1.5,
		"Starcraft I": {
			"Percentage": 75,
			"Leakage": 0.5
		}
	}
}



"""

#################################################################################################################
from bcdebug import debug

import App
import FoundationTech
import loadspacehelper
import MissionLib

import traceback

#################################################################################################################
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.57",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#################################################################################################################

# This should be the prime example of a special yield weapon defined according to Foundation Technologies.

# Global values
defaultMatrixScale = 0.1
defaultPowerDrain = 100.0
defaultDuration = 20.0
defaultCooldown = 20.0
defaultSmartcast = 1.5
defaultSCIperc = 75
defaultLeakage = 0.5


REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209
DEFENSIVE_MATRIX_DEACTIVATE = App.UtopiaModule_GetNextEventType()

def findShipInstance(pShip):
	pInstance = None
	try:
		pInstance = FoundationTech.dShips[pShip.GetName()]
		if pInstance == None:
			print "After looking, no tech pInstance for ship:", pShip.GetName(), "How odd..."
		
	except:
		pass

	return pInstance

class DefensiveMatrix(FoundationTech.TechDef):
	def __init__(self, name):
		debug(__name__ + ", Initiated AutomatedDestroyedSystemRepair counter")
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.RemoveBroadcastHandler(DEFENSIVE_MATRIX_DEACTIVATE, self.pEventHandler, "TurnDefensiveMatrixOff")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(DEFENSIVE_MATRIX_DEACTIVATE, self.pEventHandler, "TurnDefensiveMatrixOff")
		# The following are for "smartcast"
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_FIRED, self.pEventHandler, "OneWeaponFired")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_WEAPON_FIRED, self.pEventHandler, "OneWeaponFired")

	def OneWeaponFired(self, pEvent):
		pWeaponFired = App.Weapon_Cast(pEvent.GetSource())
		if pWeaponFired:
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pWeaponFired.GetTargetID()))
			if pShip:
				pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
			if pShip:
				#print "Alright, target found", pShip.GetName()
				pShields = pShip.GetShields()
				if pShields:
					pInstance = findShipInstance(pShip)
					if pInstance:
						instanceDict = pInstance.__dict__
						#print "pInstance dict: ", instanceDict
						if instanceDict.has_key("Starcraft Defensive Matrix") and instanceDict["Starcraft Defensive Matrix Active"] == 0:
							#print "Alright, shields inactive"
							pHull = pShip.GetHull()
							pCore = pShip.GetPowerSubsystem()

							fDamage = 0
							pWpTrpTube = App.TorpedoTube_Cast(pWeaponFired)
							if pWpTrpTube and hasattr(pWpTrpTube, "ReloadTorpedo"): # We know it's a torpedo!
								#print "It was a torp tube"
								pParentFired = pWeaponFired.GetParentSubsystem()
								if pParentFired:
									#print "Now we get the damage the current torpedo deals, plus its damage radius factor"
									pParentFiredCasted = App.TorpedoSystem_Cast(pParentFired)
									ammoType = pParentFiredCasted.GetCurrentAmmoType().GetTorpedoScript()
									try: # Not 100% reliable as some scripts may have the damage set inside the "Create()" instead of a separate function, but for MOST cases, it is the latter
										pTorp = __import__(ammoType)
										if hasattr(pTorp, "GetDamage"):
											fDamage = pTorp.GetDamage()
										else:
											# No chances, we take this as a danger that needs to be addressed
											if pHull:
												fDamage = pHull.GetConditionPercentage()
											else:
												fDamage = 600.0

										if hasattr(pTorp, "GetDamageRadiusFactor"): # This one is rarely on a separate function, but is not a bad option to check
											if pTorp.GetDamageRadiusFactor() > 0.1:
												fDamage = fDamage * 10 * pTorp.GetDamageRadiusFactor()
									
									except: # No chances, we take this as a danger that needs to be addressed
										if pHull:
											fDamage = pHull.GetConditionPercentage()
										else:
											fDamage = 600.0
									
							else:
								#print "I guess it is not a torpedo"

								pthisPhaser = App.PulseWeaponProperty_Cast(pWeaponFired.GetProperty())
								if pthisPhaser and hasattr(pthisPhaser, "GetModuleName"): # it's a disruptor!
									#print "It's a disruptor"
									ammoType = pthisPhaser.GetModuleName()
									try: # Not 100% reliable as some scripts may have the damage set inside the "Create()" instead of a separate function, but for MOST cases, it is the latter
										pTorp = __import__(ammoType)
										if hasattr(pTorp, "GetDamage"):
											fDamage = pTorp.GetDamage()
										else:
											# No chances, we take this as a danger that needs to be addressed
											if pHull:
												fDamage = pHull.GetConditionPercentage()
											else:
												fDamage = 600.0

										if hasattr(pTorp, "GetDamageRadiusFactor"): # This one is rarely on a separate function, but is not a bad option to check
											if pTorp.GetDamageRadiusFactor() > 0.1:
												fDamage = fDamage * 10 * pTorp.GetDamageRadiusFactor()
									
									except: # No chances, we take this as a danger that needs to be addressed
										if pHull:
											fDamage = pHull.GetConditionPercentage()
										else:
											fDamage = 600.0

								else:
									fDamage = App.EnergyWeapon_Cast(pWeaponFired).GetMaxDamage() # phasers and tractors
									pthisPhaser = App.PhaserProperty_Cast(pWeaponFired.GetProperty()) # we don't care about tractor damage radious factor
									if pthisPhaser and hasattr(pthisPhaser, "GetDamageRadiusFactor"):
										dmgRfactor = pthisPhaser.GetDamageRadiusFactor()
										if dmgRfactor > 0.1:
											fDamage = fDamage * dmgRfactor

							#print "fDamage is ", fDamage

							smartcastmult = instanceDict["Starcraft Defensive Matrix"]["Smartcast"]
							if (pHull and (pHull.GetConditionPercentage() < pHull.GetDisabledPercentage() * smartcastmult or (pHull.GetConditionPercentage() - fDamage/pHull.GetMaxCondition() < (smartcastmult -1.0) ) or pHull.GetConditionPercentage() < (smartcastmult - 1.0))) or (pCore and (pCore.GetConditionPercentage() < pCore.GetDisabledPercentage() * smartcastmult or pCore.GetCondition() < fDamage * smartcastmult or pCore.GetConditionPercentage() < (smartcastmult - 1.0))):
								#print "Detected dangerous incoming weapon, activating Defensive Matrix"
								for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
									pShields.SetCurShields(shieldDir, pShields.GetMaxShields(shieldDir))
								pShields.TurnOn()

	def TurnDefensiveMatrixOff(self, pEvent):
		#print "Deactivating defensive matrix"
		pShipID = pEvent.GetInt()
		if pShipID:
			pShip = App.ShipClass_GetObjectByID(None, pShipID)
			if pShip:
				pShields = pShip.GetShields()
				if pShields:
					pShields.TurnOff()
					for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
						pShields.SetCurShields(shieldDir, pShields.GetMaxShields(shieldDir))

	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")

		pShields = pShip.GetShields()

		if pShields and pInstance:
			instanceDict = pInstance.__dict__
			if instanceDict.has_key("Starcraft Defensive Matrix") and instanceDict.has_key("Starcraft Defensive Matrix Active") and instanceDict["Starcraft Defensive Matrix Active"] == 0:
				pHull = pShip.GetHull()
				pCore = pShip.GetPowerSubsystem()
				smartcastmult = instanceDict["Starcraft Defensive Matrix"]["Smartcast"]
				if (pHull and (pHull.GetConditionPercentage() < pHull.GetDisabledPercentage() * smartcastmult or pHull.GetConditionPercentage() < (smartcastmult - 1.0))) or (pCore and (pCore.GetConditionPercentage() < pCore.GetDisabledPercentage() * smartcastmult or pCore.GetConditionPercentage() < (smartcastmult - 1.0))):
					for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
						pShields.SetCurShields(shieldDir, pShields.GetMaxShields(shieldDir))
					pShields.TurnOn()

			if not pShields.IsDisabled():

				# Now we redistribute, we make it so all shield are damaged equally, normal damage + 5
				fDamage = 5 * pEvent.GetDamage()

				pShieldTotal = -fDamage
				for shieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
					pShieldTotal = pShieldTotal+pShields.GetCurShields(shieldDir)

				for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
					pShields.SetCurShields(shieldDir,pShieldTotal/6.0)  		#Redistribute shields equally

				if (not pEvent.IsHullHit()) and instanceDict.has_key("Starcraft Defensive Matrix") and instanceDict["Starcraft Defensive Matrix"].has_key("Starcraft I") and instanceDict["Starcraft Defensive Matrix"]["Starcraft I"].has_key("Percentage") and instanceDict["Starcraft Defensive Matrix"]["Starcraft I"]["Percentage"] > 0.0:
					pHull = pShip.GetHull()
                        	        if pHull and App.g_kSystemWrapper.GetRandomNumber(100) <= instanceDict["Starcraft Defensive Matrix"]["Starcraft I"]["Percentage"]:
						global defaultLeakage
						leakDamage = defaultLeakage
						if instanceDict["Starcraft Defensive Matrix"]["Starcraft I"].has_key("Leakage"):
							leakDamage = instanceDict["Starcraft Defensive Matrix"]["Starcraft I"]["Leakage"]
						pHull.SetCondition(pHull.GetCondition()-leakDamage)

				if pShields.GetShieldPercentage() < 0.25: # If our shields are below 25%, we deactivate our shields, they are too weak to be of use, we disable them and let the shields recharge
					pShields.TurnOff()

	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnBeamDefense")
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		return self.OnDefense(pShip, pInstance, oYield, pEvent)


	# TODO:  Make this an activated technology
	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTechs.append(self)
		pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
		pInstance.lPulseDefense.insert(0, self)
		pInstance.lBeamDefense.insert(0, self)

	def AttachDefensiveMatrix(self, pShip, pInstance):
		debug(__name__ + ", AttachDefensiveMatrix")

		pShipID = pShip.GetObjID()
		pShip = App.ShipClass_GetObjectByID(None, pShipID)
		if not pShip:
			return 0

		pSet = pShip.GetContainingSet()
		if not pSet:
			return 0

		instanceDict = pInstance.__dict__

		if not hasattr(pInstance, "StarcraftDefensiveMatrixShield"):
			pInstance.StarcraftDefensiveMatrixShield = []
		DMList = pInstance.StarcraftDefensiveMatrixShield

		sNamePrefix = "DM" + str(pShip.GetObjID()) + "_"

		# To avoid AI and multiple processes from constantly trying to avoid the shield
		pProxManager = pSet.GetProximityManager()

		sFile = "StarcraftDefensiveMatrix"
		if instanceDict["Starcraft Defensive Matrix"].has_key("MatrixFile"):
			sFile = instanceDict["Starcraft Defensive Matrix"]["MatrixFile"]

		sShipName = sNamePrefix + "DM"

		pSubShip = MissionLib.GetShip(sShipName, None, 1)

		if not pSubShip:
			for potpShip in DMList:
				if potpShip and hasattr(potpShip, "GetObjID"):
					piMatrix = App.ShipClass_GetObjectByID(None, lList[0].GetObjID())
					if piMatrix and potpShip.GetName() == sShipName:
						pSubShip = piMatrix
			if not pSubShip:
				pSubShip = loadspacehelper.CreateShip(sFile, pSet, sShipName, "")

		if not pSubShip:
			print "StarcraftDefensiveMatrix: could not find the model/ship. Skipping visuals..."
			return
		DMList.append(pSubShip)

		global defaultMatrixScale
		shipScale = defaultMatrixScale
		if instanceDict["Starcraft Defensive Matrix"].has_key("MatrixScale") and instanceDict["Starcraft Defensive Matrix"]["MatrixScale"] > 0.0:
			shipScale = instanceDict["Starcraft Defensive Matrix"]["MatrixScale"]


		# set current positions
		pSubShip.SetTranslateXYZ(0.0, 0.0, 0.0)
		pSubShip.UpdateNodeOnly()

		# set size
		pSubShip.SetScale(shipScale)
		pSubShip.UpdateNodeOnly()

		pSubShip.SetUsePhysics(0)
		pSubShip.SetTargetable(0)
		mp_send_settargetable(pSubShip.GetObjID(), 0)
		pSubShip.SetInvincible(1)
		pSubShip.SetHurtable(0)
		pSubShip.SetCollisionsOn(0)
		pSubShip.GetShipProperty().SetMass(0.000001)
		pSubShip.GetShipProperty().SetRotationalInertia(1.0e+25)
		pSubShip.GetShipProperty().SetStationary(1)
		pSubShip.SetHailable(0)
		pSubShip.SetScannable(0)
		if pSubShip.GetShields():
			pSubShip.GetShields().TurnOff()

		pShip.EnableCollisionsWith(pSubShip, 0)
		pSubShip.EnableCollisionsWith(pShip, 0)
		MultiPlayerEnableCollisionWith(pShip, pSubShip, 0)
		MultiPlayerEnableCollisionWith(pSubShip, pShip, 0)

		# Ensure the shield is on a group AI does not fire normally upon (pTractors)
		pMission        = MissionLib.GetMission()
		pFriendlies     = None
		pEnemies        = None
		pNeutrals       = None
		pTractors       = None
		if pMission:
		        pFriendlies     = pMission.GetFriendlyGroup() 
		        pEnemies        = pMission.GetEnemyGroup() 
		        pNeutrals       = pMission.GetNeutralGroup()
		        pTractors       = pMission.GetTractorGroup()

			pFriendlies.RemoveName(pSubShip.GetName())
			pEnemies.RemoveName(pSubShip.GetName())
			pNeutrals.RemoveName(pSubShip.GetName())
			pTractors.RemoveName(pSubShip.GetName())
			pTractors.AddName(pSubShip.GetName())


		if pProxManager:
			pProxManager.RemoveObject(pSubShip)

		pSubShip.UpdateNodeOnly()
		pShip.AttachObject(pSubShip)



	def DetachDefensiveMatrix(self, pShip, pInstance):
		debug(__name__ + ", DetachDefensiveMatrix")

		pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
		if pShip and hasattr(pInstance, "StarcraftDefensiveMatrixShield"):
			for pSubShip in pInstance.StarcraftDefensiveMatrixShield:
				pSet = pSubShip.GetContainingSet()
				pShip.DetachObject(pSubShip)
				DeleteObjectFromSet(pSet, pSubShip.GetName())
			del pInstance.StarcraftDefensiveMatrixShield

	def AttachShip(self, pShip, pInstance):	
		debug(__name__ + ", AttachShip")
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
			pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")

			instanceDict = pInstance.__dict__

			pShields = pShip.GetShields()
			if pShields:
				pShields.TurnOff()
				# because
				instanceDict["Starcraft Defensive Matrix Active"] = 0
			
			if not instanceDict["Starcraft Defensive Matrix"].has_key("MatrixScale"):
				global defaultMatrixScale
				instanceDict["Starcraft Defensive Matrix"]["MatrixScale"] = defaultMatrixScale

			if not instanceDict["Starcraft Defensive Matrix"].has_key("PowerDrain"):
				global defaultPowerDrain
				instanceDict["Starcraft Defensive Matrix"]["PowerDrain"] = defaultPowerDrain

			if not instanceDict["Starcraft Defensive Matrix"].has_key("Duration"):
				global defaultDuration
				instanceDict["Starcraft Defensive Matrix"]["Duration"] = defaultDuration

			if not instanceDict["Starcraft Defensive Matrix"].has_key("Cooldown"):
				global defaultCooldown
				instanceDict["Starcraft Defensive Matrix"]["Cooldown"] = defaultCooldown

			if not instanceDict["Starcraft Defensive Matrix"].has_key("Smartcast"):
				global defaultSmartcast
				instanceDict["Starcraft Defensive Matrix"]["Smartcast"] = defaultSmartcast

			if instanceDict["Starcraft Defensive Matrix"].has_key("Starcraft I"):

				if not instanceDict["Starcraft Defensive Matrix"]["Starcraft I"].has_key("Percentage"):
					global defaultSCIperc
					instanceDict["Starcraft Defensive Matrix"]["Starcraft I"]["Percentage"] = defaultSCIperc

				if not instanceDict["Starcraft Defensive Matrix"]["Starcraft I"].has_key("Leakage"):
					global defaultLeakage
					instanceDict["Starcraft Defensive Matrix"]["Starcraft I"]["Leakage"] = defaultLeakage

		#print 'Attaching Starcraft II Terran Defensive Matrix to', pInstance, instanceDict

	def DetachShip(self, pShip, pInstance):

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
			if pInstance.__dict__.has_key("Starcraft Defensive Matrix TimeDeactivate"):
				App.g_kTimerManager.DeleteTimer(pInstance.__dict__["Starcraft Defensive Matrix TimeDeactivate"].GetObjID())
			if pInstance.__dict__.has_key("Starcraft Defensive Matrix TimeDeactivate"):
				del pInstance.__dict__["Starcraft Defensive Matrix TimeDeactivate"]
			if pInstance.__dict__.has_key("Starcraft Defensive Matrix TimeCooldown"):
				del pInstance.__dict__["Starcraft Defensive Matrix TimeCooldown"]
			if pInstance.__dict__.has_key("Starcraft Defensive Matrix Active"):
				del pInstance.__dict__["Starcraft Defensive Matrix Active"]
		else:
			#print "StarcraftDefensiveMatrix Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
			pass

		if pInstance.__dict__.has_key("Starcraft Defensive Matrix TimeDeactivate"):
			del pInstance.__dict__["Starcraft Defensive Matrix TimeDeactivate"]
		#pInstance.lTechs.remove(self) # DO NOT INCLUDE THIS ON DETACHSHIP, LET THE DEFAULT DETACH DO ITS JOB!

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()
    
oDefensiveMatrix = DefensiveMatrix('Starcraft Defensive Matrix')

# called when a ship changes Power of one of its subsystems
# cause this is possibly also an alert event
def SubsystemStateChanged(pObject, pEvent):
	debug(__name__ + ", SubsystemStateChanged")

	if pObject == None:
		return

	pShipID = pObject.GetObjID()
	pShip = App.ShipClass_GetObjectByID(None, pShipID)
	if not pShip:
		return

	if pEvent == None:
		pObject.CallNextHandler(pEvent)
		return

        pSubsystem = pEvent.GetSource()

	if not pSubsystem:
		pObject.CallNextHandler(pEvent)
		return

        if pSubsystem.IsTypeOf(App.CT_SHIELD_SUBSYSTEM):
		wpnActiveState = 0
		if hasattr(pEvent, "GetBool"):
			wpnActiveState = pEvent.GetBool()
			pShields = pShip.GetShields()
			if pShields:
				pInstance = findShipInstance(pShip)
				if pInstance:
					instanceDict = pInstance.__dict__
					if instanceDict.has_key("Starcraft Defensive Matrix"):
						if wpnActiveState != instanceDict["Starcraft Defensive Matrix Active"]: # Means shields have changed
							currentTime = App.g_kUtopiaModule.GetGameTime()
							if wpnActiveState == 0: # Shields have been deactivated:
								instanceDict["Starcraft Defensive Matrix Active"] = 0
								delay = instanceDict["Starcraft Defensive Matrix"]["Cooldown"]
								instanceDict["Starcraft Defensive Matrix TimeCooldown"] = currentTime + delay

								oDefensiveMatrix.DetachDefensiveMatrix(pShip, pInstance)

								# Remove deactivation timers
								if instanceDict.has_key("Starcraft Defensive Matrix TimeDeactivate"):
									App.g_kTimerManager.DeleteTimer(instanceDict["Starcraft Defensive Matrix TimeDeactivate"].GetObjID())
									del instanceDict["Starcraft Defensive Matrix TimeDeactivate"]

							else: # Shields have been activated
								if instanceDict.has_key("Starcraft Defensive Matrix TimeCooldown") and instanceDict["Starcraft Defensive Matrix TimeCooldown"] > currentTime:
									# We are on cooldown, cannot activate shields:
									pShields.TurnOff()
									pObject.CallNextHandler(pEvent)
									return

								instanceDict["Starcraft Defensive Matrix Active"] = 1
								global DEFENSIVE_MATRIX_DEACTIVATE

								pEvent2 = App.TGIntEvent_Create()
								pEvent2.SetEventType(DEFENSIVE_MATRIX_DEACTIVATE)
								pEvent2.SetSource(pEvent.GetSource()) # We could fetch the parent from the subsystem pSubsystem.GetParentShip()
								pEvent2.SetDestination(pEvent.GetDestination())
								pEvent2.SetInt(int(pShipID)) # Or even better, fetch it from the parent ship ID

								delay = instanceDict["Starcraft Defensive Matrix"]["Duration"]

								pTimer = App.TGTimer_Create()
								pTimer.SetTimerStart( currentTime + delay )
								pTimer.SetDelay(0)
								pTimer.SetDuration(0)
								pTimer.SetEvent(pEvent2)
								App.g_kTimerManager.AddTimer(pTimer)

								instanceDict["Starcraft Defensive Matrix TimeDeactivate"] = pTimer

								oDefensiveMatrix.AttachDefensiveMatrix(pShip, pInstance)

								#print "Attempt successfull, instanceDict is ", instanceDict
					


	pObject.CallNextHandler(pEvent)
	return



# From Turrets.py, and SubModels.py
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

