import App
def Create(pTorp):
        kCoreColor = App.TGColorA()
        kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 128.0 / 255.0, 1.000000)
        kGlowColor = App.TGColorA()
        kGlowColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 1.000000)	
        kFlareColor = App.TGColorA()
        kFlareColor.SetRGBA(225.0/ 191.0, 255.0 / 49.0, 17.0 / 255.0, 1.000000)
        pTorp.CreateTorpedoModel(
                "data/Textures/Tactical/ds9torp.tga",
                kCoreColor, 
                0.2,
                6.0,	 
                "data/Textures/Tactical/ds9torp.tga", 
                kGlowColor,
                1.0,	
                0.5,	 
                0.6,	
                "data/Textures/Tactical/TorpedoFlares.tga",
                kGlowColor,						
                12,		
                0.4,		
                0.1)
        pTorp.SetDamage( GetDamage() )
        pTorp.SetDamageRadiusFactor(0.13)
        pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
        pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
        import Multiplayer.SpeciesToTorp
        pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)
        return(0)

def GetLaunchSpeed():
        return(30.0)

def GetLaunchSound():
        return("blackelmtype6photon")

def GetPowerCost():
        return(20.0)

def GetName():
        return("Type 6 Photon")

def GetDamage():
        return 850.0

def GetGuidanceLifetime():
        return 10.0

def GetMaxAngularAccel():
        return 0.35
