# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 20th July 2023
# By Alex SL Gato
# Power Drain Beam 1.0 by MLeo -> v1.1 fix
#
# Changes: 
# - "pShip.GetPowerSystem()" does not exist, but "pShip.GetPowerSubsystem()" does, so I changed one for the other
#
import App

necessaryToUpdate = 0
try:
	from Custom.Techs import TractorBeams
	if hasattr(TractorBeams,"PowerDrainBeamVersion"):
		if TractorBeams.PowerDrainBeamVersion == 1.0:
			necessaryToUpdate = 1
			print "fixing your TractorBeams.py 1.0 system mismatch"
		else :
			necessaryToUpdate = 0
			print "Congrats! Your TractorBeams.py version doesn't require of any fix we are aware of - feel free to delete FIX-TractorBeams1dot0 from your Autoload folder"
	else:
		necessaryToUpdate = 1 # the oldest versions have no signature
		print "Updating your TractorBeams.py <= 1.0 system mismatch"
except:
    print "Unable to find TractorBeams Inversion Beam and Drainer Beam"
    pass

if necessaryToUpdate:

	original = TractorBeams.PowerDrainBeam.OnTractorDefense

	def ReplacementOnTractorDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnTractorDefense")
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
			if pShip.GetPowerSubsystem():
				pShip.GetPowerSubsystem().StealPower(fStrength)
			if fStrength * fEfficient * fStruggle > 0:
				if pAttacker.GetPowerSubsystem():
					pAttacker.GetPowerSubsystem().AddPower(fStrength*fEfficient*fStruggle)

	TractorBeams.PowerDrainBeam.OnTractorDefense = ReplacementOnTractorDefense
