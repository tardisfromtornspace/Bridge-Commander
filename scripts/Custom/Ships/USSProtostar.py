#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "USSProtostar"
iconName = "USSProtostar"
longName = "USS Protostar"
shipFile = "USSProtostar"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
SubMenu = 'Protostar Class'

isRaceLoaded = 0 # A value that verifies things for later
try:
	import Custom.Autoload.RaceFedProdigy
	Foundation.ShipDef.USSProtostar = Foundation.FedProdigyShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	#import Custom.Autoload.RaceCosmosASTO
	#Foundation.ShipDef.USSProtostar = Foundation.CosmosASTOShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	isRaceLoaded = 1
except:
	print "Error while loading a race"
	isRaceLoaded = 0
	Foundation.ShipDef.USSProtostar = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	traceback.print_exc()


"""
# Let's do some calculations:
# 9.97 warp is the default the USS Protostar could get from normal warp, and going at that speed, it would have taken 4 years for X distance
# Proto-warp would take a few minutes - let's say 5 minutes - for that same X distance.
# Thus, we know protowarp is 4 * 365 * 24 *3600 / (5 * 60) = (4 * 365 * 8 * 36) = 420480 times faster
# From LibWarp, the warp scale used in-game:
# fFac = exp(-2.82 + 3.21*fSpeed - 0.41*fSpeed**2 + 0.02*fSpeed**3) + 1
# fTime = fDist / fFac
# this means that:
# # For fSpeed = 9.97
# ## fFac = exp(-2.82 + 3.21*9.97 - 0.41*9.97**2 + 0.02*9.97**3) + 1 = 3828.1300229046033
# # For some reason the in-game scale is a weird combo between TNG scale with limit at warp 10, and cannot actually cover certain speeds between warp 9.97 and warp 10 (in fact for warp 10 it would tend to a factor of 3945.19438198031 which is not even twice the in-game warp 9.97 factor but once reaching warp 10 and beyond the game just does 10^50). This means that past a certain limit the game will either make the fFac we want give far more speed or far less speed than canonically wanted.
# # For proto-warp, since fFac is 420480 times faster than for warp 9.97, then we just replace the proper variables and solve a third degree equation and we will get the factors from the in-game scale, without forgetting to pick up the only real positive solution:
# ## fFacProto = 3828.1300229046033 * 420480 - 1 = e ^ (-2.82 + 3.21*fSpeed - 0.41*fSpeed^2 + 0.02*fSpeed^3) =>
# ## ln(3828.1300229046033 * 420480 - 1) + 2.82 = 3.21*fSpeed - 0.41*fSpeed^2 + 0.02*fSpeed^3 =>
# ## 0.02*fSpeed^3 - 0.41*fSpeed^2 + 3.21*fSpeed -24.0192839124891 = 0 => For real positive numbers, fSpeed = 15.13829 aproximately.
# ## This is certainly above the canon TNG warp 10 threshold, but still sticks to the formula, with "exp(-2.82 + 3.21*fSpeed - 0.41*fSpeed**2 + 0.02*fSpeed**3) + 1" when fSpeed = 15.13829 giving us approximately 420480 times the factor obtained from warp 9.97
# So the final document fix would be this:
# If the in-game scale is not changed, then the Protostar having warp 10 or warp 15 would not matter. For game purposes the proto-warp version would still need to have a transwarp warp factor.
# If the in-game scale is changed to allow beyond warp 10 values without automatically jumping to 10^50, it would keep all other warp values others used without changing their warp speed times (specially for those mods where the TOS warp factor scale was used) and then warp 15.13829 would fit best, even if canonically that would make you travel back in time. For game purposes the proto-warp version would still need to have a transwarp warp factor.
# If the in-game scale is appropiately corrected to support corect near-warp-10 scale tending towards infinity, it would allow all ships to behave more canonically, and without really needing to change the warp scale, it would be more likely for the USS Protostar to have a Warp factor of 9.99 or slightly higher, while some high-warp vessels would need to have their warp factors modified.
# OR, on this case, we can resort to GalaxyCharts and just create an alternative warp method which multiplies regular warp factor by 420480.
"""

Foundation.ShipDef.USSProtostar.fMaxWarp = 9.97 + 0.0001
Foundation.ShipDef.USSProtostar.fCruiseWarp = 9.96 + 0.0001

Foundation.ShipDef.USSProtostar.dTechs = {
	"Polarized Hull Plating": {"Plates": ["Hull"]},
	"Proto-Warp": {
		"Setup": {
			"Nacelles": ["Proto Warp Nacelle"],
			"Core": ["Proto-Core"],
			"Body": "VasKholhr_Body",
			"NormalModel":          shipFile,
			"WarpModel":          "VasKholhr_WingUp",
			"Proto-WarpModel":          "VasKholhr_WingUp",
			"AttackModel":          "VasKholhr_WingDown",
			"Hardpoints":       {
				"Proto Warp Nacelle":  [0.000000, 0.000000, 0.075000],
			},

			"AttackHardpoints":       {
				"Proto Warp Nacelle":  [0.000000, -0.250000, 2.075000],
			},
			"WarpHardpoints":       {
				"Proto Warp Nacelle":  [0.000000, -0.250000, -2.075000],
			},
			"ProtoWarpHardpoints":       {
				"Proto Warp Nacelle":  [0.000000, -1.000000, -2.075000],
			},
		},

		"Port Wing":     ["VasKholhr_Portwing", {
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"AttackRotation":         [0, -0.6, 0],
			"AttackDuration":         200.0, # Value is 1/100 of a second
			"AttackPosition":         [0, 0, 0.03],
			"WarpRotation":       [0, 0.349, 0],
			"WarpPosition":       [0, 0, 0.02],
			"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0.349, 0],
			"Proto-WarpPosition":       [0, 0, 0.02],
			"Proto-WarpDuration":       150.0,
			},
		],
        
		"Starboard Wing":     ["VasKholhr_Starboardwing", {
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			"AttackRotation":         [0, 0.6, 0],
			"AttackDuration":         200.0, # Value is 1/100 of a second
			"AttackPosition":         [0, 0, 0.03],
			"Proto-WarpRotation":       [0, -0.349, 0],
			"Proto-WarpPosition":       [0, 0, 0.02],
			"Proto-WarpDuration":       150.0,
			},
		],
	},
} # TO-DO ADD SUBMODELS

Foundation.ShipDef.USSProtostar.desc = "The Protostar-class was a small starship class launched by Starfleet during the late 24th century that was later approved for full production in 2384 after the destruction of the prototype and namesake vessel, the USS Protostar. Unlike other Starfleet ships, the Protostar class had its navigational deflector mounted on the underside of the saucer instead of the engineering hull, which instead has a large loading ramp for entrance into the vessel. When it was developed, the Protostar class was the fastest ship in Starfleet. The class featured two distinct warp drive modes, one was a conventional warp drive capable of warp 9.97 and powered by twin warp cores, while the other was a more energy-intensive gravimetric protostar containment, which was powered by a protostar and allowed it to travel in a second warp drive mode considerably faster than conventional warp speed, crossing over four thousand light years in a matter of minutes, a journey that would originally take four years at maximum warp, but which would require rapid energy regeneration protocols after at least 2 uses.\nThe USS Protostar (NX-76884) was a Protostar-class Federation starship launched in 2382. The Protostar was launched from the San Francisco Fleet Yards on Stardate 59749.1 under the command of Captain Chakotay for a return mission to the Delta Quadrant undertaken in the years after the return of the USS Voyager. "


if menuGroup:           Foundation.ShipDef.USSProtostar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.USSProtostar.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
