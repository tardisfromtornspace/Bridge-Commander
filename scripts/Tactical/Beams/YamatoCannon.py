# YamatoCannon.py

"""
#EXAMPLE OF USAGE, REPLACE "Phaser1" for a non-repeated name:
from Tactical.Beams.YamatoCannon import Phaser as Phaser1

# Necessary to change names!!!
Phaser1.SetName("Yamato Cannon")
# I guess these can be standarized, but very recommended to change them
Phaser1.SetMaxCondition(200.000000)
Phaser1.SetCritical(0)
Phaser1.SetTargetable(1)
Phaser1.SetPrimary(0)
# unless you want all icons and hardpoint properties on the same place, adjsut these accordingly
Phaser1.SetPosition(0.000000, 2.000000, 0.000000)
Phaser1.SetPosition2D(64.000000, 33.000000)
# I guess these can be standarized, but very recommended to change them
Phaser1.SetRepairComplexity(1.000000)
Phaser1.SetDisabledPercentage(0.500000)
# unless you want all icons being the same and on the same place, adjsut these accordingly (icon 0 is a red "X" symbol)
Phaser1.SetIconNum(0)
Phaser1.SetIconPositionX(0.000000)
Phaser1.SetIconPositionY(0.000000)
Phaser1.SetIconAboveShip(1)
# unless you want all icons incidcating that the weapon can fire at the target the same and on the same place, adjsut
Phaser1.SetIndicatorIconNum(0)
Phaser1.SetIndicatorIconPositionX(0.000000)
Phaser1.SetIndicatorIconPositionY(0.000000)
# Important, where is the phaser aiming???
PhaserForward = App.TGPoint3()
PhaserForward.SetXYZ(0.000000, 1.000000, 0.000000)
PhaserUp = App.TGPoint3()
PhaserUp.SetXYZ(0.000000, 0.000000, 1.000000)
Phaser1.SetOrientation(PhaserForward, PhaserUp)
# Important, what are the arcs! also remember the beam is an ellipsoid, so Width and Length affect as well!
Phaser1.SetWidth(1.800000)
Phaser1.SetLength(1.400000)
Phaser1.SetArcWidthAngles(-1.963495, 1.963495)
Phaser1.SetArcHeightAngles(-0.098175, 2.356194)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phaser1)
"""
import App



#################################################
Phaser = App.PhaserProperty_Create("Yamato Cannon")

Phaser.SetMaxCondition(500.000000)
Phaser.SetCritical(0)
Phaser.SetTargetable(1)
Phaser.SetPrimary(0)
Phaser.SetPosition(0.000000, 0.000000, 0.000000)
Phaser.SetPosition2D(64.000000, 33.000000)
Phaser.SetRepairComplexity(1.000000)
Phaser.SetDisabledPercentage(0.500000)
Phaser.SetRadius(0.250000)
Phaser.SetDumbfire(0)
Phaser.SetWeaponID(0)
Phaser.SetGroups(0)
Phaser.SetDamageRadiusFactor(0.250000)
Phaser.SetIconNum(364)
Phaser.SetIconPositionX(63.000000)
Phaser.SetIconPositionY(34.000000)
Phaser.SetIconAboveShip(1)
Phaser.SetFireSound("Enterprise D Phaser")
Phaser.SetMaxCharge(1.000000)
Phaser.SetMaxDamage(240.000000)
Phaser.SetMaxDamageDistance(100.000000)
Phaser.SetMinFiringCharge(1.000000)
Phaser.SetNormalDischargeRate(1.000000)
Phaser.SetRechargeRate(0.066667)
Phaser.SetIndicatorIconNum(510)
Phaser.SetIndicatorIconPositionX(57.000000)
Phaser.SetIndicatorIconPositionY(29.000000)
PhaserForward = App.TGPoint3()
PhaserForward.SetXYZ(0.000000, 1.000000, 0.000000)
PhaserUp = App.TGPoint3()
PhaserUp.SetXYZ(0.000000, 0.000000, 1.000000)
Phaser.SetOrientation(PhaserForward, PhaserUp)
Phaser.SetWidth(1.800000)
Phaser.SetLength(1.400000)
Phaser.SetArcWidthAngles(-0.163495, 0.163495)
Phaser.SetArcHeightAngles(-0.298175, 0.256194)
Phaser.SetPhaserTextureStart(0)
Phaser.SetPhaserTextureEnd(0)
Phaser.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.172549, 0.007843, 1.000000)
Phaser.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.172549, 0.007843, 1.000000)
Phaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.992157, 0.835294, 0.639216, 1.000000)
Phaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.992157, 0.901961, 0.862745, 1.000000)
Phaser.SetInnerCoreColor(kColor)
Phaser.SetNumSides(6)
Phaser.SetMainRadius(0.150000)
Phaser.SetTaperRadius(0.010000)
Phaser.SetCoreScale(0.500000)
Phaser.SetTaperRatio(0.250000)
Phaser.SetTaperMinLength(5.000000)
Phaser.SetTaperMaxLength(30.000000)
Phaser.SetLengthTextureTilePerUnit(0.500000)
Phaser.SetPerimeterTile(1.000000)
Phaser.SetTextureSpeed(2.500000)
Phaser.SetTextureName("data/phaser.tga")

def returnBeam():
    return Phaser