
import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 0.650000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZQuantumCore.tga",
					kCoreColor, 
					0.0,	#size
					0.0,	#rotation speed, positive is counterclockwise -negative clockwise
					"data/Textures/Tactical/DuskTorpedoGlow.tga", 
					kGlowColor,
					0.65,	#glow pulsate speed
					1.7,	#glow max radius
					3.6,	#glow min radius
					"data/Textures/Tactical/TMPFlares.tga",
					kGlowColor,										
					0.0,	#number of flares
					0.0,	#flare size
					0.0)	#flare speed

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.32)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(45.0)

def GetLaunchSound():
	return("DuskTorpedo")

def GetPowerCost():
	return(500.0)

def GetName():
	return("Dusk Torpedo")

def GetDamage():
	return 750000.0

def GetGuidanceLifetime():
	return 17.5

def GetMaxAngularAccel():
	return 0.5

