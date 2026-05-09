
import App
import string
pWeaponLock = {}

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(245.0 / 255.0, 215.0 / 255.0, 255.0 / 255.0, 10.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(215.0 / 255.0, 195.0 / 255.0, 255.0 / 255.0, 10.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(155.0 / 255.0, 115.0 / 255.0, 255.0 / 255.0, 10.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NemQuantumCore.tga",
					kCoreColor, 
					0.5,
					1.0,	 
					"data/Textures/Tactical/S79QuantumGlow.tga", 
					kGlowColor,
					4.0,	
					2.0,	 
					3.5,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					85,		
					0.450,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(80)

def GetLaunchSound():
	return("RefluxQuantumIII")

def GetPowerCost():
	return(35.0)

def GetName():
	return("Reflux Quantum Mk.III")

def GetDamage():
	return 4800.0 * 4

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.65

def GetPercentage():
	return 0.02 # This is the percentage all the shields will drop from 0.00 (0%) to 1.00 (100%)

try:
	modRefluxWeapon = __import__("Custom.Techs.RefluxWeapon")
	if(modRefluxWeapon):
		modRefluxWeapon.oRefluxWeapon.AddTorpedo(__name__, GetPercentage())
except:
	print "Reflux Weapon script not installed, or you are missing Foundation Tech"