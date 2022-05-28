from bcdebug import debug
################################################################
#######  Gravity FX Main Script     ##########################
################################################################ 
#################        by Fernando Aluani aka USS Frontier
############################################################
# This is the script of the GravityFX mod that involves the most important things:
# The code to create, update and delete the gravity wells, and the code to apply the gravity force
################################################################
import App
import MissionLib
import math
import nt
import string
import Custom.GravityFX.Logger
from Custom.GravityFX.GravityFXlib import *
from Custom.GravityFX.ListLib import *

class GravityManager:
	def __init__(self):
		debug(__name__ + ", __init__")
		self.GMID = GetUniqueID("GravityManager")
		self.CLASS = "Gravity Manager"
		self.GravWellList = []
		self.PlayerCounterGravity = GetConfigValue("ThrusterState")
		self.ShipList = []
		self.PluginBaseDict = CreatePluginBase()
		if GetConfigValue("LogGravityManager"):
			self.Logger = Custom.GravityFX.Logger.LogCreator(self.CLASS, "scripts\Custom\GravityFX\Logs\GravityManagerLOG.txt")
			self.Logger.LogString("Initialized "+self.GMID+" logger")
		else:
			self.Logger = Custom.GravityFX.Logger.DummyLogger()
		print "Gravity FX has been loaded."

	def CreateGravWells(self):
		debug(__name__ + ", CreateGravWells")
		try:
			if self.GravWellList:
				self.DeleteAllGravWells()
			PlanetSunList = self.GetObjListInSet()
			PSNameList = []
			for well in PlanetSunList:
				GravWell = GravityWell(well)
				self.GravWellList.append(GravWell)
				PSNameList.append(well.GetName())
			pPlayer = App.Game_GetCurrentPlayer()
			if pPlayer:
				pSet = pPlayer.GetContainingSet()
				if pSet:
					self.Logger.LogString("Creating Grav Wells - Set: "+pSet.GetRegionModule())
					for pShip in pSet.GetClassObjectList(App.CT_SHIP):
						self.CreateGravWellPlugin(pShip)
			self.Logger.LogString("Creating Grav Wells: "+str(self.GravWellList))
			self.Logger.LogString("Planets/Suns List: "+str(PSNameList))
			self.RefreshShipList()
			pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, pMission, __name__+".HandleGravTorps")
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__+".HandleGravTorps")
			return
		except:
			self._LogError("CreateGravWell")
	def CreateGravWellPlugin(self, ship):
		debug(__name__ + ", CreateGravWellPlugin")
		try:
			try:
				bIsShipTravelling = App.g_kTravelManager.IsShipTravelling(ship)
			except:
				bIsShipTravelling = 0
			if GetGeneratorsOfShip(ship) != []:
				if bIsShipTravelling == 1:
					# Ship is travelling, so don't try to create a GWP for her at all.
					# Gravity can mess up the 'journey' in the TravelSet
					self.Logger.LogString("Couldn't create GWP for ship "+ship.GetName()+", he is travelling.")
					return None
				pGWP = self.GetGravWellByID(ship.GetObjID())
				if pGWP == None:
					pGWP = GravWellPlugin(ship)
					self.Logger.LogString("Created Grav Well Plugin for ship "+ship.GetName())
					self.GravWellList.append(pGWP)
				return pGWP
		except:
			self._LogError("CreateGravWellPlugin")
	def DeleteGravWellPlugin(self, ship):
		debug(__name__ + ", DeleteGravWellPlugin")
		try:
			pGWP = self.GetGravWellByID(ship.GetObjID())
			if pGWP:
				self.DeleteGravWell(pGWP)
				self.Logger.LogString("Deleted Grav Well Plugin for ship "+ship.GetName())
				del pGWP
		except:
			self._LogError("DeleteGravWellPlugin")
	def CreateTorpGravEffect(self, torp, point):
		debug(__name__ + ", CreateTorpGravEffect")
		try:
			if self.GetPluginInfoForObj(torp):
				pTGE = TorpGravEffect(torp, point)
				self.Logger.LogString("Created torp grav effect for torp "+GetTorpType(torp)+" "+str(torp.GetObjID()))
				self.GravWellList.append(pTGE)
				return pTGE
		except:
			self._LogError("CreateTorpGravEffect")
	def DeleteTorpGravEffect(self, pTGE):
		debug(__name__ + ", DeleteTorpGravEffect")
		try:
			if pTGE and pTGE.CLASS == "Torp Grav Effect":
				self.DeleteGravWell(pTGE)
				self.Logger.LogString("Deleted torp grav effect: "+pTGE.TGEID)
				del pTGE
		except:
			self._LogError("DeleteTorpGravEffect")
	def RefreshShipList(self):
		debug(__name__ + ", RefreshShipList")
		try:
			self.ShipList = self.GetObjListInSet(1)
			if GetConfigValue("LogGravityManager"):
				ShipNameList = []
				for Ship in self.ShipList:
					ShipNameList.append(Ship.GetName())
				self.Logger.LogString("Refreshed Ship List: "+str(ShipNameList))
			pPlayer = MissionLib.GetPlayer()
			if IsObjInList(pPlayer, self.ShipList) == 0 and CanBeAffected(pPlayer) == 1:
				self.ShipList.append(pPlayer)
				self.Logger.LogString("Added Player to the Ship List")
		except:
			self._LogError("RefreshShipList")
	def PrintStats(self):
		debug(__name__ + ", PrintStats")
		print "//GravManager=", self, "\n", "//GravWellList=", self.GravWellList
		l = []
		for ship in self.ShipList:
			l.append(ship.GetName())
		print "//ShipList=", l
		PlanetsList = self.GetObjListInSet()
		lp = []
		for planet in PlanetsList:
			lp.append(planet.GetName())
		print "//PlanetList=", lp
		self.Logger.LogString("Printed stats")
	def GetGravInfoOnShip(self, ship):
		debug(__name__ + ", GetGravInfoOnShip")
		return self.GetGravInfoOnObj(ship)
	def GetGravInfoOnObj(self, obj, useShortForShips = 0):
		debug(__name__ + ", GetGravInfoOnObj")
		InfoList = []
		nHowMany = 0
		WellForceDict = {}
		GravWellPluginDict = {}
		pPlayer = MissionLib.GetPlayer()
		if pPlayer == None or obj == None:
			return InfoList
		if obj.GetObjID() == pPlayer.GetObjID():
			nUseShipName = 0
		else:
			nUseShipName = 1
		if obj.IsTypeOf(App.CT_SHIP):
			WellForceDict = self.GetAllWellsAffectingObj(obj)
			GW = self.GetGravWellByID(obj.GetObjID())
			if useShortForShips == 0:
				if GW:
					#self.Logger.LogString("GGIOS: Ship is the GW: "+str(GW.GetParentName()))
					sRadius = ConvertGUtoKM(GW.Radius)
					GravWellPluginDict[GW.GetParentName()] = {'Radius': sRadius, 'Age': GW.Age, 'Type': str(GW.Type), 'Online': GW.IsOnline}
				nHowMany = nHowMany + len(WellForceDict.keys())
				if nHowMany == 0:
					if nUseShipName == 0:
						InfoList.append("This Ship isn't inside of any gravity well.")
					else:
						InfoList.append(obj.GetName()+" isn't inside of any gravity well.")
				else:
					if nUseShipName == 0:
						InfoList.append("This Ship is within "+str(nHowMany)+" Gravity Well(s).")
					else:
						InfoList.append(obj.GetName()+" is within "+str(nHowMany)+" Gravity Well(s).")	
					for index in WellForceDict.keys():
						if nUseShipName == 0:
							InfoList.append(index+" is exercising a force of "+GetStrFromFloat(WellForceDict[index])+" Km/h^2 on this Ship.")
						else:
							InfoList.append(index+" is exercising a force of "+GetStrFromFloat(WellForceDict[index])+" Km/h^2 on "+obj.GetName()+".")	
				for index in GravWellPluginDict.keys():
					if nUseShipName == 0:
						if GravWellPluginDict[index]['Online']:
							InfoList.append("This Ship is producing a gravity well. His caracteristics are: Radius = "+GetStrFromFloat(GravWellPluginDict[index]['Radius'])+", Age = "+GetStrFromFloat(GravWellPluginDict[index]['Age'])+" and Type = "+GravWellPluginDict[index]['Type'])
						else:
							InfoList.append("This Ship has an gravity well generator, it is currently offline. His caracteristics are: Radius = "+GetStrFromFloat(GravWellPluginDict[index]['Radius'])+", Age = "+GetStrFromFloat(GravWellPluginDict[index]['Age'])+" and Type = "+GravWellPluginDict[index]['Type'])
					else:
						if GravWellPluginDict[index]['Online']:
							InfoList.append(index+" is producing a gravity well. His caracteristics are: Radius = "+GetStrFromFloat(GravWellPluginDict[index]['Radius'])+", Age = "+GetStrFromFloat(GravWellPluginDict[index]['Age'])+" and Type = "+GravWellPluginDict[index]['Type'])
						else:
							InfoList.append(index+" has an gravity well generator, it is currently offline. His caracteristics are: Radius = "+GetStrFromFloat(GravWellPluginDict[index]['Radius'])+", Age = "+GetStrFromFloat(GravWellPluginDict[index]['Age'])+" and Type = "+GravWellPluginDict[index]['Type'])
			else:
				if GW:
					InfoList.append("Gravimetric Info:")
					if GW.IsOnline:
						InfoList.append("-Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.Radius))+" Kms")
						if GetConfigValue("GravDmgFactor") > 0:
							InfoList.append("-Damage Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.MaxDamageDistance))+" Kms")
						InfoList.append("-Age: "+GetStrFromFloat(GW.Age)+" Secs")
						InfoList.append("-Type: "+str(GW.Type))
					else:
						InfoList.append("-Gravity Generator Offline")
				InfoList.append("Ship Info:")
				InfoList.append("-Class: "+GetShipType(obj))
				InfoList.append("-Radius: "+GetStrFromFloat(ConvertGUtoKM(obj.GetRadius()))+" Kms")
				InfoList.append("-Mass: "+str(obj.GetMass()))
				lKeysList = WellForceDict.keys()
				if len(lKeysList) >= 1:
					InfoList.append("Affected By:")
					for sWellID in lKeysList:
						InfoList.append("-"+sWellID+": "+GetStrFromFloat(WellForceDict[sWellID])+" Km/h^2")
		elif obj.IsTypeOf(App.CT_SUN) or obj.IsTypeOf(App.CT_PLANET):
			GW = self.GetGravWellByID(obj.GetObjID())
			if GW:
				InfoList.append("Gravimetric Info:")
				InfoList.append("-Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.Radius))+" Kms")
				if GetConfigValue("GravDmgFactor") > 0:
					InfoList.append("-Damage Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.MaxDamageDistance))+" Kms")
			if obj.IsTypeOf(App.CT_SUN):
				InfoList.append("Sun Info:")
			else:
				InfoList.append("Planet Info:")
			InfoList.append("-Radius: "+GetStrFromFloat(ConvertGUtoKM(obj.GetRadius()))+" Kms")
			InfoList.append("-Density: "+GetStrFromFloat(obj.GetDensity())+" g/cm^3")
			InfoList.append("-Class: "+obj.GetClass())
			InfoList.append("-Mass: "+str(obj.GetMass()))
		elif obj.IsTypeOf(App.CT_WAYPOINT):
			pTGE = self.FindGravWellByID(obj.GetName())
			if pTGE:
				if pTGE.Lifetime == 0:
					sLife = "Endless"
				else:
					sLife = GetStrFromFloat(pTGE.Lifetime)+" Secs"
				InfoList.append("Gravimetric Info:")
				InfoList.append("-Radius: "+GetStrFromFloat(ConvertGUtoKM(pTGE.Radius))+" Kms")
				if GetConfigValue("GravDmgFactor") > 0:
					InfoList.append("-Damage Radius: "+GetStrFromFloat(ConvertGUtoKM(pTGE.MaxDamageDistance))+" Kms")
				InfoList.append("-Age: "+GetStrFromFloat(pTGE.Age)+" Secs")
				InfoList.append("-Lifetime: "+sLife)
				InfoList.append("-Type: "+str(pTGE.Type))
		return InfoList
	def GetObjListInSet(self, getmethod = 0, pSet = None):
		debug(__name__ + ", GetObjListInSet")
		List = []
		if pSet == None:
			pPlayer = App.Game_GetCurrentPlayer()
			if pPlayer:
				pSet = pPlayer.GetContainingSet()
			else:
				return List
		if pSet == None:
			return List
		pFirst = pSet.GetFirstObject()
		pObject = pSet.GetNextObject(pFirst.GetObjID())
		while pObject:
			if getmethod == 0:
				if pObject.IsTypeOf(App.CT_SUN):
					pSun = App.Sun_Cast(pObject)
					if pSun.IsAtmosphereObj() == None:
						List.append(pSun)	
				elif pObject.IsTypeOf(App.CT_PLANET):
					pPlanet = App.Planet_Cast(pObject)
					if pPlanet.IsAtmosphereObj() == None:
						List.append(pPlanet)
			elif getmethod == 1:
				if pObject.IsTypeOf(App.CT_SHIP):
					pShip = App.ShipClass_Cast(pObject)
					if CanBeAffected(pShip) == 1:
						List.append(pShip)
			elif getmethod == 2:
				if pObject.IsTypeOf(App.CT_SHIP):
					pShip = App.ShipClass_Cast(pObject)
					if CanBeAffected(pShip) == 1:
						List.append(pShip)
				elif pObject.IsTypeOf(App.CT_TORPEDO):
					pTorp = App.Torpedo_Cast(pObject)
					List.append(pTorp)
			pObject = pSet.GetNextObject(pObject.GetObjID())
			if pObject.GetObjID() == pFirst.GetObjID():
				break
		return List
	def GetPluginInfoForObj(self, obj):
		debug(__name__ + ", GetPluginInfoForObj")
		if obj.IsTypeOf(App.CT_TORPEDO):
			torp = App.Torpedo_Cast(obj)
			sType = GetTorpType(torp)
			if torp.GetPayloadType() != App.WeaponPayload.WP_TORPEDO or torp.GetGuidanceLifeTime() <= 0:
				return None
			if self.PluginBaseDict['Torpedoes'].has_key(sType):
				PluginBaseInfo = self.PluginBaseDict['Torpedoes'][sType]
				return PluginBaseInfo
			elif self.PluginBaseDict['Torpedoes'].has_key("AllAround"):
				PluginBaseInfo = self.PluginBaseDict['Torpedoes']["AllAround"]
				return PluginBaseInfo
			else:
				return None
	def GetAllWellsAffectingObj(self, obj):
		debug(__name__ + ", GetAllWellsAffectingObj")
		WellForceDict = {}
		if obj.IsTypeOf(App.CT_SHIP):
			pShip = App.ShipClass_Cast(obj)
			if CanBeAffected(pShip) == 0:
				return {}
		for GW in self.GravWellList:
			if IsShipWithinWell(obj, GW):
				if GW.GetParentID() != obj.GetObjID():
					if GW.CLASS == "Grav Well Plugin":
						if GW.IsOnline:
							GravForceKMH = GetGravForce(GW.Mass, DistanceCheck(GW.Parent, obj))
							WellForceDict[GW.Parent.GetName()] = GravForceKMH
					elif GW.CLASS == "Torp Grav Effect":
						GravForceKMH = GetGravForce(GW.Mass, DistanceCheck(GW.Parent, obj))
						WellForceDict[GW.TGEID] = GravForceKMH
					else:
						GravForceKMH = GetGravForce(GW.GetMass(), DistanceCheck(GW.Parent, obj))
						WellForceDict[GW.Parent.GetName()] = GravForceKMH
		return WellForceDict
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.GMID, "_")
		return l[len(l)-1]	
	def GetGravWell(self, name):
		debug(__name__ + ", GetGravWell")
		for GW in self.GravWellList:
			if GW.GetParentName() == name:
				return GW
		else:
			return None
	def GetGravWellByID(self, ID):
		debug(__name__ + ", GetGravWellByID")
		for GW in self.GravWellList:
			if GW.GetParentID() == ID:
				return GW
		else:
			return None
	def FindGravWellByID(self, nameID):
		debug(__name__ + ", FindGravWellByID")
		for GW in self.GravWellList:
			if GW.CLASS == "Grav Well Plugin":
				if GW.GWPID == nameID:
					return GW
			elif GW.CLASS == "Torp Grav Effect":
				if GW.TGEID == nameID:
					return GW				
			else:
				if GW.GWID == nameID:
					return GW
		else:
			return None
	def FindGravWellByCode(self, ID):
		debug(__name__ + ", FindGravWellByCode")
		for GW in self.GravWellList:
			if GW.GetObjID() == ID:
				return GW
		else:
			return None
	def DeleteGravWell(self, well):
		debug(__name__ + ", DeleteGravWell")
		GWindex = well.GetGWIndexInList()
		if GWindex:
			if well.CLASS == "Grav Well Plugin":
				well.Refresher.StopRefreshHandler()
			elif well.CLASS == "Torp Grav Effect":
				well.Parent.SetLifetime(0.0001)
				well.Refresher.StopRefreshHandler()
				well.NAVPoint.SetNavPoint(0)
				well.NAVPoint.__del__()
				well.NAVPoint = None
			well.ProxCheck.RemoveAndDelete()		
			del self.GravWellList[GWindex]
	def DeleteAllGravWells(self):
		debug(__name__ + ", DeleteAllGravWells")
		for GW in self.GravWellList:
			if GW.CLASS == "Grav Well Plugin":
				GW.Refresher.StopRefreshHandler()
			elif GW.CLASS == "Torp Grav Effect":
				GW.Parent.SetLifetime(0.0001)
				GW.Refresher.StopRefreshHandler()
				GW.NAVPoint.SetNavPoint(0)
				GW.NAVPoint.__del__()
				GW.NAVPoint = None
			GW.ProxCheck.RemoveAndDelete()
		self.GravWellList = []
	def _LogError(self, strFromFunc = None):
		debug(__name__ + ", _LogError")
		import sys
		et = sys.exc_info()
		if strFromFunc == None:
			strFromFunc = "???"
		if self.Logger:
			self.Logger.LogException(et, "ERROR at "+strFromFunc)
		else:
			error = str(et[0])+": "+str(et[1])
			print "ERROR at "+strFromFunc+", details -> "+error
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<" + self.GMID + ">"

class GravityWell:
	def __init__(self, planet):
		debug(__name__ + ", __init__")
		self.Parent = planet
		self.GWID = GetUniqueID(self.Parent.GetName()+" GravityWell")
		self.CLASS = "Gravity Well"
		self.Radius = GetMaxGravForceDist(self.Parent.GetMass())
		self.ProxCheck = MissionLib.ProximityCheck(self.Parent, -self.Radius, [], __name__ + ".ApplyGravForceHandler")
		self.ProxCheck.AddObjectTypeToCheckList(App.CT_SHIP)
		fGravDmgFac = GetConfigValue("GravDmgFactor")
		if fGravDmgFac > 0:
			self.MaxDamageDistance = self.Radius*(fGravDmgFac/100)+self.Parent.GetRadius()
		else:
			self.MaxDamageDistance = 0
		if GetConfigValue("LogGravWell"):
			self.Logger = Custom.GravityFX.Logger.LogCreator(self.GetParentName()+" GravityWell", "scripts\Custom\GravityFX\Logs\GravWellLOG_"+self.GetParentName()+".txt")
			self.Logger.LogString("Initialized "+self.GWID+" logger")
		else:
			self.Logger = Custom.GravityFX.Logger.DummyLogger()
		self.Logger.LogString(" <=====================================================>")
		self.LogStats()
	def ApplyGravForce(self, pObject, pEvent):
		#debug(__name__ + ", ApplyGravForce")
		if App.g_kUtopiaModule.IsGamePaused() == 1:
			return
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		pPlayer = MissionLib.GetPlayer()
		if pShip == None or pPlayer == None:
			return
		if IsObjInList(pShip, App.g_kGravityManager.ShipList) == 0:
			#Ship isn't on the Grav Manager ShipList, therefore she won't be affected by gravity
			return
		if IsStation(pShip):
			pSys = pShip.GetImpulseEngineSubsystem()
			if pSys:
				if pSys.IsSystemOnline():
					return
			else:
				pSys = pShip.GetPowerSubsystem()
				if pSys:
					if pSys.IsDisabled() == 0:
						return
		nDist = DistanceCheck(self.Parent, pShip)
		#print "Dist =", nDist, "MaxDist =", self.MaxDamageDistance			
		if self.MaxDamageDistance != 0 and nDist < self.MaxDamageDistance:
			DmgMass = GetMassByMaxDistance(ConvertGUtoKM(self.MaxDamageDistance))
			MaxDmg = GetGravForce(DmgMass, nDist)
			MinDmg = GetGravForce(DmgMass, self.MaxDamageDistance)
			DamageShip(pShip, MinDmg, MaxDmg)
			#print "Damaging ship"
			PlayCrushSound(pShip)
		if pShip.GetObjID() == pPlayer.GetObjID():
			if App.g_kGravityManager.PlayerCounterGravity == 1:
				pImpulseSys = pPlayer.GetImpulseEngineSubsystem()
				if pImpulseSys:
					if pImpulseSys.IsSystemOnline():
						return
		GravForceKMH = GetGravForce(self.Parent.GetMass(), nDist)
		GravForce = ConvertKMHtoImpulse(GravForceKMH)
		vGrav = GetVectorFromTo(self.Parent, pShip)
		vGrav.Scale(GravForce)
		vecGravForce = pShip.GetVelocityTG()
		vecGravForce.Add(vGrav)
		pShip.SetVelocity(vecGravForce)
	def GetGWIndexInList(self):
		debug(__name__ + ", GetGWIndexInList")
		index = 0
		for item in App.g_kGravityManager.GravWellList:
			if item == self:
				return index
			index = index + 1
		else:
			return None
	def LogStats(self):
		debug(__name__ + ", LogStats")
		self.Logger.LogString("Radius: "+str(self.Radius))
		self.Logger.LogString("Radius KM: "+str(ConvertGUtoKM(self.Radius)))
		self.Logger.LogString("Density: "+str(self.Parent.GetDensity()))
		self.Logger.LogString("Planet Radius: "+str(self.Parent.GetRadius()))
		self.Logger.LogString("Mass (From Radius): "+str(GetMassByMaxDistance(ConvertGUtoKM(self.Radius))))
		self.Logger.LogString("Mass (Get): "+str(self.GetMass()))
		self.Logger.LogString("Mass (Parent): "+str(self.Parent.GetMass()))
		self.Logger.LogString(" <=====================================================>")
	def UpdateRadius(self):
		debug(__name__ + ", UpdateRadius")
		nRad = GetMaxGravForceDist(self.GetMass())
		if self.Radius != nRad:
			self.Radius = nRad
			self.ProxCheck.SetRadius(self.Radius)
			if self.MaxDamageDistance != 0:
				fGravDmgFac = GetConfigValue("GravDmgFactor")
				self.MaxDamageDistance = self.Radius*(fGravDmgFac/100)+self.Parent.GetRadius()
			App.g_kGravityManager.Logger.LogString("Updated radius for grav well "+str(self)+", radius is now "+str(self.Radius))
			self.LogStats()
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.GWID, "_")
		return l[len(l)-1]
	def IsBlackhole(self):
		debug(__name__ + ", IsBlackhole")
		return 0
	def GetMass(self):
		debug(__name__ + ", GetMass")
		return self.Parent.GetMass()	
	def GetParentID(self):
		debug(__name__ + ", GetParentID")
		return self.Parent.GetObjID()
	def GetParentName(self):
		debug(__name__ + ", GetParentName")
		return self.Parent.GetName()
	def GetPCID(self):
		#debug(__name__ + ", GetPCID")
		return self.ProxCheck.GetObjID()
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<" + self.GWID + ">"
		
##############################################
class GravWellPlugin:
	def __init__(self, ship):
		debug(__name__ + ", __init__")
		self.Parent = ship
		self.ParentRadius = ship.GetRadius()
		self.GWPID = GetUniqueID(self.Parent.GetName()+" GravWellPlugin")
		self.CLASS = "Grav Well Plugin"
		self.Generator = GravGeneratorSystem(self)
		self.Mass = self.Generator.GetTotalMass()
		self.IsOnline = 1
		self.Type = self.Generator.Type
		self.Age = 0
		self.Radius = GetMaxGravForceDist(self.Mass)
		self.ProxCheck = MissionLib.ProximityCheck(self.Parent, -self.Radius, [], __name__ + ".ApplyGravForceHandler")
		self.ProxCheck.AddObjectTypeToCheckList(App.CT_SHIP)
		if self.Type == "Blackhole" or self.Type == "AntiGravWell":
			self.ProxCheck.AddObjectTypeToCheckList(App.CT_TORPEDO)
		self.Refresher = RefreshEventHandler(self.LifetimeLoop)
		fGravDmgFac = GetConfigValue("GravDmgFactor")
		if fGravDmgFac > 0:
			self.MaxDamageDistance = self.Radius*(fGravDmgFac/100)+self.ParentRadius
		else:
			self.MaxDamageDistance = 0
		if GetConfigValue("LogGravWellPlugins"):
			self.Logger = Custom.GravityFX.Logger.LogCreator(self.GetParentName()+" GravWellPlugin", "scripts\Custom\GravityFX\Logs\GravWellPluginLOG_"+self.GetParentName()+".txt")
			self.Logger.LogString("Initialized "+self.GWPID+" logger")
		else:
			self.Logger = Custom.GravityFX.Logger.DummyLogger()
		self.Logger.LogString("Radius: "+str(self.Radius))
		self.Logger.LogString("Mass: "+str(self.Mass))
		self.Logger.LogString("Type: \""+str(self.Type)+"\"")

	def ApplyGravForce(self, pObject, pEvent):
		debug(__name__ + ", ApplyGravForce")
		if self.IsOnline == 0:
			return
		self.Logger.LogString("AGF: stage Initial")
		if App.g_kUtopiaModule.IsGamePaused() == 1:
			return
		#self.Logger.LogString("AGF: stage 2")
		if self.Mass <= 0:
			# as this event happens faster than the lifetime loop, this check is here to ensure
			# that grav force won't be applied when the obj reached his lifetime and/or his mass reached 0.
			return
		#self.Logger.LogString("AGF: stage 3")
		if pEvent.GetDestination().IsTypeOf(App.CT_TORPEDO):
			pShip = App.Torpedo_Cast(pEvent.GetDestination())		
			self.Logger.LogString("AGF: stage 4.torp target")
			if pShip and pShip.GetParentID() == self.Parent.GetObjID():
				self.Logger.LogString("AGF: stage 5.torp from parent")
				return
		else:
			pShip = App.ShipClass_Cast(pEvent.GetDestination())
			#self.Logger.LogString("AGF: stage 4.B")
			if pShip and IsObjInList(pShip, App.g_kGravityManager.ShipList) == 0:
				#Ship isn't on the Grav Manager ShipList, therefore she won't be affected by gravity
				if IsStation(pShip) and self.Type == "Blackhole":
					self.Logger.LogString("AGF: stage 5.opt -> blackhole/station")
				else:
					self.Logger.LogString("AGF: stage 5")
					return
			if IsStation(pShip):
				pSys = pShip.GetImpulseEngineSubsystem()
				if pSys:
					if pSys.IsSystemOnline():
						self.Logger.LogString("AGF: ship was station, impulse ON")
						return
				else:
					pSys = pShip.GetPowerSubsystem()
					if pSys:
						if pSys.IsDisabled() == 0:
							self.Logger.LogString("AGF: ship was station, power ON")
							return
		#self.Logger.LogString("AGF: stage 6")
		if pShip == None:
			return
		#self.Logger.LogString("AGF: stage 7")
		#this is here to prevent the ship of this grav well plugin of affecting itself, thus creating a error
		if pShip.GetObjID() == self.Parent.GetObjID():
			return  
		#self.Logger.LogString("AGF: distance = "+str(DistanceCheck(self.Parent, pShip)))
		#self.Logger.LogString("AGF: target = "+str(pShip.GetName()))
		nDist = DistanceCheck(self.Parent, pShip)
		GravForceKMH = GetGravForce(self.Mass, nDist)
		#self.Logger.LogString("AGF: stage 9")
		GravForce = ConvertKMHtoImpulse(GravForceKMH)
		#self.Logger.LogString("AGF: stage 10")
		if self.Type == "AntiGravWell":
			self.Logger.LogString("AGF: stage 11.Anti grav")
			vGrav = GetVectorFromTo(pShip, self.Parent)
		else:
			self.Logger.LogString("AGF: stage 11.B")
			vGrav = GetVectorFromTo(self.Parent, pShip)
		#self.Logger.LogString("AGF: stage 12")
		vGrav.Scale(GravForce)
		#self.Logger.LogString("AGF: stage 13")
		vecGravForce = pShip.GetVelocityTG()
		#self.Logger.LogString("AGF: stage 14")
		vecGravForce.Add(vGrav)
		#self.Logger.LogString("AGF: stage 15")
		pShip.SetVelocity(vecGravForce)
		if self.MaxDamageDistance != 0 and nDist < self.MaxDamageDistance:
			if pShip.IsTypeOf(App.CT_SHIP):
				MaxDmg = GetGravForce(GetMassByMaxDistance(ConvertGUtoKM(self.MaxDamageDistance)), nDist)
				MinDmg = GetGravForce(GetMassByMaxDistance(ConvertGUtoKM(self.MaxDamageDistance)), self.MaxDamageDistance)
				DamageShip(pShip, MinDmg, MaxDmg)
				PlayCrushSound(pShip)
		self.Logger.LogString("AGF: stage Final")
	def LifetimeLoop(self, pObject, pEvent):
		debug(__name__ + ", LifetimeLoop")
		try:
			bIsShipTravelling =  App.g_kTravelManager.IsShipTravelling(self.Parent)
		except:
			bIsShipTravelling = 0
		bOnlineCheck = self.Generator.IsSystemOnline()
		if bIsShipTravelling == 1:
			# This ship is travelling, so we shut down our generators because we don't want gravity messing up
			# the travel.
			# This is actually a fail-safe, I'll also make that GravWellPlugins can't be created if the ship is
			# travelling.
			pPowerSys = None
			if bOnlineCheck == 1:
				self.Logger.LogString("Parent Ship is travelling, shutting down the grav generators.")
				self.Generator.SetAllPowerPercentage(0)
			bOnlineCheck = 0
		else:
			pPowerSys = self.Parent.GetPowerSubsystem()
		if pPowerSys:
			if self.Generator.IsSystemOnline():
				fPowerNeed = (self.GetPowerNeedPerSecond())/(1.0/self.Refresher.Delay)
				fPowerGot = pPowerSys.StealPower(fPowerNeed)
				fBackPowerGot = 0.0
				if fPowerGot < fPowerNeed:
					fBackPowerGot = pPowerSys.StealPowerFromReserve(fPowerNeed - fPowerGot)
				fPowerUsed = fPowerGot + fBackPowerGot
				if fPowerUsed < fPowerNeed:	bOnlineCheck = 0
			else:
				bOnlineCheck = 0
		self.IsOnline = bOnlineCheck
		if self.IsOnline:
			self.Mass = self.Generator.GetTotalMass()
			self.Age = self.Age + self.Refresher.Delay
			self.Radius = GetMaxGravForceDist(self.Mass)
			if self.MaxDamageDistance != 0:
				fGravDmgFac = GetConfigValue("GravDmgFactor")
				self.MaxDamageDistance = self.Radius*(fGravDmgFac/100)+self.ParentRadius
			self.ProxCheck.SetRadius(self.Radius)
	def GetGWIndexInList(self):
		debug(__name__ + ", GetGWIndexInList")
		index = 0
		for item in App.g_kGravityManager.GravWellList:
			if item == self:
				return index
			index = index + 1
		else:
			return None
	def SetOnline(self, bool):
		debug(__name__ + ", SetOnline")
		set = bool
		if set > 1:
			bool = 1.0
		elif set < 0:
			set = 0
		self.Generator.SetAllPowerPercentage(set)
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.GWPID, "_")
		return l[len(l)-1]
	def GetPowerNeedPerSecond(self):
		debug(__name__ + ", GetPowerNeedPerSecond")
		return self.Generator.GetTotalPowerNeedPerSecond()
	def IsBlackhole(self):
		debug(__name__ + ", IsBlackhole")
		if self.Type == "Blackhole":
			return 1
		else:
			return 0
	def GetMass(self):
		debug(__name__ + ", GetMass")
		return self.Mass	
	def GetParentID(self):
		debug(__name__ + ", GetParentID")
		return self.Parent.GetObjID()
	def GetParentName(self):
		debug(__name__ + ", GetParentName")
		return self.Parent.GetName()
	def GetPCID(self):
		debug(__name__ + ", GetPCID")
		return self.ProxCheck.GetObjID()
	def _LogError(self, strFromFunc = None):
		debug(__name__ + ", _LogError")
		import sys
		et = sys.exc_info()
		if strFromFunc == None:
			strFromFunc = "???"
		if self.Logger:
			self.Logger.LogException(et, "ERROR at "+strFromFunc)
		else:
			error = str(et[0])+": "+str(et[1])
			print "ERROR at "+strFromFunc+", details -> "+error
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<" + self.GWPID + ">"

##############################################
class TorpGravEffect:
	def __init__(self, torp, pPOS):
		debug(__name__ + ", __init__")
		PluginInfo = App.g_kGravityManager.GetPluginInfoForObj(torp)
		point = App.TGPoint3()
		point.SetXYZ(pPOS.x, pPOS.y, pPOS.z)
		self.TorpClass = GetTorpType(torp)
		self.Type = PluginInfo['Type']
		self.TGEID = GetUniqueID(self.TorpClass+" TorpGravEffect")
		self.CLASS = "Torp Grav Effect"
		self.Mass = PluginInfo['Mass']
		self.Lifetime = PluginInfo['Lifetime']
		self.Age = 0
		self.SoundDelay = PluginInfo['SoundDelay']
		self.SoundAge = 0
		self.Radius = GetMaxGravForceDist(self.Mass)
		color = App.TGColorA()
		color.SetRGBA(PluginInfo['ColorRed'], PluginInfo['ColorGreen'], PluginInfo['ColorBlue'], PluginInfo['ColorAlpha'])
		#now for the parent, a glow emmiter, we set it's lifetime to 31536000.0 seconds ( = to 1 year). Why?
		# because otherwise the glow emmiter will disappear before the right time and then BC will CRASH!
		# plus, a torp's lifetime decreases even when your game is paused...
		self.Parent = CreateGlowEmmiter(torp, point, torp.GetContainingSet(), 6.0, torp.GetRadius(), self.Radius, color, 31536000.0, torp.GetRadius())
		self.ParentRadius = self.Parent.GetRadius()
		fGravDmgFac = GetConfigValue("GravDmgFactor")
		if fGravDmgFac > 0:
			self.MaxDamageDistance = self.Radius*(fGravDmgFac/100)+self.ParentRadius
		else:
			self.MaxDamageDistance = 0
		self.ProxCheck = MissionLib.ProximityCheck(self.Parent, -self.Radius, [], __name__ + ".ApplyGravForceHandler")
		self.ProxCheck.AddObjectTypeToCheckList(App.CT_SHIP)
		if self.Type == "AntiGravTorpedo":
			self.ProxCheck.AddObjectTypeToCheckList(App.CT_TORPEDO)
			self.Sound = PlaySound("scripts\Custom\GravityFX\Sounds\TorpAntiGravEffect.wav", self.TGEID+"_Sound")			
		else:
			self.Sound = PlaySound("scripts\Custom\GravityFX\Sounds\TorpGravEffect.wav", self.TGEID+"_Sound")
		self.Refresher = RefreshEventHandler(self.LifetimeLoop)
		if self.Lifetime <= 0:
			self.Lifetime = 0
			self.AgingFactor = 0
		else:
			self.AgingFactor = self.Mass/(self.Lifetime/self.Refresher.Delay)
		self.NAVPoint = CreateNAVPoint(self.TGEID, torp.GetContainingSet(), point)
		if GetConfigValue("LogTorpGravEffects"):
			self.Logger = Custom.GravityFX.Logger.LogCreator(self.TorpClass+str(torp.GetObjID())+" TorpGravEffect", "scripts\Custom\GravityFX\Logs\TorpGravEffectLOG_"+self.TorpClass+str(torp.GetObjID())+".txt")
			self.Logger.LogString("Initialized "+self.TGEID+" logger")
		else:
			self.Logger = Custom.GravityFX.Logger.DummyLogger()
		self.Logger.LogString("Radius: "+str(self.Radius))
		self.Logger.LogString("Mass: "+str(self.Mass))
		self.Logger.LogString("Lifetime: "+str(self.Lifetime))
		self.Logger.LogString("Type: \""+str(self.Type)+"\"")

	def ApplyGravForce(self, pObject, pEvent):
		debug(__name__ + ", ApplyGravForce")
		self.Logger.LogString("AGF: stage Initial")
		if App.g_kUtopiaModule.IsGamePaused() == 1:
			return
		self.Logger.LogString("AGF: stage 2")
		if self.Lifetime != 0:
			if self.Age >= self.Lifetime or self.Mass <= 0:
				# as this event happens faster than the lifetime loop, this check is here to ensure
				# that grav force won't be applied when the obj reached his lifetime and/or his mass reached 0.
				return
		#self.Logger.LogString("AGF: stage 3")
		if pEvent.GetDestination().IsTypeOf(App.CT_TORPEDO):
			pShip = App.Torpedo_Cast(pEvent.GetDestination())
			self.Logger.LogString("AGF: stage 4.torp")		
		else:
			pShip = App.ShipClass_Cast(pEvent.GetDestination())
			if pShip and IsObjInList(pShip, App.g_kGravityManager.ShipList) == 0:
				#Ship isn't on the Grav Manager ShipList, therefore she won't be affected by gravity
				self.Logger.LogString("AGF: stage 4.ship.end")
				return
			if IsStation(pShip):
				pSys = pShip.GetImpulseEngineSubsystem()
				if pSys:
					if pSys.IsSystemOnline():
						self.Logger.LogString("AGF: ship was station, impulse ON")
						return
				else:
					pSys = pShip.GetPowerSubsystem()
					if pSys:
						if pSys.IsDisabled() == 0:
							self.Logger.LogString("AGF: ship was station, power ON")
							return
		self.Logger.LogString("AGF: stage 5")
		if pShip == None:
			return
		#self.Logger.LogString("AGF: stage 6")
		#this is here to prevent the ship of this grav well plugin of affecting itself, thus creating a error
		if pShip.GetObjID() == self.Parent.GetObjID():
			return
		self.Logger.LogString("AGF: stage 7")
		nDist = DistanceCheck(self.Parent, pShip)
		GravForceKMH = GetGravForce(self.Mass, nDist)
		try:
			pTravel = App.g_kTravelManager.GetTravel(pShip)
			if pTravel.Started == 1:
				self.Logger.LogString("AGF: stage 7 PLUS - target ship is travelling")
				fDistToOuter = self.Radius - nDist
				fChance = ((100.0*fDistToOuter)/self.Radius) - 50.0
				fFac = App.g_kSystemWrapper.GetRandomNumber(100)
				if fFac <= fChance:
					pTravel.Logger.LogString("Going to Drop Out of Travel by a torpedo gravity effect")
					pTravel.DropOutOfTravel()
				return
		except:
			pass
		GravForce = ConvertKMHtoImpulse(GravForceKMH)
		#self.Logger.LogString("AGF: stage 8")
		if self.Type == "AntiGravTorpedo":
			vGrav = GetVectorFromTo(pShip, self.Parent)
			self.Logger.LogString("AGF: stage 9.anti grav")
		else:
			vGrav = GetVectorFromTo(self.Parent, pShip)
			self.Logger.LogString("AGF: stage 9")
		vGrav.Scale(GravForce)
		#self.Logger.LogString("AGF: stage 10")
		vecGravForce = pShip.GetVelocityTG()
		#self.Logger.LogString("AGF: stage 11")
		vecGravForce.Add(vGrav)
		#self.Logger.LogString("AGF: stage 12")
		pShip.SetVelocity(vecGravForce)
		if self.MaxDamageDistance != 0 and nDist < self.MaxDamageDistance:
			if pShip.IsTypeOf(App.CT_SHIP):
				MaxDmg = GetGravForce(GetMassByMaxDistance(ConvertGUtoKM(self.MaxDamageDistance)), nDist)
				MinDmg = GetGravForce(GetMassByMaxDistance(ConvertGUtoKM(self.MaxDamageDistance)), self.MaxDamageDistance)
				DamageShip(pShip, MinDmg, MaxDmg)
				PlayCrushSound(pShip)
		self.Logger.LogString("AGF: stage Final")
	def LifetimeLoop(self, pObject, pEvent):
		debug(__name__ + ", LifetimeLoop")
		if self.Lifetime != 0:
			if self.Age >= self.Lifetime or self.Mass <= 0:
				self.Logger.LogString("Lifetime or mass ended, deleting torp grav effect")
				App.g_kGravityManager.DeleteTorpGravEffect(self)
		self.Age = self.Age + self.Refresher.Delay
		self.SoundAge = self.SoundAge + self.Refresher.Delay
		if self.SoundAge >= self.SoundDelay and self.SoundDelay != 0:
			self.Sound.Play()
			self.SoundAge = 0
		if self.Mass > 0:
			self.Radius = GetMaxGravForceDist(self.Mass)
			if self.MaxDamageDistance != 0:
				fGravDmgFac = GetConfigValue("GravDmgFactor")
				self.MaxDamageDistance = self.Radius*(fGravDmgFac/100)+self.ParentRadius
			self.ProxCheck.SetRadius(self.Radius)
		self.Logger.LogString("LL: Age = "+str(self.Age)+" // Radius = "+str(self.Radius))
		if self.Lifetime != 0:
			self.Mass = self.Mass - self.AgingFactor
	def GetGWIndexInList(self):
		debug(__name__ + ", GetGWIndexInList")
		index = 0
		for item in App.g_kGravityManager.GravWellList:
			if item == self:
				return index
			index = index + 1
		else:
			return None
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.TGEID, "_")
		return l[len(l)-1]
	def IsBlackhole(self):
		debug(__name__ + ", IsBlackhole")
		return 0	
	def GetMass(self):
		debug(__name__ + ", GetMass")
		return self.Mass
	def GetTorpType(self):
		debug(__name__ + ", GetTorpType")
		return self.TorpClass
	def GetParentID(self):
		debug(__name__ + ", GetParentID")
		return self.Parent.GetObjID()
	def GetParentName(self):
		debug(__name__ + ", GetParentName")
		return self.Parent.GetName()
	def GetPCID(self):
		debug(__name__ + ", GetPCID")
		return self.ProxCheck.GetObjID()
	def _LogError(self, strFromFunc = None):
		debug(__name__ + ", _LogError")
		import sys
		et = sys.exc_info()
		if strFromFunc == None:
			strFromFunc = "???"
		if self.Logger:
			self.Logger.LogException(et, "ERROR at "+strFromFunc)
		else:
			error = str(et[0])+": "+str(et[1])
			print "ERROR at "+strFromFunc+", details -> "+error
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<" + self.TGEID + ">"

################
class GravGeneratorSystem:
	PossibleNames = ["Gravity Generator", "Grav Generator", "Grav Gen", "GravityGenerator", "GravGenerator", "GravGen", "Anti-Gravity Generator", "Anti-Grav Generator", "Anti-Grav Gen", "AntiGravityGenerator", "AntiGravGenerator", "AntiGravGen", "Blackhole Generator", "Blackhole Gen", "BlackholeGenerator", "BlackholeGen"]

	def __init__(self, GW, lPossibleNames = []):
		debug(__name__ + ", __init__")
		self.CLASS = "Grav Generator"
		self.GGID = GetUniqueID(GW.Parent.GetName()+" GravGenerator")
		self.GravWell = GW
		self.Generators = GetGeneratorsOfShip(GW.Parent, lPossibleNames)
		self.GensPowerPercentage = {}
		self.GensIndexes = {}
		self.Type = "GravWell"
		if string.count(self.Generators[0].GetName(), "Anti") == 1:
			self.Type = "AntiGravWell"
		elif string.count(self.Generators[0].GetName(), "Blackhole") == 1:
			self.Type = "Blackhole"
		for i in range(len(self.Generators)):
			self.GensPowerPercentage[i] = 1.0
			pGen = self.Generators[i]
			self.GensIndexes[pGen.GetObjID()] = i
	def GetTotalPowerNeedPerSecond(self):
		debug(__name__ + ", GetTotalPowerNeedPerSecond")
		ret = 0
		lOnGens = self.GetOnlineGenerators()
		for pGen in lOnGens:
			ret = ret + ((pGen.GetRadius() * pGen.GetRepairComplexity()) * 50 * self.GetPowerPercentageOfGen(pGen))
		return ret
	def GetTotalMass(self):
		debug(__name__ + ", GetTotalMass")
		mass = self.GravWell.Parent.GetMass()
		lOnGens = self.GetOnlineGenerators()
		for pGen in lOnGens:
			mass = mass+(self.GravWell.Parent.GetMass()*(pGen.GetRadius()*pGen.GetRepairComplexity()*self.GetPowerPercentageOfGen(pGen)))
		return mass
	def GetOnlineGenerators(self):
		debug(__name__ + ", GetOnlineGenerators")
		list = []
		for pGen in self.Generators:
			if not (pGen.GetCondition() <= 0):
				if pGen.IsDisabled() == 0:
					list.append(pGen)
		return list
	def GetPowerPercentageOfGenIN(self, index):
		debug(__name__ + ", GetPowerPercentageOfGenIN")
		pGen = self.GetGenerator(index)
		if pGen:
			return self.GensPowerPercentage[index]
	def SetPowerPercentageOfGenIN(self, index, powerper):
		debug(__name__ + ", SetPowerPercentageOfGenIN")
		pGen = self.GetGenerator(index)
		if pGen:
			self.GensPowerPercentage[index] = powerper
	def GetPowerPercentageOfGen(self, pGen):
		debug(__name__ + ", GetPowerPercentageOfGen")
		if pGen:
			return self.GensPowerPercentage[self.GensIndexes[pGen.GetObjID()]]
	def SetPowerPercentageOfGen(self, pGen, powerper):
		debug(__name__ + ", SetPowerPercentageOfGen")
		if pGen:
			self.GensPowerPercentage[self.GensIndexes[pGen.GetObjID()]] = powerper
	def SetAllPowerPercentage(self, powerper):
		debug(__name__ + ", SetAllPowerPercentage")
		for i in range(self.GetNumGenerators()):
			self.GensPowerPercentage[i] = powerper
	def GetNumGenerators(self):
		debug(__name__ + ", GetNumGenerators")
		return len(self.Generators)
	def GetGenerator(self, index):
		debug(__name__ + ", GetGenerator")
		if 0 <= index <= self.GetNumGenerators() - 1:
			return self.Generators[index]
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.GGID, "_")
		return l[len(l)-1]
	def IsSystemOnline(self):
		debug(__name__ + ", IsSystemOnline")
		lGensOn = self.GetOnlineGenerators()
		ret = 0
		for pGen in lGensOn:
			if self.GensPowerPercentage[self.GensIndexes[pGen.GetObjID()]] > 0:
				ret = 1
		return ret
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<" + self.GGID + ">"

###################################################################################################
# The Apply Grav Force Handler
# this exists because i still didn't find a way to make the Prox Checks call a function from his GravWell instance.
###################################################################################################
def ApplyGravForceHandler(pObject, pEvent):
	#debug(__name__ + ", ApplyGravForceHandler")
	ProxCheck = pEvent.GetProximityCheck()
	for GravWell in App.g_kGravityManager.GravWellList:
		if GravWell.GetPCID() == ProxCheck.GetObjID():
			GravWell.ApplyGravForce(pObject, pEvent)

###################################################################################################
# The Handle Grav Torps handler
# this exists because i still didn't find a way to make the AddBroadcastPythonFuncHandler call a function
# from his GravManager instance...
###################################################################################################
def HandleGravTorps(pObject, pEvent):
	debug(__name__ + ", HandleGravTorps")
	pTorp = App.Torpedo_Cast(pEvent.GetSource()) 
	if pTorp and pTorp.IsTypeOf(App.CT_TORPEDO) and pTorp.GetPayloadType() == App.WeaponPayload.WP_TORPEDO and pTorp.GetGuidanceLifeTime() > 0:
		PluginInfo = App.g_kGravityManager.GetPluginInfoForObj(pTorp)
		if PluginInfo:
			pTGE = App.g_kGravityManager.CreateTorpGravEffect(pTorp, pEvent.GetWorldHitPoint())

#######################################################################################################
# HELPER FUNCTIONS
# functions to check if a ship can be affected by gravity  and other misc functions
#  this exists because ships like stations, asteroids, probes, firepoints, etc. can't be affected by gravity in-game
#  or it will cause problems.
#
# GetGeneratorsOfShip(pShip, lPossibleNames = []) --> return a list of gravity generators on given ship.
#				it checks for the gravity generators using the names in the lPossibleNames sting list, defaults to
#				["Gravity Generator", "Grav Generator", "Grav Gen", "GravityGenerator", "GravGenerator", "GravGen",
#		 "Anti-Gravity Generator", "Anti-Grav Generator", "Anti-Grav Gen", "AntiGravityGenerator", "AntiGravGenerator",
#		 "AntiGravGen"].
# CheckNoGravShipTypes --> returns 1 if the pShip can't be affected by gravity
#				   Check how to create a plugin to a ship not be affected by Grav in the readme.
#					Bear in mind that this should only be added to ships that WON'T be affected by grav
#					because problems with other mods migth occur, like firepoints, if they were affected by gravity
#					the BlindFire mod, and others that use the Firepoint ship, would had problems because their firepoints
#					are being pulled towards a planet.
# CanBeAffected --> Checks if pShip(parameter) can be affected by gravity.
#			  To do it checks if she's a not-to-be-affected ship, if she's a real ship, or if she's a station and
#			  the option to affect stations is on.
# CreatePluginBase --> returns a dict containing the info on the ships/torps plugins created for GravityFX.
# GetShipType --> helper for CheckNoGravShipType
#			returns pShips's ship script string (name)
#######################################################################################################
def GetGeneratorsOfShip(pShip, lPossibleNames = []):
	debug(__name__ + ", GetGeneratorsOfShip")
	if lPossibleNames == []:
		lPossibleNames = GravGeneratorSystem.PossibleNames
	lSubsystems = []
	for sName in lPossibleNames:
		lSubsystems = GetSubsystemsOfName(pShip, sName)
		if len(lSubsystems) > 0:
			break
	return lSubsystems

def CheckNoGravShipType(pShip):
	debug(__name__ + ", CheckNoGravShipType")
	sType = GetShipType(pShip)
	if App.g_kGravityManager.PluginBaseDict['Ships'].has_key(sType):
		PluginBaseInfo = App.g_kGravityManager.PluginBaseDict['Ships'][sType]
		if PluginBaseInfo['Type'] == "NotToBeAffected":
			return 1
		else:
			return 0
	else:
		return 0

def CanBeAffected(pShip):
	debug(__name__ + ", CanBeAffected")
	if CheckNoGravShipType(pShip) == 0:
		pShipProp = pShip.GetShipProperty()
		if pShipProp.GetGenus() == 1 and pShipProp.IsStationary() == 0:
			return 1
		elif IsStation(pShip) == 1 and GetConfigValue("AffectStations") == 1:
			return 1
		else:
			return 0
	else:
		return 0

def CreatePluginBase():	
	debug(__name__ + ", CreatePluginBase")
	PluginList = nt.listdir('scripts/Custom/GravityFX/Plugins')
	PluginList.remove('__init__.py')
	MainDict = {'Ships': {}, 'Torpedoes': {}}
	for sFile in PluginList:
		sFileStrings = string.split(sFile, '.')
		sPlugin = sFileStrings[0]
		sExt = sFileStrings[-1]
		if sExt == "py":
			pModule = __import__("Custom.GravityFX.Plugins." + sPlugin)
			InfoDict = {}
			if sPlugin == "NotToBeAffectedShips":
				for sShipScriptName in pModule.lShips:
					MainDict['Ships'][sShipScriptName] = {'Type': "NotToBeAffected"}
			else:
				sPluginType = pModule.PluginType
				InfoDict['Type'] = sPluginType
				if sPluginType == "GravTorpedo" or sPluginType == "AntiGravTorpedo":
					InfoDict['Lifetime'] = pModule.Lifetime
					InfoDict['Mass'] = pModule.Mass
					InfoDict['SoundDelay'] = pModule.SoundDelay
					InfoDict['ColorRed'] = pModule.ColorRed
					InfoDict['ColorGreen'] = pModule.ColorGreen
					InfoDict['ColorBlue'] = pModule.ColorBlue
					InfoDict['ColorAlpha'] = pModule.ColorAlpha
					MainDict['Torpedoes'][sPlugin] = InfoDict
				elif sPluginType == "NotToBeAffected":
					MainDict['Ships'][sPlugin] = InfoDict
	return MainDict


def GetShipType(pShip):
	debug(__name__ + ", GetShipType")
	if pShip.GetScript():
		return string.split(pShip.GetScript(), '.')[-1]
	return None

def GetTorpType(pTorp):
	debug(__name__ + ", GetTorpType")
	if pTorp.GetModuleName():
		return string.split(pTorp.GetModuleName(), '.')[-1]
	return None

def PlayCrushSound(pShip, chance = 4):
	debug(__name__ + ", PlayCrushSound")
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer and pShip.GetObjID() == pPlayer.GetObjID():
		x = App.g_kSystemWrapper.GetRandomNumber(100)
		if x <= chance:			
			PlayRandomCrushSound()

def PlayRandomCrushSound():
	debug(__name__ + ", PlayRandomCrushSound")
	SoundNamesDict = {'sfx\Explosions': ['collision1.wav', 'collision2.wav', 'collision3.wav', 'collision4.wav', 'collision5.wav', 'collision6.wav', 'collision7.wav', 'collision8.wav', 'explo1.wav', 'explo10.wav', 'explo11.wav', 'explo12.wav', 'explo13.wav', 'explo14.wav', 'explo15.wav', 'explo16.wav', 'explo17.wav', 'explo18.wav', 'explo19.wav', 'explo2.wav', 'explo3.wav', 'explo4.wav', 'explo5.wav', 'explo6.wav', 'explo7.wav', 'explo8.wav', 'explo9.wav', 'explo_flame_01.wav', 'explo_flame_02.wav', 'explo_flame_03.wav', 'explo_flame_04.wav', 'explo_flame_05.wav', 'explo_flame_06.wav', 'explo_flame_07.wav', 'explo_flame_08.wav', 'explo_flame_09.wav', 'explo_flame_10.wav', 'explo_large_01.wav', 'explo_large_02.wav', 'explo_large_03.wav', 'explo_large_04.wav', 'explo_large_05.wav', 'explo_large_06.wav', 'explo_large_07.wav', 'explo_large_08.wav'],
	 'scripts\Custom\NanoFXv2\ExplosionFX\Sfx\ExpCollision': ['Collision_Nano1.wav', 'Collision_Nano2.wav', 'Collision_Nano3.wav', 'Collision_Nano4.wav', 'Collision_Nano5.wav', 'Collision_Nano6.wav', 'Collision_Nano7.wav', 'Collision_Nano8.wav'],
	 'scripts\Custom\NanoFXv2\ExplosionFX\Sfx\ExpSmall': ['small 10.wav', 'small 11.wav', 'small 12.wav', 'small 13.wav', 'small 14.wav', 'small 15.wav', 'small 16.wav', 'small 17.wav', 'small 27.wav', 'small 28.wav', 'small 29.wav', 'small 30.wav', 'small 31.wav', 'small 33.wav', 'small 34.wav', 'small 35.wav', 'small 37.wav', 'small 38.wav', 'small 39.wav', 'small 40.wav', 'small 41.wav', 'small 47.wav', 'small 48.wav', 'small 49.wav'],
###	 'scripts\Custom\NanoFXv2\ExplosionFX\Sfx\ExpMed': ['med 01.wav', 'med 04.wav', 'med 05.wav', 'med 06.wav', 'med 07.wav', 'med 08.wav', 'med 11.wav', 'med 12.wav', 'med 13.wav', 'med 14.wav', 'med 16.wav', 'med 17.wav', 'med 18.wav', 'med 19.wav', 'med 26.wav', 'med 29.wav', 'med 30.wav', 'med 31.wav', 'med 32.wav', 'med 37.wav'],
	 'scripts\Custom\GravityFX\Sounds\Crush': ['ship_creak_low1.wav', 'ship_creak_low2.wav', 'ship_creak_low3.wav', 'ship_creak_low5.wav','ship_creak_medium1.wav', 'ship_creak_medium2.wav', 'ship_creak_medium3.wav', 'ship_creak_rattle1.wav']
}
	NCSpath = 'scripts\Custom\NanoFXv2\ExplosionFX\Sfx\ExpCollision'
	try:
		NanoCollisionsSounds = nt.listdir(NCSpath)
		for s in SoundNamesDict[NCSpath]:
			if s not in NanoCollisionsSounds:
				SoundNamesDict[NCSpath].remove(s)
	except:
		del SoundNamesDict[NCSpath]
	#########
	NESSpath = 'scripts\Custom\NanoFXv2\ExplosionFX\Sfx\ExpSmall'
	try:
		NanoExpSmallSounds = nt.listdir(NESSpath)
		for s in SoundNamesDict[NESSpath]:
			if s not in NanoExpSmallSounds:
				SoundNamesDict[NESSpath].remove(s)
	except:
		del SoundNamesDict[NESSpath]
	#########
	#NEMSpath = 'scripts\Custom\NanoFXv2\ExplosionFX\Sfx\ExpMed'
	#try:
	#	NanoExpMedSounds = nt.listdir(NEMSpath)
	#	for s in SoundNamesDict[NEMSpath]:
	#		if s not in NanoExpMedSounds:
	#			SoundNamesDict[NEMSpath].remove(s)
	#except:
	#	del SoundNamesDict[NEMSpath]
	#######################################################################
	dictindex = App.g_kSystemWrapper.GetRandomNumber(len(SoundNamesDict.keys()))
	soundpath = SoundNamesDict.keys()[dictindex]
	listindex = App.g_kSystemWrapper.GetRandomNumber(len(SoundNamesDict[soundpath]))
	soundName = SoundNamesDict[soundpath][listindex]
	pSound = PlaySound(soundpath+"\\"+soundName, "GravityFX-CrushSound-"+soundName)
	return pSound

#################################################################
#Helper functions for testing
#################################################################
def PrintObjList(getships = None):
	debug(__name__ + ", PrintObjList")
	l = GetObjListInSet(getships)
	print "List has", len(l), " objects."
	for item in l:
		if item.IsTypeOf(App.CT_TORPEDO):
			print GetTorpType(item)	
		else:
			print item.GetName(), item.GetMass()
	return

def PrintVector(vec, name = "Vector"):
	debug(__name__ + ", PrintVector")
	print "///"+name+"=", vec.x, vec.y, vec.z, vec.Length()
#################################################################
#################################################################
### Unbound functions of App.Planet class
##  used for getting the mass, or getting/setting the density
#################################################################
####GetMass
##return --> mass in Kg
def GetMass(self):
	debug(__name__ + ", GetMass")
	nDensity = self.GetDensity()
	# Now we get the radius, and we have a problem here because in BC the radius is in Game Units, 1 KM = approx 5.71428 GUs
	# To calculate the mass we need the radius in KMs, not in GUs. But if we convert the value to KMs the radius will be 
	# small, then the Mass will be smaller too, and gravity will be less noticeable...
	# So, in order to have a more noticeable gravity (even in GravForceXvalue 1), we will use the radius (GUs), as if it was in KMs...
	radius = self.GetRadius()
	nKesph = 4.0/3.0
	vol = nKesph*math.pi*math.pow(radius, 3)
	mass = (nDensity*math.pow(10, 12))*vol
	return mass

###############################
# This dict keeps tracks of the density of planets (by ID)
################################
PlanetDensityDict = {'Default': 5.515}

####GetDensity
##returns the density value of the planet
##if the planet doesn't have a density value set, this will return the default value, 5.515 (Earth's density), 
## also remember, the density value is in g/cm^3, earth's density is 5.515g/cm^3
def GetDensity(self):
	debug(__name__ + ", GetDensity")
	if PlanetDensityDict.has_key(self.GetObjID()):
		return PlanetDensityDict[self.GetObjID()]
	else:
		return PlanetDensityDict['Default']

####SetDensity
## value --> density value to be set, remember the density value is in g/cm^3
## return ==> nothing
def SetDensity(self, value):
	debug(__name__ + ", SetDensity")
	PlanetDensityDict[self.GetObjID()] = value
	return
