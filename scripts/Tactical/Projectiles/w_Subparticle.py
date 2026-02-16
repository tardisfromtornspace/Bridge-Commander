import App


def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(100.0 / 255.0, 100.0 / 255.0 , 255.0 / 1.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(48.0 / 177.0, 33.0 / 250.0, 105.0 / 1.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0/ 1.0, 1.0 / 255.0, 1.0 / 255.0, 1.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/PoleronCore.tga",
					kCoreColor, 
					0.84,
					1.12,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					0.01,	
					0.01,	 
					0.01,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					224,		
					0.28,		
					4.0)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.28)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(95.0)

def GetLaunchSound():
	return("Sub Particle")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Sub Particle")

def GetDamage():
	return 0.1

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 2.75

try:
	modSubparticleTorp = __import__("Custom.Techs.SubparticleTorp")
	if(modSubparticleTorp):
		modSubparticleTorp.oSubparticleTorp.AddTorpedo(__name__)
except:
	print "Subparticle Torpedo script not installed, or you are missing Foundation Tech"
