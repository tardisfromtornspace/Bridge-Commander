
import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 250.0 / 255.0, 250.0 / 255.0, 1.000000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 215.0 / 255.0, 245.0 / 255.0, 1.000000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 225.0 / 255.0, 225.0 / 255.0, 1.000000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZQuantumCore.tga",
					kCoreColor, 
					0.1,	#size
					3.2,	#rotation speed, positive is counterclockwise -negative clockwise
					"data/Textures/Tactical/ZZQuantumGlow.tga", 
					kGlowColor,
					1.0,	#glow pulsate speed
					2.0,	#glow max radius
					1.5,	#glow min radius
					"data/Textures/Tactical/TMPFlares.tga",
					kGlowColor,										
					120.0,	#number of flares
					0.5,	#flare size
					5.0)	#flare speed

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(1.50)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(59.0)

def GetLaunchSound():
	return("WDRchroniton")

def GetPowerCost():
	return(35.0)

def GetName():
	return("Chronoton Torpedo")

def GetDamage():
	return 9000

def GetGuidanceLifetime():
	return 18.0

def GetMaxAngularAccel():
	return 0.9

try:
	modChronitonTorpe = __import__("Custom.Techs.ChronitonTorpe")
	if(modChronitonTorpe):
		modChronitonTorpe.oChronitonTorpe.AddTorpedo(__name__)
except:
	print "Chroniton Torpedo script not installed, or you are missing Foundation Tech"