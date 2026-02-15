 # uncompyle6 version 3.7.4
# Python bytecode 1.5 (20121)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: .\Scripts\Tactical\Projectiles\ZZ_VoyPhoton.py
# Compiled at: 2007-09-04 01:52:12
import App

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 210.0 / 255.0, 40.0 / 255.0, 1.000000)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 210.0 / 255.0, 40.0 / 255.0, 1.000000)
   
    pTorp.CreateTorpedoModel(
                'data/Textures/Tactical/Mk10PhotonFlare.tga', 
                kCoreColor, 
                0.2,
            	1.4,	
                'data/Textures/Tactical/Mk10Photon.tga', 
                kGlowColor, 
                2.3,	
				0.6,	 
				0.95,
                'data/Textures/Tactical/Mk10PhotonFlare.tga', 
                kGlowColor, 
                11,		
				0.9,		
				0.3)
    
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.12)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 70.0


def GetLaunchSound():
    return 'Mk10Photon'


def GetPowerCost():
    return 5.0


def GetName():
    return 'Photon Torpedo'


def GetDamage():
    return 1140.0


def GetGuidanceLifetime():
    return 10.0


def GetMaxAngularAccel():
    return 3.329


def GetLifetime():
    return 30.0