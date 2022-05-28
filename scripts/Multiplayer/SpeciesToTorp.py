import App

# types for initializing torps create from C.
UNKNOWN = 0
DISRUPTOR = 1
PHOTON = 2
QUANTUM = 3
ANTIMATTER = 4
CARDTORP = 5
KLINGONTORP = 6
POSITRON = 7
PULSEDISRUPT = 8
FUSIONBOLT = 9
CARDASSIANDISRUPTOR = 10
KESSOKDISRUPTOR = 11
PHASEDPLASMA = 12
POSITRON2 = 13
PHOTON2 = 14
ROMULANCANNON = 15
A2AMISSILES = 16
A2AMISSILES2 = 17
ALKESHBOMB = 18
ANCIENTCANONS = 19
ASGARDPULSE = 20
ASURANCANONS = 21
AURORACANONS = 22
DRONES = 23
DRONES2 = 24
F302CANNON = 25
F302MISSILE = 26
GRACEPULSE = 27
HEBRIDANDRONE = 28
HIVEPULSE = 29
IONCANNON = 30
IONCANNON2 = 31
IONCANNON3 = 32
IONCANNON4 = 33
IONPULSE = 34
IONPULSE2 = 35
IONPULSE3 = 36
IONPULSE4 = 37
IONPULSE5 = 38
MARK8TACTICAL = 39
ORICANON = 40
ORIPULSE = 41
RAILGUNA = 42
REPLICATORPROJECTILE = 43
REPLICATORPROJECTILE2 = 44
SGSTAFF = 45
SGSTAFF2 = 46
SGSTAFF3 = 47
SGSTAFF4 = 48
SGSTAFF5 = 49
SGSTAFF6 = 50
SGSTAFF7 = 51
SGSTAFF8 = 52
SGSTAFF9 = 53
WRAITHBLAST = 54
MAX_TORPS = 55

# Setup tuples
kSpeciesTuple = ((UNKNOWN, None),
	(DISRUPTOR, "Disruptor"),
	(PHOTON, "PhotonTorpedo"),
	(QUANTUM, "QuantumTorpedo"),
	(ANTIMATTER, "AntimatterTorpedo"),
	(CARDTORP, "CardassianTorpedo"),
	(KLINGONTORP, "KlingonTorpedo"),
	(POSITRON, "PositronTorpedo"),
	(PULSEDISRUPT, "PulseDisruptor"),
	(FUSIONBOLT, "FusionBolt"),
	(CARDASSIANDISRUPTOR, "CardassianDisruptor"),
	(KESSOKDISRUPTOR, "KessokDisruptor"),
	(PHASEDPLASMA, "PhasedPlasma"),
	(POSITRON2, "Positron2"),
	(PHOTON2, "PhotonTorpedo2"),
	(ROMULANCANNON, "RomulanCannon"),
	(A2AMISSILES, "A2AMissiles"),
	(A2AMISSILES2, "A2AMissiles2"),
	(ALKESHBOMB, "AlkeshBomb"),
	(ANCIENTCANONS, "AncientCanons"),
	(ASGARDPULSE, "AsgardPulse"),
	(ASURANCANONS, "AsuranCanons"),
	(AURORACANONS, "AuroraCanons"),
	(DRONES, "Drones"),
	(DRONES2, "Drones2"),
	(F302CANNON, "F302Cannon"),
	(F302MISSILE, "F302Missile"),
	(GRACEPULSE, "GracePulse"),
	(HEBRIDANDRONE, "HebridanDrone"),
	(HIVEPULSE, "HivePulse"),
	(IONCANNON, "IonCannon"),
	(IONCANNON2, "IonCannon2"),
	(IONCANNON3, "IonCannon3"),
	(IONCANNON4, "IonCannon4"),
	(IONPULSE, "IonPulse"),
	(IONPULSE2, "IonPulse2"),
	(IONPULSE3, "IonPulse3"),
	(IONPULSE4, "IonPulse4"),
	(IONPULSE5, "IonPulse5"),
	(MARK8TACTICAL, "Mark8Tactical"),
	(ORICANON, "OriCanon"),
	(ORIPULSE, "OriPulse"),
	(RAILGUNA, "RailGunA"),
	(REPLICATORPROJECTILE, "ReplicatorProjectile"),
	(REPLICATORPROJECTILE2, "ReplicatorProjectile2"),
	(SGSTAFF, "sgstaff"),
	(SGSTAFF2, "sgstaff2"),
	(SGSTAFF3, "sgstaff3"),
	(SGSTAFF4, "sgstaff4"),
	(SGSTAFF5, "sgstaff5"),
	(SGSTAFF6, "sgstaff6"),
	(SGSTAFF7, "sgstaff7"),
	(SGSTAFF8, "sgstaff8"),
	(SGSTAFF9, "sgstaff9"),
	(WRAITHBLAST, "WraithBlast"),
	(MAX_TORPS, None))

def CreateTorpedoFromSpecies (iSpecies):
	if (iSpecies <= 0 or iSpecies >= MAX_TORPS):
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	pcScript = pSpecTuple [1]

	pTorp = App.Torpedo_Create (pcScript)
	return pTorp

def GetScriptFromSpecies (iSpecies):
	if (iSpecies <= 0 or iSpecies >= MAX_TORPS):
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	return pSpecTuple [1]
	
def InitObject (self, iType):
	# Get the script
	pcScript = GetScriptFromSpecies (iType)
	if (pcScript == None):
		return 0

	# call create function to initialize the torp.
	mod = __import__("Tactical.Projectiles." + pcScript)
	mod.Create(self)	

	self.UpdateNodeOnly ()

	return 1;
	
