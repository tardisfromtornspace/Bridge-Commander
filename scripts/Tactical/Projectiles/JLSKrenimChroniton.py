import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
    	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.0)
    	kGlowColor = App.TGColorA()
    	kGlowColor.SetRGBA(102.0 / 255.0, 51.0 / 255.0, 102.0 / 255.0, 1.0)
    	kFlareColor = App.TGColorA()
    	kFlareColor.SetRGBA(153.0 / 255.0, 102.0 / 255.0, 153.0 / 255.0, 1.0)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
                               		0.31,
                               		1.2,	 
					"data/textures/tactical/JTorpedoGlow.tga", 
					kGlowColor,
                               		1.0,
                              		0.2,
                              		0.3,	
					"data/textures/tactical/TorpedoFlares.tga",
					kGlowColor,										
                        	        40,
                                	0.1,
                                	0.27)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
        pTorp.SubTorp = "Tactical.Projectiles.JLSKrenimChroniton_P" # Extra for teh chronitonTorp

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(45.0)

def GetLaunchSound():
	return("JLSKrenimChroniton")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Chroniton Torpedo")

def GetDamage():
	return 0.001

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 1.1

try:
	modChronitonTorpe = __import__("Custom.Techs.ChronitonTorpe")
	if(modChronitonTorpe):
		modChronitonTorpe.oChronitonTorpe.AddTorpedo(__name__)
except:
	"Chroniton Torpedo script not installed, or you are missing Foundation Tech"

