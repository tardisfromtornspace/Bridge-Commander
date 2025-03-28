# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\AstralQueen.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
AstralQueen = App.ShipProperty_Create("AstralQueen")

AstralQueen.SetGenus(0)
AstralQueen.SetSpecies(103)
AstralQueen.SetMass(1000.000000)
AstralQueen.SetRotationalInertia(1000.000000)
AstralQueen.SetShipName("AstralQueen")
AstralQueen.SetModelFilename("data/Models/Ships/Bsg/AstralQueen/AstralQueen.nif")
AstralQueen.SetDamageResolution(0.010000)
AstralQueen.SetAffiliation(0)
AstralQueen.SetStationary(0)
AstralQueen.SetAIString("FedAttack")
AstralQueen.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(AstralQueen)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(12000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(0.000000, 0.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.500000)
Hull.SetRadius(0.250000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SubLightSys = App.ImpulseEngineProperty_Create("Sub Light Sys")

SubLightSys.SetMaxCondition(200.000000)
SubLightSys.SetCritical(0)
SubLightSys.SetTargetable(0)
SubLightSys.SetPrimary(1)
SubLightSys.SetPosition(0.000000, -1278.709961, -357.954987)
SubLightSys.SetPosition2D(0.000000, 0.000000)
SubLightSys.SetRepairComplexity(1.000000)
SubLightSys.SetDisabledPercentage(0.500000)
SubLightSys.SetRadius(250.000000)
SubLightSys.SetNormalPowerPerSecond(1.000000)
SubLightSys.SetMaxAccel(0.700000)
SubLightSys.SetMaxAngularAccel(0.080000)
SubLightSys.SetMaxAngularVelocity(0.075000)
SubLightSys.SetMaxSpeed(2.100000)
SubLightSys.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(SubLightSys)
#################################################
SLEngine1 = App.EngineProperty_Create("SL Engine 1")

SLEngine1.SetMaxCondition(2500.000000)
SLEngine1.SetCritical(0)
SLEngine1.SetTargetable(1)
SLEngine1.SetPrimary(1)
SLEngine1.SetPosition(-1.700000, -24.500000, -3.850000)
SLEngine1.SetPosition2D(0.000000, 0.000000)
SLEngine1.SetRepairComplexity(1.000000)
SLEngine1.SetDisabledPercentage(0.500000)
SLEngine1.SetRadius(0.250000)
SLEngine1.SetEngineType(SLEngine1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SLEngine1)
#################################################
SLEngine2 = App.EngineProperty_Create("SL Engine 2")

SLEngine2.SetMaxCondition(2500.000000)
SLEngine2.SetCritical(0)
SLEngine2.SetTargetable(1)
SLEngine2.SetPrimary(1)
SLEngine2.SetPosition(1.700000, -24.500000, -3.850000)
SLEngine2.SetPosition2D(0.000000, 0.000000)
SLEngine2.SetRepairComplexity(1.000000)
SLEngine2.SetDisabledPercentage(0.500000)
SLEngine2.SetRadius(0.250000)
SLEngine2.SetEngineType(SLEngine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SLEngine2)
#################################################
SLEngine3 = App.EngineProperty_Create("SL Engine 3")

SLEngine3.SetMaxCondition(2500.000000)
SLEngine3.SetCritical(0)
SLEngine3.SetTargetable(1)
SLEngine3.SetPrimary(1)
SLEngine3.SetPosition(0.000000, -24.500000, -2.300000)
SLEngine3.SetPosition2D(0.000000, 0.000000)
SLEngine3.SetRepairComplexity(1.000000)
SLEngine3.SetDisabledPercentage(0.500000)
SLEngine3.SetRadius(0.250000)
SLEngine3.SetEngineType(SLEngine3.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SLEngine3)
#################################################
CommsArray = App.SensorProperty_Create("Comms Array")

CommsArray.SetMaxCondition(2200.000000)
CommsArray.SetCritical(0)
CommsArray.SetTargetable(1)
CommsArray.SetPrimary(1)
CommsArray.SetPosition(0.000000, -15.250000, -5.925000)
CommsArray.SetPosition2D(0.000000, 0.000000)
CommsArray.SetRepairComplexity(1.000000)
CommsArray.SetDisabledPercentage(0.500000)
CommsArray.SetRadius(0.250000)
CommsArray.SetNormalPowerPerSecond(50.000000)
CommsArray.SetBaseSensorRange(1000.000000)
CommsArray.SetMaxProbes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(CommsArray)
#################################################
FTLSys = App.WarpEngineProperty_Create("FTL Sys")

FTLSys.SetMaxCondition(3200.000000)
FTLSys.SetCritical(0)
FTLSys.SetTargetable(0)
FTLSys.SetPrimary(1)
FTLSys.SetPosition(0.000000, 0.000000, 0.000000)
FTLSys.SetPosition2D(0.000000, 0.000000)
FTLSys.SetRepairComplexity(1.000000)
FTLSys.SetDisabledPercentage(0.500000)
FTLSys.SetRadius(0.250000)
FTLSys.SetNormalPowerPerSecond(10.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(FTLSys)
#################################################
FTLCoils = App.EngineProperty_Create("FTL Coils")

FTLCoils.SetMaxCondition(3200.000000)
FTLCoils.SetCritical(0)
FTLCoils.SetTargetable(1)
FTLCoils.SetPrimary(1)
FTLCoils.SetPosition(0.000000, -20.000000, -2.500000)
FTLCoils.SetPosition2D(0.000000, 0.000000)
FTLCoils.SetRepairComplexity(1.000000)
FTLCoils.SetDisabledPercentage(0.500000)
FTLCoils.SetRadius(0.250000)
FTLCoils.SetEngineType(FTLCoils.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(FTLCoils)
#################################################
PowerCore = App.PowerProperty_Create("Power Core")

PowerCore.SetMaxCondition(3000.000000)
PowerCore.SetCritical(1)
PowerCore.SetTargetable(1)
PowerCore.SetPrimary(1)
PowerCore.SetPosition(0.000000, -8.000000, 0.000000)
PowerCore.SetPosition2D(0.000000, 0.000000)
PowerCore.SetRepairComplexity(1.000000)
PowerCore.SetDisabledPercentage(0.500000)
PowerCore.SetRadius(0.250000)
PowerCore.SetMainBatteryLimit(70000.000000)
PowerCore.SetBackupBatteryLimit(10000.000000)
PowerCore.SetMainConduitCapacity(400.000000)
PowerCore.SetBackupConduitCapacity(200.000000)
PowerCore.SetPowerOutput(300.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerCore)
#################################################
SheildSys = App.ShieldProperty_Create("Sheild Sys")

SheildSys.SetMaxCondition(2.000000)
SheildSys.SetCritical(0)
SheildSys.SetTargetable(0)
SheildSys.SetPrimary(1)
SheildSys.SetPosition(0.000000, 0.000000, 0.000000)
SheildSys.SetPosition2D(0.000000, 0.000000)
SheildSys.SetRepairComplexity(1.000000)
SheildSys.SetDisabledPercentage(0.500000)
SheildSys.SetRadius(0.250000)
SheildSys.SetNormalPowerPerSecond(0.000000)
SheildSysShieldGlowColor = App.TGColorA()
SheildSysShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
SheildSys.SetShieldGlowColor(SheildSysShieldGlowColor)
SheildSys.SetShieldGlowDecay(0.000000)
SheildSys.SetMaxShields(SheildSys.FRONT_SHIELDS, 0.000000)
SheildSys.SetMaxShields(SheildSys.REAR_SHIELDS, 0.000000)
SheildSys.SetMaxShields(SheildSys.TOP_SHIELDS, 0.000000)
SheildSys.SetMaxShields(SheildSys.BOTTOM_SHIELDS, 0.000000)
SheildSys.SetMaxShields(SheildSys.LEFT_SHIELDS, 0.000000)
SheildSys.SetMaxShields(SheildSys.RIGHT_SHIELDS, 0.000000)
SheildSys.SetShieldChargePerSecond(SheildSys.FRONT_SHIELDS, 0.000000)
SheildSys.SetShieldChargePerSecond(SheildSys.REAR_SHIELDS, 0.000000)
SheildSys.SetShieldChargePerSecond(SheildSys.TOP_SHIELDS, 0.000000)
SheildSys.SetShieldChargePerSecond(SheildSys.BOTTOM_SHIELDS, 0.000000)
SheildSys.SetShieldChargePerSecond(SheildSys.LEFT_SHIELDS, 0.000000)
SheildSys.SetShieldChargePerSecond(SheildSys.RIGHT_SHIELDS, 0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(SheildSys)
#################################################
DamageControl = App.RepairSubsystemProperty_Create("Damage Control")

DamageControl.SetMaxCondition(200.000000)
DamageControl.SetCritical(0)
DamageControl.SetTargetable(0)
DamageControl.SetPrimary(1)
DamageControl.SetPosition(0.000000, 0.000000, 0.000000)
DamageControl.SetPosition2D(0.000000, 0.000000)
DamageControl.SetRepairComplexity(1.000000)
DamageControl.SetDisabledPercentage(0.500000)
DamageControl.SetRadius(0.250000)
DamageControl.SetNormalPowerPerSecond(1.000000)
DamageControl.SetMaxRepairPoints(10.000000)
DamageControl.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(DamageControl)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("AstralQueen", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sub Light Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("SL Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("SL Engine 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("SL Engine 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Comms Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FTL Coils", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sheild Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Damage Control", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
