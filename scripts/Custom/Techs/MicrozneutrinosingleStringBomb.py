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

	iPlanetOffset = 300
	fRemoveFPDelay = 10
	fSetNumTilesPerAxisRadiusDiv = 60
	iSetNumAsteroidsPerTile = 1
	fRoidSizeFactor = 0.01
	fFPPowerOutMult = 1.0
	fRemovePlanetDelay = 5
	iNumHitsToDestroy = 1

	sFirepointScript = "BigFirepoint"

	class MicrozneutrinosingleStringBombTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

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

			for aObject in pSet.GetClassObjectList(App.CT_OBJECT):
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
								print "EXTERMINATE WITH GUNSTICK"
								pPlayer.RunDeathScript()	
							else:
								print "EXTERMINATE WITH REALITY BOMB"
								#try:
								#	pFirepoint = loadspacehelper.CreateShip(sFirepointScript, pSet, aObject.GetName() + " Atom field", None)
								#	pFirepoint.SetTargetable(0)
								#	pFirepoint.SetTranslate(aObject.GetWorldLocation())
								#	pPower = pFirepoint.GetPowerSubsystem().GetProperty()
								#	pPower.SetPowerOutput(pObject.GetRadius()*fFPPowerOutMult)
								#	pFirepoint.DestroySystem(pFirepoint.GetHull())
								#	DestroyEverything(aObject)
								#except:
								#	DestroyEverything(aObject)
								DestroyEverything(aObject)
						except:
							print "Avoided a possible crash"


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
	

	def DestroyEverything(pObject):
		pSet = pObject.GetContainingSet()
		if pSet:
			try:
				try:
					kThis = App.AsteroidFieldPlacement_Create(pObject.GetName() + " Dust field", pSet.GetName(), None)
					pSeq = App.TGSequence_Create()
					pSeq.AppendAction(App.TGScriptAction_Create(__name__, "RemoveObjectDelayed", pSet, pObject), fRemovePlanetDelay)
					pSeq.AppendAction(App.TGScriptAction_Create(__name__, "PlaceAsteroidField", pSet, pObject.GetName(), pObject.GetRadius(), pObject.GetWorldLocation(), kThis))
					pSeq.Play()
					kThis.SetNumAsteroidsPerTile(0)
					kThis.UpdateNodeOnly()
					kThis.ConfigField()
					kThis.Update(0)
				except:
					print "Could not make epic scene"
					pSeq = App.TGSequence_Create()
					pSeq.AppendAction(App.TGScriptAction_Create(__name__, "RemoveObjectDelayed", pSet, pObject), fRemovePlanetDelay)
					pSeq.Play()
			except:
				print "Error while deleting element"

	oMicrozneutrinosingleStringBombTorpe = MicrozneutrinosingleStringBombTorpedo("Micro Single-string Z-Neutrino Torpedo")
	# Just a few standard torps I know of that are Phased... 
	# All but the first one, that is the first torp on my test bed ship...
	# Should be commented out on release...
	oMicrozneutrinosingleStringBombTorpe.AddTorpedo("Tactical.Projectiles.MicrozneutrinosingleStringBomb")
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

