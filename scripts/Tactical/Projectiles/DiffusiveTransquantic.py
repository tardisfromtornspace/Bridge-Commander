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
	kGlowColor.SetRGBA(170.0 / 255.0, 245.0 / 255.0, 255.0 / 255.0, 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(35.0 / 255.0, 255.0 / 255.0, 220.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(85.0 / 255.0, 150.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TransphasicFlares.tga",
					kCoreColor, 
					0.225,
					-1.25,	 
					"data/Textures/Tactical/TransphasicGlow.tga", 
					kGlowColor,
					3.25,	
					0.50,	 
					0.65,	
					"data/Textures/Tactical/TransphasicCore.tga",
					kGlowColor,										
					25,		
					0.65,		
					0.20)

	pTorp.SetDamage(GetDamage(0))
	pTorp.SetDamageRadiusFactor(450.00)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(120.0)

def GetLaunchSound():
	return("DiffusiveTransquantic")

def GetPowerCost():
	return(170.01)

def GetName():
	return("Diffusive Transquantic")

def GetDamage(ponderforAI=1): # call this as GetDamage(0) on the torp to give it proper damage.
	if ponderforAI == 1: # Damage others will see
		return (1200.0) # Still a lot but way less than the other projectiles, so it will choose this one last
	else: # True damage
		return(13500.0)

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 1.265

try:
	modTransphasicTorp = __import__("Custom.Techs.TransphasicTorp")
	if(modTransphasicTorp):
		modTransphasicTorp.oTransphasicTorp.AddTorpedo(__name__)
except:
	print "Transphasic Torpedo script not installed, or you are missing Foundation Tech"