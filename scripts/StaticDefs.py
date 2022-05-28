from bcdebug import debug
# Foundation plugin system
# March 2002
# Written by Dasher42


# Editing this file is discouraged, and distributing modified versions of this doubly so!
# It will break compatibility with future releases of Foundation, quite likely break other
# mods, and result in discouraged and frustrated users.  Don't do it!

# Mod developers:  If you want something different from this file, make a copy of it,
# and distribute a Plugins.py with your mod that imports the copy instead of the original
# StaticDefs.py.  This file is distributed in .PY form for you to look at and learn from if
# you wish, mostly.


import Foundation

import App
# App = Foundation.DummyApp()

Foundation.ShipDef('Unknown', App.SPECIES_UNKNOWN, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )	# Just a placeholder, really.

Foundation.ShipDef.Galaxy = Foundation.GalaxyDef('Galaxy', App.SPECIES_GALAXY, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Galaxy.RegisterQBShipMenu('Fed Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Galaxy.RegisterQBPlayerShipMenu('Fed Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.Galaxy.friendlyDetails[2] = 'QBFriendlyGalaxyDestroyed'
Foundation.ShipDef.Galaxy.enemyDetails[2] = 'QBEnemyGalaxyDestroyed'

Foundation.ShipDef.Sovereign = Foundation.SovereignDef('Sovereign', App.SPECIES_SOVEREIGN, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Sovereign.RegisterQBShipMenu('Fed Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Sovereign.RegisterQBPlayerShipMenu('Fed Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.Sovereign.friendlyDetails[2] = 'QBFriendlySovereignDestroyed'
Foundation.ShipDef.Sovereign.enemyDetails[2] = 'QBEnemySovereignDestroyed'

Foundation.ShipDef.Akira = Foundation.FedShipDef('Akira', App.SPECIES_AKIRA, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Akira.RegisterQBShipMenu('Fed Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Akira.RegisterQBPlayerShipMenu('Fed Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.Akira.friendlyDetails[2] = 'QBFriendlyAkiraDestroyed'
Foundation.ShipDef.Akira.enemyDetails[2] = 'QBEnemyAkiraDestroyed'

Foundation.ShipDef.Ambassador = Foundation.FedShipDef('Ambassador', App.SPECIES_AMBASSADOR, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Ambassador.RegisterQBShipMenu('Fed Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Ambassador.RegisterQBPlayerShipMenu('Fed Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.Ambassador.friendlyDetails[2] = 'QBFriendlyAmbassadorDestroyed'
Foundation.ShipDef.Ambassador.enemyDetails[2] = 'QBEnemyAmbassadorDestroyed'

Foundation.ShipDef.Nebula = Foundation.FedShipDef('Nebula', App.SPECIES_NEBULA, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Nebula.RegisterQBShipMenu('Fed Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Nebula.RegisterQBPlayerShipMenu('Fed Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.Nebula.friendlyDetails[2] = 'QBFriendlyNebulaDestroyed'
Foundation.ShipDef.Nebula.enemyDetails[2] = 'QBEnemyNebulaDestroyed'

Foundation.ShipDef.Shuttle = Foundation.ShipDef('Shuttle', App.SPECIES_SHUTTLE, { 'modes': [ Foundation.MutatorDef.StockShips ], 'iconName': 'FedShuttle', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Shuttle.RegisterQBShipMenu('Other Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Shuttle.RegisterQBPlayerShipMenu('Other Ships', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.Transport = Foundation.ShipDef('Transport', App.SPECIES_TRANSPORT, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Transport.RegisterQBShipMenu('Other Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Transport.RegisterQBPlayerShipMenu('Other Ships', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.Freighter = Foundation.ShipDef('Freighter', App.SPECIES_FREIGHTER, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Freighter.RegisterQBShipMenu('Other Ships', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.Galor = Foundation.CardShipDef('Galor', App.SPECIES_GALOR, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Galor.RegisterQBShipMenu('Card Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Galor.RegisterQBPlayerShipMenu('Card Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.Galor.friendlyDetails[2] = 'QBFriendlyGalorDestroyed'
Foundation.ShipDef.Galor.enemyDetails[2] = 'QBEnemyGalorDestroyed'

Foundation.ShipDef.Keldon = Foundation.CardShipDef('Keldon', App.SPECIES_KELDON, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Keldon.RegisterQBShipMenu('Card Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Keldon.RegisterQBPlayerShipMenu('Card Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.Keldon.friendlyDetails[2] = 'QBFriendlyKeldonDestroyed'
Foundation.ShipDef.Keldon.enemyDetails[2] = 'QBEnemyKeldonDestroyed'

Foundation.ShipDef.CardFreighter = Foundation.ShipDef('CardFreighter', App.SPECIES_CARDFREIGHTER, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Card Freighter', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.CardFreighter.RegisterQBShipMenu('Card Ships', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.CardHybrid = Foundation.CardShipDef('CardHybrid', App.SPECIES_CARDHYBRID, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Card Hybrid', 'iconName':'Hybrid', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.CardHybrid.RegisterQBShipMenu('Card Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.CardHybrid.RegisterQBPlayerShipMenu('Card Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.CardHybrid.friendlyDetails[2] = 'QBFriendlyCardHybridDestroyed'
Foundation.ShipDef.CardHybrid.enemyDetails[2] = 'QBEnemyCardHybridDestroyed'

Foundation.ShipDef.Warbird = Foundation.RomulanShipDef('Warbird', App.SPECIES_WARBIRD, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Warbird.RegisterQBShipMenu('Romulan Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Warbird.RegisterQBPlayerShipMenu('Romulan Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.Warbird.friendlyDetails[2] = 'QBFriendlyWarbirdDestroyed'
Foundation.ShipDef.Warbird.enemyDetails[2] = 'QBEnemyWarbirdDestroyed'

Foundation.ShipDef.BirdOfPrey = Foundation.KlingonShipDef('BirdOfPrey', App.SPECIES_BIRD_OF_PREY, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'BOP', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.BirdOfPrey.RegisterQBShipMenu('Klingon Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.BirdOfPrey.RegisterQBPlayerShipMenu('Klingon Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.BirdOfPrey.friendlyDetails[2] = 'QBFriendlyBOPDestroyed'
Foundation.ShipDef.BirdOfPrey.enemyDetails[2] = 'QBEnemyBOPDestroyed'

Foundation.ShipDef.Vorcha = Foundation.KlingonShipDef('Vorcha', App.SPECIES_VORCHA, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Vorcha.RegisterQBShipMenu('Klingon Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Vorcha.RegisterQBPlayerShipMenu('Klingon Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.Vorcha.friendlyDetails[2] = 'QBFriendlyVorchaDestroyed'
Foundation.ShipDef.Vorcha.enemyDetails[2] = 'QBEnemyVorchaDestroyed'

Foundation.ShipDef.KessokHeavy = Foundation.KessokShipDef('KessokHeavy', App.SPECIES_KESSOK_HEAVY, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Kessok Heavy', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.KessokHeavy.RegisterQBShipMenu('Kessok Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.KessokHeavy.RegisterQBPlayerShipMenu('Kessok Ships', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.KessokLight = Foundation.KessokShipDef('KessokLight', App.SPECIES_KESSOK_LIGHT, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Kessok Light', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.KessokLight.RegisterQBShipMenu('Kessok Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.KessokLight.RegisterQBPlayerShipMenu('Kessok Ships', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.KessokMine = Foundation.KessokShipDef('KessokMine', App.SPECIES_KESSOKMINE, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Kessok Mine', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.KessokMine.RegisterQBShipMenu('Other Ships', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.Marauder = Foundation.FerengiShipDef('Marauder', App.SPECIES_MARAUDER, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Marauder.RegisterQBShipMenu('Ferengi Ships', mode = Foundation.MutatorDef.StockShips)
Foundation.ShipDef.Marauder.RegisterQBPlayerShipMenu('Ferengi Ships', mode = Foundation.MutatorDef.StockShips)
# Revise the destroyed message
Foundation.ShipDef.Marauder.friendlyDetails[2] = 'QBFriendlyMarauderDestroyed'
Foundation.ShipDef.Marauder.enemyDetails[2] = 'QBEnemyMarauderDestroyed'

Foundation.ShipDef.FedOutpost = Foundation.StarBaseDef('FedOutpost', App.SPECIES_FED_OUTPOST, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Fed Outpost', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.FedOutpost.RegisterQBShipMenu('Bases', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.FedStarbase = Foundation.StarBaseDef('FedStarbase', App.SPECIES_FED_STARBASE, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Fed Starbase',  'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.FedStarbase.RegisterQBShipMenu('Bases', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.CardStarbase = Foundation.CardStarBaseDef('CardStarbase', App.SPECIES_CARD_STARBASE, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Card Starbase', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.CardStarbase.RegisterQBShipMenu('Bases', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.CardOutpost = Foundation.CardStarBaseDef('CardOutpost', App.SPECIES_CARD_OUTPOST, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Card Outpost', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.CardOutpost.RegisterQBShipMenu('Bases', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.CardStation = Foundation.CardStarBaseDef('CardStation', App.SPECIES_CARD_STATION, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Card Station', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.CardStation.RegisterQBShipMenu('Bases', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.Drydock = Foundation.StarBaseDef('DryDock', App.SPECIES_DRYDOCK, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Dry Dock', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Drydock.RegisterQBShipMenu('Bases', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.SpaceFacility = Foundation.StarBaseDef('SpaceFacility', App.SPECIES_SPACE_FACILITY, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Space Facility', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.SpaceFacility.RegisterQBShipMenu('Bases', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.CommArray = Foundation.StarBaseDef('CommArray', App.SPECIES_COMMARRAY, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Comm Array', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.CommArray.RegisterQBShipMenu('Other Ships', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.CommLight = Foundation.ShipDef('CommLight', App.SPECIES_COMMLIGHT, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Comm Light', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.CommLight.RegisterQBShipMenu('Other Ships', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.Probe = Foundation.ShipDef('Probe', App.SPECIES_PROBE, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )

Foundation.ShipDef.ProbeType2 = Foundation.ShipDef('ProbeType2', App.SPECIES_PROBETYPE2, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )

Foundation.ShipDef.Asteroid = Foundation.ShipDef('Asteroid', App.SPECIES_ASTEROID, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.Asteroid.RegisterQBShipMenu('Other Ships', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.SunBuster = Foundation.ShipDef('Sunbuster', App.SPECIES_SUNBUSTER, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Sun Buster', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.SunBuster.RegisterQBShipMenu('Other Ships', mode = Foundation.MutatorDef.StockShips)

Foundation.ShipDef.EscapePod = Foundation.ShipDef('EscapePod', App.SPECIES_ESCAPEPOD, { 'modes': [ Foundation.MutatorDef.StockShips ], 'name': 'Escape Pod', 'iconName': 'LifeBoat', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
Foundation.ShipDef.EscapePod.RegisterQBShipMenu('Other Ships', mode = Foundation.MutatorDef.StockShips)


# Unique ships.  I have no idea whether or not this works...

Foundation.ShipDef.Amagon = Foundation.ShipDef('Amagon', App.SPECIES_ASTEROID, { 'modes': [ Foundation.MutatorDef.StockShips ], 'iconName': 'Asteroid', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
# Revise the destroyed message
Foundation.ShipDef.Amagon.friendlyDetails[2] = 'QBFriendlyAmagonDestroyed'
Foundation.ShipDef.Amagon.enemyDetails[2] = 'QBEnemyAmagonDestroyed'


Foundation.ShipDef.BiranuStation = Foundation.ShipDef('BiranuStation', App.SPECIES_ASTEROID, { 'modes': [ Foundation.MutatorDef.StockShips ], 'iconName': 'SpaceFacility', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
# Revise the destroyed message
Foundation.ShipDef.BiranuStation.friendlyDetails[2] = 'QBFriendlyBiranuStationDestroyed'
Foundation.ShipDef.BiranuStation.enemyDetails[2] = 'QBEnemyBiranuStationDestroyed'


Foundation.ShipDef.BombFreighter = Foundation.ShipDef('BombFreighter', App.SPECIES_CARDFREIGHTER, { 'modes': [ Foundation.MutatorDef.StockShips ], 'iconName': 'CardFreighter', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
# Revise the destroyed message
Foundation.ShipDef.BombFreighter.friendlyDetails[2] = "QBFriendlyBombFreighterDestroyed"
Foundation.ShipDef.BombFreighter.enemyDetails[2] = "QBEnemyBombFreighterDestroyed"


Foundation.ShipDef.E2M0Warbird = Foundation.ShipDef('E2M0Warbird', App.SPECIES_WARBIRD, { 'modes': [ Foundation.MutatorDef.StockShips ], 'iconName': 'Warbird', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
# Revise the destroyed message
Foundation.ShipDef.E2M0Warbird.friendlyDetails[2] = "QBFriendlyE2M0WarbirdDestroyed"
Foundation.ShipDef.E2M0Warbird.enemyDetails[2] = "QBEnemyE2M0WarbirdDestroyed"


Foundation.ShipDef.Enterprise = Foundation.ShipDef('Enterprise', App.SPECIES_SOVEREIGN, { 'modes': [ Foundation.MutatorDef.StockShips ], 'iconName': 'Sovereign', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
# Revise the destroyed message
Foundation.ShipDef.Enterprise.friendlyDetails[2] = "QBFriendlyEnterpriseEnter"
Foundation.ShipDef.Enterprise.enemyDetails[2] = "QBEnemyEnterpriseEnter"


Foundation.ShipDef.Geronimo = Foundation.ShipDef('Geronimo', App.SPECIES_AKIRA, { 'modes': [ Foundation.MutatorDef.StockShips ], 'iconName': 'Akira', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
# Revise the destroyed message
Foundation.ShipDef.Geronimo.friendlyDetails[2] = "QBFriendlyGeronimoEnter"
Foundation.ShipDef.Geronimo.enemyDetails[2] = "QBEnemyGeronimoEnter"


Foundation.ShipDef.MatanKeldon = Foundation.ShipDef('MatanKeldon', App.SPECIES_KELDON, { 'modes': [ Foundation.MutatorDef.StockShips ], 'iconName': 'Keldon', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
# Revise the destroyed message
Foundation.ShipDef.MatanKeldon.friendlyDetails[2] = "QBFriendlyMatanKeldonEnter"
Foundation.ShipDef.MatanKeldon.enemyDetails[2] = "QBEnemyMatanKeldonEnter"


Foundation.ShipDef.Peregrine = Foundation.ShipDef('Peregrine', App.SPECIES_NEBULA, { 'modes': [ Foundation.MutatorDef.StockShips ], 'iconName': 'Nebula', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
# Revise the destroyed message
Foundation.ShipDef.Peregrine.friendlyDetails[2] = "QBFriendlyPeregrineEnter"
Foundation.ShipDef.Peregrine.enemyDetails[2] = "QBEnemyPeregrineEnter"


Foundation.ShipDef.RanKuf = Foundation.ShipDef('RanKuf', App.SPECIES_BIRD_OF_PREY, { 'modes': [ Foundation.MutatorDef.StockShips ], 'iconName': 'BirdOfPrey', 'hasTGLName': 1, 'hasTGLDesc': 1 } )
# Revise the destroyed message
Foundation.ShipDef.RanKuf.friendlyDetails[2] = "QBFriendlyRanKufEnter"
Foundation.ShipDef.RanKuf.enemyDetails[2] = "QBEnemyRanKufEnter"


# Foundation.ShipDef.BorgCube = Foundation.ShipDef('BorgCube', App.SPECIES_BORG, { 'modes': [ Foundation.MutatorDef.StockShips ], 'hasTGLName': 1, 'hasTGLDesc': 1 } )
# # Revise the destroyed message
# Foundation.ShipDef.BorgCube.friendlyDetails[2] = "QBFriendlyGenericShipDestroyed"
# Foundation.ShipDef.BorgCube.enemyDetails[2] = "QBEnemyGenericShipDestroyed"



Foundation.SoundDef("sfx/Weapons/federation_phaser_a.wav",	"Enterprise D Phaser Start",	0.7, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/federation_phaser_b.wav",	"Enterprise D Phaser Loop",		1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/ambassador_phaser_a.wav",	"Ambassador Phaser Start",		1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/ambassador_phaser_b.wav",	"Ambassador Phaser Loop",		1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/federation_phaser2_a.wav",	"Akira Phaser Start",			0.7, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/federation_phaser2_b.wav",	"Akira Phaser Loop",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/galaxy_phaser_a.wav",		"Galaxy Phaser Start",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/galaxy_phaser_b.wav",		"Galaxy Phaser Loop",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/ferengi_phaser_a.wav",		"Marauder Phaser Start",		1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/ferengi_phaser_b.wav",		"Marauder Phaser Loop",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/cardassian_phaser_a.wav",	"Card Phaser Start",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/cardassian_phaser_b.wav",	"Card Phaser Loop",				1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/galor_phaser_a.wav",		"Galor Phaser Start",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/galor_phaser_b.wav",		"Galor Phaser Loop",				1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/klingon_beam_a.wav",		"Vorcha Phaser Start",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/klingon_beam_b.wav",		"Vorcha Phaser Loop",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/romulan phaser_a.wav",		"Warbird Phaser Start",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/romulan phaser_b.wav",		"Warbird Phaser Loop",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/kessock beam_a.wav",		"Kessok Phaser Start",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/kessock beam_b.wav",		"Kessok Phaser Loop",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/kessock beam2_a.wav",		"Kessok Phaser2 Start",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/kessock beam2_b.wav",		"Kessok Phaser2 Loop",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/Photon Torp.wav",			"Enterprise D Torpedo",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/Photon Torp.wav",			"Akira Torpedo",				1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/Photon Torp.wav",			"Photon Torpedo",				1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/Klingon Torp.wav",			"Klingon Torpedo",				1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/Positron Torp.wav",		"Positron Torpedo",				1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/Cardassian Torp.wav",		"Cardassian Torpedo",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/Quantum Torp.wav",			"Quantum Torpedo",				1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/AntiMatter Torp.wav",		"Antimatter Torpedo",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/Disruptor Cannon.wav",		"Klingon Disruptor",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/Cardassian Cannon.wav",	"Disruptor",					1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/Pulse Disruptor.wav",		"Pulse Disruptor",				1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Weapons/Plasma Bolt.wav",			"Plasma Bolt",					1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Weapons/tractor.wav",				"Tractor Beam",					1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

# Engine noises.
Foundation.SoundDef("sfx/engine1.wav",					"Federation Engines",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/engine2.wav",					"Klingon Engines",		1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/engine2.wav",					"Romulan Engines",		1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/engine2.wav",					"Ferengi Engines",		1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/engine2.wav",					"Cardassian Engines",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/engine1.wav",					"Kessok Engines",		1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/enter warp.wav",				"Enter Warp",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/exit warp.wav",				"Exit Warp",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/warp flash.wav",				"Warp Flash",			0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Explosions/explo1.WAV",		"Explosion 1",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo2.WAV",		"Explosion 2",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo3.WAV",		"Explosion 3",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo4.WAV",		"Explosion 4",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo5.WAV",		"Explosion 5",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo6.WAV",		"Explosion 6",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo7.WAV",		"Explosion 7",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo8.WAV",		"Explosion 8",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo9.WAV",		"Explosion 9",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo10.WAV",		"Explosion 10",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo11.WAV",		"Explosion 11",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo12.WAV",		"Explosion 12",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo13.WAV",		"Explosion 13",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo14.WAV",		"Explosion 14",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo15.WAV",		"Explosion 15",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo16.WAV",		"Explosion 16",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo17.WAV",		"Explosion 17",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo18.WAV",		"Explosion 18",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo19.WAV",		"Explosion 19",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Explosions/explo_flame_01.WAV","Death Explosion 1",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_flame_02.WAV","Death Explosion 2",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_flame_03.WAV","Death Explosion 3",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_flame_04.WAV","Death Explosion 4",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_flame_05.WAV","Death Explosion 5",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_flame_06.WAV","Death Explosion 6",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_flame_07.WAV","Death Explosion 7",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_flame_08.WAV","Death Explosion 8",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_flame_09.WAV","Death Explosion 9",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_flame_10.WAV","Death Explosion 10",	1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Explosions/explo_large_01.WAV","Big Death Explosion 1",1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_large_02.WAV","Big Death Explosion 2",1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_large_03.WAV","Big Death Explosion 3",1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_large_04.WAV","Big Death Explosion 4",1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_large_05.WAV","Big Death Explosion 5",1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_large_06.WAV","Big Death Explosion 6",1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_large_07.WAV","Big Death Explosion 7",1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/explo_large_08.WAV","Big Death Explosion 8",1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/Explosions/collision1.wav",	"Collision 1",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/collision2.wav",	"Collision 2",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/collision3.wav",	"Collision 3",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/collision4.wav",	"Collision 4",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/collision5.wav",	"Collision 5",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/collision6.wav",	"Collision 6",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/collision7.wav",	"Collision 7",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/Explosions/collision8.wav",	"Collision 8",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/cloak on.wav",					"Cloak",				1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/cloak off.wav",				"Uncloak",				1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )

Foundation.SoundDef("sfx/re-entry_rumble.wav",			"AtmosphereRumble",		1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )
Foundation.SoundDef("sfx/probe launch.wav",				"Probe Launch",			1.0, { 'modes': [ Foundation.MutatorDef.StockSounds ] } )


Foundation.SystemDef('DeepSpace', 0, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Starbase12', 0, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )

Foundation.SystemDef('Albirea', 3, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Alioth', 8, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Artrus', 3, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Ascella', 5, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Belaruz', 4, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Beol', 4, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Biranu', 2, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Cebalrai', 3, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Chambana', 2, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Geble', 4, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Itari', 8, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Nepenthe', 3, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('OmegaDraconis', 5, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Ona', 3, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Poseidon', 2, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Prendel', 5, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Riha', 1, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Savoy', 3, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Serris', 3, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Tevron', 2, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Tezle', 2, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Vesuvi', 5, 3, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Voltair', 2, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('XiEntrades', 5, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.SystemDef('Yiles', 4, dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )

Foundation.BridgeDef('Galaxy', 'GalaxyBridge', dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )
Foundation.BridgeDef('Sovereign', 'SovereignBridge', dict = { 'modes': [ Foundation.MutatorDef.Stock ] } )

Foundation.MutatorDef.Stock.startShipDef = Foundation.ShipDef.Galaxy
