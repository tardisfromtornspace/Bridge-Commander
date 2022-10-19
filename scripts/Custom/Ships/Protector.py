#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Protector"
iconName = "Protector"
longName = "Protector"
shipFile = "Protector"
species = App.SPECIES_GALAXY
menuGroup = "Galaxy Quest Ships"
playerMenuGroup = "Galaxy Quest Ships"
Foundation.ShipDef.Protector = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Protector.desc = "The Protector II was a ship built by the Thermians to be identical in every way to the fictional NSEA-Protector. The Protector II was built by the Thermians who were to pick up Jason Nesmith and his crew in order to battle the evil Roth'h'ar Sarris, who desired one thing and one thing only; the Omega-13. The ship was first introduced to Nesmith; however later on after taking the job Nesmith spoke about; his crew were introduced to the ship as well. When she was launched; the Protector received a scrape on her port bow which was minor. She later was attacked by Sarris' ship the K'ragk-Vort't; causing heavy damage on her bow. She later received severe damage while entering the Tothian Minefield. Upon exiting the minefield; the crew reviewed the damage. The main problem was that the Beryllium Sphere that powers the ship was fractured under stress; leaving the vessel powerless. They then managed to to use endothermic propulsion in order to get to the nearby planet Epsilon Gorniar II in order to find a Beryllium Sphere. After passing through a wormhole and approaching Earth dangerously fast, the crew separated the Protector's upper command section. The rest of the ship, with the Thermians aboard, was able to veer off and avoid the planet, but the command section entered the atmosphere at Mark 15, crash-landing in the parking lot of a science fiction convention."


if menuGroup:           Foundation.ShipDef.Protector.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Protector.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
