#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 18/04/2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'B5TechnomageTransportIllusion'
iconName = 'B5TechnomageTransport'
longName = 'Illusioned Transport'
shipFile = 'B5TechnomageTransportIllusion' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_SHUTTLE
SubMenu = "Technomages"

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'B5TechnomageTransportIllusion',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.B5TechnomageTransportIllusion = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.B5TechnomageTransportIllusion.dTechs = {
	"Phase Cloak": 10,
	'Simulated Point Defence' : { "Distance": 75.0, "InnerDistance": 40.0, "Effectiveness": 0.92, "LimitTurn": 8.6, "LimitSpeed": 85, "LimitDamage": "-250", "Period": 1.0, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}},
	"Tachyon Sensors": 0.1
}

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.B5TechnomageTransportIllusion.hasTGLName = 1
# Foundation.ShipDef.B5TechnomageTransportIllusion.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.B5TechnomageTransportIllusion.desc = "Technomage ships are fantastic craft, as powerful as they are mysterious. We know from documented evidence taken by the ISA Excalibur that Technomage ships posses stealth technology capable of eluding even the advanced scanners of the Interstellar Alliances most powerful Destroyer, or capable of projecting a hologram to look like whatever the Technomage wants us to see."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.B5TechnomageTransportIllusion.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.B5TechnomageTransportIllusion.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
