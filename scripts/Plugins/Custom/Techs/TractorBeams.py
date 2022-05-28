# Inversion Beam v1.0
#
# By:
#	 MLeo Daalder
#
# Requirements:
#	Foundation Technologies (Version 20050510 or later)
#
# Installation:
#	Place this file in scripts\Custom\Techs
#
# dTechs configuration:
#   add:
#	"Inversion Beam": [Immunity, (Struggle, (Efficienty,)) {Configuration}]
#   where Immunity is replaced by a number which represents the diminished
#	effectiveness of the opponents Inversion Beam. This usually goes from 0 (full effectiveness)
#	to 1 (immunity to the Inversion Beam). A number below 0 means that the your shields won't hold
#	for long. ;)
#
#	Note: _NEVER_ include the ( and ) around the Struggle and Efficienty values. They are only there to
#		clarify that the values are optional (programmers may note that officially it's the [ and ] characters
#		are the way to say it's optional, but in this case it's more clear with the [ and ]).
#
#	Struggle (this is optional, do not include the [ ] around "Struggle,") is the transfer effectiveness,
#	1 is full effectiveness, anything lower means there is loss, 0 means nothing is transferd,
#	just drained.
#
# Credits:
#	Apollo for his Inversion Beam (this mod is based on his implementation of the Inversion Beam)
#	Dasher for his Foundation and FoundationTech


import App
import FoundationTech
from ftb.Tech.ATPFunctions import *

class TractorTechDef(FoundationTech.TechDef):
	def Attach(self, pInstance):
		pInstance.lTechs.append(self)
		#pInstance.lTractorDefense.append(self)


	def Detach(self, pInstance):
		pInstance.lTechs.remove(self)
		#pInstance.lTractorDefense.remove(self)
		
	def AttachShip(self, pInstance, pShip):
		#pTractor = pShip.GetTractorBeamSystem()
		if pInstance.__dict__.has_key(self.name):
			pConfig = pInstance.__dict__[self.name][-1]
			if str(pConfig)[0] != "[":
				pTractor = pShip.GetTractorBeamSystem()
				if not pTractor:
					return
				pProjector = App.TractorBeamProjector_Cast(pTractor.GetChildSubsystem(0))
				if not pProjector:
					return
				sProjector = str(pProjector)
				sFire = pProjector.GetFireSound()
				pConfig = [sProjector, sFire]
			for sound in pConfig:
				FoundationTech.dYields[sound] = self

FoundationTech.TractorTechDef = TractorTechDef

class InversionBeam(TractorTechDef):

	# Being victim...	
	#def OnTractorDefense(self, pShip, pInstance, oYield, pEvent):
	def OnYield(self, pShip, pInstance, pEvent):
		print "Testing tractor defense"
		pProjector = App.TractorBeamProjector_Cast(pEvent.GetSource())
		if(pProjector == None):
			return
		print "Projector"
		pAttacker = pProjector.GetParentShip()
		sProjector = pProjector.GetName()
		sFire = pProjector.GetFireSound()
		pAttackerInst = None		
		try:
			pAttackerInst = FoundationTech.dShips[pAttacker.GetName()]
			if pAttackerInst == None:
				return
		except:
			print "No instance for:", pAttacker.GetName(), "How odd..."
			return
		print "Attacker Instance"

		if not pAttackerInst.__dict__.has_key("Inversion Beam"):
			return

		print "Attacker has Inversion Beam"

		fStruggle = 1
		fEfficient = 1
		pConfig = {}
		if len(pInstance.__dict__["Inversion Beam"]) >= 3:
			fStruggle = pInstance.__dict__["Inversion Beam"][1]
		
		#if len(pAttackerInst.__dict__["Inversion Beam"]) >= 3:
		if len(pAttackerInst.__dict__["Inversion Beam"]) >= 4:
			fEfficient = pAttackerInst.__dict__["Inversion Beam"][2]
		#pConfig = pAttackerInst.__dict__["Inversion Beam"][-1]

		#if str(pConfig)[0] != "{":
		#	pConfig = {sProjector: pConfig, sFire: pConfig}
			
		#if len(pConfig.keys()) <= 0:
		#	return
		#print "Config"

		#if not pConfig.has_key(sProjector) or pConfig.has_key(sFire):
		#	return
		#print "Correct tractor"
		
		# When we reach this part, we know we have this tech against us.
		# 	Check if we are armed for this...
		effect = pInstance.__dict__["Inversion Beam"][0]
		if effect >= 1: # Immunity to the Inversion Beam
			return
		print "Has effect"
		
		#if pConfig.has_key(sProjector):
		#	fStrength = pConfig[sProjector]
		#else:
		#	fStrength = pConfig[sFire]
		
		fStrength = fStrength - (fStrength * effect)
		if fStrength > 0:
			ShieldDistributeNeg(pShip, fStrength)
			if fStrength * fEfficient * fStruggle > 0:
				ShieldDistributePos(pAttacker, fStrength*fEfficient*fStruggle)
#		PrintShields(pShip)
#		PrintShields(pAttacker)
		
oInversionBeam = InversionBeam("Inversion Beam")

def PrintShields(pShip):
	pShields = pShip.GetShields()
	if pShields:
		print pShip.GetName(), pShields.GetCurShields(0), pShields.GetCurShields(1), pShields.GetCurShields(2), pShields.GetCurShields(3), pShields.GetCurShields(4), pShields.GetCurShields(5)
	else:
		print pShip.GetName(), "has no shields"

# Power Drain Beam v1.0
#
# By:
#	 MLeo Daalder
#
# Requirements:
#	Foundation Technologies (Version 20050505 or later)
#
# Installation:
#	Place this file in scripts\Custom\Techs
#
# dTechs configuration:
#   add:
#	"Power Drain Beam": [Immunity, (Struggle, (Efficienty,)) {Configuration}]
#   where Immunity is replaced by a number which represents the diminished
#	effectiveness of the opponents Inversion Beam. This usually goes from 0 (full effectiveness)
#	to 1 (immunity to the Power Drain Beam). A number below 0 means that the your power supply won't hold
#	for long. ;)
#
#	Note: _NEVER_ include the ( and ) around the Struggle and Efficienty values. They are only there to
#		clarify that the values are optional (programmers may note that officially it's the [ and ] characters
#		are the way to say it's optional, but in this case it's more clear with the [ and ]).
#
#	Struggle (this is optional, do not include the [ ] around "Struggle,") is the transfer effectiveness,
#	1 is full effectiveness, anything lower means there is loss, 0 means nothing is transferd,
#	just drained.
#
# Credits:
#	Dasher for his Foundation and FoundationTech

class PowerDrainBeam(TractorTechDef):
	def OnTractorDefense(self, pShip, pInstance, oYield, pEvent):
		pProjector = App.TractorBeamProjector_Cast(pEvent.GetSource())
		if(pProjector == None):
			return
		pAttacker = pProjector.GetParentShip()
		sProjector = pProjector.GetName()
		sFire = pProjector.GetFireSound()
		pAttackerInst = None		
		try:
			pAttackerInst = FoundationTech.dShips[pAttacker.GetName()]
			if pAttackerInst == None:
				return
		except:
			print "No instance for:", pAttacker.GetName(), "How odd..."
			return

		if pAttackerInst == None or not pAttackerInst.__dict__.has_key("Power Drain Beam"):
			return

		fStruggle = 1
		fEfficient = 1
		pConfig = {}
		if len(pInstance.__dict__["Power Drain Beam"]) >= 3:
			fStruggle = pInstance.__dict__["Power Drain Beam"][1]
		
		#if len(pAttackerInst.__dict__["Inversion Beam"]) >= 3:
		if len(pAttackerInst.__dict__["Power Drain Beam"]) >= 4:
			fEfficient = pAttackerInst.__dict__["Power Drain Beam"][2]
		pConfig = pAttackerInst.__dict__["Power Drain Beam"][-1]

		if str(pConfig)[0] != "{":
			pConfig = {sProjector: pConfig, sFire: pConfig}
			
		if len(pConfig.keys()) <= 0:
			return

		if not pConfig.has_key(sProjector) or pConfig.has_key(sFire):
			return
		
		# When we reach this part, we know we have this tech against us.
		# 	Check if we are armed for this...
		effect = pInstance.__dict__["Power Drain Beam"][0]
		if effect >= 1: # Immunity to the Inversion Beam
			return

		if pConfig.has_key(sProjector):
			fStrength = pConfig[sProjector]
		else:
			fStrength = pConfig[sFire]
			
		fStrength = fStrength - (fStrength * effect)
		if fStrength > 0:
			if pShip.GetPowerSystem():
				pShip.GetPowerSystem().StealPower(fStrength)
			if fStrength * fEfficient * fStruggle > 0:
				if pAttacker.GetPowerSystem():
					pAttacker.GetPowerSystem().AddPower(fStrength*fEfficient*fStruggle)

oPowerDrainBeam = PowerDrainBeam("Power Drain Beam")
