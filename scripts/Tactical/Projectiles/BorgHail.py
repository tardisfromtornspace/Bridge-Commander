########################################################################
#	Filename:	BorgHail.py				       #
#								       #
#	Description:	Creates a powerless, invisible torpedo whose   #
#			launch sound is a Borg hail		       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################
import App

def Create(pTorp):
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0, 0, 0, 0)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kGlowColor, 
					0.2,
					1.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.3,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlaresST.tga",
					kGlowColor,										
					0,		
					0.5,		
					0.4)

	pTorp.SetDamage(0)
	pTorp.SetDamageRadiusFactor(0.0)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
    return 200.0

def GetLaunchSound():
    return 'DYfutile'

def GetPowerCost():
    return 0.0

def GetName():
    return 'Hail'

def GetGuidanceLifetime():
    return 0.0

def GetMaxAngularAccel():
    return 0.0