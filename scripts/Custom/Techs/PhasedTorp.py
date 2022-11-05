# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
"""
try:
	modPhasedTorp = __import__("Custom.Techs.PhasedTorp")
	if(modPhasedTorp):
		modPhasedTorp.oPhasedTorp.AddTorpedo(__name__)
except:
	print "Phased Torpedo script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Phased Torpedo Immune": 1
}
"""

import App

import string

global lImmunePhaseShips # Some ships immune to this blow
lImmunePhaseShips = (
                "Aegean",
                "Aegian",
                "AMVogager",
                "AncientCity",
                "Andromeda",
                "ArmoredVoyager",
                "Atlantis",
                "B5LordShip",
                "B5TriadTriumviron",
                "bcnarada",
                "BorgDiamond",
                "CA8472",
                "crossfield31",
                "DanielJackson",
                "DCMPDefiant",
                "DJEnterpriseG",
                "DJEnterpriseGDrive",
                "DJEnterpriseGSaucer",
                "DSC304Apollo",
                "DSC304Daedalus",
                "DSC304Korolev",
                "DSC304Odyssey",
                "DSC304OdysseyRefit",
                "DSC304OdysseyUpgrade",
                "DyExcalibur",
                "GalaxyX",
                "Enterprise",
                "EnterpriseF",
                "EnterpriseG",
                "EnterpriseH",
                "EnterpriseI",
                "EnterpriseJ",
                "Excalibur",
                "Firebird",
                "janeway",
                "Korolev",
                "MindridersThoughtforce",
                "MvamPrometheus",
                "MvamPrometheusDorsal",
                "MvamPrometheusSaucer",
                "MvamPrometheusVentral",
                "novaII",
                "Odyssey",
                "OdysseyRefit",
                "OdysseyUpgrade",
                "ONeill",
                "OdysseyRefit",
                "OdysseyUpgrade",
                "PsVoyagerA",
                "Satellite",
                "Sovereign",
                "Supership",
                "Tardis",
                "ThirdspaceCapitalShip",
                "VulcanXRT55D",
                "WCNemEntE",
                "Wells",
                "Windrunner",
                "WCNemEntEnoyacht",  
                "XOverAlteranWarship",
                "XOverAncientCityFed",
                "XOverAncientSatelliteFed",
                )


try:
	import Foundation
	import FoundationTech

	from ftb.Tech.ATPFunctions import *
	from math import *

	class PhasedTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

                def IsPhaseYield(self):
			return 1

		def OnYield(self, pShip, pInstance, pEvent, pTorp):
			if(pEvent.IsHullHit()):
				return

			#if pTorp.GetObjID() in self.lFired:
			#	pTorp.SetLifetime(0)
			#pTorp.SetLifetime(0)

			# Immunities, better here so all phased things are consistent with each other
			global lImmunePhaseShips
			sScript     = pShip.GetScript()
			sShipScript = string.split(sScript, ".")[-1]
			if sShipScript in lImmunePhaseShips:
				return

                        pTorp.SetLifetime(100)

			pShipID = pShip.GetObjID()

			#pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
			if not pShip:
				return
                        print "Calculating phasedTorpHit"
			# pHitPoint = ConvertPointNiToTG(pEvent.GetWorldHitPoint())
                        pHitPoint = ConvertPointNiToTG(pTorp.GetWorldLocation())
                        # an idea pTorp.GetWorldLocation()
                        # another idea .GetPosition()

			pVec = pTorp.GetVelocityTG()
			pVec.Scale(0.001)
			pHitPoint.Add(pVec)

                        #pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTorp.GetTargetID()))
                        #pSet = pTarget.GetContainingSet()

           
                        #pTorp.SetTargetOffset(pHitPoint)

			mod = pTorp.GetModuleName()
			if(self.__dict__.has_key("SubTorp")):
				mod = self.SubTorp
                        # field 4 was pTorp.GetTargetID(), now it's pShipID
			pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pTorp.GetTargetID(), pTorp.GetParentID(), __import__(mod).GetLaunchSpeed())
                        pTempTorp.SetLifetime(15.0)
			self.lFired.append(pTempTorp.GetObjID())
			pTempTorp.UpdateNodeOnly() 

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

	oPhasedTorp = PhasedTorpedo("Phased Torpedo")
	# Just a few standard torps I know of that are Phased... 
	# All but the first one, that is the first torp on my test bed ship...
	# Should be commented out on release...
	oPhasedTorp.AddTorpedo("Tactical.Projectiles.PhasedPlasma")
except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nPhased Torpedoes are there for NOT enabled or present in your current BC installation"


class PhasedTorpedoDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		if oYield and oYield.IsPhaseYield():
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)


oPhasedTorpedoImmunity = PhasedTorpedoDef('Phased Torpedo Immune')