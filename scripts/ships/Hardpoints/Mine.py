# C:\Users\Owner\Documents\FinalHP_Changes_Other\Mine.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Mine = App.HullProperty_Create("Mine")

Mine.SetMaxCondition(100.000000)
Mine.SetCritical(1)
Mine.SetTargetable(1)
Mine.SetPrimary(1)
Mine.SetPosition(0.000000, 0.000000, 0.000000)
Mine.SetPosition2D(64.000000, 64.000000)
Mine.SetRepairComplexity(4.000000)
Mine.SetDisabledPercentage(0.000000)
Mine.SetRadius(1.200000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Mine)
#################################################
MineObj = App.ShipProperty_Create("Mine Obj")

MineObj.SetGenus(3)
MineObj.SetSpecies(155)
MineObj.SetMass(60.000000)
MineObj.SetRotationalInertia(7000.000000)
MineObj.SetShipName("Mine")
MineObj.SetModelFilename("data/Models/mine/Mine.NIF")
MineObj.SetDamageResolution(10.000000)
MineObj.SetAffiliation(0)
MineObj.SetStationary(1)
MineObj.SetAIString("NonFedAttack")
MineObj.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(MineObj)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(200.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(64.000000, 64.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.500000)
ShieldGenerator.SetRadius(0.250000)
ShieldGenerator.SetNormalPowerPerSecond(1.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
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
PowerPlant = App.PowerProperty_Create("Power Plant")

PowerPlant.SetMaxCondition(200.000000)
PowerPlant.SetCritical(0)
PowerPlant.SetTargetable(0)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.000000, 0.000000, 0.000000)
PowerPlant.SetPosition2D(50.000000, 60.000000)
PowerPlant.SetRepairComplexity(1.000000)
PowerPlant.SetDisabledPercentage(0.500000)
PowerPlant.SetRadius(0.250000)
PowerPlant.SetMainBatteryLimit(70000.000000)
PowerPlant.SetBackupBatteryLimit(10000.000000)
PowerPlant.SetMainConduitCapacity(400.000000)
PowerPlant.SetBackupConduitCapacity(200.000000)
PowerPlant.SetPowerOutput(8000.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
Sensor = App.SensorProperty_Create("Sensor")

Sensor.SetMaxCondition(200.000000)
Sensor.SetCritical(0)
Sensor.SetTargetable(0)
Sensor.SetPrimary(1)
Sensor.SetPosition(0.000000, 0.000000, 0.000000)
Sensor.SetPosition2D(0.000000, 0.000000)
Sensor.SetRepairComplexity(1.000000)
Sensor.SetDisabledPercentage(0.500000)
Sensor.SetRadius(0.250000)
Sensor.SetNormalPowerPerSecond(1.000000)
Sensor.SetBaseSensorRange(1000.000000)
Sensor.SetMaxProbes(0)
App.g_kModelPropertyManager.RegisterLocalTemplate(Sensor)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Mine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Mine Obj", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
