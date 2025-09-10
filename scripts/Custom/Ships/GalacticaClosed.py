#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 09/09/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'GalacticaClosed'
iconName = 'GalacticaClosed'
longName = 'Galactica (Closed)'
shipFile = 'GalacticaClosed' 
menuGroup = 'BSG Ships'
playerMenuGroup = 'BSG Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Colonial Ships", "Battlestars"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'GalacticaClosed',
	'author': '',
	'version': '1.1',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.GalacticaClosed = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.GalacticaClosed.dTechs = {
	'Fed Ablative Armor': { "Plates": ["Armour"]},
	"AutoTargeting": { "Pulse": [6, 1] },
	'Simulated Point Defence' : { "Distance": 35.0, "InnerDistance": 5.0, "Effectiveness": 0.5, "LimitTurn": 0.125, "LimitSpeed": 35, "Period": 0.1, "MaxNumberTorps": 12, },
	"Alternate-Warp-FTL": { # (#)
		"Setup": { # (#)
			"nBSGDimensionalJump": {	"Nacelles": ["FTL Drive 1", "FTL Drive 2"], "Core": ["Reactor Module"], "Cooldown Time": 15 * 60},
			"BodySetScale": 1.0,
			"NormalSetScale": 1.0,
			"WarpSetScale": 1.0,
			"nBSGDimensionalJumpSetScale": 0.1,
			"AttackSetScale": 1.0,
			"Hardpoints":       {
				"Port Hanger":  [-5.500000, 1.000000, 0.000000, {"Disabled Percentage" : 0.5}],
				"Star Hanger":  [5.500000, 1.000000, 0.000000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P1":  [-6.900000, 2.900000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P2":  [-6.950000, 2.150000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P3":  [-7.000000, 1.020000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P4":  [-7.020000, 0.300000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P5":  [-7.020000, -0.800000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P6":  [-7.020000, -1.550000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P7":  [-7.020000, -2.675000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P8":  [-7.020000, -3.400000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P9":  [-6.930000, -4.500000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P10":  [-6.850000, -5.275000, -0.620000, {"Disabled Percentage" : 0.5}],
				"Launch Tube P1 OEP":  [-6.900000, 2.900000, -0.620000 ],
				"Launch Tube P2 OEP":  [-6.950000, 2.150000, -0.620000 ],
				"Launch Tube P3 OEP":  [-7.000000, 1.020000, -0.620000 ],
				"Launch Tube P4 OEP":  [-7.020000, 0.300000, -0.620000 ],
				"Launch Tube P5 OEP":  [-7.020000, -0.800000, -0.620000 ],
				"Launch Tube P6 OEP":  [-7.020000, -1.550000, -0.620000 ],
				"Launch Tube P7 OEP":  [-7.020000, -2.675000, -0.620000 ],
				"Launch Tube P8 OEP":  [-7.020000, -3.400000, -0.620000 ],
				"Launch Tube P9 OEP":  [-5.180000, -4.500000, -0.620000 ],
				"Launch Tube P10 OEP":  [-6.850000, -5.275000, -0.620000 ],
			},

			"nBSGDimensionalJumpHardpoints":       {
				"Port Hanger":  [-3.750000, -1.000000, -0.750000, {"Disabled Percentage" : 1.5}],
				"Star Hanger":  [3.750000, -1.000000, -0.750000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P1":  [-5.150000, 2.900000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P2":  [-5.200000, 2.150000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P3":  [-5.250000, 1.020000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P4":  [-5.270000, 0.300000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P5":  [-5.270000, -0.800000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P6":  [-5.270000, -1.550000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P7":  [-5.270000, -2.675000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P8":  [-5.270000, -3.400000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P9":  [-5.180000, -4.500000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P10":  [-5.100000, -5.275000, -0.620000, {"Disabled Percentage" : 1.5}],
				"Launch Tube P1 OEP":  [-5.150000, 2.900000, -0.620000 ],
				"Launch Tube P2 OEP":  [-5.200000, 2.150000, -0.620000 ],
				"Launch Tube P3 OEP":  [-5.250000, 1.020000, -0.620000 ],
				"Launch Tube P4 OEP":  [-5.270000, 0.300000, -0.620000 ],
				"Launch Tube P5 OEP":  [-5.270000, -0.800000, -0.620000 ],
				"Launch Tube P6 OEP":  [-5.270000, -1.550000, -0.620000 ],
				"Launch Tube P7 OEP":  [-5.270000, -2.675000, -0.620000 ],
				"Launch Tube P8 OEP":  [-5.270000, -3.400000, -0.620000 ],
				"Launch Tube P9 OEP":  [-5.180000, -4.500000, -0.620000 ],
				"Launch Tube P10 OEP":  [-5.100000, -5.275000, -0.620000 ],
			},
		},

		#"Port Wing":     ["VasKholhr_Portwing", {
		#	"SetScale": 1.0,
		#	"Position":             [1.75, 0, 0],
		#	"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
		#	"nBSGDimensionalJumpRotation":       [0, 0, 0],
		#	"nBSGDimensionalJumpPosition":       [0, 0, 0],
		#	"nBSGDimensionalJumpDuration":       150.0,
		#	},
		#],
        
		#"Starboard Wing":     ["VasKholhr_Starboardwing", {
		#	"SetScale": 1.0,
		#	"Position":             [-1.75, 0, 0],
		#	"Rotation":             [0, 0, 0],
		#	"nBSGDimensionalJumpRotation":       [0, 0, 0],
		#	"nBSGDimensionalJumpPosition":       [0, 0, 0],
		#	"nBSGDimensionalJumpDuration":       150.0,
		#	},
		#],
	},
}

Foundation.ShipDef.GalacticaClosed.fMaxWarp = 5.25
Foundation.ShipDef.GalacticaClosed.fCruiseWarp = 5.0
#                                                                                     #
# Com-man's note: Of course you need to remove the 'name': longname here too for it   #
# to work.              						                          #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.GalacticaClosed.hasTGLName = 1
# Foundation.ShipDef.GalacticaClosed.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.GalacticaClosed.desc = 'The Galactica Class Battlestar was the first class of battlestar ever to be constructed by the Twelve Colonies. Twelve were initially constructed for the First Cylon War, each representing one of the Twelve Colonies of Kobol. Several were destroyed during the war; the rest were being retired from active service slowly at the time of the Fall, presumably either to be scrapped or converted into museums. Designed and constructed during the First Cylon War, ships of this class lack the advanced computer technology and networking of more modern battlestars for fear of Cylon infiltration of their computer systems. It is due to this resistance to infiltration that one ship was able to escape the Fall of the Colonies, going on to lead a group of survivors to Earth.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.GalacticaClosed.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.GalacticaClosed.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
