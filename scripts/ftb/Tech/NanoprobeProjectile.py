##################################################################
#  NanoprobeProjectile.py
#                         by USS Frontier for the Delta Quadrant Pack
############################################################
# torpedo projectile that simulates a Nanoprobe torpedo that Voyager
# develop and used along with the Borg to be able to kill Species 8472 ships.
# Upon impact on a species 8472 ship it will instantenously kill it.
###
# NOTE: Uses Galaxy Charts to do a race check. Else it tries checking if the target ship is a DQP 8472 Bioship.
############################################
# TO APPLY PROJECTILE TECH ON A TORPEDO:
# append the following to the end of the torpedo script module file. Without the comment line headers (#)

#try:
#	import FoundationTech
#	import ftb.Tech.NanoprobeProjectile
#	oFire = ftb.Tech.NanoprobeProjectile.NanoprobeProjectileDef('Nanoprobe Projectile')
#	FoundationTech.dYields[__name__] = oFire
#except:
#	pass

######################################

import App
import FoundationTech
import MissionLib
import string

class NanoprobeProjectileDef(FoundationTech.TechDef):

	def __init__(self, name, dict = {}):
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.__dict__.update(dict)

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		pTarget = App.ShipClass_Cast(pEvent.GetDestination())
		bCanDestroy = 0
		try:
			# try checking ships race using Galaxy Charts
			import Custom.GalaxyCharts.GalaxyLIB
			if GetShipRace(pTarget) == "8472":
				bCanDestroy = 1
		except:
			# GC is probably not installed... Try checking the target ship ship script name with JLS's Delta Quadrant Pack species 8472 bioship.
			if pTarget.GetScript():
				sShipScript = string.split(pTarget.GetScript(), '.')[-1]
				if sShipScript == "JLS8472":
					bCanDestroy = 1
		if bCanDestroy == 1:
			#target is a species 8472 ship. Destroy it immediately.
			pHull = pTarget.GetHull()
			pTarget.DestroySystem(pHull)
		return


oNanoprobeProjectile = NanoprobeProjectileDef('Nanoprobe Projectile')
