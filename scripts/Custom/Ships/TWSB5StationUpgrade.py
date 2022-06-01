import Foundation
import App
# Usually you need only edit these seven lines

abbrev = 'B5StationUpgrade'
iconName = 'B5Station'
longName = 'Babylon 5 Station'
shipFile = 'THSB5StationUpgrade' 
menuGroup = 'Non canon X-Overs'
playerMenuGroup = 'Non canon X-Overs'
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'B5Station',   # The full name of your mod if applicable
	'author': '',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.B5StationUpgrade = Foundation.KlingonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.B5StationUpgrade.dTechs = {
	'Defense Grid': 200
}
# Uncomment these if you have TGL
#Foundation.ShipDef.B5StationUpgrade.hasTGLName = 1
#Foundation.ShipDef.B5StationUpgrade.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.B5StationUpgrade.desc = "Babylon 5, after the menace of the Clark's Regime, the Shadows and the Shinindrea victory in Zha'ha'Dum, was severely upgraded by the aid of the 'Future Enterprise' alternate-timeline Piccard, Garret, an alternate Sisko and the Vogagaer-B, adding artificial gravity, deflector shielding, hull plating and Klingon's disruptor batteries powerful enough to destroy a Shadow battlecrab. Here, the truth about Vorlon and Shadow tampering in the Young Races was revealed by Ambassador Guinan, Capain Garret and Katheryn Janeway; supported by Lorien the First One; and considered the start of the deep alliance formed in this parallel B5 universe against the Yonji Shinindrea."

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.B5StationUpgrade.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.B5StationUpgrade.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
