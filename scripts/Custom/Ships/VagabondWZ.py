from bcdebug import debug
import Foundation
import App

abbrev = 'VagabondWZ'
iconName = 'VagabondWZ'
longName = 'CH Vagabond Class'
shipFile = 'VagabondWZ'
menuGroup = 'Orion Pirates Ships'
playerMenuGroup = 'Orion Pirates Ships'
SubMenu = "ZZ Orions"
species = App.SPECIES_GALAXY

# Credits and mod information.
credits = {
	'modName': 'VagabondWZ',
	'author': 'Zambie Zan alexmarques400@hotmail.com',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': 'Tested in KM'
}


import K_ZZAndromedanAttackDef

Foundation.ShipDef.VagabondWZ = K_ZZAndromedanAttackDef.ZZAndromedanShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.VagabondWZ.desc = """Even though war often distracts empires from the nuisance of piracy, some governments still manage to find time to devote to eradicating threats to their supply lines. By the mid-23rd century, many pirate cartels found themselves increasingly outgunned and outclassed by the warships of the Klingons, Romulans and Federation, with the other empires gaining steady advantages. Not ready to concede defeat or flee to less defended (and less profitable) parts of space, the Orions sought to develop new and improved starships to counter those being fielded by the empires. In typical Orion fashion, the main shipyards of the Orion systems began construction of a new class of what was officially named a “heavy cargo transport”. One look at the blueprints for this vessel, however, would clearly show that it had the capability to be far more than a mere freighter.

A refined evolution of the successful raiders used during the General War, the Vagabond class continued the tradition of versatile, rugged and heavily upgradable starships that the Orions were so well known for. Taking cues from the Lyrans and Romulans, the Vagabond incorporated modular construction to allow for more customizable options and hull configurations. “Extra” cargo space could easily be used to install additional weapons and systems, while stock propulsion units had plenty of leeway for enhancements or total replacement. Due to such customizability, it was rare to encounter two Vagabond class ships of the same configuration, and those that were similar were often from the same cartel. With such potential for change, many cartel leaders opted to simply upgrade their flagships despite having the option to purchase more modern alternatives or ships of heavier hull class. These ships would be modified over the years to the point that many could scarcely be identified as being a Vagabond, causing the databases of patrol ships to flag them as “unknowns”.

One of the more common variants fielded by the cartels typically came equipped with nine phaser banks, four dual disruptor turrets, ten missile tubes and quad-impulse drives. A popular alteration was to convert the forward cargo hold into a dedicated launch bay, adding fighters and attack craft to the Vagabond’s arsenal. Most versions tended to keep the internal bridge for added command safety as well as the externally mounted cooling vanes and aft shuttle bay. Many of these ships were equipped with advanced sensor dampening systems and highly accurate scanning hardware along with powerful tractor beams and long-range transporters for detecting and capturing defenseless merchants.

With such versatility and customization, the Vagabond was a common site in the hands of pirates, mercenaries, privateers, freelancers and even privately-owned corporations for decades after its introduction. The Orions fielded other ships based on the Vagabond design but none of them became quite as popular or successful, despite being just as capable as the ship that spawned them."""

Foundation.ShipDef.VagabondWZ.dTechs = {
	"Slow Start": {"Pulses": [], "Torpedoes": [], "TorpedoesFactor": 0.8, "GlobalFactor": 0.6}
}

if menuGroup:
	Foundation.ShipDef.VagabondWZ.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:
	Foundation.ShipDef.VagabondWZ.RegisterQBPlayerShipMenu(playerMenuGroup)

# Handle potential conflicts if the ship already exists in the list.
if Foundation.shipList._keyList.has_key(longName):
	Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
	Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def PreLoadAssets():
    pass
