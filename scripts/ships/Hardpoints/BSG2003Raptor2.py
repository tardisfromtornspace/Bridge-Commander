#####  Created by:
#####  Bridge Commander Universal Tool
# Then modified to add this code


import App
import GlobalPropertyTemplates

	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.BSG2003Raptor"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__(ParentPropertyScript, globals(), locals(), ['*'])
	reload(ParentModule)

# Neat trick I found, reduces space used immensely
from ships.Hardpoints.BSG2003Raptor import *

# Local Templates
#################################################
#BSG2003Raptor = App.ShipProperty_Create("BSG2003Raptor")
#
#BSG2003Raptor.SetGenus(1)
#BSG2003Raptor.SetSpecies(108)
#BSG2003Raptor.SetMass(12.000000)
#BSG2003Raptor.SetRotationalInertia(10000.000000)
BSG2003Raptor.SetShipName("BSG2003Raptor2")
#BSG2003Raptor.SetModelFilename("data/Models/Ships/Raptor/Raptor.nif")
#BSG2003Raptor.SetDamageResolution(0.000100)
#BSG2003Raptor.SetAffiliation(0)
#BSG2003Raptor.SetStationary(0)
#BSG2003Raptor.SetAIString("NonFedAttack")
#BSG2003Raptor.SetDeathExplosionSound("g_lsDeathExplosions")
#App.g_kModelPropertyManager.RegisterLocalTemplate(BSG2003Raptor)
#################################################
MissileSys = App.TorpedoSystemProperty_Create("Missile Sys")

MissileSys.SetMaxCondition(4.500000)
MissileSys.SetCritical(0)
MissileSys.SetTargetable(0)
MissileSys.SetPrimary(1)
MissileSys.SetPosition(0.000000, 0.000000, 0.000000)
MissileSys.SetPosition2D(64.000000, 65.000000)
MissileSys.SetRepairComplexity(1.000000)
MissileSys.SetDisabledPercentage(0.500000)
MissileSys.SetRadius(0.005000)
MissileSys.SetNormalPowerPerSecond(1.000000)
MissileSys.SetWeaponSystemType(MissileSys.WST_TORPEDO)
MissileSys.SetSingleFire(0)
MissileSys.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
MissileSys.SetFiringChainString(kFiringChainString)
MissileSys.SetMaxTorpedoes(0, 8)
MissileSys.SetTorpedoScript(0, "Tactical.Projectiles.BSG2003ViperMissile")
MissileSys.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(MissileSys)
#################################################
PortLauncher = App.TorpedoTubeProperty_Create("Port Launcher")

PortLauncher.SetMaxCondition(1.500000)
PortLauncher.SetCritical(0)
PortLauncher.SetTargetable(1)
PortLauncher.SetPrimary(0)
PortLauncher.SetPosition(-0.016500, -0.020000, -0.010000)
PortLauncher.SetPosition2D(62.000000, 60.000000)
PortLauncher.SetRepairComplexity(1.000000)
PortLauncher.SetDisabledPercentage(0.500000)
PortLauncher.SetRadius(0.002500)
PortLauncher.SetDumbfire(1)
PortLauncher.SetWeaponID(3)
PortLauncher.SetGroups(4)
PortLauncher.SetDamageRadiusFactor(0.060000)
PortLauncher.SetIconNum(370)
PortLauncher.SetIconPositionX(70.000000)
PortLauncher.SetIconPositionY(45.000000)
PortLauncher.SetIconAboveShip(1)
PortLauncher.SetImmediateDelay(0.200000)
PortLauncher.SetReloadDelay(10.000000)
PortLauncher.SetMaxReady(2)
PortLauncherDirection = App.TGPoint3()
PortLauncherDirection.SetXYZ(0.000000, 0.997489, -0.070825)
PortLauncher.SetDirection(PortLauncherDirection)
PortLauncherRight = App.TGPoint3()
PortLauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
PortLauncher.SetRight(PortLauncherRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortLauncher)
#################################################
StarLauncher = App.TorpedoTubeProperty_Create("Star Launcher")

StarLauncher.SetMaxCondition(1.500000)
StarLauncher.SetCritical(0)
StarLauncher.SetTargetable(1)
StarLauncher.SetPrimary(0)
StarLauncher.SetPosition(0.016500, -0.020000, -0.010000)
StarLauncher.SetPosition2D(66.000000, 60.000000)
StarLauncher.SetRepairComplexity(1.000000)
StarLauncher.SetDisabledPercentage(0.500000)
StarLauncher.SetRadius(0.002500)
StarLauncher.SetDumbfire(1)
StarLauncher.SetWeaponID(3)
StarLauncher.SetGroups(4)
StarLauncher.SetDamageRadiusFactor(0.060000)
StarLauncher.SetIconNum(370)
StarLauncher.SetIconPositionX(85.000000)
StarLauncher.SetIconPositionY(45.000000)
StarLauncher.SetIconAboveShip(1)
StarLauncher.SetImmediateDelay(0.200000)
StarLauncher.SetReloadDelay(10.000000)
StarLauncher.SetMaxReady(2)
StarLauncherDirection = App.TGPoint3()
StarLauncherDirection.SetXYZ(0.000000, 0.997489, -0.070825)
StarLauncher.SetDirection(StarLauncherDirection)
StarLauncherRight = App.TGPoint3()
StarLauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
StarLauncher.SetRight(StarLauncherRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarLauncher)

# Property Set
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	#prop = App.g_kModelPropertyManager.FindByName("BSG2003Raptor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	#if (prop != None):
	#	pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missile Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Launcher", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Launcher", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)