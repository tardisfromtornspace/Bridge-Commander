# D:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\AdObPegasus.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.hardpoints.AdOberthBase"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.hardpoints.AdOberthBase", globals(), locals(), ['*'])
	reload(ParentModule)
# Setting up local templates.
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(700.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.066146, 0.005080)
ShieldGenerator.SetPosition2D(64.000000, 75.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.050000)
ShieldGenerator.SetNormalPowerPerSecond(300.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 4000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 4000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 4000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 4000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 4000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 11.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 9.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 10.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 10.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 8.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 8.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(880.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.100000, 0.000000, 0.000000)
Torpedoes.SetPosition2D(74.000000, 60.000000)
Torpedoes.SetRepairComplexity(3.000000)
Torpedoes.SetDisabledPercentage(0.750000)
Torpedoes.SetRadius(0.061100)
Torpedoes.SetNormalPowerPerSecond(70.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 400)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.PegasusPhoton")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
ForwardTorpedo1 = App.TorpedoTubeProperty_Create("Forward Torpedo 1")

ForwardTorpedo1.SetMaxCondition(200.000000)
ForwardTorpedo1.SetCritical(0)
ForwardTorpedo1.SetTargetable(1)
ForwardTorpedo1.SetPrimary(1)
ForwardTorpedo1.SetPosition(-0.015148, 0.405321, -0.015827)
ForwardTorpedo1.SetPosition2D(59.000000, 60.000000)
ForwardTorpedo1.SetRepairComplexity(3.000000)
ForwardTorpedo1.SetDisabledPercentage(0.600000)
ForwardTorpedo1.SetRadius(0.020000)
ForwardTorpedo1.SetDumbfire(1)
ForwardTorpedo1.SetWeaponID(1)
ForwardTorpedo1.SetGroups(1)
ForwardTorpedo1.SetDamageRadiusFactor(0.900000)
ForwardTorpedo1.SetIconNum(370)
ForwardTorpedo1.SetIconPositionX(78.000000)
ForwardTorpedo1.SetIconPositionY(35.000000)
ForwardTorpedo1.SetIconAboveShip(1)
ForwardTorpedo1.SetImmediateDelay(1.260000)
ForwardTorpedo1.SetReloadDelay(15.000000)
ForwardTorpedo1.SetMaxReady(2)
ForwardTorpedo1Direction = App.TGPoint3()
ForwardTorpedo1Direction.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTorpedo1.SetDirection(ForwardTorpedo1Direction)
ForwardTorpedo1Right = App.TGPoint3()
ForwardTorpedo1Right.SetXYZ(-1.000000, 0.000000, 0.000000)
ForwardTorpedo1.SetRight(ForwardTorpedo1Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTorpedo1)
#################################################
Pegasus = App.ShipProperty_Create("Pegasus")

Pegasus.SetGenus(1)
Pegasus.SetSpecies(102)
Pegasus.SetMass(25.000000)
Pegasus.SetRotationalInertia(12500.000000)
Pegasus.SetShipName("Pegasus")
Pegasus.SetModelFilename("data/models/ships/Pegasus/Pegasus.nif")
Pegasus.SetDamageResolution(1.000000)
Pegasus.SetAffiliation(0)
Pegasus.SetStationary(0)
Pegasus.SetAIString("FedAttack")
Pegasus.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Pegasus)
#################################################
SecondarySensorArray = App.SensorProperty_Create("Secondary Sensor Array")

SecondarySensorArray.SetMaxCondition(100.000000)
SecondarySensorArray.SetCritical(0)
SecondarySensorArray.SetTargetable(1)
SecondarySensorArray.SetPrimary(1)
SecondarySensorArray.SetPosition(0.000000, -0.783743, -0.254170)
SecondarySensorArray.SetPosition2D(64.000000, 75.000000)
SecondarySensorArray.SetRepairComplexity(1.000000)
SecondarySensorArray.SetDisabledPercentage(0.500000)
SecondarySensorArray.SetRadius(0.020000)
SecondarySensorArray.SetNormalPowerPerSecond(75.000000)
SecondarySensorArray.SetBaseSensorRange(1500.000000)
SecondarySensorArray.SetMaxProbes(25)
App.g_kModelPropertyManager.RegisterLocalTemplate(SecondarySensorArray)
#################################################
DorsalPhaser1 = App.PhaserProperty_Create("Dorsal Phaser 1")

DorsalPhaser1.SetMaxCondition(800.000000)
DorsalPhaser1.SetCritical(0)
DorsalPhaser1.SetTargetable(1)
DorsalPhaser1.SetPrimary(1)
DorsalPhaser1.SetPosition(0.166437, 0.481272, 0.032398)
DorsalPhaser1.SetPosition2D(34.000000, 40.000000)
DorsalPhaser1.SetRepairComplexity(7.000000)
DorsalPhaser1.SetDisabledPercentage(0.750000)
DorsalPhaser1.SetRadius(0.015000)
DorsalPhaser1.SetDumbfire(0)
DorsalPhaser1.SetWeaponID(5)
DorsalPhaser1.SetGroups(0)
DorsalPhaser1.SetDamageRadiusFactor(0.250000)
DorsalPhaser1.SetIconNum(350)
DorsalPhaser1.SetIconPositionX(85.000000)
DorsalPhaser1.SetIconPositionY(30.000000)
DorsalPhaser1.SetIconAboveShip(1)
DorsalPhaser1.SetFireSound("Galaxy Phaser")
DorsalPhaser1.SetMaxCharge(5.000000)
DorsalPhaser1.SetMaxDamage(350.000000)
DorsalPhaser1.SetMaxDamageDistance(60.000000)
DorsalPhaser1.SetMinFiringCharge(1.000000)
DorsalPhaser1.SetNormalDischargeRate(1.000000)
DorsalPhaser1.SetRechargeRate(0.200000)
DorsalPhaser1.SetIndicatorIconNum(506)
DorsalPhaser1.SetIndicatorIconPositionX(89.000000)
DorsalPhaser1.SetIndicatorIconPositionY(26.000000)
DorsalPhaser1Forward = App.TGPoint3()
DorsalPhaser1Forward.SetXYZ(0.707107, 0.707107, 0.000000)
DorsalPhaser1Up = App.TGPoint3()
DorsalPhaser1Up.SetXYZ(0.000000, 0.000000, 1.000000)
DorsalPhaser1.SetOrientation(DorsalPhaser1Forward, DorsalPhaser1Up)
DorsalPhaser1.SetWidth(0.001000)
DorsalPhaser1.SetLength(0.001000)
DorsalPhaser1.SetArcWidthAngles(-0.872665, 0.872665)
DorsalPhaser1.SetArcHeightAngles(-0.139626, 1.483530)
DorsalPhaser1.SetPhaserTextureStart(0)
DorsalPhaser1.SetPhaserTextureEnd(7)
DorsalPhaser1.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
DorsalPhaser1.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
DorsalPhaser1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.992157, 0.831373, 0.639216, 1.000000)
DorsalPhaser1.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.992157, 0.901961, 0.858824, 1.000000)
DorsalPhaser1.SetInnerCoreColor(kColor)
DorsalPhaser1.SetNumSides(6)
DorsalPhaser1.SetMainRadius(0.040000)
DorsalPhaser1.SetTaperRadius(0.010000)
DorsalPhaser1.SetCoreScale(0.500000)
DorsalPhaser1.SetTaperRatio(0.250000)
DorsalPhaser1.SetTaperMinLength(5.000000)
DorsalPhaser1.SetTaperMaxLength(30.000000)
DorsalPhaser1.SetLengthTextureTilePerUnit(0.050000)
DorsalPhaser1.SetPerimeterTile(1.000000)
DorsalPhaser1.SetTextureSpeed(5.000000)
DorsalPhaser1.SetTextureName("data/textures/tactical/ZZSaratogaPhas.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(DorsalPhaser1)
#################################################
DorsalPhaser2 = App.PhaserProperty_Create("Dorsal Phaser 2")

DorsalPhaser2.SetMaxCondition(800.000000)
DorsalPhaser2.SetCritical(0)
DorsalPhaser2.SetTargetable(1)
DorsalPhaser2.SetPrimary(1)
DorsalPhaser2.SetPosition(-0.166384, 0.481059, 0.032499)
DorsalPhaser2.SetPosition2D(34.000000, 40.000000)
DorsalPhaser2.SetRepairComplexity(7.000000)
DorsalPhaser2.SetDisabledPercentage(0.750000)
DorsalPhaser2.SetRadius(0.015000)
DorsalPhaser2.SetDumbfire(0)
DorsalPhaser2.SetWeaponID(5)
DorsalPhaser2.SetGroups(0)
DorsalPhaser2.SetDamageRadiusFactor(0.250000)
DorsalPhaser2.SetIconNum(330)
DorsalPhaser2.SetIconPositionX(22.000000)
DorsalPhaser2.SetIconPositionY(30.000000)
DorsalPhaser2.SetIconAboveShip(1)
DorsalPhaser2.SetFireSound("Galaxy Phaser")
DorsalPhaser2.SetMaxCharge(5.000000)
DorsalPhaser2.SetMaxDamage(350.000000)
DorsalPhaser2.SetMaxDamageDistance(60.000000)
DorsalPhaser2.SetMinFiringCharge(1.000000)
DorsalPhaser2.SetNormalDischargeRate(1.000000)
DorsalPhaser2.SetRechargeRate(0.200000)
DorsalPhaser2.SetIndicatorIconNum(505)
DorsalPhaser2.SetIndicatorIconPositionX(29.000000)
DorsalPhaser2.SetIndicatorIconPositionY(26.000000)
DorsalPhaser2Forward = App.TGPoint3()
DorsalPhaser2Forward.SetXYZ(-0.707107, 0.707107, 0.000000)
DorsalPhaser2Up = App.TGPoint3()
DorsalPhaser2Up.SetXYZ(0.000000, 0.000000, 1.000000)
DorsalPhaser2.SetOrientation(DorsalPhaser2Forward, DorsalPhaser2Up)
DorsalPhaser2.SetWidth(0.001000)
DorsalPhaser2.SetLength(0.001000)
DorsalPhaser2.SetArcWidthAngles(-0.872665, 0.872665)
DorsalPhaser2.SetArcHeightAngles(-0.139626, 1.483530)
DorsalPhaser2.SetPhaserTextureStart(0)
DorsalPhaser2.SetPhaserTextureEnd(7)
DorsalPhaser2.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
DorsalPhaser2.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
DorsalPhaser2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.992157, 0.831373, 0.639216, 1.000000)
DorsalPhaser2.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.992157, 0.901961, 0.858824, 1.000000)
DorsalPhaser2.SetInnerCoreColor(kColor)
DorsalPhaser2.SetNumSides(6)
DorsalPhaser2.SetMainRadius(0.040000)
DorsalPhaser2.SetTaperRadius(0.010000)
DorsalPhaser2.SetCoreScale(0.500000)
DorsalPhaser2.SetTaperRatio(0.250000)
DorsalPhaser2.SetTaperMinLength(5.000000)
DorsalPhaser2.SetTaperMaxLength(30.000000)
DorsalPhaser2.SetLengthTextureTilePerUnit(0.050000)
DorsalPhaser2.SetPerimeterTile(1.000000)
DorsalPhaser2.SetTextureSpeed(5.000000)
DorsalPhaser2.SetTextureName("data/textures/tactical/ZZSaratogaPhas.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(DorsalPhaser2)
#################################################
PhaseCloak = App.CloakingSubsystemProperty_Create("Phase Cloak")

PhaseCloak.SetMaxCondition(200.000000)
PhaseCloak.SetCritical(0)
PhaseCloak.SetTargetable(1)
PhaseCloak.SetPrimary(1)
PhaseCloak.SetPosition(0.000000, -0.130000, 0.000000)
PhaseCloak.SetPosition2D(0.000000, 0.000000)
PhaseCloak.SetRepairComplexity(1.000000)
PhaseCloak.SetDisabledPercentage(0.500000)
PhaseCloak.SetRadius(0.030000)
PhaseCloak.SetNormalPowerPerSecond(50.000000)
PhaseCloak.SetCloakStrength(60.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PhaseCloak)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Secondary Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Torpedo 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Pegasus", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Dorsal Phaser 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Dorsal Phaser 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phase Cloak", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
