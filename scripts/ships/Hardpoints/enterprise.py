# C:\Utopia\Current\Build\scripts\ships\Hardpoints\enterprise.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.sovereign"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.sovereign", globals(), locals(), ['*'])
	reload(ParentModule)
# Setting up local templates.
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(20000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.492363, 0.000000)
ShieldGenerator.SetPosition2D(64.000000, 65.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.300000)
ShieldGenerator.SetNormalPowerPerSecond(300.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 16000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 16000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 16000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 16000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 16000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 16000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 25.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(14000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.200000, -0.300000)
WarpCore.SetPosition2D(64.000000, 80.000000)
WarpCore.SetRepairComplexity(1.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.300000)
WarpCore.SetMainBatteryLimit(300000.000000)
WarpCore.SetBackupBatteryLimit(120000.000000)
WarpCore.SetMainConduitCapacity(1900.000000)
WarpCore.SetBackupConduitCapacity(300.000000)
WarpCore.SetPowerOutput(1600.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(5000.000000)
Engineering.SetCritical(0)
Engineering.SetTargetable(0)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, -0.200000)
Engineering.SetPosition2D(64.000000, 84.000000)
Engineering.SetRepairComplexity(1.000000)
Engineering.SetDisabledPercentage(0.100000)
Engineering.SetRadius(0.400000)
Engineering.SetNormalPowerPerSecond(1.000000)
Engineering.SetMaxRepairPoints(180.000000)
Engineering.SetNumRepairTeams(6)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
RegenerativeShields = App.ShieldProperty_Create("Regenerative Shields")

RegenerativeShields.SetMaxCondition(10000.000000)
RegenerativeShields.SetCritical(0)
RegenerativeShields.SetTargetable(1)
RegenerativeShields.SetPrimary(1)
RegenerativeShields.SetPosition(0.000000, 0.500000, 0.000000)
RegenerativeShields.SetPosition2D(64.000000, 60.000000)
RegenerativeShields.SetRepairComplexity(0.000500)
RegenerativeShields.SetDisabledPercentage(0.050000)
RegenerativeShields.SetRadius(0.400000)
RegenerativeShields.SetNormalPowerPerSecond(1.000000)
RegenerativeShieldsShieldGlowColor = App.TGColorA()
RegenerativeShieldsShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
RegenerativeShields.SetShieldGlowColor(RegenerativeShieldsShieldGlowColor)
RegenerativeShields.SetShieldGlowDecay(1.000000)
RegenerativeShields.SetMaxShields(RegenerativeShields.FRONT_SHIELDS, 18000.000000)
RegenerativeShields.SetMaxShields(RegenerativeShields.REAR_SHIELDS, 18000.000000)
RegenerativeShields.SetMaxShields(RegenerativeShields.TOP_SHIELDS, 18000.000000)
RegenerativeShields.SetMaxShields(RegenerativeShields.BOTTOM_SHIELDS, 18000.000000)
RegenerativeShields.SetMaxShields(RegenerativeShields.LEFT_SHIELDS, 18000.000000)
RegenerativeShields.SetMaxShields(RegenerativeShields.RIGHT_SHIELDS, 18000.000000)
RegenerativeShields.SetShieldChargePerSecond(RegenerativeShields.FRONT_SHIELDS, 20.000000)
RegenerativeShields.SetShieldChargePerSecond(RegenerativeShields.REAR_SHIELDS, 20.000000)
RegenerativeShields.SetShieldChargePerSecond(RegenerativeShields.TOP_SHIELDS, 20.000000)
RegenerativeShields.SetShieldChargePerSecond(RegenerativeShields.BOTTOM_SHIELDS, 20.000000)
RegenerativeShields.SetShieldChargePerSecond(RegenerativeShields.LEFT_SHIELDS, 20.000000)
RegenerativeShields.SetShieldChargePerSecond(RegenerativeShields.RIGHT_SHIELDS, 20.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(RegenerativeShields)
#################################################
MultivectralShields = App.ShieldProperty_Create("Multivectral Shields")

MultivectralShields.SetMaxCondition(10000.000000)
MultivectralShields.SetCritical(0)
MultivectralShields.SetTargetable(1)
MultivectralShields.SetPrimary(1)
MultivectralShields.SetPosition(0.000000, 0.500000, 0.000000)
MultivectralShields.SetPosition2D(64.000000, 60.000000)
MultivectralShields.SetRepairComplexity(0.999000)
MultivectralShields.SetDisabledPercentage(0.600000)
MultivectralShields.SetRadius(0.400000)
MultivectralShields.SetNormalPowerPerSecond(1.000000)
MultivectralShieldsShieldGlowColor = App.TGColorA()
MultivectralShieldsShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
MultivectralShields.SetShieldGlowColor(MultivectralShieldsShieldGlowColor)
MultivectralShields.SetShieldGlowDecay(1.000000)
MultivectralShields.SetMaxShields(MultivectralShields.FRONT_SHIELDS, 18000.000000)
MultivectralShields.SetMaxShields(MultivectralShields.REAR_SHIELDS, 18000.000000)
MultivectralShields.SetMaxShields(MultivectralShields.TOP_SHIELDS, 18000.000000)
MultivectralShields.SetMaxShields(MultivectralShields.BOTTOM_SHIELDS, 18000.000000)
MultivectralShields.SetMaxShields(MultivectralShields.LEFT_SHIELDS, 18000.000000)
MultivectralShields.SetMaxShields(MultivectralShields.RIGHT_SHIELDS, 18000.000000)
MultivectralShields.SetShieldChargePerSecond(MultivectralShields.FRONT_SHIELDS, 4.000000)
MultivectralShields.SetShieldChargePerSecond(MultivectralShields.REAR_SHIELDS, 4.000000)
MultivectralShields.SetShieldChargePerSecond(MultivectralShields.TOP_SHIELDS, 4.000000)
MultivectralShields.SetShieldChargePerSecond(MultivectralShields.BOTTOM_SHIELDS, 4.000000)
MultivectralShields.SetShieldChargePerSecond(MultivectralShields.LEFT_SHIELDS, 4.000000)
MultivectralShields.SetShieldChargePerSecond(MultivectralShields.RIGHT_SHIELDS, 4.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(MultivectralShields)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(16000.000000)
Hull.SetCritical(0)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, -0.200000)
Hull.SetPosition2D(64.000000, 65.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.600000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
        if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Regenerative Shields", App.TGModelPropertyManager.LOCAL_TEMPLATES)
        if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Multivectral Shields", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
