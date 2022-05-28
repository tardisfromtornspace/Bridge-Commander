#########################################################
#########################################################
##                                                     ##
##  Diamond BC - Projectiles v1                        ##
##  By MLeo Daalder                                    ##
##                                                     ##
##  This mod will prevent the game from crashing when  ##
##  projectile files don't exist by substituting the   ##
##  projectile with a dummy.                           ##
##                                                     ##
#########################################################
#########################################################

version = "20090411"

import App


## The method that actually verifies that
lImportantFunctions = [ "Create","GetLaunchSpeed", "GetLaunchSound", "GetPowerCost", "GetName" ]
def verifyAndCorrectProjectileFile(projectile):
	try:
		try:
			torpedoScript = __import__(projectile)
		except ImportError:
			# look in AddOn-Folder
			import string
			projectile = string.replace(projectile, "Tactical.", "Custom.AddOn.")
			torpedoScript = __import__(projectile)
			print "Projectile %s found in AddOn-Folder" % (string.split(projectile, '.')[-1])
		lMissing = []
		global lImportantFunctions
		for func in lImportantFunctions:
			if not hasattr(torpedoScript, func):
				lMissing.append(func)
		for missing in lMissing:
			print "WARNING: the projectile:", projectile, "is missing the function:", missing
	except:
		print "WARNING: the projectile:", projectile, "is not found!"
		projectile = __name__
	return projectile

def override(module, path, producer):
	parent = module
	for segment in path[:-1]:
		parent = getattr(parent, segment)
	next = getattr(parent, path[-1])
	setattr(parent, path[-1], producer(next))

## The overrides that provide crash resistance
override(App, ["TorpedoAmmoType", "SetTorpedoScript"], lambda next: lambda self, type, next=next: next(self, verifyAndCorrectProjectileFile(type)))
override(App, ["TorpedoSystemProperty", "SetTorpedoScript"], lambda next: lambda self, position, module, next=next: next(self, position, verifyAndCorrectProjectileFile(module)))
override(App, ["PulseWeaponProperty", "SetModuleName"], lambda next: lambda self, projectile, next=next: next(self, verifyAndCorrectProjectileFile(projectile)))


App.TorpedoAmmoType.__setmethods__["m_pcModule"] = lambda self, projectile, next=App.TorpedoAmmoType.__setmethods__["m_pcModule"]: next(self, verifyAndCorrectProjectileFile(projectile))




# Annoying! This is the only one of which I don't know how many it could possibly take!
originalTorpedo_Create = App.Torpedo_Create
def Torpedo_Create(*args):
	args = list(args)
	if len (args) > 0:
		args[0] = verifyAndCorrectProjectileFile(args[0])

	global originalTorpedo_Create
	return apply(originalTorpedo_Create, tuple(args))

App.Torpedo_Create = Torpedo_Create



## The last of this module part pretends that this projectile is a real projectile module ##
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 65.0 / 255.0, 0.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.2,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.3,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					8,		
					0.7,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	#import Multiplayer.SpeciesToTorp
	#pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(19.0)

def GetLaunchSound():
	return("Photon Torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("ProjectileSubstitute")

def GetDamage():
	return 500.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.15

