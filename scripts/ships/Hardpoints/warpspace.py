# C:\unzipped\DS9FX\DS9FX\scripts\ships\Hardpoints\WormholeCone.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(999999986991104.000000)
Hull.SetCritical(0)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -2.500000, 0.000000)
Hull.SetPosition2D(50.000000, 50.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.100000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(10000000000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, -2.500000, 0.000000)
ImpulseEngines.SetPosition2D(0.000000, 0.000000)
ImpulseEngines.SetRepairComplexity(1.000000)
ImpulseEngines.SetDisabledPercentage(0.000000)
ImpulseEngines.SetRadius(0.010000)
ImpulseEngines.SetNormalPowerPerSecond(1.000000)
ImpulseEngines.SetMaxAccel(0.000000)
ImpulseEngines.SetMaxAngularAccel(0.000000)
ImpulseEngines.SetMaxAngularVelocity(0.000000)
ImpulseEngines.SetMaxSpeed(0.000000)
ImpulseEngines.SetEngineSound("")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")

PowerPlant.SetMaxCondition(10000000000.000000)
PowerPlant.SetCritical(0)
PowerPlant.SetTargetable(0)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.000000, -2.500000, 0.000000)
PowerPlant.SetPosition2D(65.000000, 65.000000)
PowerPlant.SetRepairComplexity(1.000000)
PowerPlant.SetDisabledPercentage(0.000000)
PowerPlant.SetRadius(0.100000)
PowerPlant.SetMainBatteryLimit(10000000.000000)
PowerPlant.SetBackupBatteryLimit(1000000.000000)
PowerPlant.SetMainConduitCapacity(1000000.000000)
PowerPlant.SetBackupConduitCapacity(1000000.000000)
PowerPlant.SetPowerOutput(1000000.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(9999999827968.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, -2.500000, 0.000000)
SensorArray.SetPosition2D(35.000000, 40.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.000000)
SensorArray.SetRadius(0.022000)
SensorArray.SetNormalPowerPerSecond(1.000000)
SensorArray.SetBaseSensorRange(1000.000000)
SensorArray.SetMaxProbes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(120.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -2.500000, 0.000000)
ShieldGenerator.SetPosition2D(50.000000, 50.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.000000)
ShieldGenerator.SetRadius(0.020000)
ShieldGenerator.SetNormalPowerPerSecond(1.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 1.000000, 1.000000, 1.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
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
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(199999995904.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, -2.500000, 0.000000)
WarpEngines.SetPosition2D(0.000000, 0.000000)
WarpEngines.SetRepairComplexity(1.000000)
WarpEngines.SetDisabledPercentage(0.000000)
WarpEngines.SetRadius(0.250000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Warp = App.EngineProperty_Create("Warp")

Warp.SetMaxCondition(50000000188416.000000)
Warp.SetCritical(0)
Warp.SetTargetable(0)
Warp.SetPrimary(1)
Warp.SetPosition(0.000000, -2.500000, 0.000000)
Warp.SetPosition2D(95.000000, 90.000000)
Warp.SetRepairComplexity(3.000000)
Warp.SetDisabledPercentage(0.000000)
Warp.SetRadius(0.025000)
Warp.SetEngineType(Warp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(Warp)
#################################################
Impulse = App.EngineProperty_Create("Impulse")

Impulse.SetMaxCondition(49999998976.000000)
Impulse.SetCritical(0)
Impulse.SetTargetable(0)
Impulse.SetPrimary(1)
Impulse.SetPosition(0.000000, -2.500000, 0.000000)
Impulse.SetPosition2D(80.000000, 75.000000)
Impulse.SetRepairComplexity(1.000000)
Impulse.SetDisabledPercentage(0.000000)
Impulse.SetRadius(0.020000)
Impulse.SetEngineType(Impulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Impulse)
#################################################
Wormhole = App.ShipProperty_Create("Wormhole")

Wormhole.SetGenus(1)
Wormhole.SetSpecies(710)
Wormhole.SetMass(0.000000)
Wormhole.SetRotationalInertia(500.000000)
Wormhole.SetShipName("Wormhole")
Wormhole.SetModelFilename("data/Models/Bases/warpspace/outer.NIF")
Wormhole.SetDamageResolution(10.000000)
Wormhole.SetAffiliation(0)
Wormhole.SetStationary(0)
Wormhole.SetAIString("FedAttack")
Wormhole.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Wormhole)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Wormhole", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
