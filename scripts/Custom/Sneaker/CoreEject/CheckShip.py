def CheckRace(pShip):
	import Foundation
	import string

	try:
		# script thanks to nano, gets the species race
		pShipScript = string.split(pShip.GetScript(), ".")
		pShipDef = Foundation.shipList[pShipScript[-1]]
		sRaceName = pShipDef.race.name
	except:
		# basically, we didnt find the ship. going to default race
		sRaceName = "Default"

	# if its feds, return 1, if not return 0. (true or false... but does python support boolean? this is better)
	if (sRaceName == "Federation" or sRaceName == "Star Fleet" or sRaceName == "Starfleet"):
		return 1
	else:
		return 0

def CheckPower(pShip):
	import App

	# grab the power subsystem
	pPowerSys = pShip.GetPowerSubsystem()

	# get its name
	if pPowerSys:
		# grab name and condition
		pPowerName = pPowerSys.GetName()
		pPowerHealth = pPowerSys.GetCondition()

		# if its named warp core and is not at 0 health; return 1, if not return 0
		if ((pPowerName == "Warp Core" or pPowerName == "Warpcore") and pPowerHealth != 0):
			return 1
		else:
			return 0