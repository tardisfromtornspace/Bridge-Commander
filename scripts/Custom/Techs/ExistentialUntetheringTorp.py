# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         ExistentialUntetheringTorp
#         11th April 2024
#         by Alex SL Gato, based on SGHoppingTorpedo tech, which was most likely based on PhasedTorp and other ftb team techs, and a function from AlteranteSubModelFTL by Alex SL Gato (with the function itself being probably from a mod by Defiant).
#         TO-DO THIS IS A STUB, SO LATER ON GREYSTAR CAN MODIFY AT LEISURE
#         TO-DO ALSO I RECOMMEND THAT IF CURRENT IMMUNITY CHECK IMPLEMENTATION IS USED, TO FUSE THE TECHS INTO ONE SINCE ONLY SHIPS USE THE IMMUNITY
#################################################################################################################
# This tech makes ships that have been hit with certain projectiles vanish from reality at full power, and bypass shields at other levels of power.
# Use of this tech:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
"""
def GetExistentialUntetheringTorpPercentage():
	return 1.0 # returns the percentage of damage the son projectile will deal - i.e 1-0 = 100% of the damage the parent would do

def GetExistentialUntetheringYieldLevel():
	return 1.0 # returns the values of yield immunity grade - TO-DO GREYSTAR EXPLAIN THIS BETTER, PLEASE

try:
	modExistentialUntetheringTorp = __import__("Custom.Techs.ExistentialUntetheringTorp")
	if(modExistentialUntetheringTorp):
		modExistentialUntetheringTorp.oExistentialUntetheringTorp.AddTorpedo(__name__)

except:
	print "Existential Untethering Tech script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an immunity or resistance list immunity list, just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev and the proper fields accordingly
# - "Yield Level": per greystar's request, a leveling system has been added o this tech. If a ship's Yield Level is greater than a Projectile's ExistentialUntetheringYieldLevel, the ships is immune. If they are lesser than, then the ship will receive full effects. If they match, the multiplier value will come in effect.
# - "Multiplier": when a projectile with Existential Untethering and and this resistance have the same "Yield Level", torps deal phase-through damage, bypassing shields. This value indicates how much phase damage is dealt, in such a way that the final damage will be the daamge of the torpedo multiplied by the GetExistentialUntetheringTorpPercentage of the projectile, and this multiplier.
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Existential Untethering Resistance": {"Multiplier": 1.0, "Yield Level": 1},
}
"""

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.11",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

from bcdebug import debug
import traceback

import App

try:
	import Foundation
	import FoundationTech
	import MissionLib
	import Multiplayer.SpeciesToTorp

	#TO-DO FOR GREYSTAR, I DO NOT THINK THIS MODULE IS NEEDED, BUT CHECK JUST IN CASE --> from ftb.Tech.ATPFunctions import *
	from math import *

	g_DefaultPassMultiplier = 1.0 # Base phase-through percent damage a projectile will do - 1.0 means * 1.0 the damage of the parent projectile
	g_DefaultYieldValue = 0 # Apparently this level vs. a torpedo level determines if a ship is not immune, resistant or immune.
	g_defaultErrorDmg = 0.0 # Just for errors, if for some reason an event has no damage at all. This should be 0.
	g_TorpTechName = "Existential Untethering Torpedo"
	g_ResistanceTechName = "Existential Untethering Resistance"
	g_torpsNetTypeThatCanPhase = Multiplayer.SpeciesToTorp.PHASEDPLASMA # For the "torpedoes-going-through" issue

	def ConvertPointNiToTG(point):
		retval = App.TGPoint3()
		retval.SetXYZ(point.x, point.y, point.z)
		return retval

	def IsInList(item, list):
		for i in list:
			if item == i:
				return 1
		return 0

	def GetShipImmunityMultiplier(pInstance):
		debug(__name__ + ", OnProjectileDefense")	
		leMult = g_DefaultPassMultiplier
		leYiLvl = g_DefaultPassMultiplier
		if pInstance:
			pInstanceDict = pInstance.__dict__
			if pInstanceDict and pInstanceDict.has_key(g_ResistanceTechName):
				values = pInstanceDict[g_ResistanceTechName]
				if values != None:
					if pInstanceDict[g_ResistanceTechName].has_key("Multiplier"):
						leMult = pInstanceDict[g_ResistanceTechName]['Multiplier']
					if pInstanceDict[g_ResistanceTechName].has_key("Yield Level"):
						leYiLvl = pInstanceDict[g_ResistanceTechName]['Yield Level']
			
		return leMult, leYiLvl

	def accionDummy(self): # TO-DO ON THE OLD VERSION THIS WAS HERE - IT WAS SO LONG AGO I CANNOT REMEMBER WHAT IT WAS THAT YOU WANTED FOR IT, SO I'M LEAVING IT HERE
		pEnterSound = App.TGSound_Create("sfx/Weapons/ExistentialUntethering.wav", "ExistentialUntethering", 1)
		pEnterSound.SetSFX(0) 
		pEnterSound.SetInterface(1)

		App.g_kSoundManager.PlaySound("ExistentialUntethering")
		return 0

	def GetProjectileData(pTorp, pEvent):
		leMult = g_DefaultPassMultiplier	
		leYiLvl = g_DefaultYieldValue
		pDmg = g_defaultErrorDmg
		mod = None
		if pTorp and hasattr(pTorp, "GetModuleName"):
			mod = pTorp.GetModuleName()

		if mod != None:
			try:
				importedTorpInfo = __import__(mod)
			except:
				importedTorpInfo = None
				print "ExistentialUntetheringTorp ", __name__, " ERROR:"
				traceback.print_exc()

		if importedTorpInfo != None:
			if hasattr(importedTorpInfo, "GetExistentialUntetheringTorpPercentage"): # If this torp has special multipliers, then we use them
				leMult = importedTorpInfo.GetExistentialUntetheringTorpPercentage()
			if hasattr(importedTorpInfo, "GetExistentialUntetheringYieldLevel"):
				leYiLvl = importedTorpInfo.GetExistentialUntetheringYieldLevel()

		if pEvent and hasattr(pEvent, "GetDamage"):
			pDmg = pEvent.GetDamage() # We could import torp damage, but this is way better for any type of torp including those without GetDamage() and allows synergy with other techs if necessary (i.e. overcharging a torpedo or variable projectile yields)

		return leMult, leYield, pDmg, mod

	# From AlternateSubModelFTL, likely from SubModels by Defiant, but I've seen this function quite widespread.
	def DeleteObjectFromSet(pSet, sObjectName):
		if not MissionLib.GetShip(sObjectName, None, bAnySet = 1):
			return
		pSet.DeleteObjectFromSet(sObjectName)
	
		# send clients to remove this object
		if App.g_kUtopiaModule.IsMultiplayer():
			# Now send a message to everybody else that the score was updated.
			# allocate the message.
			pMessage = App.TGMessage_Create()
			pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
			
			# Setup the stream.
			kStream = App.TGBufferStream()		# Allocate a local buffer stream.
			kStream.OpenBuffer(256)				# Open the buffer stream with a 256 byte buffer.
	
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

	def FireTorpFromPointWithVectorAndNetType(kPoint, kVector, pcTorpScriptName, idTarget, pShipID, fSpeed, NetType=g_torpsNetTypeThatCanPhase, damage=0.1, dmgRd=0.15, hidden=0, detectCollison= None, TGOffset = None):

		# This is an slightly altered version of the original definition (MissionLib.py), to suit specific needs

		debug(__name__ + ", FireTorpFromPointWithVector")
		pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(idTarget))
		pSet = pTarget.GetContainingSet()
		if not pSet:
			return None

		# Create the torpedo.
		pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
		pTorp.SetDamageRadiusFactor(dmgRd)
		pTorp.SetDamage(damage)
		pTorp.SetNetType(NetType)
		pTorp.UpdateNodeOnly()

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))

		# Set up its target and target subsystem, if necessary.
		pTorp.SetTarget(idTarget)
		if not TGOffset and pShip:
			pTorp.SetTargetOffset(pShip.GetHull().GetPosition())
		else:
			pTorp.SetTargetOffset(TGOffset)
		pTorp.SetParent(pShipID)

		# Add the torpedo to the set, and place it at the specified placement.
		pSet.AddObjectToSet(pTorp, None)
		pTorp.UpdateNodeOnly()
		if hidden != 0:
			pTorp.SetHidden(1)
			pTorp.UpdateNodeOnly()

		# If there was a target, then orient the torpedo towards it.
		kTorpLocation = pTorp.GetWorldLocation()
		kTargetLocation = pTarget.GetWorldLocation()

		kTargetLocation.Subtract(kTorpLocation)
		kFwd = kTargetLocation
		kFwd.Unitize()
		kPerp = kFwd.Perpendicular()
		kPerp2 = App.TGPoint3()
		kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)
		pTorp.AlignToVectors(kFwd, kPerp2)
		pTorp.UpdateNodeOnly()

		if detectCollison != None: # We want to detect collision first
			pTorp.DetectCollision(detectCollison)
			pTorp.UpdateNodeOnly()

		# Give the torpedo an appropriate speed.
		kSpeed = CopyVector(kVector)
		kSpeed.Unitize()
		kSpeed.Scale(fSpeed)
		pTorp.SetVelocity(kSpeed)

		return pTorp
	

	class ExistentialUntetheringTorpTorp(FoundationTech.TechDef):

		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

		def IsDrainYield(self):
			debug(__name__ + ", IsDrainYield")
			return 0

		def IsPhaseYield(self):
			debug(__name__ + ", IsPhaseYield")
			return 0

		def IsExistentialUntetheringTorpYield(self):
			debug(__name__ + ", IsExistentialUntetheringTorpYield")
			return 0

		def OnYield(self, pShip, pInstance, pEvent, pTorp):

			if pShip and hasattr(pShip, "GetObjID"):
				pShipID = pShip.GetObjID()
				if pShipID:
					pShipHit = App.ShipClass_GetObjectByID(None, pShipID)
					if pShipHit and not pShipHit.IsDead():
						mySMult, mySLvl = GetShipImmunityMultiplier(pInstance)
						leMult, leYiLvl, pDmg, mod = GetProjectileData(pTorp, pEvent)
						if mySLvl < leYiLvl:
							print "TO-DO REMOVE FROM SET" # look for the remove ship function thing
							pSet = pShipHit.GetContainingSet()
							pSubName = pShipHit.GetName()
							if pSet and pSubName != None:
								DeleteObjectFromSet(pSet, pSubName)
								#TO-DO FOR GREYSTAR TWEAK THESE pShipHit.SetDeleteMe(1)
						elif mySLvl == leYiLvl and mySMult != 0 and leMult != 0 and pDmg != 0 and mod != None:
							finalHullDamage = pDmg * leMult * mySMult
							#TO-DO TRANSPHASIC TORP METHOD IS LIKE THIS. TORPEDO SHENANIGANS CAN SOMETIMES INTERFERE. IF YOU GET SOME DAMAGE PROBLEMS, CALL ME - Alex SL Gato.
							try:
								attackerID = App.NULL_ID
								try:
									attackerID = pTorp.GetParentID()
								except:
									attackerID = App.NULL_ID

								launchSpeed = __import__(mod).GetLaunchSpeed()

								pHitPoint = ConvertPointNiToTG(pTorp.GetWorldLocation())
								pVec = pTorp.GetVelocityTG()
								pVec.Scale(0.001)
								pHitPoint.Add(pVec)

								pTempTorp = FireTorpFromPointWithVectorAndNetType(pTorp.GetWorldLocation(), pVec, mod, pShipID, attackerID, launchSpeed, pTorp.GetNetType(), finalHullDamage, pTorp.GetDamageRadiusFactor(), 1, pShip)
								pTempTorp.SetLifetime(15.0)
								pTorp.SetLifetime(0.0)
								self.lFired.append(pTempTorp.GetObjID())
								pTempTorp.UpdateNodeOnly() 		
							except:
								print "ExistentialUntetheringTorp.ExistentialUntetheringTorpTorp ", __name__, " ERROR:"
								traceback.print_exc()

		def AddTorpedo(self, path):
			FoundationTech.dYields[path] = self

	oExistentialUntetheringTorp = ExistentialUntetheringTorpTorp(g_TorpTechName)

	class ExistentialUntetheringDef(FoundationTech.TechDef):
		pass # TO-DO CHECK THESE, GREYSTAR
		"""
		def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnTorpDefense")
			self.OnProjectileDefense(pShip, pInstance, pTorp, oYield, pEvent)

		def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnPulseDefense")
			self.OnProjectileDefense(pShip, pInstance, pTorp, oYield, pEvent)

		def OnProjectileDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnProjectileDefense")
			if oYield and hasattr(oYield, "IsExistentialUntetheringTorpYield") and oYield.IsExistentialUntetheringTorpYield() != 0:
				if GetProjectileImmunityMultiplier(pInstance) == 0:
					return 1

		def Attach(self, pInstance):
			pInstance.lTorpDefense.append(self)
			pInstance.lPulseDefense.append(self)
		"""

	oExistentialUntetheringResistance = ExistentialUntetheringDef(g_ResistanceTechName)

except:
	print "ExistentialUntethering Tech error:"
	traceback.print_exc()