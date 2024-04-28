#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         TimeVortexTorp.py by Alex SL Gato
#         28th April 2024
#         Based strongly on the Slipstream scripts by USS Sovereign, plus the FTech scripts by the FoundationTechnologies team.
#         Also please note, this tech is meant to be used alongside the TimeVortex Drive tech, which is a superficial but separate
#         mod (that is, it does not overwrite Slipstream scripts) of the Slipstream scripts as well.
#################################################################################################################
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# First of all, this tech depends on the TimeVortex Travel method mod, playing wihout it will probably make it useless
# At the bottom of your torpedo projectile file add this (Between the """ and """):
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

from Custom.TimeVortex.Libs import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import TimeVortexConfiguration
from Custom.TimeVortex import TimeVortexModule

#################################################################################################################
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.2",
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

	from ftb.Tech.ATPFunctions import *
	from math import *

	bOverflow = 0

	class TimeVortexTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			debug(__name__ + ", __init__")
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

			self.pEventHandler = App.TGPythonInstanceWrapper()
			self.pEventHandler.SetPyWrapper(self)

			self.pDummy = __import__("Systems.TimeVortexTunnel.TimeVortexTunnel1")
			#self.pDummy.Initialize()
			#App.g_kEventManager.RemoveBroadcastHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "PlayerRespawned")
			#App.g_kEventManager.AddBroadcastPythonMethodHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "PlayerRespawned")
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_MISSION_START, self.pEventHandler, "MissionRespawned")
			App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_MISSION_START, self.pEventHandler, "MissionRespawned")


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

		def PlayerRespawned(self, pEvent):
			debug(__name__ + ", PlayerRespawned")
			global bOverflow
			if bOverflow == 0:
				bOverflow = 1
				pTimeVortexSet = self.InitializeTimeVortexSet()
			#pTimeVortexSet = self.InitializeTimeVortexSet()

		def MissionRespawned(self, pEvent):
			debug(__name__ + ", PlayerRespawned")
			global bOverflow
			if bOverflow == 0:
				bOverflow = 1
				pTimeVortexSet = self.InitializeTimeVortexSet()
			#pTimeVortexSet = self.InitializeTimeVortexSet()

		def InitializeTimeVortexSet(self):
			#TO-DO CHECK WHAT OF THIS CAUSES A CRASH
			#pDummy = __import__("Systems.TimeVortexTunnel.TimeVortexTunnel1")
			
			#UPDATE: APPARENTLY INITILIALIZING DURING THE IMPACT CAUSES SOME SCRIPT TO CRASH - FORTUNATELY INITILIALIZING AT THE BEGINNING OF THE MISSION DOES NOT CAUSE THIS ISSUE
			#self.pDummy.Initialize()
			#TO-DO EXTRA TRY IF THIS DOES NOT CAUSE A CRASH - UPDATE AFTER TESTING, IT STILL CRASHES
			MissionLib.SetupSpaceSet("Systems.TimeVortexTunnel.TimeVortexTunnel1")
			pTimeVortexSet = self.pDummy.GetSet()

			#OLD ONE Systems.TimeVortexTunnel.TimeVortexTunnel1.LoadPlacements(Systems.TimeVortexTunnel.TimeVortexTunnel1.GetSetName())
			#self.pDummy.LoadPlacements(self.pDummy.GetSetName())
			#print "DummySetName is ", self.pDummy.GetSetName()
			return pTimeVortexSet

		def OnYield(self, pShip, pInstance, pEvent, pTorp):
			debug(__name__ + ", OnYield")
			#kShip=App.ShipClass_Cast(pEvent.GetDestination()) # TO-DO maybe pShip = kShip?
			kShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
			if pShip == None or kShip == None or pShip.IsDead() or pShip.IsDying():
				return

			import Systems.TimeVortexTunnel.TimeVortexTunnel
			import Systems.TimeVortexTunnel.TimeVortexTunnel1

			pTimeVortexSet = None

			if App.g_kSetManager.GetSet("TimeVortexTunnel1"):
				pTimeVortexSet = App.g_kSetManager.GetSet("TimeVortexTunnel1")
			else:
				print "Need to add the vortex tunnel system"
				pTimeVortexSet = self.InitializeTimeVortexSet()

			pSet = kShip.GetContainingSet()

			vNiWorldHitPoint=pEvent.GetWorldHitPoint()
			vWorldHitPoint=App.TGPoint3()
			vWorldHitPoint.SetXYZ(vNiWorldHitPoint.x,vNiWorldHitPoint.y,vNiWorldHitPoint.z)
	
			# Set spin to ship
			MissionLib.SetRandomRotation(pShip, 10)

			# Time Vortex
			# Do not do a thing if we are already in the Vortex

			if (pSet == None) or (pTimeVortexSet == None) or pSet.GetName() == pTimeVortexSet.GetName() or pSet.GetName() == "TimeVortexTunnel1":
				return

			if not App.ShipClass_GetObject(pTimeVortexSet, kShip.GetName()):
				pPlayer = App.Game_GetCurrentPlayer()

				if kShip.GetObjID() == pPlayer.GetObjID():
					

					# Get the old set
					pGame = App.Game_GetCurrentGame()
					p2Player = pGame.GetPlayer()
					pOldSet = p2Player.GetContainingSet()

					pcOldSetName = pOldSet.GetName()

					#if (bDupeRegion):
					# Same region but this set needs to be reloaded.  We need to rename the old set so that
					# inserting the new set won't delete the old set.
					pcOldSetName = pcOldSetName + "Original"
					pOldSet.SetName (pcOldSetName)

				# The commented lines below cause a crash :(
				#pSet.RemoveObjectFromSet(kShip.GetName())
				#pSet.DeleteObjectFromSet(kShip.GetName())
				pTimeVortexSet.AddObjectToSet(kShip, kShip.GetName())
				
				
				if kShip.GetObjID() == pPlayer.GetObjID():
					# Small fix for players
					pTop = App.TopWindow_GetTopWindow()
					pTop.ForceTacticalVisible()
					pTop.ForceBridgeVisible()

					# The attacker will follow you evem if their drive doesn't permit it
					pAttacker = App.ShipClass_GetObjectByID(None, pTorp.GetParentID()) #App.ShipClass_GetObjectByID(pTorp.GetContainingSet(), pTorp.GetParentID())
					if pAttacker == None:
						return

					pTimeVortexSet.AddObjectToSet(pAttacker, pAttacker.GetName())

					try:
						vWorldHitPoint=App.TGPoint3()
						vWorldHitPoint.SetXYZ(0,0,0)
						pAttacker.SetVelocity(vWorldHitPoint)
					except:
						pass

					pAttacker.UpdateNodeOnly()
					pAttacker.AddPythonFuncHandlerForInstance(App.ET_OBJECT_DESTROYED, __name__ + ".ObjectDestroyed")

					from Systems.TimeVortexTunnel.TimeVortexTunnel import *
					Systems.TimeVortexTunnel.TimeVortexTunnel.CreateMenus()
					# Hm... should we remove warp engine ability...? Nah, let's assume the engineers of the ship are intelligent enough to use the Warp Field to open a rift on the Time Vortex or something.
					#pHelmMenu = Bridge.BridgeUtils.GetBridgeMenu("Helm")
					#if pHelmMenu:
					#	warpButton = Lib.LibEngineering.GetButton("Warp", pHelmMenu)
					#	if warpButton:
					#		warpButton.SetDisabled()
					#		pAttacker.AddPythonFuncHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ReenableWarpButton")

					#App.SortedRegionMenu_ClearSetCourseMenu()

					# Purge memory when transfering between sets
					App.g_kLODModelManager.Purge()

					# Create the tunnel

					scale = 1000
					TunnelString = "TimeVortex Outer"
					pTunnel = loadspacehelper.CreateShip("timeVortex", pTimeVortexSet, TunnelString, "Player Start")
       
					# Get the ship and rotate it like the Bajoran Wormhole in DS9Set
					fTunnel = MissionLib.GetShip(TunnelString, pTimeVortexSet) 
					vCurVelocity = App.TGPoint3()
					vCurVelocity.SetXYZ(0, 0.8, 0)
					fTunnel.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

					# Invincible
					fTunnel.SetInvincible(1)
					fTunnel.SetHurtable(0)
					fTunnel.SetTargetable(0)

					# Very large ;)
					fTunnel.SetScale(scale)
					
					# Create the tunnel
					TunnelString2 = "TimeVortex Inner"
					pTunnel2 = loadspacehelper.CreateShip("timeVortex", pTimeVortexSet, TunnelString2, "Player Start")
       
					# Get the ship and rotate it like the Bajoran Wormhole in DS9Set
					fTunnel2 = MissionLib.GetShip(TunnelString2, pTimeVortexSet)
					# Disable collisions with the 2 models
					fTunnel2.EnableCollisionsWith(fTunnel, 0)
					vCurVelocity = App.TGPoint3()
					vCurVelocity.SetXYZ(0, 0.8, 0)
					fTunnel2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

					# Invincible
					fTunnel2.SetInvincible(1)
					fTunnel2.SetHurtable(0)
					fTunnel2.SetTargetable(0)

					# Very large ;)
					fTunnel2.SetScale(scale)

					# Custom tunnel textures?
					pModule = __import__(pPlayer.GetScript())

					# Is there a customization for this ship available?
					if hasattr(pModule, "TimeVortexCustomizations"):
						pCustomization = pModule.TimeVortexCustomizations()
					    
						# Customization exists, but does the tunnel texture entry exist?!
						if pCustomization.has_key('TunnelTexture'):
						# Bingo, replace textures for both tunnels then
							GFX = "scripts/Custom/TimeVortex/GFX/" + pCustomization['TunnelTexture']

							fTunnel.ReplaceTexture(GFX, "outer_glow")
							fTunnel2.ReplaceTexture(GFX, "outer_glow")

							fTunnel.RefreshReplacedTextures()
							fTunnel2.RefreshReplacedTextures()
            	
					# There no customization check for default presets
					else:
						reload(TimeVortexConfiguration)

						if TimeVortexConfiguration.TunnelGFX != 'Default':
							GFX = "scripts/Custom/TimeVortex/GFX/" + TimeVortexConfiguration.TunnelGFX

							fTunnel.ReplaceTexture(GFX, "outer_glow")
							fTunnel2.ReplaceTexture(GFX, "outer_glow")

							fTunnel.RefreshReplacedTextures()
							fTunnel2.RefreshReplacedTextures()
            	
					TimeVortexModule.SwapBackdrops()

					# Disable player collision with the cone
					fTunnel.EnableCollisionsWith(pPlayer, 0)
					fTunnel2.EnableCollisionsWith(pPlayer, 0)

					# Disable any ship collisions with the cone
					for kShip in pTimeVortexSet.GetClassObjectList(App.CT_SHIP):
						pShip = App.ShipClass_GetObject(pTimeVortexSet, kShip.GetName())
						fTunnel.EnableCollisionsWith(pShip, 0)
						fTunnel2.EnableCollisionsWith(pShip, 0)

					fTunnel.SetCollisionsOn(0)
					fTunnel2.SetCollisionsOn(0)
        
					# Position the tunnel so that it appears you're inside it
					pPlayerBackward = pPlayer.GetWorldBackwardTG()
					pPlayerDown = pPlayer.GetWorldDownTG()
					pPlayerPosition = pPlayer.GetWorldLocation()

					fTunnel.AlignToVectors(pPlayerBackward, pPlayerDown)
					fTunnel.SetTranslate(pPlayerPosition)
					fTunnel.UpdateNodeOnly()

					fTunnel2.AlignToVectors(pPlayerBackward, pPlayerDown)
					fTunnel2.SetTranslate(pPlayerPosition)
					fTunnel2.UpdateNodeOnly() 

				pTorp.SetLifetime(0.0)       
				pTorp.UpdateNodeOnly()

				fTunnelA = MissionLib.GetShip("TimeVortex Outer", pTimeVortexSet) 
				fTunnel2A = MissionLib.GetShip("TimeVortex Inner", pTimeVortexSet) 

				try:
					fTunnelA.SetCollisionsOn(0)
				except:
					pass
 				try: 
					fTunnel2A.SetCollisionsOn(0)
				except:
					pass

				kShip.UpdateNodeOnly()
				kShip.AddPythonFuncHandlerForInstance(App.ET_OBJECT_DESTROYED, __name__ + ".ObjectDestroyed")

				# update the proximity manager with this object's new position.
				pProximityManager = pTimeVortexSet.GetProximityManager()
				if (pProximityManager):
					pProximityManager.UpdateObject (kShip)

			# Repel Ship
			vVelocity = pShip.GetWorldLocation()
			vVelocity.Subtract(vWorldHitPoint)
			vVelocity.Unitize()
			vVelocity.Scale(100)
			pShip.SetVelocity(vVelocity)

			if (1==1): # TO-DO checking what causes the crash with gravityFX - apparently initializing the Dummy set crashes GravityFX
				return
			
			return

		def AddTorpedo(self, path):
			FoundationTech.dYields[path] = self

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

except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nTimeVortex Torpedoes are there for NOT enabled or present in your current BC installation"


class TimeVortexTorpedoDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		isThis = 0

		if oYield and hasattr(oYield, "IsTimeVortexYield"):
			isThis = oYield.IsTimeVortexYield()			
		#try:
		#	isThis = oYield.IsTimeVortexYield()
		#except:
		#	isThis = 0
		if oYield and isThis:
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)


oTimeVortexTorpedoImmunity = TimeVortexTorpedoDef('TimeVortex Torpedo Immune')

def ObjectDestroyed(TGObject, pEvent):
	debug(__name__ + ", ObjectDestroyed")
	kShip = App.ShipClass_Cast(pEvent.GetDestination())
	kShip = App.ShipClass_GetObjectByID(None, kShip.GetObjID())
	if (kShip == None):
		return

	pTimeVortexSet = kShip.GetContainingSet()
	#kShip.RemoveHandlerForInstance(App.ET_OBJECT_DESTROYED, __name__ + ".ObjectDestroyed")
	try:
		if App.g_kSetManager.GetSet("Belaruz4"):

			pModule = App.g_kSetManager.GetSet("Belaruz4")

		else:
            
			# Import the dest set & initialize it
		
			import Systems.Belaruz.Belaruz4
			Systems.Belaruz.Belaruz4.Initialize()	
			pModule = App.g_kSetManager.GetSet("Belaruz4")

		pModule.AddObjectToSet(kShip, kShip.GetName())
		pTimeVortexSet.DeleteObjectFromSet(kShip.GetName())
		kShip.UpdateNodeOnly()
		#TGObject.CallNextHandler(pEvent)
	except:
		pass

def ReenableWarpButton(TGObject, pEvent):
	kShip = App.ShipClass_Cast(pEvent.GetDestination())
	kShip = App.ShipClass_GetObjectByID(None, kShip.GetObjID())
	if (kShip != None):
		kShip.RemoveHandlerForInstance(App.ET_EXIT_SET, __name__ + ".ReenableWarpButton")

	pHelmMenu = Bridge.BridgeUtils.GetBridgeMenu("Helm")
	if pHelmMenu:
		warpButton = Libs.LibEngineering.GetButton("Warp", pHelmMenu)
		if warpButton and not warpButton.IsEnabled():
			warpButton.SetEnabled()