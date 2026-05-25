
import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 0.000000)   #Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(85.0 / 255.0, 150.0 / 255.0, 255.0 / 255.0, 0.000000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 0.000000)   #Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZQuantumCore.tga",
					kCoreColor, 
					0.0001,   #size
					0.0001,   #rotation speed, positive is counterclockwise -negative clockwise 
					"data/Textures/Tactical/Quantum03Glow.tga", 
					kGlowColor,
					0.0001,	#glow pulsate speed
					0.0001,	#glow max radius
					0.0001,	#glow min radius
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					0,		#number of flares
					0.0001,	#flare size	
					0.0001)   #flare speed

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.0001)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(10000)

def GetLaunchSound():
	return("")

def GetPowerCost():
	return(0.0001)

def GetName():
	return("No Torpedoes")

def GetDamage():
	return 0.0001

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.0