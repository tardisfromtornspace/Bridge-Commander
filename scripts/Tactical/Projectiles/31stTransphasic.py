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
	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(124.0 / 200.0, 180.0 / 255.0, 240.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(124.0 / 200.0, 180.0 / 255.0, 240.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(49.0 / 124.0, 114.0 / 175.0, 150.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.1,
					1.0,	 
					"data/Textures/Tactical/ArmVoyX.tga", 
					kCoreColor,
					2.0,	
					0.2,	 
					0.4,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					7,		
					0.1,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(99999999999.50)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLifetime():
        return 60

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("Transphasic")

def GetPowerCost():
	return(90)

def GetName():
	return("31st Transphasic")

def GetDamage():
	return 99991.90

def GetGuidanceLifetime():
	return 23.0

def GetMaxAngularAccel():
	return 2.235

try:
	modTransphasicTorp = __import__("Custom.Techs.TransphasicTorp")
	if(modTransphasicTorp):
		modTransphasicTorp.oTransphasicTorp.AddTorpedo(__name__)
except:
	print "Transphasic Torpedo script not installed, or you are missing Foundation Tech"