#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DJDamar"
iconName = "DJDamar"
longName = "DJ CDF Damar"
shipFile = "DJDamar"
species = App.SPECIES_GALAXY
menuGroup = "Card Ships"
playerMenuGroup = "Card Ships"
Foundation.ShipDef.DJDamar = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.DJDamar.desc = "The Dominion War ended in 2375, but for the people of the Cardassian Union, the hardships were just beginning.  The war brought significant civilian casualties in addition to the wholesale desruction of the Cardassian Defense Force.  The military dictatorship crumbled and the Detapa Council was reinstated.  One of their first acts was to cannibalize dozens of remaining Galor and Keldon class warships for supplies to support the civilian population.  Partly out of demands by the Federation, and partly out of necessity, the Cardassian military was quickly vanishing.\n\nBy the late 2380\'s, economic and social normalcy had begun to reassert itself.  Cardassia was trading with its neighbors and rebuilding its worlds at an astonishing pace.  With the reconstruction though, came the need for a rebuilt defense force to protect Cardassia\'s assets.  With Federation diplomatic cooperation, the Cardassians began the process of designing a modern cruiser to fill the absence of the once ubiqutous Galor Class.\n\nNamed after the great redeemer of the war, the Damar Class cruiser took only four years to develop, and the protoype ship was launched in 2391.  It was half a kilometer long and capable of a sustained speed of warp 9.6, the fastest of any Cardassian ship ever built.  Despite Starfleet\'s protests, the Detapa Council ordered that the ship be well armed, and new compressors and torpedoes were developed, significantly enhancing the ship\'s combat capacity over previous Cardassian ships.  In an act of diplomacy, the Federation ultimately agreed to sanction the ships so long as the production run remained limited, a request to which the Cardassians agreed.\n\nThe Damar Class cruiser is a highly advanced combat ship that enjoys a good balance of speed, maneuverability and offensive power.  The ship is a capable attacker from almost every angle, though it is weaker in the belly and more potent in the front.  The ship\'s main compressor and forward torpedoes can bring down enemy shields in short order.\n\nThe Damar Class is strong against Dominion War era ships, effective against late 24th century ships, and is capable but limited against ships from the 25th century."
Foundation.ShipDef.DJDamar.fMaxWarp = 9.6 + 0.0001
Foundation.ShipDef.DJDamar.fCruiseWarp = 9.2 + 0.0001

Foundation.ShipDef.DJDamar.dTechs = {
	'Breen Drainer Immune': 1,
	'Regenerative Shields': 130,
	'Multivectral Shields': 5,
}


if menuGroup:           Foundation.ShipDef.DJDamar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DJDamar.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
