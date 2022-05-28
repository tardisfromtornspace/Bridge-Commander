# C:\Utopia\Current\Build\scripts\ships\Hardpoints\venator.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.venator"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.venator", globals(), locals(), ['*'])
	reload(ParentModule)
# Setting up local templates.
#################################################
Beams = App.WeaponSystemProperty_Create("Beams")

Beams.SetMaxCondition(1000.000000)
Beams.SetCritical(0)
Beams.SetTargetable(0)
Beams.SetPrimary(1)
Beams.SetPosition(0.000000, 0.000000, 0.000000)
Beams.SetPosition2D(64.000000, 94.000000)
Beams.SetRepairComplexity(7.000000)
Beams.SetDisabledPercentage(0.750000)
Beams.SetRadius(0.400000)
Beams.SetNormalPowerPerSecond(300.000000)
Beams.SetWeaponSystemType(Beams.WST_PHASER)
Beams.SetSingleFire(1)
Beams.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Beams.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Beams)
#################################################
VentralBeam = App.PhaserProperty_Create("Ventral Beam")

VentralBeam.SetMaxCondition(1000.000000)
VentralBeam.SetCritical(0)
VentralBeam.SetTargetable(1)
VentralBeam.SetPrimary(1)
VentralBeam.SetPosition(0.000000, 1.000000, 0.000000)
VentralBeam.SetPosition2D(88.000000, 30.000000)
VentralBeam.SetRepairComplexity(7.000000)
VentralBeam.SetDisabledPercentage(0.750000)
VentralBeam.SetRadius(0.250000)
VentralBeam.SetDumbfire(0)
VentralBeam.SetWeaponID(1)
VentralBeam.SetGroups(1)
VentralBeam.SetDamageRadiusFactor(1.000000)
VentralBeam.SetIconNum(364)
VentralBeam.SetIconPositionX(47.000000)
VentralBeam.SetIconPositionY(92.000000)
VentralBeam.SetIconAboveShip(0)
VentralBeam.SetFireSound("milaser")
VentralBeam.SetMaxCharge(1.000000)
VentralBeam.SetMaxDamage(300.000000)
VentralBeam.SetMaxDamageDistance(30.000000)
VentralBeam.SetMinFiringCharge(1.000000)
VentralBeam.SetNormalDischargeRate(1.000000)
VentralBeam.SetRechargeRate(0.020000)
VentralBeam.SetIndicatorIconNum(364)
VentralBeam.SetIndicatorIconPositionX(47.000000)
VentralBeam.SetIndicatorIconPositionY(90.000000)
VentralBeamForward = App.TGPoint3()
VentralBeamForward.SetXYZ(0.000000, 0.000000, -1.000000)
VentralBeamUp = App.TGPoint3()
VentralBeamUp.SetXYZ(1.000000, 0.000000, 0.000000)
VentralBeam.SetOrientation(VentralBeamForward, VentralBeamUp)
VentralBeam.SetWidth(0.010000)
VentralBeam.SetLength(0.010000)
VentralBeam.SetArcWidthAngles(-0.750000, 0.750000)
VentralBeam.SetArcHeightAngles(-0.750000, 0.750000)
VentralBeam.SetPhaserTextureStart(0)
VentralBeam.SetPhaserTextureEnd(7)
VentralBeam.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.000000, 0.639216, 1.000000)
VentralBeam.SetOuterShellColor(kColor)
kColor.SetRGBA(0.054000, 0.192157, 0.992157, 1.000000)
VentralBeam.SetInnerShellColor(kColor)
kColor.SetRGBA(0.592157, 0.592157, 0.800000, 1.000000)
VentralBeam.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.803922, 0.803922, 0.900000, 1.000000)
VentralBeam.SetInnerCoreColor(kColor)
VentralBeam.SetNumSides(6)
VentralBeam.SetMainRadius(0.150000)
VentralBeam.SetTaperRadius(0.010000)
VentralBeam.SetCoreScale(0.500000)
VentralBeam.SetTaperRatio(0.250000)
VentralBeam.SetTaperMinLength(5.000000)
VentralBeam.SetTaperMaxLength(30.000000)
VentralBeam.SetLengthTextureTilePerUnit(0.500000)
VentralBeam.SetPerimeterTile(1.000000)
VentralBeam.SetTextureSpeed(2.500000)
VentralBeam.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(VentralBeam)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Beams", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ventral Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)