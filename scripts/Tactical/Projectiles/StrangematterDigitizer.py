#script modified by Dragon

import App
import string

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(225.0 / 255.0, 225.0 / 255.0, 1.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(225.0 / 255.0, 225.0 / 255.0, 1.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(225.0 / 255.0, 225.0 / 255.0, 1.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/Digitizer.tga",
					kCoreColor, 
					16.0,
					120.0,	 
					"data/Textures/Tactical/Digitizer.tga", 
					kGlowColor,
					320.0,	
					16.0,	 
					16.0,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					60,		
					5.5,		
					0.1)

	pTorp.SetDamage(1000000)
	pTorp.SetDamageRadiusFactor(50.0)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("StrangematterDigitizer")

def GetPowerCost():
	return(80.0)

def GetName():
	return("Strangematter Digitizer")

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.6

try:
	modDigitizerTorp = __import__("Custom.Techs.DigitizerTorp")
	if(modDigitizerTorp):
		modDigitizerTorp.oDigitizerTorp.AddTorpedo(__name__)
except:
	print "Digitizer Torpedo script not installed, or you are missing Foundation Tech"