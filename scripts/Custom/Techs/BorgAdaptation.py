# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 16 June 2023, by Alex SL Gato (CharaToLoki), partially based on the Shield.py script by the Foundation Technologies team and Dasher42's Foundation script
# Version: 0.5
#
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech takes part on the defensive Borg adaptation. You can add your ship to an adaptable immunity list in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev - note the number indicates how fast it learns, make it 0 so it never helps into learning and negative values so it instead makes it more difficult for others to adapt :P
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Borg Adaptation": 1
}
"""

import App

import Foundation
import FoundationTech

import nt

import string

maxCountdown = 65535 # we want to keep things moderate

# TO-DO ORDER ALPHABETICALLY AND NOT BY ADAPTING DIFFICULTY
adaptationProgress = {
"IsDrainYield" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,                          # Immunity to breen drainer and similar drainers
"Breen Damper" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,                          
"Damper Weapon" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,                         
"Breen Drainer Weapon" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,

"IsChainReactionPulsarYield" : App.g_kSystemWrapper.GetRandomNumber(90) + 20,          # Immunity to chain reaction pulsar
"Chain Reaction Pulsar": App.g_kSystemWrapper.GetRandomNumber(90) + 20,
"CRP Projectile": App.g_kSystemWrapper.GetRandomNumber(90) + 20,              

"IsChronitonYield" : App.g_kSystemWrapper.GetRandomNumber(160) + 60,                    # Immunity to Chroniton torpedoes
"IsChronTorpYield" : App.g_kSystemWrapper.GetRandomNumber(160) + 60,
"Chroniton Torp" : App.g_kSystemWrapper.GetRandomNumber(160) + 60,                      
"ChronitonTorpe" : App.g_kSystemWrapper.GetRandomNumber(160) + 60,                      
"Chroniton Torpedo" : App.g_kSystemWrapper.GetRandomNumber(160) + 60,                   

"IsCloakDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,                  # Immunity to all cloak disablers
"Cloak Disabler" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,
"Cloak Disable" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,                  

"IsComputerVirusYield" : App.g_kSystemWrapper.GetRandomNumber(60) + 0,                 # Immunity to computer viruses
"Computer Virus" : App.g_kSystemWrapper.GetRandomNumber(60) + 0,                 
"PCVirus Weapon', " : App.g_kSystemWrapper.GetRandomNumber(60) + 0,

"IsElectromagneticDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(5) + 0,        # Immunity against ElectroMagnetic attacks
"Electro-Magnetic Pulse" : App.g_kSystemWrapper.GetRandomNumber(5) + 0,        
"EMP Projectile" : App.g_kSystemWrapper.GetRandomNumber(5) + 0,

"IsImpulseDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(11) + 0,                # Immunity to all impulse disablers
"Impulse Disabler" : App.g_kSystemWrapper.GetRandomNumber(11) + 0,
"Impulse Disable" : App.g_kSystemWrapper.GetRandomNumber(11) + 0,                

"IsIonProjectileYield" : App.g_kSystemWrapper.GetRandomNumber(20) + 0,                  # Immunity to all ion weapons
"IsIonWeaponYield" : App.g_kSystemWrapper.GetRandomNumber(20) + 0,                      
"Ion Projectile" : App.g_kSystemWrapper.GetRandomNumber(20) + 0,             
"Ion Weapon" : App.g_kSystemWrapper.GetRandomNumber(20) + 0,  

"IsIsokineticYield" : App.g_kSystemWrapper.GetRandomNumber(8) + 2,                     # Immunity to all kinds of isokinetic attacks, including isokinetic cannon rounds
"Isokinetic Cannon Round" : App.g_kSystemWrapper.GetRandomNumber(8) + 2,

"IsMultipleDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(32) + 5,              # Immunity to all multiple disablers
"Multiple Disable" : App.g_kSystemWrapper.GetRandomNumber(32) + 5,

"IsNanoprobeYield" : App.g_kSystemWrapper.GetRandomNumber(4) + 0,                      # Immunity to nanoprobes
"Nanoprobe Projectile" : App.g_kSystemWrapper.GetRandomNumber(4) + 0,

"Phalantium Wave" : App.g_kSystemWrapper.GetRandomNumber(52) + 160,                    # Immunity to Phalantium Wave

"IsPhaseYield" : App.g_kSystemWrapper.GetRandomNumber(100) + 200,                       # Immunity to standard Phased weaponry (specifically torpedoes)
"IsPhasedYield" : App.g_kSystemWrapper.GetRandomNumber(100) + 200,                      # Immunity to one alternative Phased Weaponry (probably a typo, better keep it)
"Phased Torpedo" : App.g_kSystemWrapper.GetRandomNumber(100) + 200,

"IsPowerDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(14) + 2,                  # Immunity to all power disablers
"Power Disable" : App.g_kSystemWrapper.GetRandomNumber(14) + 2,

"IsRandomDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(16) + 0,                 # Immunity to all strange disablers
"Random Disable" : App.g_kSystemWrapper.GetRandomNumber(16) + 0,

"IsRefluxWeaponYield" : App.g_kSystemWrapper.GetRandomNumber(100) + 100,                 # Immunity to Reflux weaponry (specifically torpedoes)

"IsSensorDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(10) + 0,                 # Immunity to all sensor disablers
"Sensor Disable" : App.g_kSystemWrapper.GetRandomNumber(10) + 0,

"IsShieldDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(10) + 0,                 # Immunity to all shield disablers
"Shield Disable" : App.g_kSystemWrapper.GetRandomNumber(10) + 0,

"Spatial Charge" : App.g_kSystemWrapper.GetRandomNumber(40) + 40,                      # Immunity to Spatial Charge

"IsTachyonProjectileYield" : App.g_kSystemWrapper.GetRandomNumber(120) + 0,             # Immunity against Tachyon weapons
"Tachyon Weapon" : App.g_kSystemWrapper.GetRandomNumber(120) + 0,

"IsTimeVortexYield" : App.g_kSystemWrapper.GetRandomNumber(1200) + 30000,               # Immunity against Time Vortex weaponry

"IsTransphasicYield" : App.g_kSystemWrapper.GetRandomNumber(300) + 300,                # Immunity against Transphasic technology (specifically Transphasic Torpedoes)

"IsWarpDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(14) + 0,                   # Immunity to all warp disablers
"Warp Disable" : App.g_kSystemWrapper.GetRandomNumber(14) + 0,


# TO-DO this is for offensive, leaving here just in case
#"Dicohesive Tech Shields": App.g_kSystemWrapper.GetRandomNumber(100) + 100, 

}

_g_dExcludeBorgPlugins = {
	# Some random plugins that I don't want to risk people attempting to load using this tech
	"000-Fixes20030217": 1,
	"000-Fixes20030221": 1,
	"000-Fixes20030305-FoundationTriggers": 1,
	"000-Fixes20030402-FoundationRedirect": 1,
	"000-Fixes20040627-ShipSubListV3Foundation": 1,
	"000-Fixes20040715": 1,
	"000-Fixes20230424-ShipSubListV4_7Foundation": 1,
	"000-Utilities-Debug-20040328": 1,
	"000-Utilities-FoundationMusic-20030410": 1,
	"000-Utilities-GetFileNames-20030402": 1,
	"000-Utilities-GetFolderNames-20040326": 1,
}

# Based on LoadExtraPlugins by Dasher42, but heavily modified so it only imports a thing
def LoadExtraLimitedPlugins(dExcludePlugins=_g_dExcludeBorgPlugins):

	dir="scripts\\Custom\\Techs\\BorgAdaptationsDefensive" # I want to limit any vulnerabiltiy as much as I can while keeping functionality
	import string

	list = nt.listdir(dir)
	list.sort()

	dotPrefix = string.join(string.split(dir, "\\")[1:], ".") + "."

	for plugin in list:
		s = string.split(plugin, ".")
		if len(s) <= 1:
			continue
		
        	# Indexing by -1 lets us be sure we're grabbing the extension. -Dasher42
		extension = s[-1]
		fileName = string.join(s[:-1], ".")

		# We don't want to accidentally load wrong things
		if (extension == "py") and not fileName == "__init__": # I am not allowing people to just use the .pyc directly, I don't want people to not include source scripts - Alex SL Gato
			print "Borg are reviewing " + fileName + " of dir " + dir
			if dExcludePlugins.has_key(fileName):
				debug(__name__ + ": Ignoring outdated plugin" + fileName)
				continue

			import traceback
			try:
				if not adaptationProgress.has_key(fileName):
					myGoodPlugin = dotPrefix + fileName
					
					# I really wanted to make it so it only imports these two methods, but it is not letting me do it :(
					# The only other secure option I could think about is making random files with the name and those two values in the name and then splitting them up, but if there's an update you would end up with rubbish as well
					# banana = __import__(myGoodPlugin, fromlist=["defenseCounterRdm"])
					# banana = __import__(myGoodPlugin, fromlist=["defenseCounter"])

					banana = __import__(myGoodPlugin, globals(), locals(), ["defenseCounterRdm"])

					randomness = abs(banana.defenseCounterRdm())
					constantness = abs(banana.defenseCounter())
					trueRandomness = App.g_kSystemWrapper.GetRandomNumber(randomness)
					#print constantness
					#print randomness
					#print trueRandomness
					
					# This standard is to call the file as "IsXXXXYield", with XXXX being the tech, that is "IsDrainYield", "IsPhasedYield", etc. Or call it like the Yield name (f.ex. "Hopping Torpedo")
					adaptationProgress[fileName] =  trueRandomness + constantness
					
					print "Borg reviewing of this tech is a success, adapting at the following number of shots: " + str(adaptationProgress[fileName])
			except:
				print "someone attempted to add more than they should"
				traceback.print_exc()


LoadExtraLimitedPlugins()


class BorgAdaptationDef(FoundationTech.TechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent, itemName):
		if oYield:
			import traceback
			try:
				for attre in adaptationProgress.keys():
					sameYield = 0
					if not FoundationTech.oTechs.has_key(attre):
						sameYield = (0 == 1) # For some reason it doesn't recognize False like that :/
					else:
						sameYield = (oYield == FoundationTech.oTechs[attre])
					if (hasattr(oYield, str(attre)) and getattr(oYield, str(attre))()) or sameYield:
						if not adaptationProgress.has_key(attre):
							adaptationProgress[attre] = 800
						if adaptationProgress[attre] <= 0:
							adaptationProgress[attre] = -1
							print "OH NO, THE BORG ADAPTED TO THIS WEAPON"
							return 1
						elif adaptationProgress[attre] > maxCountdown:
							adaptationProgress[attre] = maxCountdown

						# let's make it so people can customize how fast can a borg ship adapt, within reason
						learningFactor = pInstance.__dict__['Borg Adaptation']
						if learningFactor > maxCountdown:
							learningFactor = maxCountdown
						elif learningFactor < -maxCountdown:
							learningFactor = -maxCountdown

						adaptationProgress[attre] = adaptationProgress[attre] - learningFactor

				if not (itemName == "None whatsoever") and not adaptationProgress.has_key(oYield):
					adaptationProgress[oYield] = 800
			except:
				print "something went wrong with Borg Adaptation technology"
				traceback.print_exc()
			# TO-DO add something for raw damage?

	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		try:
			pEmitter = App.TractorBeamProjector_Cast(pEvent.GetSource())
			itemName = pEmitter.GetFireSound()
		except:
			itemName = "None whatsoever"
		return self.OnDefense(pShip, pInstance, oYield, pEvent, itemName)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		try:
			itemName = pTorp.GetModuleName()
		except:
			itemName = "None whatsoever"
		return self.OnDefense(pShip, pInstance, oYield, pEvent, itemName)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		try:
			itemName = pTorp.GetModuleName()
		except:
			itemName = "None whatsoever"
		return self.OnDefense(pShip, pInstance, oYield, pEvent, itemName)


	# TODO:  Make this an activated technology
	def Attach(self, pInstance):
		pInstance.lTechs.append(self)
		pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
		pInstance.lPulseDefense.insert(0, self)
		pInstance.lBeamDefense.insert(0, self)
		# print 'Attaching Borg Adaptation to', pInstance, pInstance.__dict__

oBorgAdaptation = BorgAdaptationDef('Borg Adaptation')
