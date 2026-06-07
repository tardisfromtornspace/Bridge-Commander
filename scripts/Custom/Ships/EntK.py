import App
import Foundation
import traceback

abbrev = "EntK"
iconName = "EntK"
longName = "Enterprise K"
shipFile = "EntK"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed27c
	Foundation.ShipDef.EntK = Foundation.FutureFed27cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.EntK = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.EntK.desc = "The Enterprise K (N.C.C-1701-K) was designed and built in 2610 as a refit to the well known Universe class. This class would later become known as the Monarch class and was built as a flagship to the mass produced Windrunner class ships (built 2604). This ship was hastily built to fight with the Milky Way alliance in the war against the Borg and was fitted with some of the latest tech of this era, mainly being its Chronogravitometric Zero Point Beam Array, its heavy Chroniton Catalyst Launchers, Diffusive armor and shield grids and Diffusive Quantum Torpedoes. This technology had just been developed around the time the Windrunner was produced, with some of the prototype Windrunners being outfitted with Chroniton technology while the new diffusive tech was still in testing. It was used to match and diffuse the frequencies of Transphasic, Chroniton, Enyptic and Infinity Modulation technologies to render them useless against diffusive defences. \n\nLater into the Borg wars around 2612 the Enterprise K was equipped with a very small load of Diffusive Transquantic torpedoes for combat against other ships with diffusive technologies such as the Borg of the time. It was used to easily destroy borg ships with that technology, but used only in extreme circumstances to prevent assimilation. This helped drive the Borg into its near extinction. \n\nWhile not all species stayed allies after the fall of the Borg, the allies they did have would play a crucial part in the upcoming Federation/Voth wars. This war (taking place between 2639 and 2651) started out as more of a cold war type situation (from 2639 to 2646) but evolved into full out war in the next year. This war left the Federation outmatched and almost entirely disbanded by the Voth. The Enterprise K was damaged too heavily in the first years of active combat to be put back into service and was retired in early 2648. After the near destruction of the Federation, they began developing new technologies to combat the Voth, the first of which being the predecessor to temporal manipulation based technology. This led to a ceasefire in 2651 as the Voth did not have many ships to lose, and the Federation had already lost too much to easily recover. This led Starfleet to create a specific department to enhance their weapons and abilities while the main Starfleet focused on rebuilding. This new faction, which did not yet have a formal designation, started by creating a new ship out of their most advanced technology at the time. This ship came to be known as the Enterprise L (N.C.C-1701-L). This faction would also later formally be known as Timefleet when their technology began to delve into time travel and the creation of the Enterprise M as the first proto timeship."
Foundation.ShipDef.EntK.SubMenu = "27th Century"
Foundation.ShipDef.EntK.OverrideWarpFXColor = Foundation.ShipDef.EntK.OverrideWarpFXColor
Foundation.ShipDef.EntK.OverridePlasmaFXColor = Foundation.ShipDef.EntK.OverridePlasmaFXColor
Foundation.ShipDef.EntK.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'ChronitonTorpe Immune': 1,
	'Transphasic Torpedo Immune': 1,
	'Phased Torpedo Immune': 1,
	'Multivectral Shields': 25,
	"Digitizer Torpedo Immune": 1,
	'Diffusive Armor': 67500
}


if menuGroup:           Foundation.ShipDef.EntK.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EntK.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]