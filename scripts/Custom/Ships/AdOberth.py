
import Foundation
import App

#Oberth
abbrev = 'AdOberth'
iconName = 'AdOberth'
longName = 'USS Oberth'
shipFile = 'AdOberth' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Oberth Class"
species = App.SPECIES_GALAXY

credits = {
	'modName': 'AdOberth',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.AdOberth = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.AdOberth.fMaxWarp = 6.0
Foundation.ShipDef.AdOberth.fCruiseWarp = 5.2
Foundation.ShipDef.AdOberth.desc = 'USS Oberth'

Foundation.ShipDef.AdOberth.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"Plas_glow": {
				0.0: "data/Models/Ships/AdTMP/Oberth/High/Plas_glow.tga", 
				1.0: "data/Models/Ships/AdTMP/Oberth/High/Plas01_glow.tga",
			}
		}
	}
}

if menuGroup:           Foundation.ShipDef.AdOberth.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AdOberth.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

#Grissom
abbrev = 'AdObGrissom'
iconName = 'AdOberth'
longName = 'USS Grissom'
shipFile = 'AdObGrissom' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Oberth Class"
species = App.SPECIES_GALAXY

credits = {
	'modName': 'AdOberth',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.AdObGrissom = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.AdObGrissom.fMaxWarp = 6.0
Foundation.ShipDef.AdObGrissom.fCruiseWarp = 5.2
Foundation.ShipDef.AdObGrissom.desc = 'USS Grissom'

Foundation.ShipDef.AdObGrissom.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"Plas_glow": {
				0.0: "data/Models/Ships/AdTMP/Oberth/High/Plas_glow.tga", 
				1.0: "data/Models/Ships/AdTMP/Oberth/High/Plas01_glow.tga",
			}
		}
	}
}

if menuGroup:           Foundation.ShipDef.AdObGrissom.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AdObGrissom.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AdGrissomIDSwap(self):
	retval = {"Textures": [["Hu_glow", "Data/Models/ships/AdTMP/Oberth/High/Grissom_glow.tga"], ["Dauntless", "Data/Models/ships/AdTMP/Oberth/High/Grissom_glow.tga"]]}
	return retval

Foundation.ShipDef.AdObGrissom.__dict__["SDT Entry"] = AdGrissomIDSwap

#Coppernicus
#Pegasus
abbrev = 'AdObCoppernicus'
iconName = 'AdPegasus'
longName = 'USS Coppernicus'
shipFile = 'AdObCoppernicus' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Oberth Class"
species = App.SPECIES_GALAXY

credits = {
	'modName': 'AdOberth',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.AdObCoppernicus = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.AdObCoppernicus.fMaxWarp = 6.0
Foundation.ShipDef.AdObCoppernicus.fCruiseWarp = 5.2
Foundation.ShipDef.AdObCoppernicus.desc = 'USS Coppernicus'

Foundation.ShipDef.AdObCoppernicus.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"Plas_glow": {
				0.0: "data/Models/Ships/AdTMP/Oberth/High/Plas_glow.tga", 
				1.0: "data/Models/Ships/AdTMP/Oberth/High/Plas01_glow.tga",
			}
		}
	}
}

if menuGroup:           Foundation.ShipDef.AdObCoppernicus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AdObCoppernicus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AdCoppernicusIDSwap(self):
	retval = {"Textures": [["Hu_glow", "Data/Models/ships/AdTMP/Oberth/High/Coppernicus_glow.tga"], ["Dauntless", "Data/Models/ships/AdTMP/Oberth/High/Coppernicus_glow.tga"]]}
	return retval

Foundation.ShipDef.AdObCoppernicus.__dict__["SDT Entry"] = AdCoppernicusIDSwap

#Yosemite
abbrev = 'AdObYosemite'
iconName = 'AdOberth'
longName = 'USS Yosemite'
shipFile = 'AdObYosemite' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Oberth Class"
species = App.SPECIES_GALAXY

credits = {
	'modName': 'AdOberth',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.AdObYosemite = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.AdObYosemite.fMaxWarp = 6.0
Foundation.ShipDef.AdObYosemite.fCruiseWarp = 5.2
Foundation.ShipDef.AdObYosemite.desc = 'USS Yosemite'

Foundation.ShipDef.AdObYosemite.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"Plas_glow": {
				0.0: "data/Models/Ships/AdTMP/Oberth/High/Plas_glow.tga", 
				1.0: "data/Models/Ships/AdTMP/Oberth/High/Plas01_glow.tga",
			}
		}
	}
}

if menuGroup:           Foundation.ShipDef.AdObYosemite.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AdObYosemite.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AdYosemiteIDSwap(self):
	retval = {"Textures": [["Hu_glow", "Data/Models/ships/AdTMP/Oberth/High/Yosemite_glow.tga"], ["Dauntless", "Data/Models/ships/AdTMP/Oberth/High/Yosemite_glow.tga"]]}
	return retval

Foundation.ShipDef.AdObYosemite.__dict__["SDT Entry"] = AdYosemiteIDSwap

#Raman
abbrev = 'AdObRaman'
iconName = 'AdPegasus'
longName = 'USS Raman'
shipFile = 'AdObRaman' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Oberth Class"
species = App.SPECIES_GALAXY

credits = {
	'modName': 'AdOberth',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.AdObRaman = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.AdObRaman.fMaxWarp = 6.0
Foundation.ShipDef.AdObRaman.fCruiseWarp = 5.2
Foundation.ShipDef.AdObRaman.desc = 'USS Raman'

Foundation.ShipDef.AdObRaman.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"Plas_glow": {
				0.0: "data/Models/Ships/AdTMP/Oberth/High/Plas_glow.tga", 
				1.0: "data/Models/Ships/AdTMP/Oberth/High/Plas01_glow.tga",
			}
		}
	}
}

if menuGroup:           Foundation.ShipDef.AdObRaman.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AdObRaman.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AdRamanIDSwap(self):
	retval = {"Textures": [["Hu_glow", "Data/Models/ships/AdTMP/Oberth/High/Raman_glow.tga"], ["Dauntless", "Data/Models/ships/AdTMP/Oberth/High/Raman_glow.tga"]]}
	return retval

Foundation.ShipDef.AdObRaman.__dict__["SDT Entry"] = AdRamanIDSwap

#Bonestell
abbrev = 'AdObBonestell'
iconName = 'AdOberth'
longName = 'USS Bonestell'
shipFile = 'AdObBonestell' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Oberth Class"
species = App.SPECIES_GALAXY

credits = {
	'modName': 'AdOberth',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.AdObBonestell = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.AdObBonestell.fMaxWarp = 6.0
Foundation.ShipDef.AdObBonestell.fCruiseWarp = 5.2
Foundation.ShipDef.AdObBonestell.desc = 'USS Bonestell'

Foundation.ShipDef.AdObBonestell.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"Plas_glow": {
				0.0: "data/Models/Ships/AdTMP/Oberth/High/Plas_glow.tga", 
				1.0: "data/Models/Ships/AdTMP/Oberth/High/Plas01_glow.tga",
			}
		}
	}
}

if menuGroup:           Foundation.ShipDef.AdObBonestell.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AdObBonestell.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AdBonestellIDSwap(self):
	retval = {"Textures": [["Hu_glow", "Data/Models/ships/AdTMP/Oberth/High/Bonestell_glow.tga"], ["Dauntless", "Data/Models/ships/AdTMP/Oberth/High/Bonestell_glow.tga"]]}
	return retval

Foundation.ShipDef.AdObBonestell.__dict__["SDT Entry"] = AdBonestellIDSwap

#Biko
abbrev = 'AdObBiko'
iconName = 'AdPegasus'
longName = 'USS Biko'
shipFile = 'AdObBiko' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Oberth Class"
species = App.SPECIES_GALAXY

credits = {
	'modName': 'AdOberth',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.AdObBiko = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.AdObBiko.fMaxWarp = 6.0
Foundation.ShipDef.AdObBiko.fCruiseWarp = 5.2
Foundation.ShipDef.AdObBiko.desc = 'USS Biko'

Foundation.ShipDef.AdObBiko.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"Plas_glow": {
				0.0: "data/Models/Ships/AdTMP/Oberth/High/Plas_glow.tga", 
				1.0: "data/Models/Ships/AdTMP/Oberth/High/Plas01_glow.tga",
			}
		}
	}
}

if menuGroup:           Foundation.ShipDef.AdObBiko.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AdObBiko.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AdBikoIDSwap(self):
	retval = {"Textures": [["Hu_glow", "Data/Models/ships/AdTMP/Oberth/High/Biko_glow.tga"], ["Dauntless", "Data/Models/ships/AdTMP/Oberth/High/Biko_glow.tga"]]}
	return retval

Foundation.ShipDef.AdObBiko.__dict__["SDT Entry"] = AdBikoIDSwap


#Pegasus
abbrev = 'AdObPegasus'
iconName = 'AdPegasus'
longName = 'USS Pegasus'
shipFile = 'AdObPegasus' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Oberth Class"
species = App.SPECIES_GALAXY

credits = {
	'modName': 'AdOberth',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.AdObPegasus = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.AdObPegasus.fMaxWarp = 6.0
Foundation.ShipDef.AdObPegasus.fCruiseWarp = 5.2
Foundation.ShipDef.AdObPegasus.desc = 'USS Pegasus'

Foundation.ShipDef.AdObPegasus.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"Plas_glow": {
				0.0: "data/Models/Ships/AdTMP/Oberth/High/Plas_glow.tga", 
				1.0: "data/Models/Ships/AdTMP/Oberth/High/Plas01_glow.tga",
			}
		}
	}, "Phase Cloak": 10
}

if menuGroup:           Foundation.ShipDef.AdObPegasus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AdObPegasus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AdPegasusIDSwap(self):
	retval = {"Textures": [["Hu_glow", "Data/Models/ships/AdTMP/Oberth/High/Pegasus_glow.tga"], ["Dauntless", "Data/Models/ships/AdTMP/Oberth/High/Pegasus_glow.tga"]]}
	return retval

Foundation.ShipDef.AdObPegasus.__dict__["SDT Entry"] = AdPegasusIDSwap

#Tsiolkovsky
abbrev = 'AdObTsiolkovsky'
iconName = 'AdPegasus'
longName = 'USS Tsiolkovsky'
shipFile = 'AdObTsiolkovsky' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Oberth Class"
species = App.SPECIES_GALAXY

credits = {
	'modName': 'AdOberth',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.AdObTsiolkovsky = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.AdObTsiolkovsky.fMaxWarp = 6.0
Foundation.ShipDef.AdObTsiolkovsky.fCruiseWarp = 5.2
Foundation.ShipDef.AdObTsiolkovsky.desc = 'USS Tsiolkovsky'

Foundation.ShipDef.AdObTsiolkovsky.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"Plas_glow": {
				0.0: "data/Models/Ships/AdTMP/Oberth/High/Plas_glow.tga", 
				1.0: "data/Models/Ships/AdTMP/Oberth/High/Plas01_glow.tga",
			}
		}
	}
}

if menuGroup:           Foundation.ShipDef.AdObTsiolkovsky.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AdObTsiolkovsky.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AdTsiolkovskyIDSwap(self):
	retval = {"Textures": [["Hu_glow", "Data/Models/ships/AdTMP/Oberth/High/Tsiolkovsky_glow.tga"], ["Dauntless", "Data/Models/ships/AdTMP/Oberth/High/Tsiolkovsky_glow.tga"]]}
	return retval

Foundation.ShipDef.AdObTsiolkovsky.__dict__["SDT Entry"] = AdTsiolkovskyIDSwap

#Cochrane
abbrev = 'AdObCochrane'
iconName = 'AdPegasus'
longName = 'USS Cochrane'
shipFile = 'AdObCochrane' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Oberth Class"
species = App.SPECIES_GALAXY

credits = {
	'modName': 'AdOberth',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.AdObCochrane = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.AdObCochrane.fMaxWarp = 6.0
Foundation.ShipDef.AdObCochrane.fCruiseWarp = 5.2
Foundation.ShipDef.AdObCochrane.desc = 'USS Cochrane'

Foundation.ShipDef.AdObCochrane.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"Plas_glow": {
				0.0: "data/Models/Ships/AdTMP/Oberth/High/Plas_glow.tga", 
				1.0: "data/Models/Ships/AdTMP/Oberth/High/Plas01_glow.tga",
			}
		}
	}
}

if menuGroup:           Foundation.ShipDef.AdObCochrane.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AdObCochrane.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AdCochraneIDSwap(self):
	retval = {"Textures": [["Hu_glow", "Data/Models/ships/AdTMP/Oberth/High/Cochrane_glow.tga"], ["Dauntless", "Data/Models/ships/AdTMP/Oberth/High/Cochrane_glow.tga"]]}
	return retval

Foundation.ShipDef.AdObCochrane.__dict__["SDT Entry"] = AdCochraneIDSwap

#Vico
abbrev = 'AdObVico'
iconName = 'AdOberth'
longName = 'USS Vico'
shipFile = 'AdObVico' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Oberth Class"
species = App.SPECIES_GALAXY

credits = {
	'modName': 'AdOberth',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.AdObVico = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.AdObVico.fMaxWarp = 6.0
Foundation.ShipDef.AdObVico.fCruiseWarp = 5.2
Foundation.ShipDef.AdObVico.desc = 'SS Vico'

Foundation.ShipDef.AdObVico.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"Plas_glow": {
				0.0: "data/Models/Ships/AdTMP/Oberth/High/Plas_glow.tga", 
				1.0: "data/Models/Ships/AdTMP/Oberth/High/Plas01_glow.tga",
			}
		}
	}
}

if menuGroup:           Foundation.ShipDef.AdObVico.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AdObVico.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AdVicoIDSwap(self):
	retval = {"Textures": [["Hu_glow", "Data/Models/ships/AdTMP/Oberth/High/Vico_glow.tga"], ["Dauntless", "Data/Models/ships/AdTMP/Oberth/High/Vico_glow.tga"]]}
	return retval

Foundation.ShipDef.AdObVico.__dict__["SDT Entry"] = AdVicoIDSwap