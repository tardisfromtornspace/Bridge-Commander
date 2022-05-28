import App
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib

# Most of these scripts operate under 1 mutator name, but is the actual script of the tech/mod in question present... 
def GetScript():
    try:
        import Custom.QBAutostart.AdvArmorTech
        pModule = Custom.QBAutostart.AdvArmorTech
        if hasattr(pModule, "AdvArmor"):
            bIsInstalled = 1
        else:
            bIsInstalled = 0
    except:
        bIsInstalled = 0
    return bIsInstalled

# Show how can DS9FX check if the mod is active. The code which checks for active mutators is a bit different and supports partial matching.
# I.E. You have a mutator called "Foundation Technologies 4.5", you can simply return "Foundation Technologies". 
def GetMutatorName():
    return "QBautostart Extension"

def CanKillCrewMembers(pObject, pEvent):
    try:
        pSource = App.ShipClass_Cast(pEvent.GetDestination())
        if not pSource:
            return 1
        
        pShip = MissionLib.GetPlayer()
        if not pShip:
            return 1

        if not pSource.GetObjID() == pShip.GetObjID():
            return 1

        pScript = pShip.GetScript()
        if not pScript:
            return 1

        pScript = __import__(pScript)

	try:
		pArmorRatio = pScript.GetArmorRatio()
	except:
		pArmor = GetAdvArmor(pShip)
		if not pArmor:
		    return 1

        pButton = None
        lChars = ["Helm", "Tactical", "XO", "Science", "Engineer"]
        for pChar in lChars:
            pTemp = DS9FXMenuLib.GetButton("Plating Online", pChar)
            if pTemp:
                pButton = pTemp
                break

        if pButton:
            return 0
        
        return 1
    except:
        return 1

def GetAdvArmor(pShip):
    pAdvArmor = 0
    pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
    pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
    while (pSubsystem != None):
            if pSubsystem.GetName() =="Armored Hull":
                    pAdvArmor = pSubsystem
            pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
    pShip.EndGetSubsystemMatch(pIterator)
    return pAdvArmor
