# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\Glider6.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
MainHull = App.HullProperty_Create("Main Hull")

MainHull.SetMaxCondition(60.000000)
MainHull.SetCritical(1)
MainHull.SetTargetable(0)
MainHull.SetPrimary(1)
MainHull.SetPosition(0.000000, 0.000000, 0.000000)
MainHull.SetPosition2D(67.000000, 47.000000)
MainHull.SetRepairComplexity(3.000000)
MainHull.SetDisabledPercentage(0.000000)
MainHull.SetRadius(0.030000)
App.g_kModelPropertyManager.RegisterLocalTemplate(MainHull)
#################################################
SublightEngines = App.ImpulseEngineProperty_Create("Sublight Engines")

SublightEngines.SetMaxCondition(40.000000)
SublightEngines.SetCritical(0)
SublightEngines.SetTargetable(0)
SublightEngines.SetPrimary(1)
SublightEngines.SetPosition(0.000000, 0.000000, 0.000000)
SublightEngines.SetPosition2D(51.000000, 48.000000)
SublightEngines.SetRepairComplexity(1.000000)
SublightEngines.SetDisabledPercentage(0.500000)
SublightEngines.SetRadius(0.003000)
SublightEngines.SetNormalPowerPerSecond(3.000000)
SublightEngines.SetMaxAccel(5.000000)
SublightEngines.SetMaxAngularAccel(3.800000)
SublightEngines.SetMaxAngularVelocity(0.950000)
SublightEngines.SetMaxSpeed(7.000000)
SublightEngines.SetEngineSound("SGDGEngine")
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngines)
#################################################
PowerUnit = App.PowerProperty_Create("Power Unit")

PowerUnit.SetMaxCondition(45.000000)
PowerUnit.SetCritical(1)
PowerUnit.SetTargetable(1)
PowerUnit.SetPrimary(1)
PowerUnit.SetPosition(0.000000, -0.015720, 0.012500)
PowerUnit.SetPosition2D(64, 65)
PowerUnit.SetRepairComplexity(2.000000)
PowerUnit.SetDisabledPercentage(0.500000)
PowerUnit.SetRadius(0.020000)
PowerUnit.SetMainBatteryLimit(5000.000000)
PowerUnit.SetBackupBatteryLimit(2000.000000)
PowerUnit.SetMainConduitCapacity(20.000000)
PowerUnit.SetBackupConduitCapacity(10.000000)
PowerUnit.SetPowerOutput(10.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerUnit)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(30.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.032261, -0.004908)
SensorArray.SetPosition2D(65, 35)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.750000)
SensorArray.SetRadius(0.004000)
SensorArray.SetNormalPowerPerSecond(3.000000)
SensorArray.SetBaseSensorRange(1000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(1.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(67.000000, 47.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.500000)
ShieldGenerator.SetRadius(0.002000)
ShieldGenerator.SetNormalPowerPerSecond(0.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Glider6 = App.ShipProperty_Create("Glider6")

Glider6.SetGenus(1)
Glider6.SetSpecies(714)
Glider6.SetMass(25.000000)
Glider6.SetRotationalInertia(2000.000000)
Glider6.SetShipName("Glider6")
Glider6.SetModelFilename("data/Models/Ships/sgdg/DG_SG1.NIF")
Glider6.SetDamageResolution(0.000100)
Glider6.SetAffiliation(0)
Glider6.SetStationary(0)
Glider6.SetAIString("RomulanAttack")
Glider6.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Glider6)
#################################################
MainEngine = App.EngineProperty_Create("Main Engine")

MainEngine.SetMaxCondition(40.000000)
MainEngine.SetCritical(0)
MainEngine.SetTargetable(1)
MainEngine.SetPrimary(1)
MainEngine.SetPosition(0.000000, -0.048054, 0.001209)
MainEngine.SetPosition2D(64, 80)
MainEngine.SetRepairComplexity(2.000000)
MainEngine.SetDisabledPercentage(0.500000)
MainEngine.SetRadius(0.020000)
MainEngine.SetEngineType(MainEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(MainEngine)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.036000, 0.008000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
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
ViewscreenLeftPosition.SetXYZ(-0.027500, 0.000000, 0.000000)
ViewscreenLeft.SetPosition(ViewscreenLeftPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenLeft)
#################################################
ViewscreenRight = App.PositionOrientationProperty_Create("ViewscreenRight")

ViewscreenRightForward = App.TGPoint3()
ViewscreenRightForward.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenRightUp = App.TGPoint3()
ViewscreenRightUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenRightRight = App.TGPoint3()
ViewscreenRightRight.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenRight.SetOrientation(ViewscreenRightForward, ViewscreenRightUp, ViewscreenRightRight)
ViewscreenRightPosition = App.TGPoint3()
ViewscreenRightPosition.SetXYZ(0.027500, 0.000000, 0.000000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.100000, 0.000000)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.000000, 0.025000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.000000, -0.020000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.036000, 0.008000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
Repair = App.RepairSubsystemProperty_Create("Repair")

Repair.SetMaxCondition(46.000000)
Repair.SetCritical(0)
Repair.SetTargetable(0)
Repair.SetPrimary(1)
Repair.SetPosition(0.000000, 0.000000, 0.000000)
Repair.SetPosition2D(0.000000, 0.000000)
Repair.SetRepairComplexity(1.000000)
Repair.SetDisabledPercentage(0.500000)
Repair.SetRadius(0.060000)
Repair.SetNormalPowerPerSecond(0.000001)
Repair.SetMaxRepairPoints(2.000000)
Repair.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Repair)
#################################################
Staff1 = App.PulseWeaponProperty_Create("Staff 1")

Staff1.SetMaxCondition(20.000000)
Staff1.SetCritical(0)
Staff1.SetTargetable(1)
Staff1.SetPrimary(1)
Staff1.SetPosition(-0.039000, 0.045000, -0.013000)
Staff1.SetPosition2D(35, 50)
Staff1.SetRepairComplexity(1.000000)
Staff1.SetDisabledPercentage(0.500000)
Staff1.SetRadius(0.002000)
Staff1.SetDumbfire(1)
Staff1.SetWeaponID(0)
Staff1.SetGroups(0)
Staff1.SetDamageRadiusFactor(0.300000)
Staff1.SetIconNum(365)
Staff1.SetIconPositionX(50)
Staff1.SetIconPositionY(73)
Staff1.SetIconAboveShip(1)
Staff1.SetFireSound("")
Staff1.SetMaxCharge(20.000000)
Staff1.SetMaxDamage(1.000000)
Staff1.SetMaxDamageDistance(100.000000)
Staff1.SetMinFiringCharge(3.000000)
Staff1.SetNormalDischargeRate(1.000000)
Staff1.SetRechargeRate(0.300000)
Staff1.SetIndicatorIconNum(0)
Staff1.SetIndicatorIconPositionX(0)
Staff1.SetIndicatorIconPositionY(0)
Staff1Forward = App.TGPoint3()
Staff1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Staff1Up = App.TGPoint3()
Staff1Up.SetXYZ(0.000000, 0.000000, 1.000000)
Staff1.SetOrientation(Staff1Forward, Staff1Up)
Staff1.SetArcWidthAngles(-0.349066, 0.349066)
Staff1.SetArcHeightAngles(-0.349066, 0.349066)
Staff1.SetCooldownTime(0.500000)
Staff1.SetModuleName("Tactical.Projectiles.sgstaff")
App.g_kModelPropertyManager.RegisterLocalTemplate(Staff1)
#################################################
StaffWeapons = App.WeaponSystemProperty_Create("Staff Weapons")

StaffWeapons.SetMaxCondition(46.000000)
StaffWeapons.SetCritical(0)
StaffWeapons.SetTargetable(0)
StaffWeapons.SetPrimary(1)
StaffWeapons.SetPosition(0.000000, 0.000000, 0.000000)
StaffWeapons.SetPosition2D(15.000000, 15.000000)
StaffWeapons.SetRepairComplexity(1.000000)
StaffWeapons.SetDisabledPercentage(0.500000)
StaffWeapons.SetRadius(0.010000)
StaffWeapons.SetNormalPowerPerSecond(0.500000)
StaffWeapons.SetWeaponSystemType(StaffWeapons.WST_PULSE)
StaffWeapons.SetSingleFire(0)
StaffWeapons.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
StaffWeapons.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(StaffWeapons)
#################################################
Staff2 = App.PulseWeaponProperty_Create("Staff 2")

Staff2.SetMaxCondition(20.000000)
Staff2.SetCritical(0)
Staff2.SetTargetable(1)
Staff2.SetPrimary(1)
Staff2.SetPosition(0.039000, 0.045000, -0.013000)
Staff2.SetPosition2D(95, 50)
Staff2.SetRepairComplexity(1.000000)
Staff2.SetDisabledPercentage(0.500000)
Staff2.SetRadius(0.002000)
Staff2.SetDumbfire(1)
Staff2.SetWeaponID(0)
Staff2.SetGroups(0)
Staff2.SetDamageRadiusFactor(0.300000)
Staff2.SetIconNum(365)
Staff2.SetIconPositionX(103)
Staff2.SetIconPositionY(73)
Staff2.SetIconAboveShip(1)
Staff2.SetFireSound("")
Staff2.SetMaxCharge(20.000000)
Staff2.SetMaxDamage(1.000000)
Staff2.SetMaxDamageDistance(100.000000)
Staff2.SetMinFiringCharge(3.000000)
Staff2.SetNormalDischargeRate(1.000000)
Staff2.SetRechargeRate(0.300000)
Staff2.SetIndicatorIconNum(0)
Staff2.SetIndicatorIconPositionX(0)
Staff2.SetIndicatorIconPositionY(0)
Staff2Forward = App.TGPoint3()
Staff2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Staff2Up = App.TGPoint3()
Staff2Up.SetXYZ(0.000000, 0.000000, 1.000000)
Staff2.SetOrientation(Staff2Forward, Staff2Up)
Staff2.SetArcWidthAngles(-0.349066, 0.349066)
Staff2.SetArcHeightAngles(-0.349066, 0.349066)
Staff2.SetCooldownTime(0.500000)
Staff2.SetModuleName("Tactical.Projectiles.sgstaff")
App.g_kModelPropertyManager.RegisterLocalTemplate(Staff2)
#################################################
Cockpit = App.HullProperty_Create("Cockpit")

Cockpit.SetMaxCondition(45.000000)
Cockpit.SetCritical(1)
Cockpit.SetTargetable(1)
Cockpit.SetPrimary(0)
Cockpit.SetPosition(0.000000, 0.030000, 0.008000)
Cockpit.SetPosition2D(64, 50)
Cockpit.SetRepairComplexity(3.000000)
Cockpit.SetDisabledPercentage(0.000000)
Cockpit.SetRadius(0.015000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Cockpit)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Glider6", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Main Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Cockpit", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Unit", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Main Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Staff Weapons", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Staff 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Staff 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
