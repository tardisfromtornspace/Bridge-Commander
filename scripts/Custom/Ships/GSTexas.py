#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation

abbrev = "GSTexas"
iconName = "GSTexas"
longName = "Texas Class"
shipFile = "GSTexas"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.GSTexas = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})


Foundation.ShipDef.GSTexas.desc = "The Texas class was a type of Federation starship briefly operated by Starfleet in the late 24th century. Commissioned by Vice Admiral Les Buenamigo in a misguided effort to compete with other Starfleet flag officers, it was the organization's first fully automated starship. All three vessels of the class malfunctioned and became unhinged due to faulty artificial intelligence, resulting in Buenamigo's death when he lost control of the USS Aledo and a subsequent attack on Douglas Station that ultimately led to the deranged vessels being destroyed by vessels of the California-class.\n\nThe development of the Texas class began in the 2370s as a classified project headed by Lieutenant Commander Les Buenamigo. Buenamigo recruited Sam Rutherford, a first-year Starfleet Academy cadet, to code the artificial intelligence for the prototype ship and who also contributed technical designs. However, Rutherford was severely injured by the accidental explosion of the Sampaguita, his personal racing ship that he had been constructing. To preserve the secrecy of the Texas class, Buenamigo ordered Rutherford to be fitted with a cybernetic implant that would suppress all his memories of working on the project and Buenamigo himself, who did not care that this would severely alter the cadet to a different personality.\n\nIn 2381, the first three Texas-class vessels were ready for deployment. Buenamigo, now a vice admiral, intended to have them supplant the California-class on second contact missions, which he hoped would advance his career. To promote his new ships, he schemed to have the USS Cerritos enter a situation that would highlight its inadequacy and allow the Texas class to save the day in dramatic fashion. His first attempt failed when Captain Carol Freeman was able to salvage negotiations with the Karemma on Deep Space 9 that Buenamigo had sprung on her at the last minute, but his chance came when Freeman was assigned to Project Swing By, during which time he directed the Cerritos to Brekka, knowing beforehand that the planet had been occupied by the Breen.\n\nBuenamigo sent the USS Aledo to assist the Cerritos when it was in combat with three Breen interceptors in the Delos system. There was some initial confusion among the Cerritos crew, as they did not immediately recognize the ship, however, the Aledo was successful in destroying all three enemy combatants, the last one on a collision course with the Cerritos. With the success of this mission, Buenamigo confidently told Freeman that the Aledo had passed its sea trials.\n\nDue to this and the expose revealing the misadventures on the Cerritos, Starfleet Command had decided to have the California-class line set to be decommissioned. However, Freeman hastily declared a mission race to prove the class' worth. The Aledo won the contest, but when Ensign D'Vana Tendi realized the ship broke the Prime Directive by not scanning for life forms again on the planet LT-358, Freeman attempted to convince him that his ships were unfit for duty.\n\nAdding to the troubles, Rutherford, now serving on the Cerritos, realized that the AI on the ships was based on the same type of AI he used to later create Badgey, a hologram who developed patricidal impulses and attempted to murder him the moment he was freed from the holodeck's safety protocols, and, realizing the Aledo had likely malfunctioned in the same fashion, hurriedly warned Freeman of the danger. Realizing they knew the truth and heedless of Rutherford's warning that the vessels were emotionally unstable, Buenamigo gave the Aledo full autonomy and ordered the ship to destroy the Cerritos under the assumption that it fell to enemy hands. However, the ship refused and told its father it no longer took orders from him, locking out the admiral from its systems before killing him. It proceeded to activate its sister ships, USS Dallas and USS Corpus Christi and began to ravage Douglas Station. The trio overpowered the Sovereign-class USS Van Citters before the Cerritos lured the ships away using Rutherford as bait. As this was happening, former Ensign Beckett Mariner, who had resigned from Starfleet in the run-up to the incident and was now serving on the Free Spirit alongside Petra Aberdeen as an archaeologist, viewed an FNN report on the rampage and immediately chose to intervene.\n\nWith the aid of Brad Boimler, Freeman allowed Lieutenant Shaxs to eject the warp core to destroy their pursuers; however, the Aledo survived with minor damage and attacked the helpless ship. The arrival of the Free Spirit, along with the entire fleet of California-class ships saved the Cerritos, destroying the Aledo under a hail of phaser fire."
Foundation.ShipDef.GSTexas.fMaxWarp = 15.0
Foundation.ShipDef.GSTexas.fCruiseWarp = 10
Foundation.ShipDef.GSTexas.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Multivectral Shields': 5
}

if menuGroup:           Foundation.ShipDef.GSTexas.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.GSTexas.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
