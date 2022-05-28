# D:\Spiele\Bridge Commander\scripts\ships\Hardpoints\BigFirepoint.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
BigFirepoint = App.HullProperty_Create("BigFirepoint")

BigFirepoint.SetMaxCondition(10.000000)
BigFirepoint.SetCritical(1)
BigFirepoint.SetTargetable(1)
BigFirepoint.SetPrimary(1)
BigFirepoint.SetPosition(0.000000, 0.000000, 0.000000)
BigFirepoint.SetPosition2D(64.000000, 64.000000)
BigFirepoint.SetRepairComplexity(4.000000)
BigFirepoint.SetDisabledPercentage(0.000000)
BigFirepoint.SetRadius(0.240000)
App.g_kModelPropertyManager.RegisterLocalTemplate(BigFirepoint)
#################################################
Mass = App.ShipProperty_Create("Mass")

Mass.SetGenus(3)
Mass.SetSpecies(App.SPECIES_PROBE)
Mass.SetMass(100.000000)
Mass.SetRotationalInertia(1.000000)
Mass.SetShipName("Big Firepoint")
Mass.SetModelFilename("data/Models/Misc/asteroid.nif")
Mass.SetDamageResolution(1.000000)
Mass.SetAffiliation(0)
Mass.SetStationary(0)
Mass.SetAIString("NonFedAttack")
Mass.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Mass)
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

PowerPlant.SetMaxCondition(10.000000)
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
PowerPlant.SetPowerOutput(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("BigFirepoint", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Mass", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
