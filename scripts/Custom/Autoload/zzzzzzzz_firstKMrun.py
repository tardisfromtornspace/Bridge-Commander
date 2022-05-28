import App
import Foundation
import gameinfo

lUMMEnable = [
("Master Switch", 1),
("EraSelection", 1),
("GravityFXConfig", 1),
("KMIntro09", 1),
("BridgePlugin", 1),
("JaggieFix", 1),
("DS9FXConfig", 1),
("GalaxyChartsConfig", 1),
("BCSTheBeginning", 1),
("FoundationMutators", 1),
("NanoFX", 1),
("ExtraResolutions", 1),
("QBStartShipSelector", 1),
("LoadGameConfig", 1),
("DS9FX: Game Crash Fix", 1),
]


sCurKMVer = App.g_kConfigMapping.GetStringValue("General Options", "KM Version")


if sCurKMVer != gameinfo.GAME_TAG:
	print "KM Version changed, enabling all Mods"

	# UMM
	for k in lUMMEnable:
		App.g_kConfigMapping.SetIntValue("Unified MainMenu Mod Configuration", k[0], k[1])

	# Foundation
	for i in Foundation.mutatorList:
		i.Enable()
	Foundation.SaveConfig()
		
	App.g_kConfigMapping.SetStringValue("General Options", "KM Version", gameinfo.GAME_TAG)
	App.g_kConfigMapping.SaveConfigFile("Options.cfg")
