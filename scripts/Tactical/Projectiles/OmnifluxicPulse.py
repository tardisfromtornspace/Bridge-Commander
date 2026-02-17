import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(60.0 / 255.0, 255.0 / 255.0, 200.0 / 255.0, 1.000000)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(40.0 / 255.0, 60.0 / 255.0, 245.0 / 255.0, 1.000000)
    
    
    pTorp.CreateTorpedoModel(
        			'data/Textures/Tactical/OmnifluxicCore.tga', 
           			kCoreColor, 
              		0.38, 
                	1.0, 
                 	'data/Textures/Tactical/OmnifluxicGlow.tga', 
                  	kGlowColor, 
                   	1.0, 
                    0.4, 
                    0.5, 
                    'data/Textures/Tactical/TorpedoFlares.tga', 
                    kGlowColor, 
                    0, 
                    0.0, 
                    0.00)
    
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.2)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.POSITRON)
    return 0


def GetLaunchSpeed():
    return (290.0)


def GetLaunchSound():
    return ('OmnifluxicPulse')


def GetPowerCost():
    return (30.0)


def GetName():
    return ('Omnifluxic Pulse')


def GetDamage():
    return (5750.0 * 4)


def GetGuidanceLifetime():
    return (0.15)


def GetMaxAngularAccel():
    return (0.0)

"""
# Hm.... maybe?
try:
	modTimeVortexTorp = __import__("Custom.Techs.TimeVortexTorp")
	if(modTimeVortexTorp):
		modTimeVortexTorp.oTimeVortexTorp.AddTorpedo(__name__)
except:
	print "TimeVortex Torpedo script not installed, or you are missing Foundation Tech"
"""
