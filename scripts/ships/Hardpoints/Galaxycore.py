# C:\Program Files\Bridge Commander\scripts\ships\Hardpoints\Galaxycore.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(10.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(50.000000, 50.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.160000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(10.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(0.000000, 0.000000)
ImpulseEngines.SetRepairComplexity(1.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.250000)
ImpulseEngines.SetNormalPowerPerSecond(1.000000)
ImpulseEngines.SetMaxAccel(5.000000)
ImpulseEngines.SetMaxAngularAccel(0.000001)
ImpulseEngines.SetMaxAngularVelocity(0.000001)
ImpulseEngines.SetMaxSpeed(2.500000)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")

PowerPlant.SetMaxCondition(10.000000)
PowerPlant.SetCritical(0)
PowerPlant.SetTargetable(0)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.000000, 0.000000, 0.000000)
PowerPlant.SetPosition2D(65.000000, 65.000000)
PowerPlant.SetRepairComplexity(1.000000)
PowerPlant.SetDisabledPercentage(0.500000)
PowerPlant.SetRadius(0.200000)
PowerPlant.SetMainBatteryLimit(2500000.000000)
PowerPlant.SetBackupBatteryLimit(1000000.000000)
PowerPlant.SetMainConduitCapacity(20000.000000)
PowerPlant.SetBackupConduitCapacity(20000.000000)
PowerPlant.SetPowerOutput(4000.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(10.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.020000, 0.000000)
SensorArray.SetPosition2D(35.000000, 40.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.022000)
SensorArray.SetNormalPowerPerSecond(1.000000)
SensorArray.SetBaseSensorRange(1000.000000)
SensorArray.SetMaxProbes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(10.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.010000, 0.000000)
ShieldGenerator.SetPosition2D(50.000000, 50.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
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
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(10.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, 0.000000, 0.000000)
WarpEngines.SetPosition2D(0.000000, 0.000000)
WarpEngines.SetRepairComplexity(1.000000)
WarpEngines.SetDisabledPercentage(0.500000)
WarpEngines.SetRadius(0.250000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Warp = App.EngineProperty_Create("Warp")

Warp.SetMaxCondition(10.000000)
Warp.SetCritical(0)
Warp.SetTargetable(0)
Warp.SetPrimary(1)
Warp.SetPosition(0.000000, -0.030000, 0.000000)
Warp.SetPosition2D(95.000000, 90.000000)
Warp.SetRepairComplexity(1.000000)
Warp.SetDisabledPercentage(0.750000)
Warp.SetRadius(0.025000)
Warp.SetEngineType(Warp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(Warp)
#################################################
Impulse = App.EngineProperty_Create("Impulse")

Impulse.SetMaxCondition(10.000000)
Impulse.SetCritical(0)
Impulse.SetTargetable(0)
Impulse.SetPrimary(1)
Impulse.SetPosition(0.000000, -0.020000, 0.000000)
Impulse.SetPosition2D(80.000000, 75.000000)
Impulse.SetRepairComplexity(1.000000)
Impulse.SetDisabledPercentage(0.500000)
Impulse.SetRadius(0.020000)
Impulse.SetEngineType(Impulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Impulse)
#################################################
Galaxycore = App.ShipProperty_Create("Galaxycore")

Galaxycore.SetGenus(1)
Galaxycore.SetSpecies(198)
Galaxycore.SetMass(1000.000000)
Galaxycore.SetRotationalInertia(500.000000)
Galaxycore.SetShipName("Galaxy Warpcore")
Galaxycore.SetModelFilename("data/Models/Misc/Galaxycore/coreanimated.NIF")
Galaxycore.SetDamageResolution(10.000000)
Galaxycore.SetAffiliation(0)
Galaxycore.SetStationary(0)
Galaxycore.SetAIString("FedAttack")
Galaxycore.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Galaxycore)
#################################################
HullStore = App.HullProperty_Create("HullStore")

HullStore.SetMaxCondition(10.000000)
HullStore.SetCritical(0)
HullStore.SetTargetable(0)
HullStore.SetPrimary(0)
HullStore.SetPosition(0.000000, 0.000000, 0.000000)
HullStore.SetPosition2D(50.000000, 50.000000)
HullStore.SetRepairComplexity(1.000000)
HullStore.SetDisabledPercentage(0.000000)
HullStore.SetRadius(0.200000)
App.g_kModelPropertyManager.RegisterLocalTemplate(HullStore)

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
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Galaxycore", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("HullStore", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
