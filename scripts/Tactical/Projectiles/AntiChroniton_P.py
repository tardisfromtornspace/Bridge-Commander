import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(100.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(200.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 1.000000)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
    
    
    pTorp.CreateTorpedoModel(
        			'data/Textures/Tactical/AntiChroniton.tga', 
           			kCoreColor, 
              		0.38, 
                	1.0, 
                 	'data/Textures/Tactical/AntiChronitonGlow.tga', 
                  	kGlowColor, 
                   	1.0, 
                    0.4, 
                    0.5, 
                    'data/Textures/Tactical/TorpedoFlares.tga', 
                    kFlareColor, 
                    0, 
                    0.0, 
                    0.00)
    
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.2)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHASEDPLASMA)
    return 0


def GetLaunchSpeed():
    return (290.0)


def GetLaunchSound():
    return ('AntiChroniton')


def GetPowerCost():
    return (30.0)


def GetName():
    return ('Anti Chroniton')


def GetDamage():
    return (5200.0)


def GetGuidanceLifetime():
    return (1.0)


def GetMaxAngularAccel():
    return (1.0)

try:
	modChronitonTorpe = __import__("Custom.Techs.ChronitonTorpe")
	if(modChronitonTorpe):
		modChronitonTorpe.oChronitonTorpe.AddTorpedo(__name__)
except:
	print "Chroniton Torpedo script not installed, or you are missing Foundation Tech"
