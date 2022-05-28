# by USS Sovereign, DS9FXComet cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'DS9FXComet'
iconName = 'DS9FXComet'
longName = 'DS9FXComet'
shipFile = 'DS9FXComet' 
species = App.SPECIES_GALAXY

# Ship foundation def
Foundation.ShipDef.DS9FXComet = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.DS9FXComet.desc = "Comets are small, fragile, irregularly shaped bodies composed of a mixture of non-volatile grains and frozen gases. They have highly elliptical orbits that bring them very close to the systems Sun and swing them deeply into space.\n\nComet structures are diverse and very dynamic, but they all develop a surrounding cloud of diffuse material, called a coma, that usually grows in size and brightness as the comet approaches a Sun. Usually a small, bright nucleus (less than 10 km in diameter) is visible in the middle of the coma. The coma and the nucleus together constitute the head of the comet.\n\nAs comets approach a Sun they develop enormous tails of luminous material that extend for millions of kilometers from the head, away from a Sun. When far from a Sun, the nucleus is very cold and its material is frozen solid within the nucleus. In this state comets are sometimes referred to as a \"dirty iceberg\" or \"dirty snowball,\" since over half of their material is ice. When a comet approaches within a few AU of a Sun, the surface of the nucleus begins to warm, and volatiles evaporate. The evaporated molecules boil off and carry small solid particles with them, forming the comet's coma of gas and dust.\n\nWhen the nucleus is frozen, it can be seen only by reflected sunlight. However, when a coma develops, dust reflects still more sunlight, and gas in the coma absorbs ultraviolet radiation and begins to fluoresce. At about 5 AU from a Sun, fluorescence usually becomes more intense than reflected light.\n\nAs the comet absorbs ultraviolet light, chemical processes release hydrogen, which escapes the comet's gravity, and forms a hydrogen envelope.\n\nA Sun's radiation pressure and solar wind accelerate materials away from the comet's head at differing velocities according to the size and mass of the materials. Thus, relatively massive dust tails are accelerated slowly and tend to be curved. The ion tail is much less massive, and is accelerated so greatly that it appears as a nearly straight line extending away from the comet opposite the systems Sun."

Foundation.ShipDef.DS9FXComet.fCrew = "Off"

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

