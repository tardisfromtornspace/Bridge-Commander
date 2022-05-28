import App
import trails.TauriT1
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.5, 0.5, 1.0, 1.0)
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.8, 0.8, 1.0, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.2)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)


        ## Add a creation handler to the torpedo :)
        trails.TauriT1.AddCreationHandler(pTorp, __name__ + ".AttachSmoke")
        return(0)

def AttachSmoke(self, pEvent = None):
    ## Attach Missile Effect
    pTorpedo = App.Torpedo_Cast(pEvent.GetDestination())
    if not pTorpedo:
        return (1)
    ## Create and Play a sequence
    trails.TauriT1.SetupSmokeTrail(pTorpedo)
    return (0)

def GetLaunchSpeed():
	return(45)

def GetLaunchSound():
	return("TauriT1")

def GetPowerCost():
	return(1.0)

def GetName():
	return("Tauri Torpedo Type 1")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 60.0

def GetMaxAngularAccel():
	return 0.16

def GetLifetime():
	return 60.0
