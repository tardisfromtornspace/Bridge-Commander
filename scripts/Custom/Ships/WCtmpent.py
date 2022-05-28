import App
import Foundation



abbrev = 'WCtmpent'
iconName = 'WCtmpent'
longName = 'Enterprise 1701 WC'
shipFile = 'WCtmpent'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpent = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpent.fMaxWarp
# Foundation.ShipDef.WCtmpent.fCruiseWarp
Foundation.ShipDef.WCtmpent.desc = "USS Enterprise NCC-1701"
Foundation.ShipDef.WCtmpent.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grille_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille_glow.tga", 
				1.0: "data/Models/Ships/WCtmpent/grille2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpent/grille_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpent.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpent.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def EnterpIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCtmpent/EnterpID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpent.__dict__['SDT Entry'] = EnterpIDSwap


import App
import Foundation



abbrev = 'WCtmpConst'
iconName = 'WCtmpent'
longName = 'Constitution 1700 WC'
shipFile = 'WCtmpConst'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpConst = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpConst.fMaxWarp
# Foundation.ShipDef.WCtmpConst.fCruiseWarp
Foundation.ShipDef.WCtmpConst.desc = "USS Constitution NCC-1700"
Foundation.ShipDef.WCtmpConst.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grille_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille_glow.tga", 
				1.0: "data/Models/Ships/WCtmpent/grille2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpent/grille_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpConst.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpConst.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def ConstitIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCtmpent/ConstitID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpConst.__dict__['SDT Entry'] = ConstitIDSwap


import App
import Foundation



abbrev = 'WCtmpConstell'
iconName = 'WCtmpenta'
longName = 'Constellation 1017-A WC'
shipFile = 'WCtmpConstell'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpConstell = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpConstell.fMaxWarp
# Foundation.ShipDef.WCtmpConstell.fCruiseWarp
Foundation.ShipDef.WCtmpConstell.desc = "USS Constellation NCC-1017-A"
Foundation.ShipDef.WCtmpConstell.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grilleb_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga", 
				1.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2b_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpConstell.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpConstell.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def ConstellIDSwap(self):
       retval = {"Textures": [["blankbid_glow.tga", "Data/Models/SharedTextures/WCtmpent/ConstellID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpConstell.__dict__['SDT Entry'] = ConstellIDSwap


import App
import Foundation



abbrev = 'WCtmpDefiant'
iconName = 'WCtmpenta'
longName = 'Defiant 1764-A WC'
shipFile = 'WCtmpDefiant'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpDefiant = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpDefiant.fMaxWarp
# Foundation.ShipDef.WCtmpDefiant.fCruiseWarp
Foundation.ShipDef.WCtmpDefiant.desc = "USS Defiant NCC-1764-A"
Foundation.ShipDef.WCtmpDefiant.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grilleb_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga", 
				1.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2b_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpDefiant.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpDefiant.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def DefiantIDSwap(self):
       retval = {"Textures": [["blankbid_glow.tga", "Data/Models/SharedTextures/WCtmpent/DefiantID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpDefiant.__dict__['SDT Entry'] = DefiantIDSwap


import App
import Foundation



abbrev = 'WCtmpEagle'
iconName = 'WCtmpenta'
longName = 'Eagle 956 WC'
shipFile = 'WCtmpEagle'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpEagle = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpEagle.fMaxWarp
# Foundation.ShipDef.WCtmpEagle.fCruiseWarp
Foundation.ShipDef.WCtmpEagle.desc = "USS Eagle NCC-956"
Foundation.ShipDef.WCtmpEagle.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grilleb_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga", 
				1.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2b_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpEagle.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpEagle.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def EagleIDSwap(self):
       retval = {"Textures": [["blankbid_glow.tga", "Data/Models/SharedTextures/WCtmpent/EagleID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpEagle.__dict__['SDT Entry'] = EagleIDSwap


import App
import Foundation



abbrev = 'WCtmpEndeav'
iconName = 'WCtmpenta'
longName = 'Endeavour 1895 WC'
shipFile = 'WCtmpEndeav'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpEndeav = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpEndeav.fMaxWarp
# Foundation.ShipDef.WCtmpEndeav.fCruiseWarp
Foundation.ShipDef.WCtmpEndeav.desc = "USS Endeavour NCC-1895"
Foundation.ShipDef.WCtmpEndeav.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grilleb_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga", 
				1.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2b_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpEndeav.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpEndeav.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def EndeavIDSwap(self):
       retval = {"Textures": [["blankbid_glow.tga", "Data/Models/SharedTextures/WCtmpent/EndeavID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpEndeav.__dict__['SDT Entry'] = EndeavIDSwap


import App
import Foundation



abbrev = 'WCtmpEnterpA'
iconName = 'WCtmpenta'
longName = 'Enterprise 1701-A WC'
shipFile = 'WCtmpEnterpA'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpEnterpA = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpEnterpA.fMaxWarp
# Foundation.ShipDef.WCtmpEnterpA.fCruiseWarp
Foundation.ShipDef.WCtmpEnterpA.desc = "USS Enterprise NCC-1701-A"
Foundation.ShipDef.WCtmpEnterpA.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grilleb_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga", 
				1.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2b_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpEnterpA.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpEnterpA.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def EnterpAIDSwap(self):
       retval = {"Textures": [["blankbid_glow.tga", "Data/Models/SharedTextures/WCtmpent/EnterpAID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpEnterpA.__dict__['SDT Entry'] = EnterpAIDSwap


import App
import Foundation



abbrev = 'WCtmpEssex'
iconName = 'WCtmpent'
longName = 'Essex 1697 WC'
shipFile = 'WCtmpEssex'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpEssex = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpEssex.fMaxWarp
# Foundation.ShipDef.WCtmpEssex.fCruiseWarp
Foundation.ShipDef.WCtmpEssex.desc = "USS Essex NCC-1697"
Foundation.ShipDef.WCtmpEssex.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grille_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille_glow.tga", 
				1.0: "data/Models/Ships/WCtmpent/grille2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpent/grille_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpEssex.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpEssex.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def EssexIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCtmpent/EssexID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpEssex.__dict__['SDT Entry'] = EssexIDSwap


import App
import Foundation



abbrev = 'WCtmpExcalib'
iconName = 'WCtmpent'
longName = 'Excalibur 1664 WC'
shipFile = 'WCtmpExcalib'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpExcalib = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpExcalib.fMaxWarp
# Foundation.ShipDef.WCtmpExcalib.fCruiseWarp
Foundation.ShipDef.WCtmpExcalib.desc = "USS Excalibur NCC-1664"
Foundation.ShipDef.WCtmpExcalib.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grille_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille_glow.tga", 
				1.0: "data/Models/Ships/WCtmpent/grille2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpent/grille_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpExcalib.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpExcalib.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def ExcalibIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCtmpent/ExcalibID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpExcalib.__dict__['SDT Entry'] = ExcalibIDSwap


import App
import Foundation



abbrev = 'WCtmpExeter'
iconName = 'WCtmpent'
longName = 'Exeter 1672 WC'
shipFile = 'WCtmpExeter'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpExeter = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpExeter.fMaxWarp
# Foundation.ShipDef.WCtmpExeter.fCruiseWarp
Foundation.ShipDef.WCtmpExeter.desc = "USS Exeter NCC-1672"
Foundation.ShipDef.WCtmpExeter.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grille_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille_glow.tga", 
				1.0: "data/Models/Ships/WCtmpent/grille2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpent/grille_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpExeter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpExeter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def ExeterIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCtmpent/ExeterID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpExeter.__dict__['SDT Entry'] = ExeterIDSwap


import App
import Foundation



abbrev = 'WCtmpPotemkin'
iconName = 'WCtmpent'
longName = 'Potemkin 1657 WC'
shipFile = 'WCtmpPotemkin'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpPotemkin = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpPotemkin.fMaxWarp
# Foundation.ShipDef.WCtmpPotemkin.fCruiseWarp
Foundation.ShipDef.WCtmpPotemkin.desc = "USS Potemkin NCC-1657"
Foundation.ShipDef.WCtmpPotemkin.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grille_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille_glow.tga", 
				1.0: "data/Models/Ships/WCtmpent/grille2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpent/grille_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpPotemkin.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpPotemkin.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def PotemkinIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCtmpent/PotemkinID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpPotemkin.__dict__['SDT Entry'] = PotemkinIDSwap


import App
import Foundation



abbrev = 'WCtmpIntrepid'
iconName = 'WCtmpenta'
longName = 'Intrepid 1631-A WC'
shipFile = 'WCtmpIntrepid'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpIntrepid = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpIntrepid.fMaxWarp
# Foundation.ShipDef.WCtmpIntrepid.fCruiseWarp
Foundation.ShipDef.WCtmpIntrepid.desc = "USS Intrepid NCC-1631-A"
Foundation.ShipDef.WCtmpIntrepid.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grilleb_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga", 
				1.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2b_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpIntrepid.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpIntrepid.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def IntrepidIDSwap(self):
       retval = {"Textures": [["blankbid_glow.tga", "Data/Models/SharedTextures/WCtmpent/IntrepidID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpIntrepid.__dict__['SDT Entry'] = IntrepidIDSwap


import App
import Foundation



abbrev = 'WCtmpHood'
iconName = 'WCtmpent'
longName = 'Hood 1703 WC'
shipFile = 'WCtmpHood'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpHood = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpHood.fMaxWarp
# Foundation.ShipDef.WCtmpHood.fCruiseWarp
Foundation.ShipDef.WCtmpHood.desc = "USS Hood NCC-1703"
Foundation.ShipDef.WCtmpHood.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grille_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille_glow.tga", 
				1.0: "data/Models/Ships/WCtmpent/grille2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpent/grille_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpHood.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpHood.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def HoodIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCtmpent/HoodID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpHood.__dict__['SDT Entry'] = HoodIDSwap


import App
import Foundation



abbrev = 'WCtmpLexing'
iconName = 'WCtmpent'
longName = 'Lexington 1709 WC'
shipFile = 'WCtmpLexing'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpLexing = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpLexing.fMaxWarp
# Foundation.ShipDef.WCtmpLexing.fCruiseWarp
Foundation.ShipDef.WCtmpLexing.desc = "USS Lexington NCC-1709"
Foundation.ShipDef.WCtmpLexing.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grille_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille_glow.tga", 
				1.0: "data/Models/Ships/WCtmpent/grille2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpent/grille_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpLexing.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpLexing.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def LexingIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCtmpent/LexingID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpLexing.__dict__['SDT Entry'] = LexingIDSwap


import App
import Foundation



abbrev = 'WCtmpFarragut'
iconName = 'WCtmpent'
longName = 'Farragut 1647 WC'
shipFile = 'WCtmpFarragut'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpFarragut = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpFarragut.fMaxWarp
# Foundation.ShipDef.WCtmpFarragut.fCruiseWarp
Foundation.ShipDef.WCtmpFarragut.desc = "USS Farragut NCC-1647"
Foundation.ShipDef.WCtmpFarragut.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grille_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille_glow.tga", 
				1.0: "data/Models/Ships/WCtmpent/grille2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2_glow": {
				0.0: "data/Models/Ships/WCtmpent/grille2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpent/grille_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpFarragut.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpFarragut.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def FarragutIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCtmpent/FarragutID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpFarragut.__dict__['SDT Entry'] = FarragutIDSwap


import App
import Foundation



abbrev = 'WCtmpKongo'
iconName = 'WCtmpenta'
longName = 'Kongo 1710 WC'
shipFile = 'WCtmpKongo'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpKongo = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpKongo.fMaxWarp
# Foundation.ShipDef.WCtmpKongo.fCruiseWarp
Foundation.ShipDef.WCtmpKongo.desc = "USS Kongo NCC-1710"
Foundation.ShipDef.WCtmpKongo.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grilleb_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga", 
				1.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2b_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpKongo.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpKongo.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def KongoIDSwap(self):
       retval = {"Textures": [["blankbid_glow.tga", "Data/Models/SharedTextures/WCtmpent/KongoID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpKongo.__dict__['SDT Entry'] = KongoIDSwap


import App
import Foundation



abbrev = 'WCtmpRepublic'
iconName = 'WCtmpenta'
longName = 'Republic 1371 WC'
shipFile = 'WCtmpRepublic'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpRepublic = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpRepublic.fMaxWarp
# Foundation.ShipDef.WCtmpRepublic.fCruiseWarp
Foundation.ShipDef.WCtmpRepublic.desc = "USS Republic NCC-1371"
Foundation.ShipDef.WCtmpRepublic.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grilleb_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga", 
				1.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2b_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpRepublic.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpRepublic.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def RepublicIDSwap(self):
       retval = {"Textures": [["blankbid_glow.tga", "Data/Models/SharedTextures/WCtmpent/RepublicID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpRepublic.__dict__['SDT Entry'] = RepublicIDSwap


import App
import Foundation



abbrev = 'WCtmpYorktown'
iconName = 'WCtmpenta'
longName = 'Yorktown 1717 WC'
shipFile = 'WCtmpYorktown'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Constitution'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCtmpYorktown = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCtmpYorktown.fMaxWarp
# Foundation.ShipDef.WCtmpYorktown.fCruiseWarp
Foundation.ShipDef.WCtmpYorktown.desc = "USS Yorktown NCC-1717"
Foundation.ShipDef.WCtmpYorktown.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"startTrack": {
			"grilleb_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga", 
				1.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga",
			}
		},
		"stopTrack": {
			"grille2b_glow": {
				0.0: "data/Models/Ships/WCtmpenta/grilleb2_glow.tga", 
				4.0: "data/Models/Ships/WCtmpenta/grilleb_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCtmpYorktown.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCtmpYorktown.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def YorktownIDSwap(self):
       retval = {"Textures": [["blankbid_glow.tga", "Data/Models/SharedTextures/WCtmpent/YorktownID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCtmpYorktown.__dict__['SDT Entry'] = YorktownIDSwap
