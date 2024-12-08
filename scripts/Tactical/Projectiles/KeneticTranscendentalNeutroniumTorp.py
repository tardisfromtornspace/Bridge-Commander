###############################################################################
# requires Future Technologies Addition 1.0 or higher
###############################################################################

import App
import MissionLib

###############################################################################
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 82.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(1.000000, 0.784314, 0.000000, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(250.0 / 255.0, 18.0 / 255.0, 2.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_PlasmaTorpCORE.tga",
					kCoreColor, 
					0.5,
					1.0,	 
					"data/Textures/Tactical/ZZ_PlasmaTorpGLOW.tga", 
					kGlowColor,
					50.0,	
					0.5,	 
					0.7,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					50,		
					0.4,		
					0.6)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.05)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(85)

def GetLaunchSound():
	return("KeneticTranscendentalNeutroniumTorp")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Trans-Neutronium Torp")

def GetDamage():
	return 6500000

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 1.5

def TargetHit(pObject, pEvent):
	return