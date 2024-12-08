from bcdebug import debug
import App
import FoundationTech
import Foundation

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.corboniteMultivect() in Apollo's Advanced Technologies.


kEmptyColor = App.TGColorA()
kEmptyColor.SetRGBA(App.g_kSubsystemFillColor.r,App.g_kSubsystemFillColor.g,App.g_kSubsystemFillColor.b,App.g_kSubsystemFillColor.a)
kFillColor = App.TGColorA()
kFillColor.SetRGBA(210.0/255.0, 210.0/255.0, 210.0/255.0, App.g_kSubsystemFillColor.a)

NonSerializedObjects = (
"oAblative",
)

class AblativeDef(FoundationTech.GaugeTechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		repair = pInstance.__dict__['Tetraburnium Armour']

		print 'AblativeDef.OnDefense', pShip.GetName(), repair, pEvent.GetDamage()

		pSubName = self.GetSystemName()
		if str(repair)[0] == "[":
			pSubName = repair[1]
			repair = repair[0]
			
		if repair > 0.0:

			if str(pInstance.__dict__['Tetraburnium Armour'])[0] == "[":
				pInstance.__dict__['Tetraburnium Armour'][0] = repair = repair - pEvent.GetDamage()
				
			else:
				pInstance.__dict__['Tetraburnium Armour'] = repair = repair - pEvent.GetDamage()



			pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			while pSubsystem:
				if pSubsystem.GetName() == pSubName:
					pSubsystem.SetCondition(repair)
					# pSubsystem.SetCondition(pInstance.__dict__['Tetraburnium Armour'])
				elif pSubsystem.GetCondition() > 0.0 and not pSubsystem.IsDisabled():
					pSubsystem.SetCondition(pSubsystem.GetMaxCondition())
					iChildren = pSubsystem.GetNumChildSubsystems()
					if iChildren > 0:
						for iIndex in range(iChildren):
							pChild = pSubsystem.GetChildSubsystem(iIndex)
							if pChild.IsDisabled():
								continue
							pChild.SetCondition(pChild.GetMaxCondition())

				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
			pShip.EndGetSubsystemMatch(pIterator)
		else:
			pInstance.__dict__[self.GetSystemPointer()].SetCondition(repair)
			self.DetachShip(pShip, pInstance)
			self.Detach(pInstance)


	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnBeamDefense")
		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		if pEvent.IsHullHit():
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		if pEvent.IsHullHit():
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		if pEvent.IsHullHit():
			return self.OnDefense(pShip, pInstance, oYield, pEvent)


	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTechs.append(self)
		pInstance.lTorpDefense.append(self)
		pInstance.lPulseDefense.append(self)
		pInstance.lBeamDefense.append(self)

	def Detach(self, pInstance):
		debug(__name__ + ", Detach")
		pInstance.lTechs.remove(self)
		pInstance.lTorpDefense.remove(self)
		pInstance.lPulseDefense.remove(self)
		pInstance.lBeamDefense.remove(self)

	def GetSystemName(self):
		debug(__name__ + ", GetSystemName")
		return "Tetraburnium Armour"

	def GetSystemPointer(self):
		debug(__name__ + ", GetSystemPointer")
		return 'pArmour'
		
	def GetFillColor(self):
		debug(__name__ + ", GetFillColor")
		global kFillColor
		return kFillColor
		
	def GetEmptyColor(self):
		debug(__name__ + ", GetEmptyColor")
		global kEmptyColor
		return kEmptyColor

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()

oAblative = AblativeDef('Tetraburnium Armour')

# dHealths = {}
# 
# def SetShipID(pDisplay, ID):
# 	global dHealths
# 	# Get the game object.
# 	pGame = App.Game_GetCurrentGame()
# 
# 	idShip = pDisplay.GetShipID()
# 
# 	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(ID))
# 
# 	pShieldsDisplay = pDisplay.GetShieldsDisplay()
# 	pDamageDisplay = pDisplay.GetDamageDisplay()
# 	pHealthGauge = pDisplay.GetHealthGauge()
# 
# 	pArmour = None
# 	if pShip:
# 	# To bad the Instance hasn't been created when this is called... -MLeoDaalder
# 
# 	#	if FoundationTech.dShips.has_key(pShip.GetName()):
# 	#		pInstance = FoundationTech.dShips[pShip.GetName()]
# 	#		if pInstance.__dict__.has_key("Tetraburnium Armour"):
# 	 	pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
# 		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
# 		while pSubsystem != None:
# 			if pSubsystem.GetName() == "Tetraburnium Armour":
# 				pArmour = pSubsystem
# 				pShip.EndGetSubsystemMatch(pIterator)
# 				break
# 			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
# 		pShip.EndGetSubsystemMatch(pIterator)
# 		if pArmour:
# 			kEmptyColor = App.TGColorA()
# 			kEmptyColor.SetRGBA(App.g_kSubsystemFillColor.r,App.g_kSubsystemFillColor.g,App.g_kSubsystemFillColor.b,App.g_kSubsystemFillColor.a)
# 			kFillColor = App.TGColorA()
# 			kFillColor.SetRGBA(210.0/255.0, 210.0/255.0, 210.0/255.0, App.g_kSubsystemFillColor.a)
# 
# 			pHealthGauge.SetEmptyColor(kEmptyColor)
# 			pHealthGauge.SetFillColor(kFillColor)
# 			dHealths[ID] = pHealthGauge
# 		else:
# 			kFillColor = App.TGColorA()
# 			kFillColor.SetRGBA(App.g_kSubsystemFillColor.r,App.g_kSubsystemFillColor.g,App.g_kSubsystemFillColor.b,App.g_kSubsystemFillColor.a)
# 			kEmptyColor = App.TGColorA()
# 			kEmptyColor.SetRGBA(App.g_kSubsystemEmptyColor.r,App.g_kSubsystemEmptyColor.g,App.g_kSubsystemEmptyColor.b,App.g_kSubsystemEmptyColor.a)
# 
# 			pHealthGauge.SetEmptyColor(kEmptyColor)
# 			pHealthGauge.SetFillColor(kFillColor)
# 
# 				
# 
#  	# If we currently have a valid ship ID, remove events for it.
# 	if idShip != App.NULL_ID:
# 		# Remove display specific events before setting new ShipID.
# 		pShieldsDisplay.RemoveEvents()
# 		pDamageDisplay.RemoveEvents()
# 
# 	# Set new ship ID.
# 	pDisplay.SetShipIDVar(ID)
# 
# 	# If valid ship ID.
# 	if (ID != App.NULL_ID):
# 		pHealthGauge.SetVisible(0)
# 	else:
# 		# No ship.
# 		pHealthGauge.SetNotVisible(0)
# 
# 	# Update displays for new ship.
# 	pShieldsDisplay.UpdateForNewShip()
# 	pDamageDisplay.UpdateForNewShip()
# 
# 
# 	if (pShip != None):
# 		if pArmour:
# 			pHealthGauge.SetObject(pArmour)
# 		else:
# 			pHealthGauge.SetObject(pShip.GetHull())
# 	else:
# 		pHealthGauge.SetObject(pShip)
# 
# # For some reason this won't work....
# #Foundation.OverrideDef.FTBTetraburniumArmourGUI = Foundation.OverrideDef("FTB Tetraburnium Armour GUI", "Tactical.Interface.ShipDisplay.SetShipID", __name__ ".SetShipID", FoundationTech.dMode)
# 
# import Tactical.Interface.ShipDisplay
# pOrgSetShipID = Tactical.Interface.ShipDisplay.SetShipID
# Tactical.Interface.ShipDisplay.SetShipID = SetShipID
