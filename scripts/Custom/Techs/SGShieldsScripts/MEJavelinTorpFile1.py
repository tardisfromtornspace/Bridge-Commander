# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 18th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.1
# Meant to be used alongside the SGShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGShieldsScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file adds Mass Effect javelin torpedoes to the list of guaranteed bleedthrough to SG Shields, according to SGShields in-script documentation. Due to the parent script implementation, we could add multiple files that add elements, and repeated elements on the lists will not be repeatedly included on the parent script

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
# On this case, we want to add the equivalent to this:
#{"ProjectileName": {"GuaranteedBleedthrough": 0.1, "WhitelistFilename": ["Quantum", "QuantumTorpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"], "BlacklistFilename": ["AntiQuantum", "Quantumania"]}

ProjectileName = "mass effect javelin"
ProjectileGuaranteedBleedthrough = 0.5
ProjectileWhitelistFilename = ["MEJavelinTorp"]  # Case-sensitive
ProjectileBlacklistName = ["not a mass effect", "not a mass-effect", "not a masseffect", " not mass effect", " not masseffect", " not mass-effect", " no mass effect", " no masseffect", " no mass-effect", "anti-mass effect", "anti-mass-effect", "antimasseffect"]  # Case-insensitive
ProjectileBlacklistFilename = ["Javelin"]  # Case-sensitive
#ProjRacesImmune = ["Reaper"]

# Below here we have an example for phasers - something which btw I totally do not think can penetrate SG Shields, it's just an example I used for testing bleedthrough and which I leave here in case somebody wants to add on another file a certain type of beam to bypass SG Shields
# {"BeamName": {"GuaranteedBleedthrough": 0.05, "WhitelistHardname": ["Ventral Phaser 1"], "BlacklistName": ["not a phaser", "notphaser", "laser", "nophaser"]}
#BeamName = "Phaser"
#BeamGuaranteedBleedthrough = 0.05
#BeamWhitelistHardname = ["Ventral Phaser 1"]
#BeamBlacklistName = ["not a phaser", "notphaser", "laser", "nophaser"]
#BeamRacesImmune = ["Ori"]