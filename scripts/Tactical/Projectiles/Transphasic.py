###############################################################################
#		
#	Script for filling in the attributes of Fusion torpedoes.
#	
#	Created:	012/10/04 -	 MRJOHN
###############################################################################

import App
import string
pWeaponLock = {}

###############################################################################
#	Create(pTorp)
#	
#	Creates a Fusion torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(230.0 / 255.0, 220.0 / 255.0, 78.0 / 255.0, 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(230.0 / 255.0, 245.0 / 255.0, 208.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoFlares.tga",
					kCoreColor, 
					0.175,
					0.93,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.8,	
					0.23,	 
					0.47,	
					"data/Textures/Tactical/TorpedoCore.tga",
					kGlowColor,										
					16,		
					0.4,		
					0.20)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(9999.75)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("Transphasic")

def GetPowerCost():
	return(90.01)

def GetName():
	return("Transphasic")

def GetDamage():
	return 19000

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.435

try:
	modTransphasicTorp = __import__("Custom.Techs.TransphasicTorp")
	if(modTransphasicTorp):
		modTransphasicTorp.oTransphasicTorp.AddTorpedo(__name__)
except:
	print "Transphasic Torpedo script not installed, or you are missing Foundation Tech"