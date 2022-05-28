# D:\Activision\Bridge Commander\scripts\ships\Hardpoints\blackhole.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Blackhole = App.ShipProperty_Create("Blackhole")

Blackhole.SetGenus(3)
Blackhole.SetSpecies(926)
Blackhole.SetMass(9.3703148425787104e+025)
Blackhole.SetRotationalInertia(1e+050)
Blackhole.SetShipName("Blackhole")
Blackhole.SetModelFilename("data\Models\Misc\\blackhole\Blackhole.nif")
Blackhole.SetDamageResolution(1.000000)
Blackhole.SetAffiliation(10)
Blackhole.SetStationary(0)
Blackhole.SetAIString("FedAttack")
Blackhole.SetDeathExplosionSound("g_IsBigDeathExplosion")
App.g_kModelPropertyManager.RegisterLocalTemplate(Blackhole)
#################################################
Center = App.HullProperty_Create("Center")

Center.SetMaxCondition(10000000000.000000)
Center.SetCritical(0)
Center.SetTargetable(1)
Center.SetPrimary(1)
Center.SetPosition(0.000000, 0.000000, 0.000000)
Center.SetPosition2D(0.000000, 0.000000)
Center.SetRepairComplexity(1.000000)
Center.SetDisabledPercentage(1.000000)
Center.SetRadius(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Center)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(10000000000.000000)
WarpCore.SetCritical(0)
WarpCore.SetTargetable(0)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, 0.000000, 0.000000)
WarpCore.SetPosition2D(0.000000, 0.000000)
WarpCore.SetRepairComplexity(1.000000)
WarpCore.SetDisabledPercentage(1.000000)
WarpCore.SetRadius(1.000000)
WarpCore.SetMainBatteryLimit(9999999827968.000000)
WarpCore.SetBackupBatteryLimit(9999999827968.000000)
WarpCore.SetMainConduitCapacity(1000000.000000)
WarpCore.SetBackupConduitCapacity(1000000.000000)
WarpCore.SetPowerOutput(9999999827968.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
repair = App.RepairSubsystemProperty_Create("repair")

repair.SetMaxCondition(100000000.000000)
repair.SetCritical(0)
repair.SetTargetable(0)
repair.SetPrimary(1)
repair.SetPosition(0.000000, 0.000000, 0.000000)
repair.SetPosition2D(0.000000, 0.000000)
repair.SetRepairComplexity(1.000000)
repair.SetDisabledPercentage(1.000000)
repair.SetRadius(0.000001)
repair.SetNormalPowerPerSecond(1.000000)
repair.SetMaxRepairPoints(99999997952.000000)
repair.SetNumRepairTeams(5)
App.g_kModelPropertyManager.RegisterLocalTemplate(repair)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(1.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(0.000000, 0.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(1.000000)
ShieldGenerator.SetRadius(0.000010)
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
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(1.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.000000, 0.000000)
SensorArray.SetPosition2D(0.000000, 0.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(1.000000)
SensorArray.SetRadius(0.000100)
SensorArray.SetNormalPowerPerSecond(1.000000)
SensorArray.SetBaseSensorRange(10.000000)
SensorArray.SetMaxProbes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
GravityGenerator = App.HullProperty_Create("Blackhole Generator")

GravityGenerator.SetMaxCondition(100.000000)
GravityGenerator.SetCritical(0)
GravityGenerator.SetTargetable(0)
GravityGenerator.SetPrimary(0)
GravityGenerator.SetPosition(0.000000, 0.0, 0.0)
GravityGenerator.SetPosition2D(0.000000, 0.000000)
GravityGenerator.SetRepairComplexity(0.000000)
GravityGenerator.SetDisabledPercentage(0.01)
GravityGenerator.SetRadius(1.00000)
App.g_kModelPropertyManager.RegisterLocalTemplate(GravityGenerator)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Blackhole", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Center", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("repair", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Blackhole Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)