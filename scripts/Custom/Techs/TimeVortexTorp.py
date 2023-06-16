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

import App

import string

import MissionLib
import loadspacehelper
import nt
import Actions.MissionScriptActions
from Custom.TimeVortex.Libs import DS9FXMenuLib

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

	class TimeVortexTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

		def IsTimeVortexYield(self):
			return 1


		def PhaseYield(self):
			return 0

		def IsDrainYield(self):
			return 0

		def OnYield(self, pShip, pInstance, pEvent, pTorp):

			kShip=App.ShipClass_Cast(pEvent.GetDestination())
			if (kShip==None):
				return

			import Systems.TimeVortexTunnel.TimeVortexTunnel
			import Systems.TimeVortexTunnel.TimeVortexTunnel1

			pTimeVortexSet = None

			if App.g_kSetManager.GetSet("TimeVortexTunnel1"):
				pTimeVortexSet = App.g_kSetManager.GetSet("TimeVortexTunnel1")
			else:
				pDummy = __import__("Systems.TimeVortexTunnel.TimeVortexTunnel1")
				pDummy.Initialize()
				pTimeVortexSet = pDummy.GetSet()
				Systems.TimeVortexTunnel.TimeVortexTunnel1.LoadPlacements(Systems.TimeVortexTunnel.TimeVortexTunnel1.GetSetName())

			pSet = kShip.GetContainingSet()


			vNiWorldHitPoint=pEvent.GetWorldHitPoint()
			vWorldHitPoint=App.TGPoint3()
			vWorldHitPoint.SetXYZ(vNiWorldHitPoint.x,vNiWorldHitPoint.y,vNiWorldHitPoint.z)
	
			# Set spin to ship
			MissionLib.SetRandomRotation(pShip, 10)

			# Time Vortex
			# Do not do a thing if we are already in the Vortex

			if (pSet == None):
				return

			if pSet.GetName() == pTimeVortexSet.GetName() or pSet.GetName() == "TimeVortexTunnel1":
				return

			# Repel Ship
			vVelocity = pShip.GetWorldLocation()
			vVelocity.Subtract(vWorldHitPoint)
			vVelocity.Unitize()
			vVelocity.Scale(100)
			pShip.SetVelocity(vVelocity)

			if not App.ShipClass_GetObject(pTimeVortexSet, kShip.GetName()):
				pPlayer = App.Game_GetCurrentPlayer()

				if kShip.GetName() == pPlayer.GetName():
					

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
				
				
				if kShip.GetName() == pPlayer.GetName():
					# Small fix for players
					pTop = App.TopWindow_GetTopWindow()
					pTop.ForceTacticalVisible()
					pTop.ForceBridgeVisible()

					# The attacker will follow you evem if their drive doesn't permit it
					pAttacker = App.ShipClass_GetObjectByID(pTorp.GetContainingSet(), pTorp.GetParentID())
					if pAttacker == None:
						return

					pTimeVortexSet.AddObjectToSet(pAttacker, pAttacker.GetName())

					pAttacker.SetVelocity(0)

					pAttacker.UpdateNodeOnly()
					pAttacker.AddPythonFuncHandlerForInstance(App.ET_OBJECT_DESTROYED, __name__ + ".ObjectDestroyed")

					from Systems.TimeVortexTunnel.TimeVortexTunnel import *
					Systems.TimeVortexTunnel.TimeVortexTunnel.CreateMenus()
					App.SortedRegionMenu_ClearSetCourseMenu()

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
			
			return

		def AddTorpedo(self, path):
			FoundationTech.dYields[path] = self

	def ConvertPointNiToTG(point):
		retval = App.TGPoint3()
		retval.SetXYZ(point.x, point.y, point.z)
		return retval

	def IsInList(item, list):
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
		try:
			isThis = oYield.IsTimeVortexYield()
		except:
			isThis = 0
		if oYield and isThis:
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)


oTimeVortexTorpedoImmunity = TimeVortexTorpedoDef('TimeVortex Torpedo Immune')

def ObjectDestroyed(TGObject, pEvent):
	kShip = App.ShipClass_Cast(pEvent.GetDestination())
	if (kShip == None):
		return
	pTimeVortexSet = kShip.GetContainingSet()
	#kShip.RemoveHandlerForInstance(App.ET_OBJECT_DESTROYED, __name__ + ".ObjectDestroyed")

	import Systems.DeepSpace.DeepSpace
	from Systems.DeepSpace.DeepSpace import *



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