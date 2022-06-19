#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Shadow_Fighter2"
iconName = "Shadow_Fighter"
longName = "Shadow Fighter"
shipFile = "Shadow_Fighter"
species = App.SPECIES_SHUTTLE

Foundation.ShipDef.Shadow_Fighter2 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})

Foundation.ShipDef.Shadow_Fighter2.dTechs = { "Phase Cloak": 10, 'Breen Drainer Immune': 1, 'Shadow Dispersive Hull': 1}

Foundation.ShipDef.Shadow_Fighter2.desc = "The Shadow Fighter was the standard fighter used by the Shadows. Shadow fighters are extremely tough, fast and powerful. It appears to feature the same resilient, blast refracting material as the larger Shadow Vessels. The squat, spiky body of the Shadow Fighter is built around a central pulse cannon which, when fired causes the entire craft to convulse, appearing to 'spit' as it discharges the weapon. More than capable of holding its own against most fighters used by the Younger Races, the only non-First One fighter seen to outmatch the Shadow Fighter was the early White Star prototype."
Foundation.ShipDef.Shadow_Fighter2.CloakingSFX = "shadowscream"
Foundation.ShipDef.Shadow_Fighter2.DeCloakingSFX = "shadowscream"
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#   Com-man's note: Removing these lines was nesecary to prevent BC giving the        #
#   black screen yellow cursor error.                                                 #
#                                                                                     #
#######################################################################################
