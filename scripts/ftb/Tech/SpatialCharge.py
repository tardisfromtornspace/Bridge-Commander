from bcdebug import debug
#########################################################################################################################
###	Spatial Charges:												#
###		0 - Not active												#
###		1 - The effect designed by Sneaker, modified to work with NanoFX aswell					#
###	Sneaker and NanoFX are now compatible ;-)									#
#########################################################################################################################

import App

import FoundationTech
import MissionLib

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.drainerWeapon() in Apollo's Advanced Technologies.


class SpatialChargeDef(FoundationTech.TechDef):
	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		debug(__name__ + ", OnYield")
		if FoundationTech.EffectsLib:
			FoundationTech.EffectsLib.CreateSpecialFXSeq(pShip,pEvent,"Spatial")

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()


oSpatialCharge = SpatialChargeDef('Spatial Charge')

# print 'Spatial Charges loaded'
