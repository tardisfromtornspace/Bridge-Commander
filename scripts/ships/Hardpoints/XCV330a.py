# D:\Setup\Setup Files\Program Setup Files\Games\Game Updates\Star Trek\Bridge Commander\BC MOD\Update\scripts\ships\Hardpoints\XCV330a.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
XCV330a = App.ShipProperty_Create("XCV330a")

XCV330a.SetGenus(1)
XCV330a.SetSpecies(101)
XCV330a.SetMass(10.000000)
XCV330a.SetRotationalInertia(1000.000000)
XCV330a.SetShipName("XCV330a")
XCV330a.SetModelFilename("data/Models/Ships/XCV330/XCV330a.nif")
XCV330a.SetDamageResolution(10.000000)
XCV330a.SetAffiliation(0)
XCV330a.SetStationary(0)
XCV330a.SetAIString("FedAttack")
XCV330a.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(XCV330a)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(4000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -0.550000, 0.000000)
Hull.SetPosition2D(64.000000, 64.000000)
Hull.SetRepairComplexity(2.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.050000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
Bridge = App.HullProperty_Create("Bridge")

Bridge.SetMaxCondition(4000.000000)
Bridge.SetCritical(1)
Bridge.SetTargetable(1)
Bridge.SetPrimary(0)
Bridge.SetPosition(0.000000, 1.600000, 0.110000)
Bridge.SetPosition2D(64.000000, 30.000000)
Bridge.SetRepairComplexity(2.000000)
Bridge.SetDisabledPercentage(0.000000)
Bridge.SetRadius(0.050000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Bridge)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(2000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 1.567000, -0.086000)
SensorArray.SetPosition2D(64.000000, 20.000000)
SensorArray.SetRepairComplexity(2.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.030000)
SensorArray.SetNormalPowerPerSecond(50.000000)
SensorArray.SetBaseSensorRange(500.000000)
SensorArray.SetMaxProbes(15)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
HullIntegrity = App.ShieldProperty_Create("Hull Polarizer")

HullIntegrity.SetMaxCondition(2200.000000)
HullIntegrity.SetCritical(0)
HullIntegrity.SetTargetable(0)
HullIntegrity.SetPrimary(1)
HullIntegrity.SetPosition(0.000000, 0.000000, 0.000000)
HullIntegrity.SetPosition2D(64.000000, 50.000000)
HullIntegrity.SetRepairComplexity(2.000000)
HullIntegrity.SetDisabledPercentage(0.500000)
HullIntegrity.SetRadius(0.010000)
HullIntegrity.SetNormalPowerPerSecond(0.000000)
HullIntegrityShieldGlowColor = App.TGColorA()
HullIntegrityShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
HullIntegrity.SetShieldGlowColor(HullIntegrityShieldGlowColor)
HullIntegrity.SetShieldGlowDecay(1.000000)
HullIntegrity.SetMaxShields(HullIntegrity.FRONT_SHIELDS, 90.000000)
HullIntegrity.SetMaxShields(HullIntegrity.REAR_SHIELDS, 90.000000)
HullIntegrity.SetMaxShields(HullIntegrity.TOP_SHIELDS, 90.000000)
HullIntegrity.SetMaxShields(HullIntegrity.BOTTOM_SHIELDS, 90.000000)
HullIntegrity.SetMaxShields(HullIntegrity.LEFT_SHIELDS, 90.000000)
HullIntegrity.SetMaxShields(HullIntegrity.RIGHT_SHIELDS, 90.000000)
HullIntegrity.SetShieldChargePerSecond(HullIntegrity.FRONT_SHIELDS, 1.000000)
HullIntegrity.SetShieldChargePerSecond(HullIntegrity.REAR_SHIELDS, 1.000000)
HullIntegrity.SetShieldChargePerSecond(HullIntegrity.TOP_SHIELDS, 1.000000)
HullIntegrity.SetShieldChargePerSecond(HullIntegrity.BOTTOM_SHIELDS, 1.000000)
HullIntegrity.SetShieldChargePerSecond(HullIntegrity.LEFT_SHIELDS, 1.000000)
HullIntegrity.SetShieldChargePerSecond(HullIntegrity.RIGHT_SHIELDS, 1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(HullIntegrity)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(1.000000)
Engineering.SetCritical(0)
Engineering.SetTargetable(0)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, 0.000000)
Engineering.SetPosition2D(0.000000, 0.000000)
Engineering.SetRepairComplexity(2.000000)
Engineering.SetDisabledPercentage(0.100000)
Engineering.SetRadius(0.010000)
Engineering.SetNormalPowerPerSecond(0.000000)
Engineering.SetMaxRepairPoints(20.000000)
Engineering.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
t = App.TorpedoSystemProperty_Create("t")

t.SetMaxCondition(1.000000)
t.SetCritical(0)
t.SetTargetable(0)
t.SetPrimary(1)
t.SetPosition(0.000000, 0.000000, 0.000000)
t.SetPosition2D(0.000000, 0.000000)
t.SetRepairComplexity(2.000000)
t.SetDisabledPercentage(0.500000)
t.SetRadius(0.010000)
t.SetNormalPowerPerSecond(0.000000)
t.SetWeaponSystemType(t.WST_TORPEDO)
t.SetSingleFire(1)
t.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
t.SetFiringChainString(kFiringChainString)
t.SetMaxTorpedoes(0, 0)
t.SetTorpedoScript(0, "Tactical.Projectiles.NXTorpedo")
t.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(t)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(2000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.550000, 0.000000)
WarpCore.SetPosition2D(64.000000, 96.000000)
WarpCore.SetRepairComplexity(2.000000)
WarpCore.SetDisabledPercentage(0.000000)
WarpCore.SetRadius(0.020000)
WarpCore.SetMainBatteryLimit(15000.000000)
WarpCore.SetBackupBatteryLimit(15000.000000)
WarpCore.SetMainConduitCapacity(187.500000)
WarpCore.SetBackupConduitCapacity(18.750000)
WarpCore.SetPowerOutput(150.000000*0.999)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(1.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, 0.000000, 0.000000)
WarpEngines.SetPosition2D(0.000000, 0.000000)
WarpEngines.SetRepairComplexity(2.000000)
WarpEngines.SetDisabledPercentage(0.500000)
WarpEngines.SetRadius(0.010000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
PortNacelle = App.EngineProperty_Create("Port Nacelle")

PortNacelle.SetMaxCondition(2000.000000)
PortNacelle.SetCritical(0)
PortNacelle.SetTargetable(1)
PortNacelle.SetPrimary(1)
PortNacelle.SetPosition(-0.855000, -0.600000, 0.000000)
PortNacelle.SetPosition2D(32.000000, 90.000000)
PortNacelle.SetRepairComplexity(2.000000)
PortNacelle.SetDisabledPercentage(0.500000)
PortNacelle.SetRadius(0.200000)
PortNacelle.SetEngineType(PortNacelle.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortNacelle)
#################################################
StarNacelle = App.EngineProperty_Create("Star Nacelle")

StarNacelle.SetMaxCondition(2000.000000)
StarNacelle.SetCritical(0)
StarNacelle.SetTargetable(1)
StarNacelle.SetPrimary(1)
StarNacelle.SetPosition(0.855000, -0.600000, 0.000000)
StarNacelle.SetPosition2D(96.000000, 90.000000)
StarNacelle.SetRepairComplexity(2.000000)
StarNacelle.SetDisabledPercentage(0.500000)
StarNacelle.SetRadius(0.200000)
StarNacelle.SetEngineType(StarNacelle.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarNacelle)
#################################################
FusionEngine = App.ImpulseEngineProperty_Create("Fusion Engine")

FusionEngine.SetMaxCondition(1.000000)
FusionEngine.SetCritical(0)
FusionEngine.SetTargetable(0)
FusionEngine.SetPrimary(1)
FusionEngine.SetPosition(0.000000, 0.000000, 0.000000)
FusionEngine.SetPosition2D(0.000000, 0.000000)
FusionEngine.SetRepairComplexity(2.000000)
FusionEngine.SetDisabledPercentage(0.500000)
FusionEngine.SetRadius(0.010000)
FusionEngine.SetNormalPowerPerSecond(100.000000)
FusionEngine.SetMaxAccel(2.000000)
FusionEngine.SetMaxAngularAccel(0.200000)
FusionEngine.SetMaxAngularVelocity(0.300000)
FusionEngine.SetMaxSpeed(8.000000)
FusionEngine.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(FusionEngine)
#################################################
Engine = App.EngineProperty_Create("Engine")

Engine.SetMaxCondition(2000.000000)
Engine.SetCritical(0)
Engine.SetTargetable(1)
Engine.SetPrimary(1)
Engine.SetPosition(0.000000, -0.810000, 0.000000)
Engine.SetPosition2D(64.000000, 80.000000)
Engine.SetRepairComplexity(2.000000)
Engine.SetDisabledPercentage(0.500000)
Engine.SetRadius(0.200000)
Engine.SetEngineType(Engine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine)
#################################################
ShuttleBay = App.HullProperty_Create("Shuttle Bay")

ShuttleBay.SetMaxCondition(1.000000)
ShuttleBay.SetCritical(0)
ShuttleBay.SetTargetable(0)
ShuttleBay.SetPrimary(0)
ShuttleBay.SetPosition(0.050000, 1.410000, 0.042500)
ShuttleBay.SetPosition2D(0.000000, 0.000000)
ShuttleBay.SetRepairComplexity(5.000000)
ShuttleBay.SetDisabledPercentage(0.750000)
ShuttleBay.SetRadius(0.150000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay)
#################################################
ShuttleBayOEP = App.ObjectEmitterProperty_Create("Shuttle Bay OEP")

ShuttleBayOEPForward = App.TGPoint3()
ShuttleBayOEPForward.SetXYZ(1.000000, 0.000000, 0.000000)
ShuttleBayOEPUp = App.TGPoint3()
ShuttleBayOEPUp.SetXYZ(0.000000, 0.000000, 1.000000)
ShuttleBayOEPRight = App.TGPoint3()
ShuttleBayOEPRight.SetXYZ(0.000000, 1.000000, 0.000000)
ShuttleBayOEP.SetOrientation(ShuttleBayOEPForward, ShuttleBayOEPUp, ShuttleBayOEPRight)
ShuttleBayOEPPosition = App.TGPoint3()
ShuttleBayOEPPosition.SetXYZ(0.050000, 1.410000, 0.042500)
ShuttleBayOEP.SetPosition(ShuttleBayOEPPosition)
ShuttleBayOEP.SetEmittedObjectType(ShuttleBayOEP.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBayOEP)
#################################################
ProbeLauncher = App.ObjectEmitterProperty_Create("Probe Launcher")

ProbeLauncherForward = App.TGPoint3()
ProbeLauncherForward.SetXYZ(0.000000, 1.000000, 0.000000)
ProbeLauncherUp = App.TGPoint3()
ProbeLauncherUp.SetXYZ(0.000000, 0.000000, 1.000000)
ProbeLauncherRight = App.TGPoint3()
ProbeLauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
ProbeLauncher.SetOrientation(ProbeLauncherForward, ProbeLauncherUp, ProbeLauncherRight)
ProbeLauncherPosition = App.TGPoint3()
ProbeLauncherPosition.SetXYZ(0.000000, 0.840000, 0.000000)
ProbeLauncher.SetPosition(ProbeLauncherPosition)
ProbeLauncher.SetEmittedObjectType(ProbeLauncher.OEP_PROBE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ProbeLauncher)
#################################################
DecoyLauncher = App.ObjectEmitterProperty_Create("Decoy Launcher")

DecoyLauncherForward = App.TGPoint3()
DecoyLauncherForward.SetXYZ(0.000000, 1.000000, 0.000000)
DecoyLauncherUp = App.TGPoint3()
DecoyLauncherUp.SetXYZ(0.000000, 0.000000, 1.000000)
DecoyLauncherRight = App.TGPoint3()
DecoyLauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
DecoyLauncher.SetOrientation(DecoyLauncherForward, DecoyLauncherUp, DecoyLauncherRight)
DecoyLauncherPosition = App.TGPoint3()
DecoyLauncherPosition.SetXYZ(0.000000, 0.000000, 0.000000)
DecoyLauncher.SetPosition(DecoyLauncherPosition)
DecoyLauncher.SetEmittedObjectType(DecoyLauncher.OEP_DECOY)
App.g_kModelPropertyManager.RegisterLocalTemplate(DecoyLauncher)
#################################################
ViewscreenForward = App.PositionOrientationProperty_Create("ViewscreenForward")

ViewscreenForwardForward = App.TGPoint3()
ViewscreenForwardForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenForwardUp = App.TGPoint3()
ViewscreenForwardUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenForwardRight = App.TGPoint3()
ViewscreenForwardRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenForward.SetOrientation(ViewscreenForwardForward, ViewscreenForwardUp, ViewscreenForwardRight)
ViewscreenForwardPosition = App.TGPoint3()
ViewscreenForwardPosition.SetXYZ(0.000000, 2.000000, 0.000000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
#################################################
ViewscreenBack = App.PositionOrientationProperty_Create("ViewscreenBack")

ViewscreenBackForward = App.TGPoint3()
ViewscreenBackForward.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenBackUp = App.TGPoint3()
ViewscreenBackUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenBackRight = App.TGPoint3()
ViewscreenBackRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenBack.SetOrientation(ViewscreenBackForward, ViewscreenBackUp, ViewscreenBackRight)
ViewscreenBackPosition = App.TGPoint3()
ViewscreenBackPosition.SetXYZ(0.000000, -1.500000, 0.000000)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
#################################################
ViewscreenLeft = App.PositionOrientationProperty_Create("ViewscreenLeft")

ViewscreenLeftForward = App.TGPoint3()
ViewscreenLeftForward.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenLeftUp = App.TGPoint3()
ViewscreenLeftUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenLeftRight = App.TGPoint3()
ViewscreenLeftRight.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenLeft.SetOrientation(ViewscreenLeftForward, ViewscreenLeftUp, ViewscreenLeftRight)
ViewscreenLeftPosition = App.TGPoint3()
ViewscreenLeftPosition.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenLeft.SetPosition(ViewscreenLeftPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenLeft)
#################################################
ViewscreenRight = App.PositionOrientationProperty_Create("ViewscreenRight")

ViewscreenRightForward = App.TGPoint3()
ViewscreenRightForward.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenRightUp = App.TGPoint3()
ViewscreenRightUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenRightRight = App.TGPoint3()
ViewscreenRightRight.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenRight.SetOrientation(ViewscreenRightForward, ViewscreenRightUp, ViewscreenRightRight)
ViewscreenRightPosition = App.TGPoint3()
ViewscreenRightPosition.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUp.SetPosition(ViewscreenUpPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenUp)
#################################################
ViewscreenDown = App.PositionOrientationProperty_Create("ViewscreenDown")

ViewscreenDownForward = App.TGPoint3()
ViewscreenDownForward.SetXYZ(0.000000, 0.000000, -1.000000)
ViewscreenDownUp = App.TGPoint3()
ViewscreenDownUp.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenDownRight = App.TGPoint3()
ViewscreenDownRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenDown.SetOrientation(ViewscreenDownForward, ViewscreenDownUp, ViewscreenDownRight)
ViewscreenDownPosition = App.TGPoint3()
ViewscreenDownPosition.SetXYZ(0.000000, 0.000000, -1.000000)
ViewscreenDown.SetPosition(ViewscreenDownPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenDown)
#################################################
FirstPersonCamera = App.PositionOrientationProperty_Create("FirstPersonCamera")

FirstPersonCameraForward = App.TGPoint3()
FirstPersonCameraForward.SetXYZ(0.000000, 1.000000, 0.000000)
FirstPersonCameraUp = App.TGPoint3()
FirstPersonCameraUp.SetXYZ(0.000000, 0.000000, 1.000000)
FirstPersonCameraRight = App.TGPoint3()
FirstPersonCameraRight.SetXYZ(1.000000, 0.000000, 0.000000)
FirstPersonCamera.SetOrientation(FirstPersonCameraForward, FirstPersonCameraUp, FirstPersonCameraRight)
FirstPersonCameraPosition = App.TGPoint3()
FirstPersonCameraPosition.SetXYZ(0.000000, 2.000000, 0.000000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("XCV330a", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Bridge", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull Polarizer", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("t", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Nacelle", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Nacelle", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fusion Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay OEP", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Probe Launcher", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Decoy Launcher", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenForward", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenBack", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenLeft", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenRight", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenUp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenDown", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FirstPersonCamera", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
