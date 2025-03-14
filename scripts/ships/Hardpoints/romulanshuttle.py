#####  Created by:
#####  Tactical Display Icon Editor
## reset cannons, warps, impulse, resized much


import App
import GlobalPropertyTemplates

# Local Templates
#################################################
FwdTorpedo = App.TorpedoTubeProperty_Create("Fwd Torpedo")

FwdTorpedo.SetMaxCondition(2200.000000)
FwdTorpedo.SetCritical(0)
FwdTorpedo.SetTargetable(1)
FwdTorpedo.SetPrimary(1)
FwdTorpedo.SetPosition(-0.001227, 0.072966, -0.005807)
FwdTorpedo.SetPosition2D(67.000000, 21.000000)
FwdTorpedo.SetRepairComplexity(3.000000)
FwdTorpedo.SetDisabledPercentage(0.750000)
FwdTorpedo.SetRadius(0.080000)
FwdTorpedo.SetDumbfire(1)
FwdTorpedo.SetWeaponID(1)
FwdTorpedo.SetGroups(1)
FwdTorpedo.SetDamageRadiusFactor(0.999999)
FwdTorpedo.SetIconNum(370)
FwdTorpedo.SetIconPositionX(75.000000)
FwdTorpedo.SetIconPositionY(35.000000)
FwdTorpedo.SetIconAboveShip(1)
FwdTorpedo.SetImmediateDelay(0.250000)
FwdTorpedo.SetReloadDelay(20.000000)
FwdTorpedo.SetMaxReady(1)
FwdTorpedoDirection = App.TGPoint3()
FwdTorpedoDirection.SetXYZ(0.000000, 1.000000, 0.000000)
FwdTorpedo.SetDirection(FwdTorpedoDirection)
FwdTorpedoRight = App.TGPoint3()
FwdTorpedoRight.SetXYZ(1.000000, 0.000000, 0.000000)
FwdTorpedo.SetRight(FwdTorpedoRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(FwdTorpedo)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(5000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -0.100000, 0.000000)
ShieldGenerator.SetPosition2D(66.000000, 38.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.120000)
ShieldGenerator.SetNormalPowerPerSecond(180.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.109804, 0.549020, 0.137255, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 3000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 3000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 3000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 3000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 3000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 3000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 20.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 8.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 8.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 3.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 3.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 3.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(4000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(66.000000, 38.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.040000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(6000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000059, 0.043335, 0.011127)
SensorArray.SetPosition2D(66.000000, 7.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.006000)
SensorArray.SetNormalPowerPerSecond(50.000000)
SensorArray.SetBaseSensorRange(1600.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(2400.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.300000, 0.000000)
WarpCore.SetPosition2D(65.000000, 55.000000)
WarpCore.SetRepairComplexity(2.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.190000)
WarpCore.SetMainBatteryLimit(80000.000000)
WarpCore.SetBackupBatteryLimit(40000.000000)
WarpCore.SetMainConduitCapacity(470.000000)
WarpCore.SetBackupConduitCapacity(70.000000)
WarpCore.SetPowerOutput(400.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(2400.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(-0.234938, -0.218531, -0.046803)
ImpulseEngines.SetPosition2D(64.000000, 104.000000)
ImpulseEngines.SetRepairComplexity(4.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.120000)
ImpulseEngines.SetNormalPowerPerSecond(50.000000)
ImpulseEngines.SetMaxAccel(2.500000)
ImpulseEngines.SetMaxAngularAccel(0.900000)
ImpulseEngines.SetMaxAngularVelocity(0.900000)
ImpulseEngines.SetMaxSpeed(8.200000)
ImpulseEngines.SetEngineSound("Klingon Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
PortCannon = App.PulseWeaponProperty_Create("Port Cannon")

PortCannon.SetMaxCondition(600.000000)
PortCannon.SetCritical(0)
PortCannon.SetTargetable(1)
PortCannon.SetPrimary(1)
PortCannon.SetPosition(-0.002008, 0.069748, -0.003017)
PortCannon.SetPosition2D(5.000000, 40.000000)
PortCannon.SetRepairComplexity(9.000000)
PortCannon.SetDisabledPercentage(0.750000)
PortCannon.SetRadius(0.250000)
PortCannon.SetDumbfire(1)
PortCannon.SetWeaponID(1)
PortCannon.SetGroups(1)
PortCannon.SetDamageRadiusFactor(0.300000)
PortCannon.SetIconNum(365)
PortCannon.SetIconPositionX(67.000000)
PortCannon.SetIconPositionY(42.000000)
PortCannon.SetIconAboveShip(1)
PortCannon.SetFireSound("Pulse Disruptor")
PortCannon.SetMaxCharge(3.800000)
PortCannon.SetMaxDamage(200.000000)
PortCannon.SetMaxDamageDistance(100.000000)
PortCannon.SetMinFiringCharge(3.600000)
PortCannon.SetNormalDischargeRate(1.000000)
PortCannon.SetRechargeRate(0.400000)
PortCannon.SetIndicatorIconNum(512)
PortCannon.SetIndicatorIconPositionX(55.000000)
PortCannon.SetIndicatorIconPositionY(37.000000)
PortCannonForward = App.TGPoint3()
PortCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
PortCannonUp = App.TGPoint3()
PortCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
PortCannon.SetOrientation(PortCannonForward, PortCannonUp)
PortCannon.SetArcWidthAngles(-0.436332, 0.436332)
PortCannon.SetArcHeightAngles(-0.436332, 0.436332)
PortCannon.SetCooldownTime(0.200000)
PortCannon.SetModuleName("Tactical.Projectiles.PulseDisruptor")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortCannon)
#################################################
StarCannon = App.PulseWeaponProperty_Create("Star Cannon")

StarCannon.SetMaxCondition(600.000000)
StarCannon.SetCritical(0)
StarCannon.SetTargetable(1)
StarCannon.SetPrimary(1)
StarCannon.SetPosition(0.001312, 0.069833, -0.003091)
StarCannon.SetPosition2D(123.000000, 40.000000)
StarCannon.SetRepairComplexity(9.000000)
StarCannon.SetDisabledPercentage(0.750000)
StarCannon.SetRadius(0.250000)
StarCannon.SetDumbfire(1)
StarCannon.SetWeaponID(2)
StarCannon.SetGroups(1)
StarCannon.SetDamageRadiusFactor(0.300000)
StarCannon.SetIconNum(365)
StarCannon.SetIconPositionX(86.000000)
StarCannon.SetIconPositionY(42.000000)
StarCannon.SetIconAboveShip(1)
StarCannon.SetFireSound("Pulse Disruptor")
StarCannon.SetMaxCharge(3.800000)
StarCannon.SetMaxDamage(200.000000)
StarCannon.SetMaxDamageDistance(100.000000)
StarCannon.SetMinFiringCharge(3.600000)
StarCannon.SetNormalDischargeRate(1.000000)
StarCannon.SetRechargeRate(0.400000)
StarCannon.SetIndicatorIconNum(513)
StarCannon.SetIndicatorIconPositionX(74.000000)
StarCannon.SetIndicatorIconPositionY(37.000000)
StarCannonForward = App.TGPoint3()
StarCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
StarCannonUp = App.TGPoint3()
StarCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
StarCannon.SetOrientation(StarCannonForward, StarCannonUp)
StarCannon.SetArcWidthAngles(-0.436332, 0.436332)
StarCannon.SetArcHeightAngles(-0.436332, 0.436332)
StarCannon.SetCooldownTime(0.200000)
StarCannon.SetModuleName("Tactical.Projectiles.PulseDisruptor")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarCannon)
#################################################
DisruptorCannons = App.WeaponSystemProperty_Create("Disruptor Cannons")

DisruptorCannons.SetMaxCondition(600.000000)
DisruptorCannons.SetCritical(0)
DisruptorCannons.SetTargetable(0)
DisruptorCannons.SetPrimary(1)
DisruptorCannons.SetPosition(0.000000, 0.650000, 0.030000)
DisruptorCannons.SetPosition2D(64.000000, 44.000000)
DisruptorCannons.SetRepairComplexity(9.000000)
DisruptorCannons.SetDisabledPercentage(0.750000)
DisruptorCannons.SetRadius(0.100000)
DisruptorCannons.SetNormalPowerPerSecond(80.000000)
DisruptorCannons.SetWeaponSystemType(DisruptorCannons.WST_PULSE)
DisruptorCannons.SetSingleFire(0)
DisruptorCannons.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
DisruptorCannons.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(DisruptorCannons)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(3200.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.237953, -0.306927, 0.053082)
WarpEngines.SetPosition2D(64.000000, 104.000000)
WarpEngines.SetRepairComplexity(3.000000)
WarpEngines.SetDisabledPercentage(0.750000)
WarpEngines.SetRadius(0.100000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(2200.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000528, 0.073097, -0.005920)
Torpedoes.SetPosition2D(64.000000, 10.000000)
Torpedoes.SetRepairComplexity(3.000000)
Torpedoes.SetDisabledPercentage(0.750000)
Torpedoes.SetRadius(0.001000)
Torpedoes.SetNormalPowerPerSecond(50.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 15)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.KlingonTorpedo")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
CloakingDevice = App.CloakingSubsystemProperty_Create("Cloaking Device")

CloakingDevice.SetMaxCondition(800.000000)
CloakingDevice.SetCritical(0)
CloakingDevice.SetTargetable(1)
CloakingDevice.SetPrimary(1)
CloakingDevice.SetPosition(0.000000, 0.300000, 0.000000)
CloakingDevice.SetPosition2D(64.000000, 65.000000)
CloakingDevice.SetRepairComplexity(6.000000)
CloakingDevice.SetDisabledPercentage(0.750000)
CloakingDevice.SetRadius(0.070000)
CloakingDevice.SetNormalPowerPerSecond(380.000000)
CloakingDevice.SetCloakStrength(90.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CloakingDevice)
#################################################
ImpulseEngine = App.EngineProperty_Create("Impulse Engine")

ImpulseEngine.SetMaxCondition(2400.000000)
ImpulseEngine.SetCritical(0)
ImpulseEngine.SetTargetable(1)
ImpulseEngine.SetPrimary(1)
ImpulseEngine.SetPosition(0.000306, -0.068251, 0.003887)
ImpulseEngine.SetPosition2D(64.000000, 85.000000)
ImpulseEngine.SetRepairComplexity(4.000000)
ImpulseEngine.SetDisabledPercentage(0.500000)
ImpulseEngine.SetRadius(0.010000)
ImpulseEngine.SetEngineType(ImpulseEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngine)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")

PortWarp.SetMaxCondition(1600.000000)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-0.032710, -0.026054, -0.006031)
PortWarp.SetPosition2D(46.000000, 78.000000)
PortWarp.SetRepairComplexity(3.000000)
PortWarp.SetDisabledPercentage(0.750000)
PortWarp.SetRadius(0.004000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")

StarWarp.SetMaxCondition(1600.000000)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(0.032196, -0.026059, -0.005827)
StarWarp.SetPosition2D(82.000000, 78.000000)
StarWarp.SetRepairComplexity(3.000000)
StarWarp.SetDisabledPercentage(0.750000)
StarWarp.SetRadius(0.004000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(400.000000)
Engineering.SetCritical(0)
Engineering.SetTargetable(0)
Engineering.SetPrimary(1)
Engineering.SetPosition(-0.000309, 0.030972, 0.014768)
Engineering.SetPosition2D(64.000000, 80.000000)
Engineering.SetRepairComplexity(4.000000)
Engineering.SetDisabledPercentage(0.100000)
Engineering.SetRadius(0.003000)
Engineering.SetNormalPowerPerSecond(1.000000)
Engineering.SetMaxRepairPoints(16.000000)
Engineering.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
romulanshuttle = App.ShipProperty_Create("romulanshuttle")

romulanshuttle.SetGenus(1)
romulanshuttle.SetSpecies(310)
romulanshuttle.SetMass(45.000000)
romulanshuttle.SetRotationalInertia(200.000000)
romulanshuttle.SetShipName("romulanshuttle")
romulanshuttle.SetModelFilename("data/Models/Ships/romulanshuttle.nif")
romulanshuttle.SetDamageResolution(6.000000)
romulanshuttle.SetAffiliation(0)
romulanshuttle.SetStationary(0)
romulanshuttle.SetAIString("NonFedAttack")
romulanshuttle.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(romulanshuttle)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.920000, 0.000000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.700000, 0.000000)
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
ViewscreenLeftPosition.SetXYZ(0.000000, 0.920000, 0.000000)
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
ViewscreenRightPosition.SetXYZ(0.000000, 0.920000, 0.000000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.000000, 0.920000, 0.000000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.920000, 0.000000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.920000, 0.000000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)

# Property Set
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Disruptor Cannons", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fwd Torpedo", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Cloaking Device", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("romulanshuttle", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
