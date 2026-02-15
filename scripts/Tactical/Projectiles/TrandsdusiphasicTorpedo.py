###############################################################################
#	Filename:	PhotonTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	
###############################################################################

import App
import MissionLib

###############################################################################
#	
#	
#	
#	
#	
#	
#	
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(240.0 / 255.0, 220.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(85.0 / 255.0, 65.0 / 255.0, 110.0 / 255.0, 0.800000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.5,
					0.93,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.23,	 
					0.47,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					150,		
					0.54,		
					0.08)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(2.5)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("TrandsdusiphasicTorpedo")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Trandsdusiphasic Torpedo")

def GetDamage():
	return 5750.0

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 0.35

def GetFlashColor():
	return (200.0, 135.0, 255.0)

# Sets the percentage of shield damage the torpedo will do
def GetPercentage():
	return 0.50

try:
	modRefluxWeapon = __import__("Custom.Techs.RefluxWeapon")
	if(modRefluxWeapon):
		modRefluxWeapon.oRefluxWeapon.AddTorpedo(__name__, GetPercentage())
except:
	print "Reflux Weapon script not installed, or you are missing Foundation Tech"