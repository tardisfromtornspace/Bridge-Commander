###############################################################################################################
#          EMP Projectile
#                                           by USS Frontier
###############################################################################################################
# The EMP (Eletro-Magnetic Pulse) Projectile is a relatively simple projectile tech, but a very usefull one.
# EMP Projectiles upon hitting their target have a chance (defined by the torpedo module) to decrease the power
# of all shields of the enemy ship by a percentage (also defined by the torp module).
###############################################################################################################
# To add the EMP Projectile tech to a torpedo, add the following code at the end of the script:
# And remove the "#" symbols

#try:
#	import FoundationTech
#	import ftb.Tech.EMPProjectile
#
#	oFire = ftb.Tech.EMPProjectile.EMPProjectileDef('EMP Projectile', {
#	'nPercentage': 5,
#	'nChance': 50,
#})
#	FoundationTech.dYields[__name__] = oFire
#except:
#	import sys
#	et = sys.exc_info()
#	error = str(et[0])+": "+str(et[1])
#	print "ERROR at script: " + __name__ +", details -> "+error

#########################################################################################################################
import App
import FoundationTech
import MissionLib

class EMPProjectileDef(FoundationTech.TechDef):

	def __init__(self, name, dict):
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.nPercentage = None
		self.nChance = None
		self.__dict__.update(dict)
		if not self.nPercentage:
			nPercentage = 10

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		nChance = self.nChance
		#print "Chance--->>>", nChance, "%"
		if App.g_kSystemWrapper.GetRandomNumber(100) <= nChance:
			pTarget = App.ShipClass_Cast(pEvent.GetDestination())
			tDmg = pTorp.GetDamage()
			Percentage = self.nPercentage
			#print "Dmg%--->>>", Percentage, "// Damage--->>>", tDmg, "// Target--->>>", pTarget.GetName()
			pShields = pTarget.GetShields()
			PerFactor = 100/Percentage
			for ShieldVecs in range(App.ShieldClass.NUM_SHIELDS):
				pShieldStatus = pShields.GetCurShields(ShieldVecs)
				DmgToShields = pShieldStatus/PerFactor
				#if (tDmg > DmgToShields):
				#	DmgToShields = tDmg
				if (pShieldStatus <= DmgToShields):
					pShieldStatus = 0
				#print "Shield Status--->>>", pShieldStatus
				#print "EMP Torpedo sucessfull, drained", DmgToShields, "damage from all shields from target."
				pShields.SetCurShields(ShieldVecs,pShieldStatus-DmgToShields)
			return


oEMPProjectile = EMPProjectileDef('EMP Projectile', {
	'nPercentage': 10,
	'nChance': 50,
})
