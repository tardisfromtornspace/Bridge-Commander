
import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 4.000000)   #Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(182.0 / 255.0, 203.0 / 255.0, 239.0 / 255.0, 8.000000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 3.000000)   #Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZQuantumCore.tga",
					kCoreColor, 
					0.3,   #size
					8.0,   #rotation speed, positive is counterclockwise -negative clockwise 
					"data/Textures/Tactical/Quantum03Glow.tga", 
					kGlowColor,
					1.5,	#glow pulsate speed
					0.7,	#glow max radius
					0.6,	#glow min radius
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					150,		#number of flares
					0.15,	#flare size	
					0.02)   #flare speed

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(105.0)

def GetLaunchSound():
	return("27CDiffusionCannon")

def GetPowerCost():
	return(5.0)

def GetName():
	return("27CDiffusionCannon")

def GetDamage():
	return 3000.0

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.60
