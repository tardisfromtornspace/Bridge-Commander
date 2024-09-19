#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "USSValorJJ"
iconName = "UssValor"
longName = "USS Valor"
shipFile = "USSValorJJ"
species = App.SPECIES_GALAXY
menuGroup =  'Fed Ships'
playerMenuGroup = 'Fed Ships'
Foundation.ShipDef.USSValorJJ = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.USSValorJJ.dTechs = {'Ablative Armour': 7500}

Foundation.ShipDef.USSValorJJ.fMaxWarp = 9.0 + 0.0001
Foundation.ShipDef.USSValorJJ.fCruiseWarp = 7.6 + 0.0001

Foundation.ShipDef.USSValorJJ.desc = "After the destruction of the Vengeance and its fall to earth, the process of removing the wreck and rebuilding the city was long and tedious, but soon the scraps of what used to be the vengeance were brought into the Earth Space Dock. Once the pieces were fully secured and locked in place, the technology and systems were gutted from the ship, leaving only the outer hull, which itself was scrapped and melted down for new ships. It took years for the technology to be reverse engineered. Well over two decades after the Vengeance incident and well after the launch of the JJverses Excelsior class ships, the technology was finally reverse engineered and fitted onto a cloned Vengeance hull. Unlike the vengeance however, this new ship was painted with a standard federation color scheme and given a registry. 'NX-3000' was given to this ship named the 'U.S.S Valor'. Because this was also a first generation prototype, the class was named the Valor class as well. The AI used on the Vengeance was upscaled and replicated, possibly not needing a crew at all. As a test, this new ship was sent to patrol the neutral zone with minimal crew. Over time, the AI started to gain more knowledge and sentience and soon killed off the crew. The Valor soon veered off course and started to target any ship in range. Before being formally engaged by the federation, the Valor had disabled or destroyed several klingon ships and federation transports. This began the JJ universes version of the M5 Computer incident. Once it was realized that the federation had lost contact with the Valor and several ships in the area, they assumed it was a klingon incursion force. They prepared three constitution class ships, two refit and the other still waiting to be refit, and two excelsior class vessels for combat, including the U.S.S Enterprise N.C.C 1701-A, the U.S.S Discovery N.C.C 1998 and the U.S.S Endeavour N.C.C-1895(not refit). They also included the U.S.S Excelsior NX-2000, and the U.S.S Achilles N.C.C-2011. The battle was long and hard fought, but in the end the Valor was destroyed. In the aftermath, the Endeavour was destroyed, the Excelsior and the Discovery were heavily damaged, and the Enterprise and Achilles were moderately damaged. The wreckage of the Valor was town back to the nearest starbase where the project was immediately terminated and the ship was dismantled. The Dreadnought/Valor class design was not destroyed however, and was later used to influence the ambassador, galaxy and sovereign classes of the JJ universe, with the weapons, hull and size tuned down a bit of course."


if menuGroup:           Foundation.ShipDef.USSValorJJ.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.USSValorJJ.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
