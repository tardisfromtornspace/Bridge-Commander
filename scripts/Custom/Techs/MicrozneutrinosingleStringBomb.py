# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
# You can add a secondary torpedo version by copying the file and adding "_P" to the end of the new file name, which will be the torpedo after the shield
"""
try:
	modMicrozneutrinosingleStringBomb = __import__("Custom.Techs.MicrozneutrinosingleStringBomb")
	if(modMicrozneutrinosingleStringBomb):
		modMicrozneutrinosingleStringBomb.oMicrozneutrinosingleStringBombTorpe.AddTorpedo(__name__)
except:
	print "Micro Z-Neutrino Wave flattened into a single String Bomb script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an immunity list and a resistance list, in order to keep the files unaltered... just add to your scripts/ships/shipFileName.py the following lines:

# In scripts/ships/yourShip.py
"""
def ImImmuneToZNeutrinos(): # Immunity against Reality Bombs
      return 1
"""
# For a resistance that will prevent it from exploding but won't protect you from an indiract blast, go to Custom/Ships/shipFileName.py and add this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Micro Single-string Z-Neutrino Torpedo Resistant": 1
}
"""

import App
import MissionLib
try:
	import Foundation
	import FoundationTech
	import loadspacehelper

	from ftb.Tech.ATPFunctions import *
	from math import *

	from threading import *

	sema = Semaphore()

	iPlanetOffset = 300
	fRemoveFPDelay = 10
	fSetNumTilesPerAxisRadiusDiv = 60
	iSetNumAsteroidsPerTile = 1
	fRoidSizeFactor = 0.01
	fFPPowerOutMult = 1.0
	fRemovePlanetDelay = 5
	iNumHitsToDestroy = 1

	sFirepointScript = "BigFirepoint"

	NonSerializedObjects = ( "lock", )

	class MicrozneutrinosingleStringBombTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []
			self.pEventHandler = App.TGPythonInstanceWrapper()
			self.pEventHandler.SetPyWrapper(self)

		def IsMicrozneutrinosingleStringTorpYield(self):
			return 1

		def OnYield(self, pShip, pInstance, pEvent, pTorp):

			pTorp.SetLifetime(0)

			pShipID = pShip.GetObjID()

			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
			if not pShip:
				return

			pHitPoint = ConvertPointNiToTG(pEvent.GetWorldHitPoint())
			pSet = pShip.GetContainingSet()

			mustKillPlayer = 0
			haveKilledPlayer = 0

			for aObject in pSet.GetClassObjectList(App.CT_PHYSICS_OBJECT):
				print aObject
				Percentage = "a"
				try:
					Percentage = pInstance.__dict__['Micro Single-string Z-Neutrino Torpedo Resistant'] # This means the defender can defend itself from the drain.
				except:
					try:
						paShip = App.ShipClass_Cast(aObject)
						pShipModule = __import__(paShip.GetScript())
						Percentage = pShipModule.ImImmuneToZNeutrinos()
						print "I am supposed to be immune"
					except:
						print "I do not have the immune"
						Percentage = "a"

				if Percentage == "a":
					kTemp = App.TGPoint3()
					kTemp = aObject.GetWorldLocation()
					kTemp.Subtract(pHitPoint)
					fKey = kTemp.Length()

					if fKey <= 1000000.0:
						try:
							pGame = App.Game_GetCurrentGame()
							pEpisode = pGame.GetCurrentEpisode()
							pMission = pEpisode.GetCurrentMission()
							pPlayer = MissionLib.GetPlayer()
							if (aObject.GetName() == pPlayer.GetName()):
								print "EXTERMINATE WITH GUNSTICK... later"
								mustKillPlayer = 1						
							else:
								print "EXTERMINATE WITH REALITY BOMB"
								try:
									pFirepoint = loadspacehelper.CreateShip(sFirepointScript, pSet, aObject.GetName() + " Atom field", None)
									pFirepoint.SetTargetable(0)
									pFirepoint.SetTranslate(aObject.GetWorldLocation())
									pPower = pFirepoint.GetPowerSubsystem().GetProperty()
									pPower.SetPowerOutput(pObject.GetRadius()*fFPPowerOutMult)
									pFirepoint.DestroySystem(pFirepoint.GetHull())
									#paShip = App.ShipClass_Cast(aObject)
									#AddDamage(paShip)

									DestroyEverything(aObject)
								except:
									DestroyEverything(aObject)
								#DestroyEverything(aObject)
						except:
							print "Avoided a possible crash"
								
			print mustKillPlayer
			if mustKillPlayer == 1:

				pGame = App.Game_GetCurrentGame()
				pEpisode = pGame.GetCurrentEpisode()
				pMission = pEpisode.GetCurrentMission()
				pPlayer = MissionLib.GetPlayer()
				eType = App.Mission_GetNextEventType()
				try:
					sema.acquire()

					pSequence = App.TGSequence_Create()
					#pAction = App.TGScriptAction_Create(__name__, "accionDummy")
					#pSequence.AddAction(pAction, None, 15)
					pAction = App.TGScriptAction_Create(__name__, "accionDummyDeath")
					pSequence.AddAction(pAction, None, 5)
					pSequence.Play()
					haveKilledPlayer = 1

					sema.release()	
				except:
					print "Error while killing player"

			print mustKillPlayer
			if haveKilledPlayer == 0:
				#NOTE: Using App.CT_OBJECT may not be a good idea, that will kill characters as well
				for aObject in pSet.GetClassObjectList(App.CT_PLANET):
					try:
						kTemp = App.TGPoint3()
						kTemp = aObject.GetWorldLocation()
						kTemp.Subtract(pHitPoint)
						fKey = kTemp.Length()

						if fKey <= 1000000.0:
							DestroyEverything(aObject)
					except:
						print "a PLANET survived"

				for aObject in pSet.GetClassObjectList(App.CT_SUN):
					try:
						kTemp = App.TGPoint3()
						kTemp = aObject.GetWorldLocation()
						kTemp.Subtract(pHitPoint)
						fKey = kTemp.Length()

						if fKey <= 1000000.0:
							DestroyEverything(aObject)
					except:
						print "a SUN survived"

				for aObject in pSet.GetClassObjectList(App.CT_BACKDROP):
					try:
						kTemp = App.TGPoint3()
						kTemp = aObject.GetWorldLocation()
						kTemp.Subtract(pHitPoint)
						fKey = kTemp.Length()

						if fKey <= 1000000.0:
							DestroyEverything(aObject)
					except:
						print "a BACKDROP survived"

				for aObject in pSet.GetClassObjectList(App.CT_BACKDROP_SPHERE):
					try:
						kTemp = App.TGPoint3()
						kTemp = aObject.GetWorldLocation()
						kTemp.Subtract(pHitPoint)
						fKey = kTemp.Length()

						if fKey <= 1000000.0:
							DestroyEverything(aObject)
					except:
						print "a BACK. SPHERE survived"

				for aObject in pSet.GetClassObjectList(App.CT_STAR_SPHERE):
					try:
						kTemp = App.TGPoint3()
						kTemp = aObject.GetWorldLocation()
						kTemp.Subtract(pHitPoint)
						fKey = kTemp.Length()

						if fKey <= 1000000.0:
							DestroyEverything(aObject)
					except:
						print "a CT_STAR_SPHERE survived"

				for aObject in pSet.GetClassObjectList(App.CT_NEBULA):
					try:
						kTemp = App.TGPoint3()
						kTemp = aObject.GetWorldLocation()
						kTemp.Subtract(pHitPoint)
						fKey = kTemp.Length()

						if fKey <= 1000000.0:
							DestroyEverything(aObject)
					except:
						print "a CT_NEBULA survived"

				for aObject in pSet.GetClassObjectList(App.CT_META_NEBULA):
					try:
						kTemp = App.TGPoint3()
						kTemp = aObject.GetWorldLocation()
						kTemp.Subtract(pHitPoint)
						fKey = kTemp.Length()

						if fKey <= 1000000.0:
							DestroyEverything(aObject)
					except:
						print "a CT_META_NEBULA survived"

				for aObject in pSet.GetClassObjectList(App.CT_ASTEROID_FIELD):
					try:
						kTemp = App.TGPoint3()
						kTemp = aObject.GetWorldLocation()
						kTemp.Subtract(pHitPoint)
						fKey = kTemp.Length()

						if fKey <= 1000000.0:
							DestroyEverything(aObject)
					except:
						print "a CT_ASTEROID_FIELD survived"

				for aObject in pSet.GetClassObjectList(App.CT_ASTEROID_TILE):
					try:
						kTemp = App.TGPoint3()
						kTemp = aObject.GetWorldLocation()
						kTemp.Subtract(pHitPoint)
						fKey = kTemp.Length()

						if fKey <= 1000000.0:
							DestroyEverything(aObject)
					except:
						print "a CT_ASTEROID_TILE survived"

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

	def RemoveObjectDelayed(pAction, pSet, pObject):
		pSet.RemoveObjectFromSet(pObject.GetName())
		return 0

	def accionDummy(self):
		# TO-DO add dust sound as .wav
		pEnterSound = App.TGSound_Create("sfx/Weapons/vanishToDust.wav", "Enter", 0)
		pEnterSound.SetSFX(0) 
		pEnterSound.SetInterface(1)

		App.g_kSoundManager.PlaySound("Enter")
		return 0

	def accionDummyDeath(self):
		# TO-DO add dust sound as .wav
		pEnterSound = App.TGSound_Create("scripts/Custom/Jumpspace/SFX/dummy.wav", "Enter", 0)
		pEnterSound.SetSFX(0) 
		pEnterSound.SetInterface(1)

		App.g_kSoundManager.PlaySound("Enter")

		pGame = App.Game_GetCurrentGame()
		pEpisode = pGame.GetCurrentEpisode()
		pMission = pEpisode.GetCurrentMission()
		pPlayer = MissionLib.GetPlayer()

		pPlayer.RunDeathScript()
		# See if by reducing the health a lot and then firing something else it breaks.
		#pPropertySet = pPlayer.GetPropertySet()
		#mod = __import__('Custom.Techs.CriticalWeak')
		#mod.LoadPropertySet(pPropertySet)
		#pPlayer.SetupProperties()
		#pShip = pGame.GetPlayer()
		#pGame.SetPlayer(pShip)
	
		#pPlayer.DestroySystem(pPlayer.GetHull())

		#pPlayer.SetDead()

		#iHDamageMax = pShip.GetHull().GetCondition()
		#pPlayer.DamageSystem(pShip.GetHull(), (iHDamageMax * 1.1))

		return 0


	def PlaceAsteroidField(pAction, pSet, sName, fRadius, kLocation, kThis):
		kThis.SetStatic(0)
		kThis.SetNavPoint(0)
		kThis.SetTranslate(kLocation)
		kThis.SetFieldRadius(fRadius)
		kThis.SetNumTilesPerAxis(fRadius/fSetNumTilesPerAxisRadiusDiv)
		kThis.SetNumAsteroidsPerTile(iSetNumAsteroidsPerTile)
		kThis.SetAsteroidSizeFactor(fRoidSizeFactor)
		kThis.UpdateNodeOnly()
		kThis.ConfigField()
		kThis.Update(0)
		return 0

	def AddDamage(pThingToDamage):
		pThingToDamage.AddObjectDamageVolume(0.422150, 5.159405, 0.615038, 1.000000, 60000.000000)
		pThingToDamage.AddObjectDamageVolume(0.422158, 5.159409, 0.615041, 1.000000, 60000.000000)
		pThingToDamage.AddObjectDamageVolume(-0.030887, 4.797346, 0.330181, 1.000000, 60000.000000)
		pThingToDamage.AddObjectDamageVolume(-0.324254, 4.562893, 0.145721, 1.000000, 60000.000000)
		pThingToDamage.AddObjectDamageVolume(-0.641755, 4.309156, -0.053913, 1.000000, 60000.000000)
		pThingToDamage.AddObjectDamageVolume(-2.109845, -2.967318, 0.920673, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-2.109845, -2.967318, 0.920673, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(0.023524, -1.645499, 1.594733, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(0.543860, -1.431186, 1.523595, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(1.350096, -1.169250, 1.396949, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(1.996839, -0.952223, 1.325684, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-4.567484, 0.618553, 0.783764, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-4.567488, 0.618553, 0.783770, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-4.629547, 0.608376, 0.138782, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-4.614378, 0.696918, -0.269310, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(1.003745, -1.059366, -1.661196, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(1.003746, -1.059365, -1.661201, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(0.824475, -1.969406, 1.062877, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-0.531316, -2.008771, -1.609570, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-0.531314, -2.008766, -1.609583, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-2.309185, -0.876976, -1.389301, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-2.962406, -0.414332, -1.243696, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-3.637032, 0.100612, -1.041938, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(4.754462, 1.713995, -0.362329, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(4.762648, 1.766002, -0.356338, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(4.691274, 1.691397, 0.278308, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(0.304715, 1.331106, -0.388636, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(0.356646, 1.296530, -0.401717, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(0.067270, 6.195809, -0.833527, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(4.479577, 0.470430, 0.034391, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(4.466055, -0.263201, 0.061560, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-4.830773, 1.870873, 0.071484, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-0.180488, 3.018775, -0.578173, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-0.242935, 2.059572, 1.039179, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-0.250446, 3.287237, 0.650929, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-0.220363, -5.155837, 0.003401, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-0.525843, 5.525585, -0.355180, 1.000000, 6000.000000)
		pThingToDamage.AddObjectDamageVolume(-0.328363, 0.769045, 1.167307, 1.000000, 6000.000000)
		pThingToDamage.DamageRefresh(1)
	

	def DestroyEverything(pObject):
		pSet = pObject.GetContainingSet()
		if pSet:
			try:
				try:
					kThis = App.AsteroidFieldPlacement_Create(pObject.GetName() + " Dust field", pSet.GetName(), None)
					pSeq = App.TGSequence_Create()
					pSeq.AppendAction(App.TGScriptAction_Create(__name__, "RemoveObjectDelayed", pSet, pObject), fRemovePlanetDelay)
					pAction = App.TGScriptAction_Create(__name__, "accionDummy")
					pSeq.AddAction(pAction, None, 0)
				#	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "PlaceAsteroidField", pSet, pObject.GetName(), pObject.GetRadius(), pObject.GetWorldLocation(), kThis))
					pSeq.Play()
				#	kThis.SetNumAsteroidsPerTile(0)
				#	kThis.UpdateNodeOnly()
				#	kThis.ConfigField()
				#	kThis.Update(0)
				except:
					print "Could not make epic scene"
					pSeq = App.TGSequence_Create()
					pAction = App.TGScriptAction_Create(__name__, "accionDummy")
					pSeq.AddAction(pAction, None, 0)
					pSeq.AppendAction(App.TGScriptAction_Create(__name__, "RemoveObjectDelayed", pSet, pObject), fRemovePlanetDelay)
					pSeq.Play()
			except:
				print "Error while deleting element"

	oMicrozneutrinosingleStringBombTorpe = MicrozneutrinosingleStringBombTorpedo("Micro Single-string Z-Neutrino Torpedo")
	# Just a few standard torps I know of that are Phased... 
	# All but the first one, that is the first torp on my test bed ship...
	# Should be commented out on release...
	oMicrozneutrinosingleStringBombTorpe.AddTorpedo("Tactical.Projectiles.SingleStringZNeutrinoTorpedo")

except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nsingle-string Z-Neutrino micro Torpedoes are there but NOT enabled or present in your current BC installation"
try:
	class MicrozneutrinosingleStringBombTorpeDef(FoundationTech.TechDef):

		def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			isThis = 0
			try:
				isThis = oYield.IsMicrozneutrinosingleStringTorpYield()
			except:
				isThis = 0
			if oYield and isThis:
				return 1

		def Attach(self, pInstance):
			pInstance.lTorpDefense.append(self)


	oMicrozneutrinosingleStringBombTorpeImmunity = MicrozneutrinosingleStringBombTorpeDef('Micro Single-string Z-Neutrino Torpedo Resistant')
except:
	print "Z-Neutrino energy immunity went wrong"

