###############################################################################
#	Filename:	PoleronTorp.py
#	By:		edtheborg
###############################################################################

import App
pWeaponLock = {}

###############################################################################
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(174.0 / 255.0, 152.0 / 255.0, 154.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(168.0 / 255.0, 115.0 / 255.0, 93.0 / 255.0, 0.200000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(169.0 / 255.0, 136.0 / 255.0, 140.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/PhqCore.tga",
					kCoreColor,
					0.1,
					1.2,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.0,	
					0.2,	 
					0.3,	
					"data/Textures/Tactical/PhqFlares.tga",
					kFlareColor,										
					300,		
					0.1,		
					0.27)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.19)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(52)

def GetLaunchSound():
	return("26thCenturyChroniton")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Chroniton")

def GetDamage():
	return 6800

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.5

try:
	modChronitonTorpe = __import__("Custom.Techs.ChronitonTorpe")
	if(modChronitonTorpe):
		modChronitonTorpe.oChronitonTorpe.AddTorpedo(__name__)
except:
	print "Chroniton Torpedo script not installed, or you are missing Foundation Tech"
