import App
import Foundation


abbrev = "WCexcelnx"
iconName = "WCexcelnx"
longName = "NX-2000 Excelsior"
shipFile = "WCexcelnx"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelnx = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelnx.desc = "USS Excelsior NX-2000"
Foundation.ShipDef.WCexcelnx.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelnx.SubSubMenu = "TMP"
Foundation.ShipDef.WCexcelnx.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelnx.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelnx.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelnxIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCnxexcelID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelnx.__dict__['SDT Entry'] = WCexcelnxIDSwap


abbrev = "WCexcelncc"
iconName = "WCexcelncc"
longName = "NCC-2000 Excelsior"
shipFile = "WCexcelncc"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelncc = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelncc.desc = "USS Excelsior NCC-2000"
Foundation.ShipDef.WCexcelncc.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelncc.SubSubMenu = "TMP"
Foundation.ShipDef.WCexcelncc.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelncc.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelncc.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelnccIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCnccexcelID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelncc.__dict__['SDT Entry'] = WCexcelnccIDSwap


abbrev = "WCexcelrefit"
iconName = "WCexcelrefit"
longName = "NCC-1701-B Enterprise"
shipFile = "WCexcelrefit"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelrefit = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelrefit.desc = "USS Enterprise NCC-1701-B"
Foundation.ShipDef.WCexcelrefit.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelrefit.SubSubMenu = "TMP"
Foundation.ShipDef.WCexcelrefit.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelrefit.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelrefit.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelrefitIDSwap(self):
       retval = {"Textures": [["gblankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCentbID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelrefit.__dict__['SDT Entry'] = WCexcelrefitIDSwap


abbrev = "WCcentaur"
iconName = "WCcentaur"
longName = "NCC-42043 Centaur"
shipFile = "WCcentaur"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCcentaur = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCcentaur.desc = "USS Centaur NCC-42043"
Foundation.ShipDef.WCcentaur.SubMenu = "Centaur Class Pack"
Foundation.ShipDef.WCcentaur.SubSubMenu = "Centaur Class"


if menuGroup:           Foundation.ShipDef.WCcentaur.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCcentaur.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCcentaurIDSwap(self):
       retval = {"Textures": [["wccentaurblankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCcentaurID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCcentaur.__dict__['SDT Entry'] = WCcentaurIDSwap

abbrev = "WCexcelmelb"
iconName = "WCexcelncc"
longName = "NCC-62043 Melbourne"
shipFile = "WCexcelmelb"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelmelb = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelmelb.desc = "USS Melbourne NCC-62043"
Foundation.ShipDef.WCexcelmelb.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelmelb.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelmelb.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelmelb.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelmelb.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelmelbIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCmelbID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelmelb.__dict__['SDT Entry'] = WCexcelmelbIDSwap

abbrev = "WCexcelalbatani"
iconName = "WCexcelrefit"
longName = "NCC-42995 Al-Batani"
shipFile = "WCexcelalbatani"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCalbatani = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCalbatani.desc = "USS Al-Batani NCC-42995"
Foundation.ShipDef.WCalbatani.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCalbatani.SubSubMenu = "DS9 / Voyager"
Foundation.ShipDef.WCalbatani.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCalbatani.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCalbatani.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCalbataniIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCalbataniID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCalbatani.__dict__['SDT Entry'] = WCalbataniIDSwap

abbrev = "WCexcelberlin"
iconName = "WCexcelnx"
longName = "NCC-14232 Berlin"
shipFile = "WCexcelberlin"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelberlin = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelberlin.desc = "USS Berlin NCC-14232"
Foundation.ShipDef.WCexcelberlin.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelberlin.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelberlin.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelberlin.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelberlin.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelberlinIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCberlinID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelberlin.__dict__['SDT Entry'] = WCexcelberlinIDSwap

abbrev = "WCcentbuckner"
iconName = "WCcentaur"
longName = "NX-42000 Buckner"
shipFile = "WCcentbuckner"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCcentbuckner = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCcentbuckner.desc = "USS Buckner NX-42000"
Foundation.ShipDef.WCcentbuckner.SubMenu = "Centaur Class Pack"
Foundation.ShipDef.WCcentbuckner.SubSubMenu = "Centaur Class"


if menuGroup:           Foundation.ShipDef.WCcentbuckner.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCcentbuckner.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCcentbucknerIDSwap(self):
       retval = {"Textures": [["wccentaurblankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCbucknerID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCcentbuckner.__dict__['SDT Entry'] = WCcentbucknerIDSwap

abbrev = "WCexcelcairo"
iconName = "WCexcelncc"
longName = "NCC-42136 Cairo"
shipFile = "WCexcelcairo"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelcairo = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelcairo.desc = "USS Cairo NCC-42136"
Foundation.ShipDef.WCexcelcairo.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelcairo.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelcairo.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelcairo.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelcairo.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelcairoIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCcairoID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelcairo.__dict__['SDT Entry'] = WCexcelcairoIDSwap

abbrev = "WCexcelcharleston"
iconName = "WCexcelncc"
longName = "NCC-42285 Charleston"
shipFile = "WCexcelcharleston"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelcharleston = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelcharleston.desc = "USS Charleston NCC-42285"
Foundation.ShipDef.WCexcelcharleston.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelcharleston.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelcharleston.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelcharleston.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelcharleston.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelcharlestonIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCcharlestonID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelcharleston.__dict__['SDT Entry'] = WCexcelcharlestonIDSwap

abbrev = "WCexcelcrazyhorse"
iconName = "WCexcelncc"
longName = "NCC-50446 Crazy Horse"
shipFile = "WCexcelcrazyhorse"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelcrazyhorse = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelcrazyhorse.desc = "USS Crazy Horse NCC-50446"
Foundation.ShipDef.WCexcelcrazyhorse.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelcrazyhorse.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelcrazyhorse.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelcrazyhorse.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelcrazyhorse.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelcrazyhorseIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCcrazyhorseID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelcrazyhorse.__dict__['SDT Entry'] = WCexcelcrazyhorseIDSwap

abbrev = "WCexcelcrockett"
iconName = "WCexcelncc"
longName = "NCC-38955 Crockett"
shipFile = "WCexcelcrockett"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelcrockett = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelcrockett.desc = "USS Crockett NCC-38955"
Foundation.ShipDef.WCexcelcrockett.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelcrockett.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelcrockett.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelcrockett.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelcrockett.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelcrockettIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCcrockettID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelcrockett.__dict__['SDT Entry'] = WCexcelcrockettIDSwap

abbrev = "WCexcelfearless"
iconName = "WCexcelnx"
longName = "NCC-14598 Fearless"
shipFile = "WCexcelfearless"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelfearless = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelfearless.desc = "USS Fearless NCC-14598"
Foundation.ShipDef.WCexcelfearless.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelfearless.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelfearless.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelfearless.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelfearless.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelfearlessIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCfearlessID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelfearless.__dict__['SDT Entry'] = WCexcelfearlessIDSwap

abbrev = "WCexcelfrederickson"
iconName = "WCexcelds9"
longName = "NCC-42111 Frederickson"
shipFile = "WCexcelfrederickson"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelfrederickson = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelfrederickson.desc = "USS Frederickson NCC-42111"
Foundation.ShipDef.WCexcelfrederickson.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelfrederickson.SubSubMenu = "DS9 / Voyager"


if menuGroup:           Foundation.ShipDef.WCexcelfrederickson.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelfrederickson.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelfredericksonIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCfredericksonID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelfrederickson.__dict__['SDT Entry'] = WCexcelfredericksonIDSwap

abbrev = "WCexcelgorkon"
iconName = "WCexcelnx"
longName = "NCC-40521 Gorkon"
shipFile = "WCexcelgorkon"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelgorkon = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelgorkon.desc = "USS Gorkon NCC-40521"
Foundation.ShipDef.WCexcelgorkon.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelgorkon.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelgorkon.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelgorkon.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelgorkon.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelgorkonIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCgorkonID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelgorkon.__dict__['SDT Entry'] = WCexcelgorkonIDSwap

abbrev = "WCexcelgrissom"
iconName = "WCexcelnx"
longName = "NCC-42857 Grissom"
shipFile = "WCexcelgrissom"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelgrissom = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelgrissom.desc = "USS Grissom NCC-42857"
Foundation.ShipDef.WCexcelgrissom.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelgrissom.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelgrissom.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelgrissom.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelgrissom.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelgrissomIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCgrissomID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelgrissom.__dict__['SDT Entry'] = WCexcelgrissomIDSwap

abbrev = "WCexcelhood"
iconName = "WCexcelds9"
longName = "NCC-42296 Hood"
shipFile = "WCexcelhood"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelhood = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelhood.desc = "USS Hood NCC-42296"
Foundation.ShipDef.WCexcelhood.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelhood.SubSubMenu = "DS9 / Voyager"


if menuGroup:           Foundation.ShipDef.WCexcelhood.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelhood.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelhoodIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WChoodID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelhood.__dict__['SDT Entry'] = WCexcelhoodIDSwap

abbrev = "WCexcelintrepid"
iconName = "WCexcelnx"
longName = "NCC-38907 Intrepid"
shipFile = "WCexcelintrepid"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelintrepid = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelintrepid.desc = "USS Intrepid NCC-38907"
Foundation.ShipDef.WCexcelintrepid.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelintrepid.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelintrepid.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelintrepid.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelintrepid.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelintrepidIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCintrepidID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelintrepid.__dict__['SDT Entry'] = WCexcelintrepidIDSwap

abbrev = "WCexcellakota"
iconName = "WCexcelrefit"
longName = "NCC-42768 Lakota"
shipFile = "WCexcellakota"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcellakota = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcellakota.desc = "USS Lakota NCC-42768"
Foundation.ShipDef.WCexcellakota.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcellakota.SubSubMenu = "DS9 / Voyager"
Foundation.ShipDef.WCexcellakota.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcellakota.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcellakota.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcellakotaIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WClakotaID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcellakota.__dict__['SDT Entry'] = WCexcellakotaIDSwap

abbrev = "WCexcellexington"
iconName = "WCexcelnx"
longName = "NCC-14427 Lexington"
shipFile = "WCexcellexington"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcellexington = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcellexington.desc = "USS Lexington NCC-14427"
Foundation.ShipDef.WCexcellexington.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcellexington.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcellexington.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcellexington.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcellexington.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcellexingtonIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WClexingtonID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcellexington.__dict__['SDT Entry'] = WCexcellexingtonIDSwap

abbrev = "WCexcellivingston"
iconName = "WCexcelncc"
longName = "NCC-34099 Livingston"
shipFile = "WCexcellivingston"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcellivingston = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcellivingston.desc = "USS Livingston NCC-34099"
Foundation.ShipDef.WCexcellivingston.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcellivingston.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcellivingston.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcellivingston.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcellivingston.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcellivingstonIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WClivingstonID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcellivingston.__dict__['SDT Entry'] = WCexcellivingstonIDSwap

abbrev = "WCexcelmalinche"
iconName = "WCexcelds9"
longName = "NCC-38997 Malinche"
shipFile = "WCexcelmalinche"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelmalinche = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelmalinche.desc = "USS Malinche NCC-38997"
Foundation.ShipDef.WCexcelmalinche.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelmalinche.SubSubMenu = "DS9 / Voyager"
Foundation.ShipDef.WCexcelmalinche.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelmalinche.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelmalinche.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelmalincheIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCmalincheID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelmalinche.__dict__['SDT Entry'] = WCexcelmalincheIDSwap

abbrev = "WCexcelokinawa"
iconName = "WCexcelds9"
longName = "NCC-13958 Okinawa"
shipFile = "WCexcelokinawa"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelokinawa = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelokinawa.desc = "USS Okinawa NCC-13958"
Foundation.ShipDef.WCexcelokinawa.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelokinawa.SubSubMenu = "DS9 / Voyager"


if menuGroup:           Foundation.ShipDef.WCexcelokinawa.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelokinawa.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelokinawaIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCokinawaID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelokinawa.__dict__['SDT Entry'] = WCexcelokinawaIDSwap

abbrev = "WCexcelpotemkin"
iconName = "WCexcelnx"
longName = "NCC-18253 Potemkin"
shipFile = "WCexcelpotemkin"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelpotemkin = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelpotemkin.desc = "USS Potemkin NCC-18253"
Foundation.ShipDef.WCexcelpotemkin.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelpotemkin.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelpotemkin.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelpotemkin.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelpotemkin.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelpotemkinIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCpotemkinID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelpotemkin.__dict__['SDT Entry'] = WCexcelpotemkinIDSwap

abbrev = "WCexcelrepulse"
iconName = "WCexcelnx"
longName = "NCC-2544 Repulse"
shipFile = "WCexcelrepulse"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelrepulse = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelrepulse.desc = "USS Repulse NCC-2544"
Foundation.ShipDef.WCexcelrepulse.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelrepulse.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelrepulse.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelrepulse.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelrepulse.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelrepulseIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCrepulseID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelrepulse.__dict__['SDT Entry'] = WCexcelrepulseIDSwap

abbrev = "WCexcelroosevelt"
iconName = "WCexcelncc"
longName = "NCC-2573 Roosevelt"
shipFile = "WCexcelroosevelt"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelroosevelt = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelroosevelt.desc = "USS Roosevelt NCC-2573"
Foundation.ShipDef.WCexcelroosevelt.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelroosevelt.SubSubMenu = "TMP"
Foundation.ShipDef.WCexcelroosevelt.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelroosevelt.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelroosevelt.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelrooseveltIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCrooseveltID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelroosevelt.__dict__['SDT Entry'] = WCexcelrooseveltIDSwap

abbrev = "WCexceltecumseh"
iconName = "WCexcelds9"
longName = "NCC-14934 Tecumseh"
shipFile = "WCexceltecumseh"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexceltecumseh = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexceltecumseh.desc = "USS Tecumseh NCC-14394"
Foundation.ShipDef.WCexceltecumseh.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexceltecumseh.SubSubMenu = "DS9 / Voyager"


if menuGroup:           Foundation.ShipDef.WCexceltecumseh.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexceltecumseh.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexceltecumsehIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCtecumsehID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexceltecumseh.__dict__['SDT Entry'] = WCexceltecumsehIDSwap

abbrev = "WCexcelvalleyforge"
iconName = "WCexcelds9"
longName = "NCC-43305 Valley Forge"
shipFile = "WCexcelvalleyforge"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelvalleyforge = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelvalleyforge.desc = "USS Valley Forge NCC-43305"
Foundation.ShipDef.WCexcelvalleyforge.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelvalleyforge.SubSubMenu = "DS9 / Voyager"


if menuGroup:           Foundation.ShipDef.WCexcelvalleyforge.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelvalleyforge.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelvalleyforgeIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCvalleyforgeID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelvalleyforge.__dict__['SDT Entry'] = WCexcelvalleyforgeIDSwap

abbrev = "WCexceldallas"
iconName = "WCexcelds9"
longName = "NCC-2019 Dallas"
shipFile = "WCexceldallas"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexceldallas = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexceldallas.desc = "USS Dallas NCC-2019"
Foundation.ShipDef.WCexceldallas.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexceldallas.SubSubMenu = "DS9 / Voyager"


if menuGroup:           Foundation.ShipDef.WCexceldallas.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexceldallas.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexceldallasIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCdallasID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexceldallas.__dict__['SDT Entry'] = WCexceldallasIDSwap

abbrev = "WCexcelrighteous"
iconName = "WCexcelncc"
longName = "NCC-42451 Righteous"
shipFile = "WCexcelrighteous"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.WCexcelrighteous = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCexcelrighteous.desc = "USS Righteous NCC-42451"
Foundation.ShipDef.WCexcelrighteous.SubMenu = "Excelsior Class Pack"
Foundation.ShipDef.WCexcelrighteous.SubSubMenu = "TNG"
Foundation.ShipDef.WCexcelrighteous.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"nacelleoff_glow": {
				0.0: "data/Models/Ships/WCExcelsior/nacelleoff_glow.tga", 
				1.0: "data/Models/Ships/WCExcelsior/nacelleon_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.WCexcelrighteous.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCexcelrighteous.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


def WCexcelrighteousIDSwap(self):
       retval = {"Textures": [["blankid_glow.tga", "Data/Models/SharedTextures/WCExcelsior/WCrighteousID_glow.tga"]]}
       return retval


Foundation.ShipDef.WCexcelrighteous.__dict__['SDT Entry'] = WCexcelrighteousIDSwap