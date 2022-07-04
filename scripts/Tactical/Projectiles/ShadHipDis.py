###############################################################################
#	Filename:	PositronTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of positron torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a positron torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((255.0 / 255.0), (96.0 / 255.0), (0.0 / 255.0), 0.9)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, 0.5, 1.0, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 4.0, 0.2, 0.7, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 32, 0.2, 0.7)
    pTorp.SetDamage(3500)
    pTorp.SetDamageRadiusFactor(0.99)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    return 0


def GetLaunchSpeed():
	return(70.0)

def GetLaunchSound():
	return("Positron Torpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Jumpspace Disruptor")

def GetDamage():
	return 3500.0

def GetGuidanceLifetime():
	return 0.1

def GetMaxAngularAccel():
	return 9.9
