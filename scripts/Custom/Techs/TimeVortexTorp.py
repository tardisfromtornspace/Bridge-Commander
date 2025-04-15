#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         TimeVortexTorp.py by Alex SL Gato
#         14th April 2025
#         Based slightly on USS Frontier's GalaxyCharts and several FTech scripts by the FoundationTechnologies team.
#         Also please note, this tech is meant to be used alongside the DoctorWhoTimeVortexDrive TravellingMethod and its associated systems (see the DoctorWhoTimeVortexDrive in-script readme), which are files that GalaxyCharts takes into account.
#################################################################################################################
# First of all, this tech depends on the DoctorWhoTimeVortexDrive TravellingMethod method mod, playing wihout it will probably make it useless.
# This torpedo will yeet the target to the Time Vortex unless that ship is immune to such projectiles.
# To make a projectile use this tech, add this at the bottom of your torpedo projectile file (Between the """ and """):
"""
try:
	modTimeVortexTorp = __import__("Custom.Techs.TimeVortexTorp")
	if(modTimeVortexTorp):
		modTimeVortexTorp.oTimeVortexTorp.AddTorpedo(__name__)
except:
	print "TimeVortex Torpedo script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"TimeVortex Torpedo Immune": 1
}
"""
#################################################################################################################
from bcdebug import debug
import traceback

import App

import Actions.MissionScriptActions
import Bridge.BridgeUtils
import Lib.LibEngineering
import loadspacehelper
import MissionLib
import nt
import string
import traceback

#################################################################################################################
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.4",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#################################################################################################################

global lImmunePhaseShips # Some ships immune to this blow
lImmunePhaseShips = (
                "Aeon",
                "BattleTardis",
                "Tardis",
                )


try:
	import Foundation
	import FoundationTech

	from math import *

	bOverflow = 0
	pTimeVortexSet = None
	pathToSet = "Custom.GalaxyCharts.TravelerSystems.DrWTimeVortexDriveTunnelTravelSet"
	pathToModule = "Custom.TravellingMethods.DoctorWhoTimeVortexDrive"

	sDestination = "Systems.Void.Void1" #pathToSet #"DrWTimeVortexDriveTunnelTravelSet"

	vDir = App.TGPoint3()
	vDir.SetXYZ(1.0, 0.0, 0.0)
	vDir.Unitize()
	vUp = App.TGPoint3()
	vUp.SetXYZ(0.0, 1.0, 0.0)
	vUp.Unitize()

	class TimeVortexTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			debug(__name__ + ", __init__")
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

			self.pEventHandler = App.TGPythonInstanceWrapper()
			self.pEventHandler.SetPyWrapper(self)

			self.pTimeVortexSet = None
			self.pSet = None

		def IsTimeVortexYield(self):
			debug(__name__ + ", IsTimeVortexYield")
			return 1

		def PhaseYield(self):
			debug(__name__ + ", PhaseYield")
			return 0

		def IsPhaseYield(self):
			debug(__name__ + ", IsPhaseYield")
			return 0

		def IsDrainYield(self):
			debug(__name__ + ", IsDrainYield")
			return 0

		def MissionRespawned(self, pEvent):
			debug(__name__ + ", PlayerRespawned")

			myTimeVortexModule = None
			try:
				myTimeVortexModule = __import__(pathToModule)
			except:
				myTimeVortexModule = None
				traceback.print_exc()

			if myTimeVortexModule != None and hasattr(myTimeVortexModule, "GetTravelSetToUse"):
				pSet = None
				try:
					pSet = myTimeVortexModule.GetTravelSetToUse(None, 1, 1) # All ships will end on the non-AI set.
				except:
					pSet = None
					traceback.print_exc()

				if pSet != None:
					self.pSet = pSet
			return 0

				

		def OnYield(self, pShip, pInstance, pEvent, pTorp):
			debug(__name__ + ", OnYield")
			if self.pSet == None:
				self.MissionRespawned(pEvent)

			if pShip is None or not hasattr(pShip, "GetObjID"):
				return
			iShipID = pShip.GetObjID()
			kShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip == None or not hasattr(kShip, "GetObjID") or kShip == None or pShip.IsDead() or pShip.IsDying():
				return

			# Set spin to ship
			#MissionLib.SetRandomRotation(pShip, 10)
			iPlayerID = App.NULL_ID
			pPlayer = App.Game_GetCurrentPlayer()
			if pPlayer and hasattr(pPlayer, "GetObjID"):
				iPlayerID = pPlayer.GetObjID()

			iAttackerID = App.NULL_ID
			pAttacker = App.ShipClass_GetObjectByID(None, pTorp.GetParentID())
			if pAttacker and hasattr(pAttacker, "GetObjID"):
				iAttackerID = pAttacker.GetObjID()

			isShipPlayer = (iPlayerID != None and iPlayerID != App.NULL_ID and iShipID == iPlayerID)
			attackerEandNotSelf = (iAttackerID != None and iAttackerID != App.NULL_ID and iAttackerID != iShipID)

			if self.pSet != None:
				pTorp.SetLifetime(0.0)
				pTorp.UpdateNodeOnly()
				pSet = pShip.GetContainingSet()
				if pSet and self.pSet.GetName() != pSet.GetName():
					"""
					#pInstance = findShipInstance(pShip)
					#pInstance.TimeVortexRightToYeet = 1

					#if isShipPlayer:
						#Sorry for the lateness, I've tried a lot of things, performing the same thing as AddShipToSetVague, creating a method that makes a ship call the TravelManager to warp into the Time Vortex, even just warping the ship to to the Void1 set at such low speeds that it was eseentially trapped inside the Time Vortex. All of those work for each vessel, as long as they are not the player. For the player, they will cause a crash when the ship dies... not from changing sets, playing, ending simulations or such. Just from dying. Or so I thought. In the end, it was a separate script causing issues with self-destruct regardless of having this module installed or not, normal ones work LOL. Enjoy :D This works fully.
						# Workaround for players
						#pShip.AddPythonFuncHandlerForInstance(App.ET_OBJECT_DESTROYED, __name__ + ".ObjectDestroyed")
					
						# The attacker will "follow" you even if their drive doesn't permit it... actually nvm, with GC they CAN and WILL sometimes follow you if they have the required drive.
						#if attackerEandNotSelf:
						#	AddShipToSetVagueID(None, iAttackerID, self.pSet)
						#try:
						#	pAnotherActionW = App.TGScriptAction_Create(__name__, "wePackingPal", iShipID, sDestination)
						#	if pAnotherActionW:
						#		pSeq = App.TGSequence_Create()
						#		pSeq.AddAction(pAnotherActionW, App.TGAction_CreateNull(), 1.0)
						#		pSeq.Play()
						#except:
						#	traceback.print_exc()

					#else:
					"""
					AddShipToSetVagueID(None, iShipID, self.pSet, None, isShipPlayer)

			return

		def AddTorpedo(self, path):
			FoundationTech.dYields[path] = self

	def IsShipWarping(pShip):
		debug(__name__ + ", IsShipWarping")
		return App.g_kTravelManager.IsShipTravelling(pShip)

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

	def wePackingPal(pAction, iShipID, place, method="Time-Vortex Drive", ignoreWarnings = 0):
		if iShipID == None or iShipID == App.NULL_ID:
			return 0
		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip or not hasattr(pShip, "GetName") or (ignoreWarnings == 0 and (pShip.IsDead() or pShip.IsDying())):
			return 0
		else:
			if IsShipWarping(pShip) == 1:
				App.g_kTravelManager.ChangeDestinationOfShip(pShip, place)
			else:
				oResult = App.g_kTravelManager.EngageTravelToOfShip(pShip, place, "Time-Vortex Drive") # "Warp" If this works, create a new travel type called IYeetYou which can only be used if a certain pInstance value is added - or maybe use the timevortex pInstance values finally for something useful
				#if oResult == 1:
				#	pShip.AddPythonFuncHandlerForInstance(App.ET_OBJECT_EXPLODING, __name__ + ".ObjectDestroyed")
				print "oResult: ", oResult

		return 0

	def AddShipToSetVagueID(pAction, iShipID, pNewSet, pOldSet=None, isShipPlayer=0, ignoreWarnings=0):
		# This should be easy, first we call pOldSet.RemoveObjectFromSet and then pNewSet.AddObjectToSet, and then update the new system's proximity manager, right? Yes, but on this case, wrong too.
		# While normally this would work without issue, somehow when we call this from here, the game derps out and trying to do so makes the game crash immediately UNLESS we add a delay, which works totally fine for non-player vessels. However for the player vessel things are different - the player changes set? fine. The player changes type of ship, Mvams or teleports? Fine. The player dies? The game will still crash.
		# Temporary fix? Do not teleport the player, simple.
		if iShipID == None or iShipID == App.NULL_ID:
			return 0
		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip or not hasattr(pShip, "GetName") or (ignoreWarnings == 0 and (pShip.IsDead() or pShip.IsDying())):
			return 0
		else:
			sObjectName = pShip.GetName()
			if sObjectName is None:
				return 0
			if pOldSet == None:
				pOldSet = pShip.GetContainingSet()			
			if pOldSet != None:
				if pOldSet.GetName() == pNewSet.GetName():
					return 0

			if pNewSet != None and not App.ShipClass_GetObject(pNewSet, pShip.GetName()):
				if pAction == None:
					# We call to us in a sec, ok?
					try:
						pAnotherAction = App.TGScriptAction_Create(__name__, "AddShipToSetVagueID", iShipID, pNewSet, pOldSet, isShipPlayer)
						if pAnotherAction:
							pSeq = App.TGSequence_Create()
							pSeq.AddAction(pAnotherAction, App.TGAction_CreateNull(), 1.0)
							pSeq.Play()
					except:
						traceback.print_exc()
				else:
					# We perform the easy delete... or at least we should
					if pOldSet != None:
						###
						#poProxManager = pOldSet.GetProximityManager() 
						#if poProxManager:
						#	poProxManager.RemoveObject(pShip)
						###
						pOldSet.RemoveObjectFromSet(sObjectName)

					pShip.UpdateNodeOnly()

					pNewSet.AddObjectToSet(pShip, sObjectName)

					pShip.UpdateNodeOnly()

					pProximityManager = pNewSet.GetProximityManager()
					if (pProximityManager):
						pProximityManager.UpdateObject(pShip)

					if isShipPlayer:
						#pPlayer = App.Game_GetCurrentPlayer()
						pShip.AddPythonFuncHandlerForInstance(App.ET_OBJECT_EXPLODING, __name__ + ".ObjectDestroyed")
						# Small fix for players
						try:
							pTop = App.TopWindow_GetTopWindow()
							pTop.ForceTacticalVisible()
							pTop.ForceBridgeVisible()
						except:
							traceback.print_exc()

						try:
							pSubtitleAction = App.SubtitleAction_CreateC("We have been launched into the Time Vortex! Careful, we could be erased from time itself!")
							if pSubtitleAction:
								pSubtitleAction.SetDuration(6.0)
								pSequence = App.TGSequence_Create()
								pSequence.AddAction(pSubtitleAction)
								pSequence.Play()
						except:
							traceback.print_exc()

					pShip.UpdateNodeOnly()

		return 0



	def ConvertPointNiToTG(point):
		debug(__name__ + ", ConvertPointNiToTG")
		retval = App.TGPoint3()
		retval.SetXYZ(point.x, point.y, point.z)
		return retval

	def IsInList(item, list):
		debug(__name__ + ", IsInList")
		for i in list:
			if item == i:
				return 1
		return 0

	oTimeVortexTorp = TimeVortexTorpedo("TimeVortex Torpedo")
	# Just a few standard torps I know of that are TimeVortex... 
	# All but the first one, that is the first torp on my test bed ship...
	# Should be commented out on release...
	oTimeVortexTorp.AddTorpedo("Tactical.Projectiles.TimeMissile")

	class TimeVortexTorpedoDef(FoundationTech.TechDef):

		def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			return self.OnTorpDefense(pShip, pInstance, pTorp, oYield, pEvent)

		def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			isThis = 0

			if oYield and hasattr(oYield, "IsTimeVortexYield"):
				isThis = oYield.IsTimeVortexYield()

			if oYield and isThis:
				return 1

		def Attach(self, pInstance):
			pInstance.lTorpDefense.append(self)
			pInstance.lPulseDefense.append(self)


	oTimeVortexTorpedoImmunity = TimeVortexTorpedoDef('TimeVortex Torpedo Immune')

except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nTimeVortex Torpedoes are there for NOT enabled or present in your current BC installation"


def ObjectDestroyed(TGObject, pEvent): # Because the player may not want to be trapped inside when dying.
	# Temporary thing - make it ominous:
	debug(__name__ + ", ObjectDestroyed")

	# Even if this does not fix it, at least it will move the ship to a better area in case they are stuck -> die to go back to a normal place, good option for when GC is inactive.
	kShip = App.ShipClass_Cast(pEvent.GetDestination())
	if kShip:
		iShipID = kShip.GetObjID()
		if iShipID != None and iShipID != App.NULL_ID:
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip:
				#pSubtitleAction = App.SubtitleAction_CreateC("What few people knew was that, inside this ship, there was a being inherent to existance itself. And thus, with their power, they could return this vessel to a regular system, or doom the entire multiverse with it - SUTEKH")
				#if pSubtitleAction:
				#	pSubtitleAction.SetDuration(6.0)
				#	pSequence = App.TGSequence_Create()
				#	pSequence.AddAction(pSubtitleAction)
				#	pSequence.Play()

				pTimeVortexSet = pShip.GetContainingSet()

				try:
					if App.g_kSetManager.GetSet("Belaruz4"):
						print "Belaruz 4 was found"
						pModule = App.g_kSetManager.GetSet("Belaruz4")

					else:
            					print "Belaruz 4 was not initiated"
						# Import the dest set & initialize it
		
						import Systems.Belaruz.Belaruz4
						Systems.Belaruz.Belaruz4.Initialize()	
						pModule = App.g_kSetManager.GetSet("Belaruz4")

					try:
						pAnotherAction = App.TGScriptAction_Create(__name__, "AddShipToSetVagueID", iShipID, pModule, None, 0, 1)
						if pAnotherAction:
							pSeq = App.TGSequence_Create()
							pSeq.AddAction(pAnotherAction, App.TGAction_CreateNull(), 0.0)
							pSeq.Play()
					except:
						traceback.print_exc()
				except:
					traceback.print_exc()
					pass

	TGObject.CallNextHandler(pEvent)