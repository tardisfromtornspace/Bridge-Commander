#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 10/25/2009                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'PAHLexington'
iconName = 'WCJJEnterprise'
longName = 'PAH U.S.S. Lexington'
shipFile = 'PAHLexington' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_AMBASSADOR
SubMenu = "Prime Alt Hybrid Constitution Class"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'USS Enterprise - Star Trek 2009',
	'author': 'Blackrook32',
	'version': '1.0',
	'sources': [ '' ],
	'comments': ''
}

Foundation.ShipDef.PAHLexington = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.PAHLexington.fMaxWarp = 7.5
Foundation.ShipDef.PAHLexington.fCruiseWarp = 9.2
Foundation.ShipDef.PAHLexington.desc = 'This 23rd Century ship is featured in the film Star Trek 2009. The Prime Alternate Hybrid is a envisioned cr.2267 version.'

Foundation.ShipDef.PAHLexington.dTechs = {
	# Here comes the PAHWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"PAHWarpStartUp": {
		"track": {
			"bussard_pow_glow": {
				0.0: "data/Models/Ships/STXI_PrimeAltHybrid/PAHEnterprise/bussard_pow_glow.tga", 
				1.0: "data/Models/Ships/STXI_PrimeAltHybrid/PAHEnterprise/bussard_pow_spec.tga",
			}
		}
	}
}

if menuGroup:           Foundation.ShipDef.PAHLexington.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.PAHLexington.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]