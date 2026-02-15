 # uncompyle6 version 3.7.4
# Python bytecode 1.5 (20121)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: .\Scripts\Tactical\Projectiles\ZZ_VoyPhoton.py
# Compiled at: 2007-09-04 01:52:12
import App

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(245.0 / 255.0, 163.0 / 255.0, 0.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 205.0 / 130.0, 100.0 / 255.0, 1.0)
   
    pTorp.CreateTorpedoModel(
                'data/Textures/Tactical/SFRD_NXphotonicTorpedoCore.tga', 
                kCoreColor, 
                0.95, 
                1.0, 
                'data/Textures/Tactical/SFPhoton.tga', 
                kGlowColor, 
                2.0, 
                1.55, 
                1.75, 
                'data/Textures/Tactical/TorpedoFlares.tga', 
                kGlowColor, 
                0, 
                0.5, 
                0.975)
    
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.07)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 70.0


def GetLaunchSound():
    return 'PhotonTorp8'


def GetPowerCost():
    return 5.0


def GetName():
    return 'Photon Torpedoes'


def GetDamage():
    return 950.0


def GetGuidanceLifetime():
    return 8.0


def GetMaxAngularAccel():
    return 3.45


def GetLifetime():
    return 10.55