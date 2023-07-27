#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         DampeningAOEDefensiveField.py by Alex SL Gato
#         Version 0.3
#         27th July 2023
#         Based on scripts\Custom\DS9FX\DS9FXPulsarFX\PulsarManager by USS Sovereign, Inversion Beam and Power Drain Beam 1.0 by MLeo Daalder, Apollo, and Dasher; and GraviticLance by Alex SL Gato, which was based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/Shields by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team. Also based on PhaseCloak.py by MLeo, Apollo and Dasher.
#                          
#################################################################################################################
# This tech basically makes the ship unhurtable until a shield is breached and a hit comes from there.
# Usage Example:  Add this (the lines under the triple ") to the dTechs attribute of your ShipDef, in the Ship plugin file (replace "Sovereign" with the proper abbrev).
'''
Foundation.ShipDef.Sovereign.dTechs = {
	"Dicohesive Tech Shields": {}
}
'''
# Ok so for the moment I need people to add these hardpoint properties to the ship they want to use with this tech, the ship uses that for reference
'''
################################################
# THESE ARE ONLY FOR THE DICOHESIVE 0.2 MOD
#################################################
FrontShieldIndicator = App.HullProperty_Create("FrontShieldIndicator")

FrontShieldIndicator.SetMaxCondition(1.000000)
FrontShieldIndicator.SetCritical(0)
FrontShieldIndicator.SetTargetable(0)
FrontShieldIndicator.SetPrimary(0)
FrontShieldIndicator.SetPosition(0.000000, 100.300000, 0.000000)
FrontShieldIndicator.SetPosition2D(0.000000, 0.000000)
FrontShieldIndicator.SetRepairComplexity(0.000001)
FrontShieldIndicator.SetDisabledPercentage(0.000000)
FrontShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(FrontShieldIndicator)
#################################################
BackShieldIndicator = App.HullProperty_Create("BackShieldIndicator")

BackShieldIndicator.SetMaxCondition(1.000000)
BackShieldIndicator.SetCritical(0)
BackShieldIndicator.SetTargetable(0)
BackShieldIndicator.SetPrimary(0)
BackShieldIndicator.SetPosition(0.000000, -100.300000, 0.000000)
BackShieldIndicator.SetPosition2D(0.000000, 0.000000)
BackShieldIndicator.SetRepairComplexity(0.000001)
BackShieldIndicator.SetDisabledPercentage(0.000000)
BackShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(BackShieldIndicator)
#################################################
PortShieldIndicator = App.HullProperty_Create("PortShieldIndicator")

PortShieldIndicator.SetMaxCondition(1.000000)
PortShieldIndicator.SetCritical(0)
PortShieldIndicator.SetTargetable(0)
PortShieldIndicator.SetPrimary(0)
PortShieldIndicator.SetPosition(-100.300000, 0.000000, 0.000000)
PortShieldIndicator.SetPosition2D(0.000000, 0.000000)
PortShieldIndicator.SetRepairComplexity(0.000001)
PortShieldIndicator.SetDisabledPercentage(0.000000)
PortShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortShieldIndicator)
#################################################
StarShieldIndicator = App.HullProperty_Create("StarShieldIndicator")

StarShieldIndicator.SetMaxCondition(1.000000)
StarShieldIndicator.SetCritical(0)
StarShieldIndicator.SetTargetable(0)
StarShieldIndicator.SetPrimary(0)
StarShieldIndicator.SetPosition(100.300000, 0.000000, 0.000000)
StarShieldIndicator.SetPosition2D(0.000000, 0.000000)
StarShieldIndicator.SetRepairComplexity(0.000001)
StarShieldIndicator.SetDisabledPercentage(0.000000)
StarShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarShieldIndicator)
#################################################
TopShieldIndicator = App.HullProperty_Create("TopShieldIndicator")

TopShieldIndicator.SetMaxCondition(1.000000)
TopShieldIndicator.SetCritical(0)
TopShieldIndicator.SetTargetable(0)
TopShieldIndicator.SetPrimary(0)
TopShieldIndicator.SetPosition(0.000000, 0.000000, 100.300000)
TopShieldIndicator.SetPosition2D(0.000000, 0.000000)
TopShieldIndicator.SetRepairComplexity(0.000001)
TopShieldIndicator.SetDisabledPercentage(0.000000)
TopShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(TopShieldIndicator)
#################################################
BottomShieldIndicator = App.HullProperty_Create("BottomShieldIndicator")

BottomShieldIndicator.SetMaxCondition(1.000000)
BottomShieldIndicator.SetCritical(0)
BottomShieldIndicator.SetTargetable(0)
BottomShieldIndicator.SetPrimary(0)
BottomShieldIndicator.SetPosition(0.000000, 0.000000, -100.300000)
BottomShieldIndicator.SetPosition2D(0.000000, 0.000000)
BottomShieldIndicator.SetRepairComplexity(0.000001)
BottomShieldIndicator.SetDisabledPercentage(0.000000)
BottomShieldIndicator.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(BottomShieldIndicator)
################################################
################################################
'''
# At the end of the LoadProperties
'''
	prop = App.g_kModelPropertyManager.FindByName("FrontShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("BackShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("PortShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("StarShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("TopShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("BottomShieldIndicator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
'''

import App
import FoundationTech

from bcdebug import debug
import traceback

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.3",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.corboniteReflector() in Apollo's Advanced Technologies.

try:

	pAllShipsWithTheTech = {} # Has the ship, with the pInstances as keys

	class DicohesiveTechVoidDef(FoundationTech.TechDef):

		#def __init__(self, name):
		#	FoundationTech.TechDef.__init__(self, name)
		#	self.pEventHandler = App.TGPythonInstanceWrapper()
		#	self.pEventHandler.SetPyWrapper(self)
		#	App.g_kEventManager.RemoveBroadcastHandler(App.ET_SHIELD_COLLISION, self.pEventHandler, "ShieldChange")
		#	App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_SHIELD_COLLISION, self.pEventHandler, "ShieldChange")
		#	print "Initialized Dicohesive Tech Shields"

		def OnDefense(self, pShip, pInstance, oYield, pEvent):
			debug(__name__ + ", OnDefense")

			if not pShip:
				return
			# position of the impact
			kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())
			fRadius = pEvent.GetRadius()
			fDamage = pEvent.GetDamage()

			pShields = pShip.GetShields()
			shieldHitBroken = 0
			if not pShields or pShields.IsDisabled():
				shieldHitBroken = 1
				pShip.SetVisibleDamageRadiusModifier(1.0)
				pShip.SetVisibleDamageStrengthModifier(1.0)

				while pSubsystem:
					self.StoreHurt(pInstance, pSubsystem, shieldHitBroken, fDamage, pShip, fRadius, kPoint)
					pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

				pShip.EndGetSubsystemMatch(pIterator)
				return
			pShields.TurnOn()
			if not pInstance.__dict__['Dicohesive Tech Shields'].has_key("Systems"):
				pInstance.__dict__['Dicohesive Tech Shields']["Systems"] = {}

			# get the references on the right lists
			# 0 is front, 1 is back, 2 is top, 3 is bottom, 4 is left, 5 is right
			nReferencias = ["FrontShieldIndicator", "BackShieldIndicator", "TopShieldIndicator", "BottomShieldIndicator", "PortShieldIndicator", "StarShieldIndicator"]
			lReferencias = []
			kIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			while (1):
				pSubsystem = pShip.GetNextSubsystemMatch(kIterator)
				if not pSubsystem:
					break
				if pSubsystem.GetName() in nReferencias:
					lReferencias.append(pSubsystem)

			pShip.EndGetSubsystemMatch(kIterator)

			# get the nearest reference
			pReferenciado = None
			dMasCercano = 0
			bPlateDisabled = 0
			print "lReferencias es ", lReferencias
			for pPunto in lReferencias:
				print pPunto.GetName()
				vDifference = NiPoint3ToTGPoint3(pPunto.GetPosition())
				vDifference.Subtract(kPoint)
				print vDifference.Length()
				if pReferenciado == None or vDifference.Length() < dMasCercano:
					dMasCercano = vDifference.Length()
					pReferenciado = pPunto.GetName()

			if not pReferenciado: # Something went wrong, but it is better to keep recording the damage
				print "Something went wrong when finding references, ship will likely be immortal"
				pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
				while pSubsystem:
					self.StoreHurt(pInstance, pSubsystem, shieldHitBroken, fDamage, pShip, fRadius, kPoint)
					pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
				pShip.EndGetSubsystemMatch(pIterator)
				return
			shieldDir = nReferencias.index(pReferenciado)
			#for shieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
				#print shieldDir
			fCurr = pShields.GetCurShields(shieldDir)
			#print fCurr
			fMax = pShields.GetMaxShields(shieldDir)
			if fCurr < 0.10 * fMax:
				if fCurr < 0.05 * fMax:
					shieldHitBroken = 1
				nerf = fCurr - fDamage
				if nerf < 0:
					nerf = 0
				pShields.SetCurShields(shieldDir, nerf)


			pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			#print "pEvent.IsHullHit() and shieldHitBroken for shieldir of name", pEvent.IsHullHit(), shieldHitBroken, shieldDir, pReferenciado
			if pEvent.IsHullHit() and shieldHitBroken == 1: #TO-DO and things
				#print "Hurt"
				pShip.SetVisibleDamageRadiusModifier(1.0)
				pShip.SetVisibleDamageStrengthModifier(1.0)

				while pSubsystem:
					self.StoreHurt(pInstance, pSubsystem, shieldHitBroken, fDamage, pShip, fRadius, kPoint)
					pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

				pShip.EndGetSubsystemMatch(pIterator)

			else:
				#print "Heal"
				pShip.SetInvincible(1)
				pShip.SetVisibleDamageRadiusModifier(0.0)
				pShip.SetVisibleDamageStrengthModifier(0.0)

				while pSubsystem:
					self.Heal(pInstance, pSubsystem)
					pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			pShip.EndGetSubsystemMatch(pIterator)

		def Heal(self, pInstance, pSubsystem):
			if not pInstance.__dict__['Dicohesive Tech Shields']["Systems"].has_key(pSubsystem.GetName()):
				pInstance.__dict__['Dicohesive Tech Shields']["Systems"][pSubsystem.GetName()] = pSubsystem.GetMaxCondition()
			if pSubsystem.GetCondition() > pInstance.__dict__['Dicohesive Tech Shields']["Systems"][pSubsystem.GetName()]:
				pInstance.__dict__['Dicohesive Tech Shields']["Systems"][pSubsystem.GetName()] = pSubsystem.GetCondition()

			pSubsystem.SetCondition(pInstance.__dict__['Dicohesive Tech Shields']["Systems"][pSubsystem.GetName()])
			iChildren = pSubsystem.GetNumChildSubsystems()
			if iChildren > 0:
				for iIndex in range(iChildren):
					pChild = pSubsystem.GetChildSubsystem(iIndex)
					self.Heal(pInstance, pChild)

		def StoreHurt(self, pInstance, pSubsystem, shieldHitBroken, fDamage, pShip, fRadius, kPoint):
			pInstance.__dict__['Dicohesive Tech Shields']["Systems"][pSubsystem.GetName()] = pSubsystem.GetCondition()
			if shieldHitBroken == 1 and pSubsystem.IsCritical() and pSubsystem.GetCondition() < fDamage:
				iamarmoredunderneath = pInstance.__dict__.has_key('Adv Armor Tech')
				vDifference = NiPoint3ToTGPoint3(pSubsystem.GetPosition())
				vDifference.Subtract(kPoint)
				if vDifference.Length() < fRadius and not iamarmoredunderneath:
					pShip.SetInvincible(0)
					pShip.DestroySystem(pSubsystem)
					return
			iChildren = pSubsystem.GetNumChildSubsystems()
			if iChildren > 0:
				for iIndex in range(iChildren):
					pChild = pSubsystem.GetChildSubsystem(iIndex)
					self.StoreHurt(pInstance, pChild, shieldHitBroken, fDamage, pShip)

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
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None:
				global pAllShipsWithTheTech

				#pGame = App.Game_GetCurrentGame()
				#pEpisode = pGame.GetCurrentEpisode()
				#pMission = pEpisode.GetCurrentMission()

				#print "script of the ship is ", pShip.GetScript()
				#pPropertySet = pShip.GetPropertySet()
				#mod = __import__('Custom.Techs.DicohesiveShieldsReference')
				#mod.LoadPropertySet(pPropertySet)

				#pShip.SetupProperties()
				#mod = __import__('Custom.Techs.DicohesiveShieldsReference')
				#pShip.Update() # TO-DO comprueba que esto funciona
				#pShip.UpdateNodeOnly()
				#if pShip.GetName() == pGame.GetPlayer().GetName():
				#	pShip = pGame.GetPlayer()
				#	pGame.SetPlayer(pShip)

				dMasterDict = pInstance.__dict__['Dicohesive Tech Shields']
				pAllShipsWithTheTech[pInstance] = pShip

				pShip.SetInvincible(1)
				pHull=pShip.GetHull()
				hull_max=pHull.GetMaxCondition()
				pHull.SetCondition(hull_max)
				pCloak = pShip.GetCloakingSubsystem()
				if pCloak:
					pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_COMPLETED, __name__ + ".CloakHandler")
					pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
					pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")
			pInstance.lTechs.append(self)
			pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
			pInstance.lPulseDefense.insert(0, self)
			pInstance.lBeamDefense.insert(0, self)
			# print 'Attaching Dicohesive Shields to', pInstance, pInstance.__dict__

		def Detach(self, pInstance):		
			pInstance.lTechs.remove(self)
			pInstance.lTorpDefense.remove(self)
			pInstance.lPulseDefense.remove(self)
			pInstance.lBeamDefense.remove(self)
		
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip:
				pCloak = pShip.GetCloakingSubsystem()
				if pCloak:
					pShip.RemoveHandlerForInstance(App.ET_CLOAK_COMPLETED, __name__ + ".CloakHandler")
					pShip.RemoveHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
					pShip.RemoveHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")

		# def Activate(self):
		# 	FoundationTech.oWeaponHit.Start()
		# def Deactivate(self):
		# 	FoundationTech.oWeaponHit.Stop()

		#def ShieldChange(self, pEvent):
		#	pTarget = App.ShipClass_Cast(pEvent.GetDestination())
		#	if pTarget == None:
		#		#print "Dicohesive Tech Shields: cancelling, no target"
		#		return
		#      # This is a stub, not wholly necessary yet	

	oDicohesiveTechVoid = DicohesiveTechVoidDef('Dicohesive Tech Shields')
    
	def NiPoint3ToTGPoint3(p):
		debug(__name__ + ", NiPoint3ToTGPoint3")
		kPoint = App.TGPoint3()
		kPoint.SetXYZ(p.x, p.y, p.z)
		return kPoint
    
	def CloakHandler(pObject, pEvent):
		App.DamageableObject_Cast(pObject).SetCollisionsOn(0)	#Set collisions off, so simple !!!
		pSound = App.g_kSoundManager.GetSound("PhaseCloakOn")
		if pSound:
			pSound.AttachToNode(pObject.GetNode())
			pSound.Play()
		pShip = App.ShipClass_Cast(pObject)
		if pShip:
			pShields = pShip.GetShields()
			if pShields:
				pShields.TurnOn()
		pObject.CallNextHandler(pEvent)

	def DecloakHandler(pObject, pEvent):
		App.DamageableObject_Cast(pObject).SetCollisionsOn(1)	#Set collisions on, so simple !!!
		pSound = App.g_kSoundManager.GetSound("PhaseCloakOff")
		if pSound:
			pSound.AttachToNode(pObject.GetNode())
			pSound.Play()
		pShip = App.ShipClass_Cast(pObject)
		if pShip:
			pShields = pShip.GetShields()
			if pShields:
				pShields.TurnOn()
		pObject.CallNextHandler(pEvent)
except:
	print "Something went wrong wih Dicohesive Tech Shields technology"
	traceback.print_exc()