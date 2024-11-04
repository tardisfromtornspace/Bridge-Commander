###############################################################################
#	Filename:	QuantumTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of quantum torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a quantum torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/naradaCore.tga",
					kCoreColor, 
					0.4,
					1.2, 	 
					"data/Textures/Tactical/naradaGlow.tga", 
					kGlowColor,
					0.3,	
					0.3,	 
					0.3,	
					"data/Textures/Tactical/naradaFlares.tga",
					kGlowColor,										
					8,		
					0.3,		
					0.5)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.14)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(39.0)

def GetLaunchSound():
	return("baznaradaPhoton")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Narada MIRV Photon")

def GetDamage():
	return 650.0

def GetGuidanceLifetime():
	return 5.5

def GetMaxAngularAccel():
	return 0.55

import traceback
try:
    import FoundationTech
    import ftb.Tech.TimedTorpedoes
    oFire = ftb.Tech.TimedTorpedoes.MIRVMultiTargetTorpedo(
        'MIRVMultiTargetTorpedo', {
        'spreadNumber': 10,
        'spreadDensity': 358.0,
        'warheadModule': "Tactical.Projectiles.naradaPhoton",
        'shellLive': 1,
    })
    FoundationTech.dOnFires[__name__] = oFire
except:
    print "Something went wrong with TimedTorpedoes"
    traceback.print_exc()
