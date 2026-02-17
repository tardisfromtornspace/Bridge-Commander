import App


def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 0.0 / 255.0 , 20.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 245.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(215.0/ 255.0, 0.0 / 255.0, 255.0 / 255.0, 1.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CyclomorphicTriOmniumCore.tga",
					kCoreColor, 
					0.25,
					1.1,	 
					"data/Textures/Tactical/CyclomorphicTriOmniumGlow.tga", 
					kGlowColor,
					0.01,	
					1.3,	
					1.5,	
					"data/Textures/Tactical/CyclomorphicTriOmniumFlares.tga",
					kFlareColor,										
					275,		
					0.650,		
					4.0)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.30)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(105.0)

def GetLaunchSound():
	return("CyclomorphicTriOmnium")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Cyclomorphic Tri-Omnium")

def GetDamage():
	return 5750.0 * 4.25

def GetGuidanceLifetime():
	return 12.5

def GetMaxAngularAccel():
	return 2.5

try:
	modSubparticleTorp = __import__("Custom.Techs.SubparticleTorp")
	if(modSubparticleTorp):
		modSubparticleTorp.oSubparticleTorp.AddTorpedo(__name__)
except:
	print "Subparticle Torpedo script not installed, or you are missing Foundation Tech"
