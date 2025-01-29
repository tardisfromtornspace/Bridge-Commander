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

"""
* TO-DOs:
** Create models for the Protowarp version and the Submodels for the parts (also check if the ported model has those parts).
*** You need several models (update Custom ships file accordingly):
**** Final Protowarp model.
**** port nacelle (without pylon) - moves Z downward
**** starboard nacelle (without pylon) - moves Z downward
**** port pylon (also includes a part of the lower hull) rotates Y axis to below its normal position.
**** star pylon (also includes a part of the lower hull) rotates Y axis to below its normal position.
**** central pylon (maybe also contains proto-core) - moves on the X axis backwards. By default it is stored on the limit between dish and body.
**** central pylon upper part (which covers the grey middle central upper area between dish and body) - moves on X backwards and Z up.
**** central pylon lower part (which covers the grey middle central lower area between dish and body) - moves on X backwards and Z down.
**** central pylon upper part 2 (which covers the grey middle central upper area between dish and body) - moves on X backwards and Z up.
**** central pylon lower part 2 (which covers the grey middle central lower area between dish and body) - moves on X backwards and Z down.
**** then the body upper part and lower part bifurcates into six pieces that rotate and then move on the X and Y axis to hide themselves to allow the central pylon to move
***** the two upper ones rotate on the Y axis.
***** the two middle ones open on the X axis.
***** The two lower ones just move on the Y axis forward.
**** port dish coverage, covers some of the area the port pylon left behind - moves on Y axis backwards and X to port.
**** star dish coverage, covers some of the area the star pylon left behind - moves on Y axis backwards and X to star.
* Update Protostar's Custom ships file so it moves the hardpoints to a correct spot, including the Proto-Core (use the ModelPropertyEditor for this)
"""

Foundation.ShipDef.USSProtostar.dTechs = {
	"Polarized Hull Plating": {"Plates": ["Hull"]},
	"Alternate-Warp-FTL": {
		"Setup": {
			"Proto-Warp": {	"Nacelles": ["Proto Warp Nacelle"], "Core": ["Proto-Core"], },
			"Body": shipFile, #"USSProtostarBody",  
			"NormalModel":          shipFile,
			"WarpModel":          shipFile,
			"Proto-WarpModel":          shipFile, #"USSProtostarProtoWarp",
			"AttackModel":          shipFile, # TO-DO COMMENT AND FIX THE OTHERS
			"BodySetScale": 1.0,
			"NormalSetScale": 1.0,
			#"WarpSetScale": 1.0,
			"Proto-WarpSetScale": 1.0,
			#"AttackSetScale": 1.0,
			"Hardpoints":       {
				"Proto Warp Nacelle":  [0.000000, 0.000000, 0.075000],
				"Port Warp": [-0.270000, -0.250000, 0.075000],
				"Star Warp": [-0.270000, -0.250000, 0.075000],
			},

			#"AttackHardpoints":       {
			#	"Proto Warp Nacelle":  [0.000000, -0.250000, 2.075000],
			#},
			#"WarpHardpoints":       {
			#	"Proto Warp Nacelle":  [0.000000, -0.250000, -2.075000],
			#},
			"Proto-WarpHardpoints":       {
				"Proto Warp Nacelle":  [0.000000, -1.000000, -2.075000],
				"Port Warp": [-0.300000, -0.250000, 0.005000],
				"Star Warp": [-0.300000, -0.250000, 0.005000],
			},
		},
		"""
		"Port Pylon":     ["USSProtostarPP", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			#"AttackRotation":         [0, -0.6, 0],
			#"AttackDuration":         200.0, # Value is 1/100 of a second
			#"AttackPosition":         [0, 0, 0.03],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, 0, 0.001],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, -0.3, 0],
			"Proto-WarpPosition":       [0, 0, -0.01],
			"Proto-WarpDuration":       150.0,
			},
		],
        
		"Starboard Pylon":     ["USSProtostarSP", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			#"AttackRotation":         [0, 0.6, 0],
			#"AttackDuration":         200.0, # Value is 1/100 of a second
			#"AttackPosition":         [0, 0, 0.03],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, 0, 0.001],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0.3, 0],
			"Proto-WarpPosition":       [0, 0, -0.01],
			"Proto-WarpDuration":       150.0,
			},
		],

		"Port PylonP":     ["USSProtostarPDC", { # TO-DO These two parts below are for a model that has some inaccuracies, if we find a better model or make one ourselves, adjust accordingly. Among these, the commented parts below should be addressed, and the two parts immadiately below should be removed/fused with the port and starboard pylons
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			#"AttackRotation":         [0, -0.6, 0],
			#"AttackDuration":         200.0, # Value is 1/100 of a second
			#"AttackPosition":         [0, 0, 0.03],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, 0, 0.001],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, -0.3, 0],
			"Proto-WarpPosition":       [0, 0, -0.01],
			"Proto-WarpDuration":       150.0,
			},
		],
		"Starboard PylonP":     ["USSProtostarSDC", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			#"AttackRotation":         [0, 0.6, 0],
			#"AttackDuration":         200.0, # Value is 1/100 of a second
			#"AttackPosition":         [0, 0, 0.03],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, 0, 0.001],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0.3, 0],
			"Proto-WarpPosition":       [0, 0, -0.01],
			"Proto-WarpDuration":       150.0,
			},
		],
		"""
		"Port Nacelle":     ["USSProtostarPN", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0.265, -0.36, 0.075],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			#"AttackRotation":         [0, -0.6, 0.5],
			#"AttackDuration":         200.0, # Value is 1/100 of a second
			"AttackPosition":       [0.265, -0.36, -0.1],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, 0, 0.001],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [0.265, -0.36, -0.1],
			"Proto-WarpDuration":       150.0,
			},
		],
		"Starboard Nacelle":     ["USSProtostarSN", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [-0.265, -0.36, 0.075],
			"Rotation":             [0, 0, 0],
			#"AttackRotation":         [0, 0.6, 0.1],
			#"AttackDuration":         200.0, # Value is 1/100 of a second
			"AttackPosition":       [-0.265, -0.36, -0.1],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, 0, 0.001],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [-0.265, -0.36, -0.1],
			"Proto-WarpDuration":       150.0,
			},
		],


		"Central NacelleU":     ["USSProtostarCNU", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, -0.078, -0.022],
			"Rotation":             [0, 0, 0],
			"AttackPosition":       [0, -0.34, 0.012],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [0, -0.34, 0.012],
			"Proto-WarpDuration":       250.0,
			"Proto-WarpDelayEntry":       0.15,
			},
		],
		"Central NacelleD":     ["USSProtostarCND", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, -0.078, -0.042],
			"Rotation":             [0, 0, 0],
			"AttackPosition":       [0, -0.34, -0.07],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [0, -0.34, -0.07],
			"Proto-WarpDuration":       300.0,
			"Proto-WarpDelayEntry":       0.15,
			},
		],

		
		"Central Nacelle":     ["USSProtostarCN", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0.052, -0.02],
			"Rotation":             [0, 0, 0],
			"AttackPosition":       [0, -0.1, -0.02],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [0, -0.1, -0.02],
			"Proto-WarpDuration":       250.0,
			"Proto-WarpDelayEntry":       0.15,
			},
		],

		"Starboard Central Body":     ["USSProtostarSD", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [-0.025, -0.16, -0.015],
			"Rotation":             [0, 0, 0],
			"AttackPosition":       [-0.08, -0.15, -0.015],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [-0.10, -0.15, -0.015],
			"Proto-WarpDuration":       150.0,
			"Proto-WarpDelayExit":       0.25,
			},
		],
		"Port Central Body":     ["USSProtostarPD", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0.025, -0.16, -0.015],
			"Rotation":             [0, 0, 0],
			"AttackPosition":       [0.08, -0.15, -0.015],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [0.08, -0.15, -0.015],
			"Proto-WarpDuration":       150.0,
			"Proto-WarpDelayExit":       0.25,
			},
		],
	},
}

"""
		# Central NacelleD and Central NacelleU are accompanied by these rotating parts, which can be simulated by the parts themselves being partly hidden by the main protowarp core part.
		"Central NacelleU1":     ["USSProtostarCN", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [0, -1.0, 0.05],
			"Proto-WarpDuration":       250.0,
			},
		],
		"Central NacelleD1":     ["USSProtostarCN", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [0, -1.0, -0.05],
			"Proto-WarpDuration":       250.0,
			},
		],

		# Four plates that cover the protocore up and down when inactive, they fold upwards (downwards for the "D" parts) when engaging protowarp
		"S Central Body U":     ["USSProtostarSD", {
			"Experimental": 1,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, -0.7, 0],
			"Proto-WarpPosition":       [-0.5, 0.0, 0],
			"Proto-WarpDuration":       150.0,
			},
		],
		"S Central Body D":     ["USSProtostarCN", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [-0.5, 0.3, -0.1],
			"Proto-WarpDuration":       150.0,
			},
		],
		"P Central Body U":     ["USSProtostarPD", {
			"Experimental": 1,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0.7, 0],
			"Proto-WarpPosition":       [0.5, 0.0, 0],
			"Proto-WarpDuration":       150.0,
			},
		],
		"P Central Body D":     ["USSProtostarCN", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0.7, 0],
			"Proto-WarpPosition":       [0.5, 0.3, -0.1],
			"Proto-WarpDuration":       150.0,
			},
		],

		# These parts cover a hole on the model
		"S Dish Cover":     ["USSProtostarSDC", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [-0.5, -0.3, 0],
			"Proto-WarpDuration":       250.0,
			},
		],
		"P Dish Cover":     ["USSProtostarPDC", {
			"Experimental": 0,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0],
			#"WarpRotation":       [0, 0, 0],
			#"WarpPosition":       [0, -0.01, 0],
			#"WarpDuration":       150.0,
			"Proto-WarpRotation":       [0, 0, 0],
			"Proto-WarpPosition":       [0.5, -0.3, 0],
			"Proto-WarpDuration":       250.0,
			},
		],

"""

Foundation.ShipDef.USSProtostar.desc = "The USS Protostar (NX-76884) was the first Protostar-class Federation starship launched in 2382. The Protostar was launched from the San Francisco Fleet Yards on Stardate 59749.1 under the command of Captain Chakotay for a return mission to the Delta Quadrant undertaken in the years after the return of the USS Voyager.\nThe Protostar-class was a small starship class launched by Starfleet during the late 24th century that was later approved for full production in 2384.\nWhen it was developed, the Protostar class was the fastest ship in Starfleet, due to its main feature: two distinct warp drive modes, one, a conventional warp drive capable of warp 9.97 and powered by twin warp cores; the other, a more energy-intensive gravimetric protostar containment, which was powered by a protostar and allowed considerably faster travel speed than conventional warp speed. Such was proto-warp, that it could cross over four thousand light years, a journey that would have taken 4 years at conventional maximum warp 9.97, in a matter of minutes. Due to the proto-core's energy requirements, rapid energy regeneration protocols were needed to be performed after at least 2 consecutive proto-warp uses.\nUnlike other Starfleet ships, the Protostar class had its navigational deflector mounted on the underside of the saucer instead of the engineering hull, which instead has a large loading ramp for entrance into the vessel. Also an oddity amongst Federation vessels of the time, is that the ship was equipped with polarized hull plating as part of its main defences.\nTactical-wise, its shields are not the best, but it is fast and nimble and carries an acceptable weapons array."


if menuGroup:           Foundation.ShipDef.USSProtostar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.USSProtostar.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
