###############################################################################
#	Filename:	GlowEmmiter.py
#	
#	Confidential and Proprietary, Copyright by Creator-->>see below
#	
#	Script for filling in the attributes of a Glow Emmiter.
#	
#	Created:	28/8/06 -	Fernando Aluani aka USS Frontier
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Glow Emmiter.
#
#	YES A GLOW!
#	This isn't used as a torpedo, but in fact it is used as a GLOW emmiter.	
#
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################

###############################################################################
### Custom Variables ###############
CoreSize = 4.0
GlowRate = 6.0                 #
GlowMinSize = 100.0            #  Just some default values, incase they aren't set before this emmiter is created.  
GlowMaxSize = 300.0            #
GlowColor = App.TGColorA()
GlowColor.SetRGBA(254.0 / 255.0, 0.0 / 255.0, 86.0 / 255.0, 0.3700000)
###############################################################################

def Create(pTorp):
	global GlowRate, GlowMinSize, GlowMaxSize, GlowColor, CoreSize
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 0.800000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					CoreSize,
					0.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					GlowColor,
					GlowRate,	
					GlowMinSize,	 
					GlowMaxSize,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					0,		
					0.0,		
					0.01)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.01)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(0.0)

def GetLaunchSound():
	return("")

def GetPowerCost():
	return(0.0)

def GetName():
	return("Glow Emmiter")

def GetDamage():
	return 0.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.0

###############################################################################
### Custom Function ###############
# used to set custom variables values 
####################################################
def SetCustomVar(type, value):
	global GlowRate, GlowMinSize, GlowMaxSize, GlowColor, CoreSize
	if type == "Glow Rate":
		GlowRate = value
	elif type == "Glow Max Size":
		GlowMaxSize = value
	elif type == "Glow Min Size":
		GlowMinSize = value
	elif type == "Glow Color":
		GlowColor = value
	elif type == "Core Size":
		CoreSize = value
	else:
		print "Couldn't set GravityWellGlow Custom Vars. Type used not valid."
	return