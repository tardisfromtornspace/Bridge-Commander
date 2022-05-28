# C:\Utopia\Current\Build\scripts\ships\Hardpoints\asteroid3.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
City = App.HullProperty_Create("City")

City.SetMaxCondition(9000.000000)
City.SetCritical(1)
City.SetTargetable(1)
City.SetPrimary(1)
City.SetPosition(0.000000, 0.000000, 0.000000)
City.SetPosition2D(64.000000, 64.000000)
City.SetRepairComplexity(4.000000)
City.SetDisabledPercentage(0.000000)
City.SetRadius(5.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(City)
#################################################
CityBuildings = App.ShipProperty_Create("City Buildings")

CityBuildings.SetGenus(3)
CityBuildings.SetSpecies(917)
CityBuildings.SetMass(10000.000000)
CityBuildings.SetRotationalInertia(190000.000000)
CityBuildings.SetShipName("City")
CityBuildings.SetModelFilename("data/Models/Environment/City/City.NIF")
CityBuildings.SetDamageResolution(15.000000)
CityBuildings.SetAffiliation(0)
CityBuildings.SetStationary(0)
CityBuildings.SetAIString("NonFedAttack")
CityBuildings.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(CityBuildings)
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
PowerPlant.SetPosition(0.100000, 0.100000, 0.100000)
PowerPlant.SetPosition2D(50.000000, 60.000000)
PowerPlant.SetRepairComplexity(1.000000)
PowerPlant.SetDisabledPercentage(0.500000)
PowerPlant.SetRadius(0.250000)
PowerPlant.SetMainBatteryLimit(70000.000000)
PowerPlant.SetBackupBatteryLimit(10000.000000)
PowerPlant.SetMainConduitCapacity(400.000000)
PowerPlant.SetBackupConduitCapacity(200.000000)
PowerPlant.SetPowerOutput(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("City", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("City Buildings", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
