import Foundation
import FoundationTech

import ftb.Tech
import ftb.Tech.ATPFunctions

mode = FoundationTech.mode

Foundation.SoundDef('Custom/FTB/Sfx/Weapons/RomPlasmaBurst.wav', 'FTB Plasma', 1.0, { 'modes': [ mode ] })
oIPhasers = Foundation.OverrideDef('Inaccurate Phasers', 'TacticalControlHandlers.FireWeapons', 'FoundationTech.FireWeapons', { 'modes': [ mode ] } )

Foundation.LoadExtraPlugins("scripts\\Custom\\Techs")
#Foundation.LoadExtraPlugins("scripts\\ftb\\Tech")
#Include standard techs to initialize them
from ftb.Tech import AblativeArmour,DamperWeapon,DisablerYields,Shields


Foundation.ERA_ENT = 1
Foundation.ERA_TOS = 2
Foundation.ERA_TMP = 4
Foundation.ERA_PRETNG = 8
Foundation.ERA_TNG = 16
Foundation.ERA_DS9 = 32
Foundation.ERA_NEMESIS = 64
