# File: Z (Python 1.5)

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create('Hull')
Hull.SetMaxCondition(100.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.0, 0.0, 0.0)
Hull.SetPosition2D(64.0, 64.0)
Hull.SetRepairComplexity(4.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(0.2)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ZZRMine = App.ShipProperty_Create('ZZRMine')
ZZRMine.SetGenus(3)
ZZRMine.SetSpecies(155)
ZZRMine.SetMass(10.0)
ZZRMine.SetRotationalInertia(10.0)
ZZRMine.SetShipName('ZZRMine')
ZZRMine.SetModelFilename('data/Models/Ships/ZZRMine/ZZRMine.NIF')
ZZRMine.SetDamageResolution(10.0)
ZZRMine.SetAffiliation(0)
ZZRMine.SetStationary(0)
ZZRMine.SetAIString('')
ZZRMine.SetDeathExplosionSound('g_lsDeathExplosions')
App.g_kModelPropertyManager.RegisterLocalTemplate(ZZRMine)
#################################################
ShieldGenerator = App.ShieldProperty_Create('Shield Generator')
ShieldGenerator.SetMaxCondition(200.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.0, 0.0, 0.0)
ShieldGenerator.SetPosition2D(64.0, 64.0)
ShieldGenerator.SetRepairComplexity(1.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(0.2)
ShieldGenerator.SetNormalPowerPerSecond(1.0)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.0, 0.0, 0.0, 0.0)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 0.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 0.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 0.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 0.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 0.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 0.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 1.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 1.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 1.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 1.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 1.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 1.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
PowerPlant = App.PowerProperty_Create('Power Plant')
PowerPlant.SetMaxCondition(200.0)
PowerPlant.SetCritical(0)
PowerPlant.SetTargetable(0)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.0, 0.0, 0.0)
PowerPlant.SetPosition2D(50.0, 60.0)
PowerPlant.SetRepairComplexity(1.0)
PowerPlant.SetDisabledPercentage(0.5)
PowerPlant.SetRadius(0.2)
PowerPlant.SetMainBatteryLimit(50000.0)
PowerPlant.SetBackupBatteryLimit(10000.0)
PowerPlant.SetMainConduitCapacity(7500.0)
PowerPlant.SetBackupConduitCapacity(500.0)
PowerPlant.SetPowerOutput(7000.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
Sensor = App.SensorProperty_Create('Sensor')
Sensor.SetMaxCondition(200.0)
Sensor.SetCritical(0)
Sensor.SetTargetable(0)
Sensor.SetPrimary(1)
Sensor.SetPosition(0.0, 0.0, 0.0)
Sensor.SetPosition2D(0.0, 0.0)
Sensor.SetRepairComplexity(1.0)
Sensor.SetDisabledPercentage(0.5)
Sensor.SetRadius(0.2)
Sensor.SetNormalPowerPerSecond(1.0)
Sensor.SetBaseSensorRange(2000.0)
Sensor.SetMaxProbes(0)
App.g_kModelPropertyManager.RegisterLocalTemplate(Sensor)


def LoadPropertySet(pObj):
    "Sets up the object's properties."
    prop = App.g_kModelPropertyManager.FindByName('Shield Generator', App.TGModelPropertyManager.LOCAL_TEMPLATES)
    if prop != None:
        pObj.AddToSet('Scene Root', prop)
    
    prop = App.g_kModelPropertyManager.FindByName('Power Plant', App.TGModelPropertyManager.LOCAL_TEMPLATES)
    if prop != None:
        pObj.AddToSet('Scene Root', prop)
    
    prop = App.g_kModelPropertyManager.FindByName('Sensor', App.TGModelPropertyManager.LOCAL_TEMPLATES)
    if prop != None:
        pObj.AddToSet('Scene Root', prop)
    
    prop = App.g_kModelPropertyManager.FindByName('Hull', App.TGModelPropertyManager.LOCAL_TEMPLATES)
    if prop != None:
        pObj.AddToSet('Scene Root', prop)
    
    prop = App.g_kModelPropertyManager.FindByName('ZZRMine', App.TGModelPropertyManager.LOCAL_TEMPLATES)
    if prop != None:
        pObj.AddToSet('Scene Root', prop)
    

