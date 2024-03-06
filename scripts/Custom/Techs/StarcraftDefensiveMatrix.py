"""
#         Starcraft Defensive Matrix
#         4th March 2024
#         Based strongly on Shields.py by the FoundationTech team (and QuickBattleAddon.corboniteReflector() in Apollo's Advanced Technologies) and Turrets.py by Alex SL Gato, and based on SubModels by USS Defiant and their team.
#################################################################################################################
# This tech gives a ship a Defensive Matrix like on Starcraft.

#Sample Setup:

Foundation.ShipDef.Sovereign.dTechs = {
	"Starcraft Defensive Matrix": {
		"MatrixScale": 1.0,
		"PowerDrain": 100,
		"Duration": 20,
		"Cooldown": 20,
		"Starcraft I": {
			"Percentage": 75,
			"Leakage": 0.5
		}
	}
}



"""

#################################################################################################################
from bcdebug import debug

import App
import FoundationTech

#################################################################################################################
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.1",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#################################################################################################################

# This should be the prime example of a special yield weapon defined according to Foundation Technologies.

NonSerializedObjects = (
"oDefensiveMatrix",
)

class DefensiveMatrix(FoundationTech.TechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		# TO-DO ADD DEFENSIVE MATRIX MODEL TO THE SHIP AS IF ATTACHED, PLUS LISTENING TO SHIELDS UP AND DOWN

		pShields = pShip.GetShields()

		if pShields and not pShields.IsDisabled():

			# Now we redistribute, we make it so all shield are damaged equally, normal damage + 5
			fDamage = 5 * pEvent.GetDamage()

			pShieldTotal = -fDamage
			for shieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
				pShieldTotal = pShieldTotal+pShields.GetCurShields(shieldDir)

			for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
				pShields.SetCurShields(shieldDir,pShieldTotal/6.0)  		#Redistribute shields equally
			
			#If the option "Starcraft I" exists, then we add a random chance for the hull to receive 0.5 damage if the hull was not hit
			if pEvent.IsHullHit():
				return

			if pInstance.__dict__["Starcraft Defensive Matrix"].has_key("Starcraft I") and pInstance.__dict__["Starcraft Defensive Matrix"]["Starcraft I"].has_key("Percentage") and pInstance.__dict__["Starcraft Defensive Matrix"]["Starcraft I"]["Percentage"] > 0.0:
				pHull = pShip.GetHull()
                                if pHull and App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__["Starcraft Defensive Matrix"]["Starcraft I"]["Percentage"]:
					leakDamage = 0.5
					if pInstance.__dict__["Starcraft Defensive Matrix"]["Starcraft I"].has_key("Leakage"):
						leakDamage = pInstance.__dict__["Starcraft Defensive Matrix"]["Starcraft I"]["Leakage"]
					pHull.SetCondition(pHull.GetCondition()-leakDamage)

	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnBeamDefense")
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		return self.OnDefense(pShip, pInstance, oYield, pEvent)


	# TODO:  Make this an activated technology
	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTechs.append(self)
		pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
		pInstance.lPulseDefense.insert(0, self)
		pInstance.lBeamDefense.insert(0, self)
		# print 'Attaching Starcraft II Terran Defensive Matrix to', pInstance, pInstance.__dict__

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()
    
oDefensiveMatrix = DefensiveMatrix('Starcraft Defensive Matrix')


