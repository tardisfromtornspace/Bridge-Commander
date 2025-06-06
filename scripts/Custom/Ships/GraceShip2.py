#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 23/05/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'GraceShip2'
iconName = 'GraceShip2'
shipFile = 'GraceShip2' 
species = 749
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'GraceShip2',
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
Foundation.ShipDef.GraceShip2 = Foundation.ShipDef(abbrev, species, { 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.GraceShip2.dTechs = {
	'SG Shields': { "RaceShieldTech": "Grace" },
	'Simulated Point Defence' : { "Distance": 60.0, "InnerDistance": 12.0, "Effectiveness": 0.99, "LimitTurn": 8.5, "LimitSpeed": 250, "LimitDamage": "-600", "Period": 8.0, "MaxNumberTorps": 2, "Pulse": {"Priority": 1}},
}

Foundation.ShipDef.GraceShip2.fMaxWarp = 4.0
Foundation.ShipDef.GraceShip2.fCruiseWarp = 3.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
Foundation.ShipDef.GraceShip2.hasTGLName = 1
Foundation.ShipDef.GraceShip2.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
#Foundation.ShipDef.GraceShip2.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#   Com-man's note: Removing these lines was nesecary to prevent BC giving the        #
#   black screen yellow cursor error.                                                 #
#                                                                                     #
#######################################################################################
