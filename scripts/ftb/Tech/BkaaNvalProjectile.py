##################################################################
#  BkaaNvalProjectile.py
#                         by USS Frontier for the Delta Quadrant Pack
############################################################
# torpedo projectile that simulates a Bkaa Nval Torpedo
# developed and used by the Tradophians to be able to kill Xerohymid ships.
# Upon impact on a Xerohymid ship it will instantenously kill it.
###
# NOTE: Uses Galaxy Charts to do a race check. Else it tries checking if the target ship is a DQP 8472 Bioship.
############################################
# TO APPLY PROJECTILE TECH ON A TORPEDO:
# append the following to the end of the torpedo script module file. Without the comment line headers (#)

#try:
#	import FoundationTech
#	import ftb.Tech.BkaaNvalProjectile
#	oFire = ftb.Tech.BkaaNvalProjectile.BkaaNvalProjectileDef('BkaaNval Projectile')
#	FoundationTech.dYields[__name__] = oFire
#except:
#	pass

######################################

import App
import FoundationTech
import MissionLib
import string

class BkaaNvalProjectileDef(FoundationTech.TechDef):

	def __init__(self, name, dict = {}):
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.__dict__.update(dict)

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		pTarget = App.ShipClass_Cast(pEvent.GetDestination())
		bCanDestroy = 0
		try:
			# try checking ships race using Galaxy Charts
			import Custom.GalaxyCharts.GalaxyLIB
			if GetShipRace(pTarget) == "Xerohymid":
				bCanDestroy = 1
		except:
			# GC is probably not installed... Try checking the target ship ship script name with Sic Mvndvs Circulum pack Xerohymid Warship
			if pTarget.GetScript():
				sShipScript = string.split(pTarget.GetScript(), '.')[-1]
				if sShipScript == "XerohymidWarship":
					bCanDestroy = 1
		if bCanDestroy == 1:
			#target is a Xerohymid ship. Destroy it immediately.
			pHull = pTarget.GetHull()
			pTarget.DestroySystem(pHull)
		return


oBkaaNvalProjectile = BkaaNvalProjectileDef('BkaaNval Projectile')
