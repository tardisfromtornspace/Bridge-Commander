#script modified by D&G Productions

import App
import MissionLib

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(245.0 / 255.0, 215.0 / 255.0, 255.0 / 255.0, 5.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(215.0 / 255.0, 175.0 / 255.0, 255.0 / 255.0, 5.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(205.0 / 255.0, 165.0 / 255.0, 235.0 / 255.0, 5.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NemQuantumCore.tga",
					kCoreColor, 
					0.8,
					1.0,	 
					"data/Textures/Tactical/S79QuantumGlow.tga", 
					kGlowColor,
					4.0,	
					7.0,	 
					7.05,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					96,		
					0.395,		
					0.15)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.45)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(135.0)

def GetLaunchSound():
	return("Reflux_Quantum")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Reflux Quantums")

def GetDamage():
	return 12800.0

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 0.5

# Sets the percentage of shield damage the torpedo will do
def GetPercentage():
	return 0.15

try:
	modRefluxWeapon = __import__("Custom.Techs.RefluxWeapon")
	if(modRefluxWeapon):
		modRefluxWeapon.oRefluxWeapon.AddTorpedo(__name__, GetPercentage())
except:
	print "Reflux Weapon script not installed, or you are missing Foundation Tech"