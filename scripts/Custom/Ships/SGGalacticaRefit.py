#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 08/10/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'SGGalacticaRefit'
iconName = 'Galactica'
longName = 'SGGalacticaRefit'
shipFile = 'SGGalacticaRefit' 
menuGroup = 'Non canon X-Overs'
playerMenuGroup = 'Non canon X-Overs'
species = App.SPECIES_GALAXY
SubMenu = ["Colonial Ships", "Battlestars"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Galactica',
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
Foundation.ShipDef.SGGalacticaRefit = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.SGGalacticaRefit.dTechs = {
	'Fed Ablative Armor': { "Plates": ["Armour"]},
	'SG Shields': { "RaceShieldTech": "Go'auld" }
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.SGGalacticaRefit.hasTGLName = 1
# Foundation.ShipDef.SGGalacticaRefit.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.SGGalacticaRefit.desc = "The Galactica Class Battlestar was the first class of battlestar ever to be constructed by the Twelve Colonies. Twelve were initially constructed for the First Cylon War, each representing one of the Twelve Colonies of Kobol. Several were destroyed during the war; the rest were being retired from active service slowly at the time of the Failed Cylon attack at the Colonies (since a shockwave that emanated from the unknown-at-the-moment Gemmenon Stargate incapacitated temporarily both the Cylon Fleet and the virus, allowing the infected colonial ships to respond), presumably either to be scrapped or converted into museums. Designed and constructed during the First Cylon War, ships of this class lacked the advanced computer technology and networking of more modern battlestars for fear of Cylon infiltration of their computer systems. It is due to this resistance to infiltration that this ship was one of the ships immune to the failed Cylon attack in the Colonies. One of this vessels, the BS-75 or Battlestar Galactica was sent into an exploration mission in search of Kobol (and any Stargate or alien technology and information). After finding a crippled, abandoned Goa'uld Cheops vessel and multiple intact Tel'taks and Death Gliders, this ship was upgraded with a quantum theoretically-unhackable-by-the-Cylons crystal computer, shield emmiters, and some Pulse Weapons and Prometheon(Naquadah)-based railguns. However, in order to allow Vipers to land, the aft section lacked shielding."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.SGGalacticaRefit.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SGGalacticaRefit.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
