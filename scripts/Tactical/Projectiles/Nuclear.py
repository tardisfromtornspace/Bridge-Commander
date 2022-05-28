import App
import trails.Nuclear
import loadspacehelper
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.0, 0.0, 0.0, 1.0)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.0, 0.0, 0.0, 1.0)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.05)	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )
	pTorpID = pTorp.GetObjID()
	pTorpShip = loadspacehelper.CreateShip("Nuclear", pTorp.GetContainingSet(), "SolidTorpedo" + str(pTorpID), "")
	pTorp.AttachObject(pTorpShip)
	pTorp.AddPythonFuncHandlerForInstance(App.ET_WEAPON_HIT, __name__ + ".TorpedoHit")

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)


        ## Add a creation handler to the torpedo :)
        trails.Nuclear.AddCreationHandler(pTorp, __name__ + ".AttachSmoke")
        return(0)

def AttachSmoke(self, pEvent = None):
    ## Attach Missile Effect
    pTorpedo = App.Torpedo_Cast(pEvent.GetDestination())
    if not pTorpedo:
        return (1)
    ## Create and Play a sequence
    trails.Nuclear.SetupSmokeTrail(pTorpedo)
    return (0)

def TorpedoHit(pObject, pEvent):
	pTorp = None
	pTorp = App.TorpedoClass_Cast(pObject)
	if not pTorp:
		pObject.CallNextHandler(pEvent)
		return

	global pTorpShip
	pTorpID = pTorp.GetObjID()
	if not pTorpShip.has_key(pTorpID):
		pObject.CallNextHandler(pEvent)
		return
	if not pTorpShip[pTorpID]:
		pObject.CallNextHandler(pEvent)
		return
	pSet = pTorp.GetContainingSet()
	if not pSet:
		pObject.CallNextHandler(pEvent)
		return
	pSet.DeleteObjectFromSet(pTorpShip[pTorpID].GetName())
	pObject.CallNextHandler(pEvent)

def GetLaunchSpeed():
	return(11)

def GetLaunchSound():
	return("Nuclear")

def GetPowerCost():
	return(1.0)

def GetName():
	return("Spatial Torpedo")

def GetDamage():
	return 500.0

def GetGuidanceLifetime():
	return 60.0

def GetMaxAngularAccel():
	return 0.16

def GetLifetime():
	return 60.0
