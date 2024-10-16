# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\OriSatellite.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(4000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(65.000000, 45.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.250000)
ShieldGenerator.SetRadius(0.100000)
ShieldGenerator.SetNormalPowerPerSecond(900.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(1.000000, 0.647059, 0.192157, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 100000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 100000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 100000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 100000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 100000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 100000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 140.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 140.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 140.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 140.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 140.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 140.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(5000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(66.000000, 38.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.100000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(4000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, -0.090000, 0.000000)
SensorArray.SetPosition2D(65.000000, 25.000000)
SensorArray.SetRepairComplexity(2.000000)
SensorArray.SetDisabledPercentage(0.250000)
SensorArray.SetRadius(0.100000)
SensorArray.SetNormalPowerPerSecond(150.000000)
SensorArray.SetBaseSensorRange(1700.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ReactorModule = App.PowerProperty_Create("Reactor Module")

ReactorModule.SetMaxCondition(4000.000000)
ReactorModule.SetCritical(1)
ReactorModule.SetTargetable(1)
ReactorModule.SetPrimary(1)
ReactorModule.SetPosition(0.000000, -0.175000, 0.000000)
ReactorModule.SetPosition2D(65.000000, 10.000000)
ReactorModule.SetRepairComplexity(1.000000)
ReactorModule.SetDisabledPercentage(0.250000)
ReactorModule.SetRadius(0.100000)
ReactorModule.SetMainBatteryLimit(2000000.000000)
ReactorModule.SetBackupBatteryLimit(100000.000000)
ReactorModule.SetMainConduitCapacity(2500.000000)
ReactorModule.SetBackupConduitCapacity(500.000000)
ReactorModule.SetPowerOutput(2000.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ReactorModule)
#################################################
SublightEngines = App.ImpulseEngineProperty_Create("Sublight Engines")

SublightEngines.SetMaxCondition(4000.000000)
SublightEngines.SetCritical(0)
SublightEngines.SetTargetable(0)
SublightEngines.SetPrimary(1)
SublightEngines.SetPosition(0.000000, 0.000000, 0.000000)
SublightEngines.SetPosition2D(64.000000, 104.000000)
SublightEngines.SetRepairComplexity(2.000000)
SublightEngines.SetDisabledPercentage(0.500000)
SublightEngines.SetRadius(0.070000)
SublightEngines.SetNormalPowerPerSecond(470.000000)
SublightEngines.SetMaxAccel(0.350000)
SublightEngines.SetMaxAngularAccel(0.350000)
SublightEngines.SetMaxAngularVelocity(0.500000)
SublightEngines.SetMaxSpeed(0.000000)
SublightEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngines)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(1000.000000)
Engineering.SetCritical(0)
Engineering.SetTargetable(0)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, 0.000000)
Engineering.SetPosition2D(64.000000, 80.000000)
Engineering.SetRepairComplexity(1.000000)
Engineering.SetDisabledPercentage(0.100000)
Engineering.SetRadius(0.100000)
Engineering.SetNormalPowerPerSecond(1.000000)
Engineering.SetMaxRepairPoints(5.000000)
Engineering.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
OriSatellite = App.ShipProperty_Create("Ori Satellite")

OriSatellite.SetGenus(1)
OriSatellite.SetSpecies(760)
OriSatellite.SetMass(15000.000000)
OriSatellite.SetRotationalInertia(5000.000000)
OriSatellite.SetShipName("OriSatellite")
OriSatellite.SetModelFilename("data/Models/Ships/OriSatellite/OriSatellite.nif")
OriSatellite.SetDamageResolution(0.000100)
OriSatellite.SetAffiliation(0)
OriSatellite.SetStationary(0)
OriSatellite.SetAIString("FedAttack")
OriSatellite.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(OriSatellite)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.500000, 1.500000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.650000, 0.200000)
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
ViewscreenLeftPosition.SetXYZ(0.000000, 0.500000, 1.500000)
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
ViewscreenRightPosition.SetXYZ(0.000000, 0.500000, 1.500000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.012686, 2.250000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.029979, -1.000000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.500000, 1.500000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
RotationalThrusters = App.EngineProperty_Create("Rotational Thrusters")

RotationalThrusters.SetMaxCondition(4000.000000)
RotationalThrusters.SetCritical(0)
RotationalThrusters.SetTargetable(1)
RotationalThrusters.SetPrimary(1)
RotationalThrusters.SetPosition(0.000000, 0.000000, 0.000000)
RotationalThrusters.SetPosition2D(65.000000, 65.000000)
RotationalThrusters.SetRepairComplexity(1.000000)
RotationalThrusters.SetDisabledPercentage(0.250000)
RotationalThrusters.SetRadius(0.100000)
RotationalThrusters.SetEngineType(RotationalThrusters.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(RotationalThrusters)
#################################################
MainWeapon = App.WeaponSystemProperty_Create("Main Weapon")

MainWeapon.SetMaxCondition(2000.000000)
MainWeapon.SetCritical(0)
MainWeapon.SetTargetable(0)
MainWeapon.SetPrimary(1)
MainWeapon.SetPosition(0.000000, 0.000000, 0.000000)
MainWeapon.SetPosition2D(0.000000, 0.000000)
MainWeapon.SetRepairComplexity(3.000000)
MainWeapon.SetDisabledPercentage(0.500000)
MainWeapon.SetRadius(0.100000)
MainWeapon.SetNormalPowerPerSecond(1.000000)
MainWeapon.SetWeaponSystemType(MainWeapon.WST_PHASER)
MainWeapon.SetSingleFire(1)
MainWeapon.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
MainWeapon.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(MainWeapon)
#################################################
MainBeam = App.PhaserProperty_Create("Main Beam")

MainBeam.SetMaxCondition(1000.000000)
MainBeam.SetCritical(0)
MainBeam.SetTargetable(1)
MainBeam.SetPrimary(1)
MainBeam.SetPosition(0.000000, 0.300000, 0.000000)
MainBeam.SetPosition2D(65.000000, 100.000000)
MainBeam.SetRepairComplexity(1.000000)
MainBeam.SetDisabledPercentage(0.500000)
MainBeam.SetRadius(0.250000)
MainBeam.SetDumbfire(0)
MainBeam.SetWeaponID(0)
MainBeam.SetGroups(0)
MainBeam.SetDamageRadiusFactor(0.250000)
MainBeam.SetIconNum(364)
MainBeam.SetIconPositionX(63.000000)
MainBeam.SetIconPositionY(107.000000)
MainBeam.SetIconAboveShip(0)
MainBeam.SetFireSound("OriSatellite")
MainBeam.SetMaxCharge(2.000000)
MainBeam.SetMaxDamage(35000.000000)
MainBeam.SetMaxDamageDistance(60.000000)
MainBeam.SetMinFiringCharge(2.000000)
MainBeam.SetNormalDischargeRate(1.000000)
MainBeam.SetRechargeRate(0.025000)
MainBeam.SetIndicatorIconNum(510)
MainBeam.SetIndicatorIconPositionX(57.000000)
MainBeam.SetIndicatorIconPositionY(102.000000)
MainBeamForward = App.TGPoint3()
MainBeamForward.SetXYZ(0.000000, 1.000000, 0.000000)
MainBeamUp = App.TGPoint3()
MainBeamUp.SetXYZ(1.000000, 0.000000, 0.000000)
MainBeam.SetOrientation(MainBeamForward, MainBeamUp)
MainBeam.SetWidth(0.000100)
MainBeam.SetLength(0.000100)
MainBeam.SetArcWidthAngles(-0.400000, 0.400000)
MainBeam.SetArcHeightAngles(-0.400000, 0.400000)
MainBeam.SetPhaserTextureStart(0)
MainBeam.SetPhaserTextureEnd(0)
MainBeam.SetPhaserWidth(0.700000)
kColor = App.TGColorA()
kColor.SetRGBA(0.866667, 0.619608, 0.043137, 1.000000)
MainBeam.SetOuterShellColor(kColor)
kColor.SetRGBA(0.823529, 0.592157, 0.050980, 0.803922)
MainBeam.SetInnerShellColor(kColor)
kColor.SetRGBA(0.870588, 0.705882, 0.129412, 1.000000)
MainBeam.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.827451, 0.619608, 0.129412, 0.603922)
MainBeam.SetInnerCoreColor(kColor)
MainBeam.SetNumSides(12)
MainBeam.SetMainRadius(0.100000)
MainBeam.SetTaperRadius(0.025000)
MainBeam.SetCoreScale(0.600000)
MainBeam.SetTaperRatio(0.250000)
MainBeam.SetTaperMinLength(30.000000)
MainBeam.SetTaperMaxLength(30.000000)
MainBeam.SetLengthTextureTilePerUnit(0.000500)
MainBeam.SetPerimeterTile(1.000000)
MainBeam.SetTextureSpeed(-0.000180)
MainBeam.SetTextureName("data/OriWeapon.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(MainBeam)
#################################################
StarMissiles = App.TorpedoTubeProperty_Create("Star Missiles")

StarMissiles.SetMaxCondition(1200.000000)
StarMissiles.SetCritical(0)
StarMissiles.SetTargetable(0)
StarMissiles.SetPrimary(1)
StarMissiles.SetPosition(0.000000, 0.200000, 0.000000)
StarMissiles.SetPosition2D(65.000000, 100.000000)
StarMissiles.SetRepairComplexity(1.000000)
StarMissiles.SetDisabledPercentage(0.250000)
StarMissiles.SetRadius(0.003000)
StarMissiles.SetDumbfire(1)
StarMissiles.SetWeaponID(0)
StarMissiles.SetGroups(24)
StarMissiles.SetDamageRadiusFactor(0.200000)
StarMissiles.SetIconNum(370)
StarMissiles.SetIconPositionX(76.000000)
StarMissiles.SetIconPositionY(107.000000)
StarMissiles.SetIconAboveShip(1)
StarMissiles.SetImmediateDelay(0.000000)
StarMissiles.SetReloadDelay(20.000000)
StarMissiles.SetMaxReady(5)
StarMissilesDirection = App.TGPoint3()
StarMissilesDirection.SetXYZ(0.000000, 1.000000, 0.000000)
StarMissiles.SetDirection(StarMissilesDirection)
StarMissilesRight = App.TGPoint3()
StarMissilesRight.SetXYZ(1.000000, 0.000000, 0.000000)
StarMissiles.SetRight(StarMissilesRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarMissiles)
#################################################
Missiles = App.TorpedoSystemProperty_Create("Missiles")

Missiles.SetMaxCondition(2200.000000)
Missiles.SetCritical(0)
Missiles.SetTargetable(0)
Missiles.SetPrimary(1)
Missiles.SetPosition(0.000000, 0.000000, 0.000000)
Missiles.SetPosition2D(64.000000, 10.000000)
Missiles.SetRepairComplexity(1.000000)
Missiles.SetDisabledPercentage(0.250000)
Missiles.SetRadius(0.090000)
Missiles.SetNormalPowerPerSecond(100.000000)
Missiles.SetWeaponSystemType(Missiles.WST_TORPEDO)
Missiles.SetSingleFire(0)
Missiles.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Missiles.SetFiringChainString(kFiringChainString)
Missiles.SetMaxTorpedoes(0, 4000)
Missiles.SetTorpedoScript(0, "Tactical.Projectiles.A2AMissiles2")
Missiles.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Missiles)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Ori Satellite", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Reactor Module", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Main Weapon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Main Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Missiles", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Missiles", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Rotational Thrusters", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
