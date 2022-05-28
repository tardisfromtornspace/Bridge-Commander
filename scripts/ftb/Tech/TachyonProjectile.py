from bcdebug import debug
import App
import FoundationTech
import MissionLib
from DisablerYields import *


NonSerializedObjects = (
"oTachyonWeapon",
)

class TachyonWeaponDef(MultipleDisableDef):

	def IsDrainYield(self):
		debug(__name__ + ", IsDrainYield")
		return 1

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
                debug(__name__ + ", OnYield")
                self.pShipID = pShip.GetObjID()
		pPlayer = MissionLib.GetPlayer()
                pBridge = App.g_kSetManager.GetSet("bridge")
                
		if pPlayer.GetObjID() == pShip.GetObjID() and pBridge:
	                pEngineer = App.CharacterClass_GetObject(pBridge, "Engineer")
	                pDatabase = pEngineer.GetDatabase()
                        # only play when shields are online
                        if self.GetShieldStatus():
                                pSequence = App.TGSequence_Create()
                                pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "ShieldsFailed", None, 0, pDatabase, App.CSP_SPONTANEOUS))
                                pSequence.Play()
                        
                if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
                        pSeq = App.TGSequence_Create()
                        iTime = 5 # seconds
                        while(iTime >= 0):
                                pAction	= App.TGScriptAction_Create(__name__, "Update", self, 0)
                                pSeq.AppendAction(pAction, 0.1)
                                iTime = iTime - 0.1
                        pAction	= App.TGScriptAction_Create(__name__, "Update", self, 1)
                        pSeq.AppendAction(pAction, 0.1)
                        pSeq.Play()

        def GetShip(self):
                debug(__name__ + ", GetShip")
                return App.ShipClass_GetObjectByID(None, self.pShipID)

	def GetShields(self):
		debug(__name__ + ", GetShields")
		pShip = self.GetShip()
		if pShip:
			return pShip.GetShields()

	def GetShieldStatus(self):
		debug(__name__ + ", GetShieldStatus")
		pShields = self.GetShields()
		if pShields:
			return pShields.IsOn()

def Update(pAction, self, iOnOff):
        debug(__name__ + ", Update")
        pShields = self.GetShields()
        if iOnOff == 0:
                if pShields:
                        pShields.TurnOff()
        else:
                if pShields:
                        pShip = self.GetShip()
                        # turn Shields on if we are not green alert
                        if pShip.GetAlertLevel() > 0:
                                pShields.TurnOn()
        return 0


oTachyonWeapon = TachyonWeaponDef('Tachyon Weapon', {})
