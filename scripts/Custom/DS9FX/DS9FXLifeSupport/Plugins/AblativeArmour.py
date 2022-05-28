import App
import Foundation
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib

# Most of these scripts operate under 1 mutator name, but is the actual script of the tech/mod in question present... 
def GetScript():
    try:
        import ftb.Tech.AblativeArmour
        pModule = ftb.Tech.AblativeArmour
        if hasattr(pModule, "oAblative"):
            bIsInstalled = 1
        else:
            bIsInstalled = 0
    except:
        bIsInstalled = 0
    return bIsInstalled

# Show how can DS9FX check if the mod is active. The code which checks for active mutators is a bit different and supports partial matching.
# I.E. You have a mutator called "Foundation Technologies 4.5", you can simply return "Foundation Technologies". 
def GetMutatorName():
    return "Foundation Technologies"

def CanKillCrewMembers(pObject, pEvent):
    try:
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if not pShip:
            return 1

        pType = DS9FXLifeSupportLib.GetShipType(pShip)
        if not pType:
            return 1

        if Foundation.shipList.has_key(pType):
            fdShip = Foundation.shipList[pType]
            if fdShip:
                if hasattr(fdShip, "dTechs"):
                    pTech = fdShip.dTechs
                    if pTech.has_key("Ablative Armour"):
                        lArmor = pTech["Ablative Armour"]
                        if len(lArmor) == 2:
                            sName = lArmor[1]
                        else:
                            sName = "Ablative Armour"

                        pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

                        pPlating = None
			while pSubsystem:
				if pSubsystem.GetName() == sName:
					if not pSubsystem.IsDisabled():
                                            pPlating = pSubsystem
                                            break

                                pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
			pShip.EndGetSubsystemMatch(pIterator)

			if not pPlating:
                            return 1
                        
                        return 0
        return 1
    except:
        return 1
