###############################################################################
#	Filename:	phasedplasmaTypB.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of antimatter torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates an phasedplasmaTypB.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(188.0 / 282.0, 60.0 / 285.0, 10.0 / 109.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(188.0 / 82.0, 60.0 / 285.0, 10.0 / 109.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(35.0 / 255.0, 120.0 / 255.0, 70.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.3,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					12,		
					0.5,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.12)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(35.0)

def GetLaunchSound():
	return("Quantum Torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Phased")

def GetDamage():
	return 1300.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 0.7

try:
	modPhasedTorp = __import__("Custom.Techs.PhasedTorp")
	if(modPhasedTorp):
		modPhasedTorp.oPhasedTorp.AddTorpedo(__name__)
except:
	print "Phased Torpedo script not installed, or you are missing Foundation Tech"
