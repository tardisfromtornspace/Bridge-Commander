from bcdebug import debug
###############################################################################
##	Filename:	GlowFX.py
##
##	Nano's Glow Effects Fixes for Light Flickers Version 1.0
##
##	Created:	03/21/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################

import App
import MissionLib
import Foundation
import Actions.EffectScriptActions
import Actions.ShipScriptActions

###############################################################################
## Fix Glows After ship Docks with StarBase...
###############################################################################
def RepairShipFullyGlowFix(pAction, iShipID):
	debug(__name__ + ", RepairShipFullyGlowFix")
	"Repairs a ship fully. Every subsystem is restored to full health."

	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(iShipID))

	if(pShip is None):
		return 0

	# Iterate over all the subsystems of the ship.
	pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
	pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

	while (pSubsystem != None):
		Actions.ShipScriptActions.RepairSubsystemFully(pAction, pSubsystem.GetObjID())
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

	pShip.EndGetSubsystemMatch(pIterator)

	# Set all of ship's shields to max.
	pShields = pShip.GetShields()

	if (pShields != None):
		for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
			pShields.SetCurShields(ShieldDir, pShields.GetMaxShields(ShieldDir))

	# Set the power of the ship to max.
	pPower = pShip.GetPowerSubsystem()
	if (pPower != None):
		pPower.SetMainBatteryPower(pPower.GetMainBatteryLimit())
		pPower.SetBackupBatteryPower(pPower.GetBackupBatteryLimit())

	pShip.RemoveVisibleDamage()

	# Replenish probe supply.
	pSensors = pShip.GetSensorSubsystem()
	if pSensors:
		pProp = pSensors.GetProperty()
		if pProp:
			pSensors.SetNumProbes(pProp.GetMaxProbes())

	### Addition for Glow Fix ###
	NanoGlowFX(pShip)
	###

	return(0)

###############################################################################
## Fix Glows
###############################################################################
def NanoGlowFX(pShip):

	debug(__name__ + ", NanoGlowFX")
	import Custom.NanoFXv2.NanoFX_Config
	if (Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On"):
		if (App.g_kLODModelManager.AreGlowMapsEnabled() == 1) and App.g_kLODModelManager.GetDropLODLevel() == 0: # else the game will crash on not high graphics
			App.g_kLODModelManager.SetGlowMapsEnabled(0)
			App.g_kLODModelManager.SetGlowMapsEnabled(1)

###############################################################################
## End of Glow FX Fixes
###############################################################################


