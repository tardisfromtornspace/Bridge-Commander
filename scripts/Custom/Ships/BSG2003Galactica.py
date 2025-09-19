#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created manually                                                                   #
#  Date: 19/09/2025                                                                   #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG2003Galactica'
iconName = 'Galactica'
longName = 'Galactica'
shipFile = 'BSG2003Galactica' 
menuGroup = 'BSG (2003) Ships'
playerMenuGroup = 'BSG (2003) Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Colonial Ships", "Battlestars"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG2003Galactica',
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
Foundation.ShipDef.BSG2003Galactica = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.BSG2003Galactica.dTechs = {
	'Fed Ablative Armor': { "Plates": ["Armour"]},
	"AutoTargeting": { "Pulse": [6, 1] },
	'Simulated Point Defence' : { "Distance": 35.0, "InnerDistance": 5.0, "Effectiveness": 0.75, "LimitTurn": 0.26, "LimitSpeed": 55, "Period": 0.1, "MaxNumberTorps": 12, },
	"Alternate-Warp-FTL": {
		"Setup": {
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

		#"Port Wing":     ["VasKholhr_Portwing", { # Future TO-DO if we can get the pods separate from the main hull, we can just adjust this script!
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

Foundation.ShipDef.BSG2003Galactica.fMaxWarp = 5.25
Foundation.ShipDef.BSG2003Galactica.fCruiseWarp = 5.0

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003Galactica.hasTGLName = 1
# Foundation.ShipDef.BSG2003Galactica.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003Galactica.desc = "The Jupiter-Class Battlestar, sometimes also known as Galactica-class or Columbia-type, was the first class of battlestar ever to be designed and constructed by the Twelve Colonies as a united government. Twelve were initially constructed for the First Cylon War, each representing one of the Twelve Colonies of Kobol. Several were destroyed during the war; the rest were being retired from active service slowly at the time of the Fall, presumably either to be scrapped or converted into museums. Designed and constructed during the First Cylon War, ships of this class lack the advanced computer technology and networking of more modern battlestars for fear of Cylon infiltration of their computer systems. It is due to this resistance to infiltration that one ship being refurbished as a war museum, the Galactica, was able to escape the Fall of the Colonies, going on to lead a group of survivors to Earth."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003Galactica.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003Galactica.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
