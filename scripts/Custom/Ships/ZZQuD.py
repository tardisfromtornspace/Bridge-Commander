import Foundation
import App
from bcdebug import debug

abbrev = 'ZZQuD'
iconName = 'ZZQuD'
longName = "ZZ DD QuD Insurrection"
shipFile = 'ZZQuD'
menuGroup = 'Klingon Ships'
playerMenuGroup = 'Klingon Ships'
species = App.SPECIES_GALAXY

credits = {'modName': 'ZZQuD', 'author': 'Zambie Zan', 'version': '1.0', 'sources': ['http://'], 'comments': 'Aug/2026'}

import F_ZZAndromedanLightDef

Foundation.ShipDef.ZZQuD = F_ZZAndromedanLightDef.ZZAndromedanLightShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.ZZQuD.desc = """The QuD (Insurrection) class is a larger variant of the B'rel class Bird of Prey, designed to fill a tactical gap in the Klingon Defense Forces. The concept was developed by Colonel Gatl'naH, a brilliant tactical mind at the Academy.\nIn 1655 IR, while running simulations of a prolonged war with the Federation, he identified a major hole in the Klingon order of battle. When Gatl'naH raised the issue with the Klingon High Council, most members dismissed the idea, arguing that the qa'HoS cruisers were sufficient and that any war with the Federation would likely be short.\nAfter the Council rejected his proposal, the undaunted Colonel secretly modified a Bird of Prey simulation and created a private destroyer variant. Impressed by the results when Gatl'naH demonstrated his concept, the Council members present immediately authorized design and construction of the new ship. It was named QuD ("Insurrection") in honor of the Colonel for forcing a change in the Council's final decision.\n\nFrequency-Modulated Meson Particle Accelerator (FMPA)\n\nAlso known as the "Meson Gun" or "Shield Breaker", the FMPA is a highly classified Klingon weapon. Only the researchers who developed it fully understand its principles.\n\n2x Photon Launchers (2f)\n2x Disruptor Cannons (2f)\n2x Heavy Disruptor Cannons (2f)\n1x FMPA Cannon (Shield Breaker)\nBy ZambieZan."""

if menuGroup:
	Foundation.ShipDef.ZZQuD.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:
	Foundation.ShipDef.ZZQuD.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
	Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
	Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

Foundation.ShipDef.ZZQuD.dTechs = {"AutoTargeting": { "Pulse": [2, 1] }}