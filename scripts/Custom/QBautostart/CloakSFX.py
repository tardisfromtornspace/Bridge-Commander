import App
import MissionLib
import Lib.LibEngineering
import loadspacehelper
import Bridge.BridgeMenus
import BridgeHandlers
import Foundation
import string

def init():
	pMission = MissionLib.GetMission()
             
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_CLOAK_BEGINNING, pMission, __name__+".ObjectCloaking")               
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_DECLOAK_BEGINNING, pMission, __name__+".ObjectDeCloaking")

              
def ObjectCloaking(pObject, pEvent):
	pPlayer    = MissionLib.GetPlayer()
	pPlayerSet = pPlayer.GetContainingSet()

	pShip = App.ShipClass_Cast(pEvent.GetDestination())

	if not pShip:
		return

	pShipID = pShip.GetObjID()
	if not pShipID:
		return

	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return

	pShipSet = pShip.GetContainingSet()

	if pShipSet and pPlayerSet and (pPlayerSet.GetName() == pShipSet.GetName()):		
		if pShip.GetScript():
			sShip = string.split(pShip.GetScript(), '.')[-1]
			if Foundation.shipList.has_key(sShip):
				pFoundationShip = Foundation.shipList[sShip]                                        
				if pFoundationShip and hasattr(pFoundationShip, "CloakingSFX"):
					sCloakSFX = pFoundationShip.CloakingSFX
					sDeCloakSFX = pFoundationShip.DeCloakingSFX
					
					pCloakSound = App.g_kSoundManager.GetSound(sCloakSFX)
					
					App.g_kSoundManager.StopSound(sDeCloakSFX)
						
					if pCloakSound:
						pCloakSound.Play()						
					else:		
						DefaultCloak()			
				else:
					DefaultCloak()	
			else:
				DefaultCloak()	


		if(pPlayer.GetName() == pShip.GetName()):
			try:
				pBridge = App.g_kSetManager.GetSet("bridge")

				g_pBrex	     = App.CharacterClass_GetObject(pBridge, "Engineer")
				pBrexMenu    = g_pBrex.GetMenu()
				pTransporter = Lib.LibEngineering.GetButton("Transporter", pBrexMenu)
				pTransporter.SetDisabled()
			except:
				print("No Transporters")
				return				
						
        
def ObjectDeCloaking(pObject, pEvent):
	pPlayer    = MissionLib.GetPlayer()
	pPlayerSet = pPlayer.GetContainingSet()

	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if not pShip:
		return

	pShipID = pShip.GetObjID()
	if not pShipID:
		return

	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return

	pShipSet = pShip.GetContainingSet()

	if pShipSet and pPlayerSet and (pPlayerSet.GetName() == pShipSet.GetName()):	
		if pShip.GetScript():
			sShip = string.split(pShip.GetScript(), '.')[-1]
			if Foundation.shipList.has_key(sShip):
				pFoundationShip = Foundation.shipList[sShip]                                        
				if pFoundationShip and hasattr(pFoundationShip, "DeCloakingSFX"):
					sDeCloakSFX = pFoundationShip.DeCloakingSFX
					sCloakSFX   = pFoundationShip.CloakingSFX
					
					pDeCloakSound = App.g_kSoundManager.GetSound(sDeCloakSFX)
					
					App.g_kSoundManager.StopSound(sCloakSFX)
					
					if pDeCloakSound:
						pDeCloakSound.Play()						
					else:
						DefaultDeCloak()			
				else:
					DefaultDeCloak()	
			else:
				DefaultDeCloak()



		if(pPlayer.GetName() == pShip.GetName()):	
			try:
				pBridge = App.g_kSetManager.GetSet("bridge")

				g_pBrex	     = App.CharacterClass_GetObject(pBridge, "Engineer")
				pBrexMenu    = g_pBrex.GetMenu()
				pTransporter = Lib.LibEngineering.GetButton("Transporter", pBrexMenu)
				pTransporter.SetEnabled()
			except:
				print("No Transporters")
				return				
			

def DefaultCloak():

	pCloakSound = App.g_kSoundManager.GetSound("Default Cloak")
	
	App.g_kSoundManager.StopSound("Default DeCloak")
	
	if pCloakSound:
		pCloakSound.Play()
	else:	
		print("Uh Oh Problem with Cloaking SFX")	


def DefaultDeCloak():
	
	pDeCloakSound = App.g_kSoundManager.GetSound("Default DeCloak")

	App.g_kSoundManager.StopSound("Default Cloak")
	
	if pDeCloakSound:
		pDeCloakSound.Play()
	else:
		print("Uh Oh Problem with Cloaking SFX")
						
