import App
import MissionLib

MODINFO = { "Author": "ed",
				"Download": "",
				"Version": "2.0",
				"License": "",
				"Description": "Allows in-game switching of disruptor projectiles"
				}




def CyclePulseType(pObject, pEvent):
	global CurIndex
	CurIndex=CurIndex+1
	SetPulseScript(CurIndex)
	return

def SetPulseScript(Index):
	global PulseButton
	global CurIndex
	CurIndex=Index
	try:
		pShip=MissionLib.GetPlayer()
		pPulseSys=pShip.GetPulseWeaponSystem()
		pPulseProperty=pPulseSys.GetProperty()
		pShipModule=__import__(pShip.GetScript())
		PulseType=pShipModule.GetPulseModule(CurIndex)
		if (PulseType=="End"):
			CurIndex=1
			PulseType=pShipModule.GetPulseModule(CurIndex)
		BtnName=pShipModule.GetPulseName(CurIndex)
		PulseButton.SetName(App.TGString(BtnName))
		if (pPulseSys):
			for iPulseNum in range(pPulseSys.GetNumChildSubsystems()):
				pSubsystem = pPulseSys.GetChildSubsystem(iPulseNum)
				pWeapon = App.PulseWeapon_Cast(pSubsystem)
				pPulseCannon = App.PulseWeaponProperty_Cast(pWeapon.GetProperty())
				pPulseCannon.SetModuleName(PulseType)
	except:
		CurIndex=1
		PulseButton.SetName(App.TGString("No Pulse Routine"))
		return
	return PulseType

# The Button
def init():
	global PulseButton
	global CurIndex
	import Lib.LibEngineering
	PulseButton=Lib.LibEngineering.CreateMenuButton("No Pulse Routine", "Tactical", __name__ + ".CyclePulseType")
	SetPulseScript(1)
	return


def Restart():
	global CurIndex
	global PulseButton
	SetPulseScript(1)
	return
