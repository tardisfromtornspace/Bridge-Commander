import App
def Create(pTorp):
        kCoreColor = App.TGColorA()
        kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
        kGlowColor = App.TGColorA()
        kGlowColor.SetRGBA((25.0 / 255.0), (25.0 / 255.0), (50.0 / 255.0), 1.0)
        kFlareColor = App.TGColorA()
        kFlareColor.SetRGBA((50.0 / 255.0), (50.0 / 255.0), (100.0 / 255.0), 1.0)
        pTorp.CreateTorpedoModel(
                "Scripts/Custom/BCSTNG/CWP/Textures/BlackelmquantumCore.tga",
                kCoreColor,
                0.2,
                1.2,
                "Scripts/Custom/BCSTNG/CWP/Textures/BlackelmTorpedoGlow.tga",
                kGlowColor,
                3.0,
                0.2,
                0.4,
                "Scripts/Custom/BCSTNG/CWP/Textures/BlackelmTorpedoFlares.tga",
                kFlareColor,
                0,
                0.15,
                0.3)
        pTorp.SetDamage(GetDamage())
        pTorp.SetDamageRadiusFactor(0.14)
        pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
        pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
        import Multiplayer.SpeciesToTorp
        pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)  
        return (0)

def GetLaunchSpeed():
        return (35.0)

def GetLaunchSound():
        return ("blackelmtype2quantum")

def GetPowerCost():
        return (10.0)

def GetName():
        return ("Type 2 Quantum : 5")

def GetDamage():
        return 1200.0

def GetGuidanceLifetime():
        return 6.0

def GetMaxAngularAccel():
        return 0.25

try:
        import FoundationTech
        import ftb.Tech.TimedTorpedoes

        oFire = ftb.Tech.TimedTorpedoes.MIRVSingleTargetTorpedo(
                'Spread5', {
                        'spreadNumber':	5,
                        'spreadDensity': 7.5,
                        'warheadModule': 'Custom.BCSTNG.CWP.Scripts.blackelmtype2quantum',
                        'shellLive': 0,
                })
        FoundationTech.dOnFires[__name__] = oFire
except:
        pass


