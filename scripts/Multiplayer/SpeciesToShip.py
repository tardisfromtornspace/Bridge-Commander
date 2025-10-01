from bcdebug import debug
import App

# types for initializing objects create from C.
UNKNOWN			= 0
AKIRA			= 1
AMBASSADOR		= 2
GALAXY			= 3
NEBULA			= 4
SOVEREIGN		= 5
BIRDOFPREY		= 6
VORCHA			= 7
WARBIRD			= 8
MARAUDER		= 9
GALOR			= 10
KELDON			= 11
CARDHYBRID		= 12
KESSOKHEAVY		= 13
KESSOKLIGHT		= 14
SHUTTLE			= 15
DEFIANT			= 16
INTREPID		= 17
USSLENNOX		= 18
NORWAY			= 19
NOVA			= 20
MPNEGHVAR		= 21
STEAMRUNNER		= 22
VALDORE			= 23
DELTAFLYER		= 24
PERAGRINEF1		= 25
DANUBEMKI		= 26
DANUBEMKII		= 27
BUG			= 28
LAKOTA			= 29
CARDFREIGHTER		= 30
FREIGHTER		= 31
TRANSPORT		= 32
MVAMPROMETHEUS		= 33
MVAMPROMETHEUSDORSAL	= 34
MVAMPROMETHEUSSAUCER	= 35
MVAMPROMETHEUSVENRAL	= 36
GALAXYSAUCER            = 37
GALAXYSTARDRIVE         = 38
HUTET			= 39
HIDEKI			= 40
BREEN                   = 41
SCIMITAR		= 42
DOMBB			= 43
NOVAII			= 44
AEGIAN			= 45
KAZONRAIDER		= 46
EXCALIBUR		= 47
DOMBC			= 48
GRIFFIN                 = 49
FALCON                  = 50
PRAETOR                 = 51
SHRIKE                  = 52
VENATOR                 = 53
KVORT                   = 54
FIREHAWK                = 55
LCRAPTOR                = 56
ROMULANSHUTTLE          = 57
KLINGONSHUTTLE          = 58
VENTURESCOUT            = 59
JUNK                    = 60
CLOAKFIREBIRDOFPREY     = 61
EXCELSIOR               = 62
FEKLHRMK2               = 63
SABRE                   = 64
CHEYENNE                = 65
KTINGA                  = 66
BORGDIAMOND             = 67
SPHERE                  = 68
WORKERBEE               = 69
SONAB                   = 70
TYPE9                   = 71
TYPE11                  = 72
SOVEREIGNYACHT          = 73
SOVEREIGNYACHTWARP      = 74
EXIMIUS                 = 75
CENTAUR                 = 76
MIRANDA                 = 77
MIRADORN                = 78
CONSTITUTION            = 79
MERCHANTMAN             = 80
KAREMMA                 = 81
VASKHOLHR		= 82
MIRANDAPOD		= 83
FEDCONST		= 84
FEDCONSTOPEN		= 85
ALKESH			= 86
ALKESHTRANSPORT		= 87
ANCIENTCRUISER		= 88
ANCIENTWARSHIP		= 89
ANUBISFLAGSHIP		= 90
APOPHISFLAGSHIP		= 91
BELISKNER		= 92
BELISKNERREFIT		= 93
DANIELJACKSON		= 94
DEATHGLIDER		= 95
DSC304APOLLO		= 96
DSC304DAEDALUS		= 97
DSC304KOROLEV		= 98
DSC304ODYSSEY		= 99
DSC304ODYSSEYREFIT	= 100
DSC304ODYSSEYUPGRADE	= 101
EARLYHATAK		= 102
F302			= 103
GRACESHIP		= 104
HATAKREFIT		= 105
HATAKVARIANT		= 106
HEBRIDANDRONE		= 107
MARTINSSHIP		= 108
MODIFIEDTELTAK		= 109
NEEDLETHREADER		= 110
ONEILL			= 111
ORIFIGHTER		= 112
ORIWARSHIP		= 113
OSIRISCRUISER		= 114
PUDDLEJUMPER		= 115
PYRAMIDSHIP		= 116
REPLICATORBELISKNER	= 117
REPLICATORHATAK		= 118
REPLICATORVESSEL	= 119
REPLICATORWARSHIP	= 120
SATELLITE		= 121
SPIDER			= 122
SUPERWEAPON		= 123
TELTAK			= 124
TELTAKREFIT		= 125
TELTAKUPGRADE		= 126
TELTAKVARIANT		= 127
UPGRADEDHATAK		= 128
VALHALLA		= 129
WRAITHDART		= 130
X301			= 131
X303			= 132
X303REFIT		= 133
X303UPGRADE		= 134
ROMULANOUTPOST	        = 135
CA8472                  = 136
SPACEFACILITY		= 137
COMMARRAY		= 138
COMMLIGHT		= 139
DRYDOCK			= 140
PROBE			= 141
DECOY			= 142
SUNBUSTER		= 143
CARDOUTPOST		= 144
CARDSTARBASE		= 145
CARDSTATION		= 146
FEDOUTPOST		= 147
FEDSTARBASE		= 148
ASTEROID		= 149
ASTEROID1		= 150
ASTEROID2		= 151
ASTEROID3		= 152
AMAGON			= 153
BIRANUSTATION		= 154
ENTERPRISE		= 155
GERONIMO		= 156
PEREGRINE		= 157
ASTEROIDH1		= 158
ASTEROIDH2		= 159
ASTEROIDH3		= 160
ESCAPEPOD		= 161
CARDPOD 		= 162
DEFPOD  		= 163
GALPOD  		= 164
GREENPOD                = 165
KESSOKMINE		= 166
LOWCUBE			= 167
DS9			= 168
MINE                    = 169
CITY                    = 170
STARBASE220             = 171
FIREPOINT               = 172
BIGFIREPOINT            = 173
DRYDOCKREPAIR           = 174
HIDDENCORE              = 175
IMPERIALBASE            = 176
STARBASE329		= 177
VAS_PORT_WING		= 178
VAS_STARPORT_WING	= 179
COWP			= 180
COWPASTEROID		= 181
PULSEMINE		= 182
TORPEDOMINE		= 183
INTREPID_N_LEFT		= 184
INTREPID_N_RIGHT	= 185
BLACKHOLE		= 186
CN_FEDSTARBASE		= 187
ADMINDEF		= 188
RAIDER1			= 189
PROMELLIAN		= 190
QUANTAR			= 191
DJENTERPRISEG		= 192
DJENTERPRISEG_DRIVE	= 193
DJENTERPRISEG_SAUCER	= 194
DJENTERPRISEG_THUNDERB	= 195
SCORPION		= 196
BREENDN			= 197
BREENBCH		= 198
BREENCA			= 199
BREENCL			= 200
BREENDD			= 201
TYPE18			= 202
PHOENIX                 = 203
BREENBB			= 204
SOVEREIGN_NOYACHT	= 205

MAX_SHIPS = 206
MAX_FLYABLE_SHIPS = 156

# Setup tuples
kSpeciesTuple = (
	(None, 0, "Neutral", 0),
	("Akira", 		App.SPECIES_AKIRA, "Federation", 1),
	("Ambassador", 		App.SPECIES_AMBASSADOR, "Federation", 1),
	("Galaxy", 		App.SPECIES_GALAXY, "Federation", 1),
	("Nebula" , 		App.SPECIES_NEBULA, "Federation", 1),
	("Sovereign" , 		App.SPECIES_SOVEREIGN, "Federation", 1),
	("BirdOfPrey", 		App.SPECIES_BIRD_OF_PREY, "Klingon", 1),
	("Vorcha" , 		App.SPECIES_VORCHA, "Klingon", 1),
	("Warbird" , 		App.SPECIES_WARBIRD, "Romulan", 1),
	("Marauder" , 		App.SPECIES_MARAUDER, "Ferengi", 1),
	("Galor" , 		App.SPECIES_GALOR, "Cardassian", 1),
	("Keldon" , 		App.SPECIES_KELDON, "Cardassian", 1),
	("CardHybrid", 		App.SPECIES_CARDHYBRID, "Cardassian", 1),
	("KessokHeavy" , 	App.SPECIES_KESSOK_HEAVY, "Kessok", 1),
	("KessokLight" , 	App.SPECIES_KESSOK_LIGHT, "Kessok", 1),  
	("Shuttle" , 		App.SPECIES_SHUTTLE, "Federation", 1),
	("Defiant",		136, "Federation", 1),
	("LCIntrepid",		114, "Federation", 1),
	("USSLennox",		128, "Federation", 1),
	("norway",		116, "Federation", 1),
	("Nova",		117, "Federation", 1),
	("MPneghvar",		403, "Klingon", 1),
	("Steamrunner",		120, "Federation", 1),
	("ValdoreG",		302, "Romulan", 1),
	("deltaflyer",		112, "Federation", 1),
	("PeragrineF1",		119, "Federation", 1),
	("DanubemkI",		111, "Federation", 1),
        ("DanubemkII",		127, "Federation", 1),
	("bug",			923, "Other", 1),
	("PsExcelsiorRefitTNG1" , 110, "Federation", 1),
	("CardFreighter", 	App.SPECIES_CARDFREIGHTER, "Cardassian", 1),
	("Freighter" , 		App.SPECIES_FREIGHTER, "Federation", 1),
	("Transport" , 		App.SPECIES_TRANSPORT, "Federation", 1),
        ("MvamPrometheus" , 	113, "Federation", 1),
	("MvamPrometheusDorsal" , 121, "Federation", 1),
        ("MvamPrometheusSaucer" , 122, "Federation", 1),
        ("MvamPrometheusVentral" , 123, "Federation", 1),
        ("GalaxySaucer" , 	125, "Federation", 1),
        ("GalaxyStardrive" , 	126, "Federation", 1),
	("Hutet", 		205, "Cardassian", 1),
        ("Hideki", 		206, "Cardassian", 1),
        ("Breen", 		717, "Other", 1),
        ("BreenBB", 		717, "Other", 1),
	("Reman Scimitar" , 	718, "Romulan", 1),
	("DomBB" , 		901, "Other", 1),
	("novaII",		118, "Federation", 1),
	("Aegian",		109, "Federation", 1),
        ("Kazonraider",		915, "Other", 1),
        ("DomBC" , 		902, "Other", 1),
        ("griffin",		303, "Romulan", 1),
        ("Falcon",		304, "Romulan", 1),
        ("Praetor",		305, "Romulan", 1),
        ("Shrike",		306, "Romulan", 1),
        ("venator",		307, "Romulan", 1),
        ("Kvort",		404, "Klingon", 1),
        ("Firehawk",		308, "Romulan", 1),
        ("LCRaptor",		309, "Romulan", 1),
        ("romulanshuttle", 	310, "Romulan", 1),
        ("KlingonShuttle", 	405, "Klingon", 1),
        ("VentureScout",	139, "Federation", 1),
        ("Junk",		918, "Other", 1),
        ("CloakFireBirdOfPrey",	App.SPECIES_BIRD_OF_PREY, "Klingon", 1),
        ("ExcelsiorP81" , 	129, "Federation", 1),
        ("FeklhrMK2",		406, "Klingon", 1),
        ("Sabre",		130, "Federation", 1),
        ("Cheyenne",		131, "Federation", 1),
        ("Phoenix",		132, "Federation", 1),
        ("KTinga",		407, "Klingon", 1),
        ("BorgDiamond" , 	720, "Borg", 1),
        ("sphere" , 		721, "Borg", 1),
        ("WorkerBee",		919, "Other", 1),
        ("SonaB",		920, "Other", 1),
        ("type9",		133, "Federation", 1),
        ("Type11",		146, "Federation", 1),
        ("sovereignyacht",	134, "Federation", 1),
        ("sovereignyachtwarp",	135, "Federation", 1),
        ("WCNemEntEyacht",	134, "Federation", 1),
        ("WCNemEntEnoyacht",	135, "Federation", 1),
        ("Eximius",		143, "Federation", 1),
        ("LCCentaur",   	144, "Federation", 1),
        ("Miranda",   		147, "Federation", 1),
        ("Miradorn", 		922, "Other", 1),
        ("EnterpriseNCC1701",   148, "Federation", 1),
        ("Merchantman", 	924, "Other", 1),
        ("Karemman", 		925, "Other", 1),
	("VasKholhr", 		311, "Romulan", 1),
	("ZZSaratogaPod2", 	150, "Federation", 1),
	("FedConst",		140, "Federation", 1),
	("FedConstOpen",	141, "Federation", 1),
	("scorpion",		719, "Romulan", 1),
	("BreenDN",		722, "Other", 1),
	("BreenBCH",		723, "Other", 1),
	("BreenCA",		724, "Other", 1),
	("BreenCL",		725, "Other", 1),
	("BreenDD",		726, "Other", 1),
	("SFRD_T18",		158, "Federation", 1),
	("Raider1",		927, "Other", 1),
	("SFRD_Promellian",	928, "Other", 1),
	("QuanTar",		929, "Other", 1),
	("DJEnterpriseG",	159, "Federation", 1),
	("DJEnterpriseGDrive",	160, "Federation", 1),
	("DJEnterpriseGSaucer",	161, "Federation", 1),
	("DJEnterpriseGThunderbird",	162, "Federation", 1),
        ("DyExcalibur",		138, "Federation", 1),
	("RomulanOutpost", 	716, "Romulan", 1),
        ("CA8472" , 		903, "Other", 1),
	("SpaceFacility" , 	App.SPECIES_SPACE_FACILITY, "Federation", 1),
	("CommArray" , 		App.SPECIES_COMMARRAY, "Federation", 1),
	("CommLight", 		App.SPECIES_COMMLIGHT, "Cardassian", 1),
	("DryDock" , 		App.SPECIES_DRYDOCK, "Federation", 1),
	("Probe" , 		App.SPECIES_PROBE, "Federation", 1),
	("Decoy" , 		App.SPECIES_PROBETYPE2, "Federation", 1),
	("Sunbuster" , 		App.SPECIES_SUNBUSTER, "Kessok", 1),
	("CardOutpost" , 	App.SPECIES_CARD_OUTPOST, "Cardassian", 1),
	("CardStarbase" , 	App.SPECIES_CARD_STARBASE, "Cardassian", 1),
	("CardStation" , 	App.SPECIES_CARD_STATION, "Cardassian", 1),
	("FedOutpost" , 	App.SPECIES_FED_OUTPOST, "Federation", 1),
	("FedStarbase" , 	App.SPECIES_FED_STARBASE, "Federation", 1),
	("Asteroid" , 		App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroid1" , 		App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroid2" , 		App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroid3" , 		App.SPECIES_ASTEROID, "Neutral", 1),
	("Amagon", 		App.SPECIES_ASTEROID, "Cardassian", 1),
	("BiranuStation", 	App.SPECIES_SPACE_FACILITY, "Neutral", 1),
	("Enterprise", 		App.SPECIES_SOVEREIGN, "Federation", 1),
	("Geronimo", 		App.SPECIES_AKIRA, "Federation", 1),
	("Peregrine", 		App.SPECIES_NEBULA, "Federation", 1),
	("Asteroidh1" , 	App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroidh2" , 	App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroidh3" , 	App.SPECIES_ASTEROID, "Neutral", 1),
	("Escapepod" , 		App.SPECIES_ESCAPEPOD, "Neutral", 1),
        ("card pod" , 		App.SPECIES_ESCAPEPOD, "Neutral", 1),
        ("defpod" , 		App.SPECIES_ESCAPEPOD, "Neutral", 1),
        ("Galaxy Escape Pod" , 	App.SPECIES_ESCAPEPOD, "Neutral", 1),
        ("greenmisc" , 		App.SPECIES_ESCAPEPOD, "Neutral", 1),
	("KessokMine" , 	App.SPECIES_KESSOKMINE, "Kessok", 1),
	("LowCube" , 		App.SPECIES_BORG, "Borg", 1),
	("ds9" , 		137, "Federation", 1),
	("AdminDef" ,		157, "Federation", 1),
        ("Mine" , 		155, "Federation", 1),
        ("City", 		917, "Neutral", 1),
        ("Starbase220", 	145, "Federation", 1),
        ("Firepoint", 		App.SPECIES_PROBE, "Other", 1),
        ("BigFirepoint", 	App.SPECIES_PROBE, "Other", 1),
        ("DryDockRepair", 	App.SPECIES_DRYDOCK, "Federation", 1),
        ("HiddenCore",		921, "Other", 1),
        ("KlingonImperialStarbase",	408, "Klingon", 1),
	("StarBase329", 	149, "Federation", 1),
	("VasKholhr_PortWing",	312, "Romulan", 1),
	("VasKholhr_Starboardwing",	313, "Romulan", 1),
	("cOWP", 		207, "Cardassian", 1),
	("CowpAsteroid", 	208, "Cardassian", 1),
	("pulsemine", 		151, "Federation", 1),
	("torpedomine", 	152, "Federation", 1),
	("LCIntrepid_n_left", 	153, "Federation", 1),
	("LCIntrepid_n_right", 	154, "Federation", 1),
	("blackhole", 		926, "Other", 1),
	("CN_FedStarbase",	156, "Federation", 1),
	("Alkesh" , 		878, "Stargate", 1),
	("AlkeshTransport" , 	879, "Stargate", 1),
	("AncientCruiser", 	825, "Stargate", 1),
	("AncientWarship", 	827, "Stargate", 1),
	("AnubisFlagship" , 	880, "Stargate", 1),
	("ApophisFlagship" , 	881, "Stargate", 1),
	("Beliskner", 		817, "Stargate", 1),
	("BelisknerRefit" , 	818, "Stargate", 1),
	("DanielJackson" , 	819, "Stargate", 1),
	("DeathGlider" , 	882, "Stargate", 1),
	("DSC304Apollo" , 	848, "Stargate", 1),
	("DSC304Daedalus" , 	850, "Stargate", 1),
	("DSC304Korolev" , 	852, "Stargate", 1),
	("DSC304Odyssey" , 	853, "Stargate", 1),
	("DSC304OdysseyRefit" , 854, "Stargate", 1),
	("DSC304OdysseyUpgrade" , 855, "Stargate", 1),
	("EarlyHatak" , 	883, "Stargate", 1),
	("F302", 		857, "Stargate", 1),
	("GraceShip" , 		800, "Stargate", 1),
	("HatakRefit" , 	892, "Stargate", 1),  
	("HatakVariant" , 	893, "Stargate", 1),
	("HebridanDrone" , 	802, "Stargate", 1),
	("MartinsShip" , 	804, "Stargate", 1),
	("ModifiedTelTak" , 	894, "Stargate", 1),
	("NeedleThreader", 	895, "Stargate", 1),
	("ONeill", 		820, "Stargate", 1),
	("OriFighter" , 	813, "Stargate", 1),
	("OriWarship" , 	815, "Stargate", 1),
	("OsirisCruiser", 	607, "Stargate", 1),
	("PuddleJumper" , 	832, "Stargate", 1),
	("PyramidShip" , 	600, "Stargate", 1),
	("ReplicatorBeliskner" , 836, "Stargate", 1),
	("ReplicatorHatak" , 	837, "Stargate", 1),
	("ReplicatorVessel" , 	838, "Stargate", 1),
	("ReplicatorWarship" , 	839, "Stargate", 1),
	("Satellite" , 		840, "Stargate", 1),
	("Spider" , 		841, "Stargate", 1),
	("Superweapon" , 	608, "Stargate", 1),
	("TelTak" , 		602, "Stargate", 1),
	("TelTakRefit", 	603, "Stargate", 1),
	("TelTakUpgrade" , 	604, "Stargate", 1),
	("TelTakVariant", 	605, "Stargate", 1),
	("UpgradedHatak" , 	606, "Stargate", 1),
	("Valhalla", 		821, "Stargate", 1),
	("WraithDart" , 	823, "Stargate", 1),
	("X301", 		874, "Stargate", 1),
	("x303" , 		875, "Stargate", 1),
	("X303Refit", 		876, "Stargate", 1),
	("X303Upgrade", 	877, "Stargate", 1),

	(None, 0, "Neutral", 1))
	
def GetShipFromSpecies(iSpecies):
    debug(__name__ + ", GetShipFromSpecies")
    # fix signed stuff
    if iSpecies < 0:
	    iSpecies = iSpecies + 256
    debug(__name__ + ", GetShipFromSpecies num %d" % iSpecies)
    if ((iSpecies <= 0) or (iSpecies >= MAX_SHIPS)):
	debug(__name__ + ", GetShipFromSpecies return None")
        return None
    pSpecTuple = kSpeciesTuple[iSpecies]
    pcScript = pSpecTuple[0]
    debug(__name__ + ", GetShipFromSpecies Loading %s" % pcScript)
    ShipScript = __import__(('ships.' + pcScript))
    ShipScript.LoadModel()
    return ShipScript.GetShipStats()


def GetScriptFromSpecies(iSpecies):
    debug(__name__ + ", GetScriptFromSpecies")
    if ((iSpecies <= 0) or (iSpecies >= MAX_SHIPS)):
        return None
    pSpecTuple = kSpeciesTuple[iSpecies]
    return pSpecTuple[0]


def InitObject(self, iType):
        debug(__name__ + ", InitObject")
        kStats = GetShipFromSpecies(iType)
	debug(__name__ + ", InitObject: GetShipFromSpecies Done")
        if (kStats == None):
		debug(__name__ + ", InitObject bye")
                return 0
        self.SetupModel(kStats['Name'])
	debug(__name__ + ", InitObject: SetupModel Done")
	sShipScript = GetScriptFromSpecies(iType)
	if sShipScript:
		self.SetScript('ships.' + sShipScript)
        pPropertySet = self.GetPropertySet()
        if kStats.has_key("NormalHP"):
                mod = __import__(('ships.Hardpoints.' + kStats["NormalHP"]))
        else:
                mod = __import__(('ships.Hardpoints.' + kStats['HardpointFile']))
        App.g_kModelPropertyManager.ClearLocalTemplates()
        reload(mod)
        mod.LoadPropertySet(pPropertySet)
	debug(__name__ + ", SetupProperties")
        self.SetupProperties()
        self.UpdateNodeOnly()
	debug(__name__ + ", InitObject End")
        return 1


def CreateShip(iType):
        debug(__name__ + ", CreateShip")
        kStats = GetShipFromSpecies(iType)
        if (kStats == None):
                return None
        pShip = App.ShipClass_Create(kStats['Name'])
        sModule = ('ships.' + kSpeciesTuple[iType][0])
        pShip.SetScript(sModule)
        pPropertySet = pShip.GetPropertySet()
        mod = __import__(('ships.Hardpoints.' + kStats['HardpointFile']))
        App.g_kModelPropertyManager.ClearLocalTemplates()
        reload(mod)
        mod.LoadPropertySet(pPropertySet)
        pShip.SetupProperties()
        pShip.UpdateNodeOnly()
        pShip.SetNetType(iType)
        return pShip


def GetIconNum(iSpecies):
    debug(__name__ + ", GetIconNum")
    pSpecTuple = kSpeciesTuple[iSpecies]
    iNum = pSpecTuple[1]
    return iNum


def GetSideFromSpecies(iSpecies):
    debug(__name__ + ", GetSideFromSpecies")
    pSpecTuple = kSpeciesTuple[iSpecies]
    pcSide = pSpecTuple[2]
    return pcSide


def GetClassFromSpecies(iSpecies):
    debug(__name__ + ", GetClassFromSpecies")
    pSpecTuple = kSpeciesTuple[iSpecies]
    iClass = pSpecTuple[3]
    return iClass

