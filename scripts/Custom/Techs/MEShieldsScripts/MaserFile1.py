# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 17th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the MEShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/MEShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file adds Masers (a type of invisible laser, which ME barriers excluding reapers cannot even block partially) to the list of guaranteed bleedthrough to ME Shields, according to MEShields in-script documentation. Due to the parent script implementation, we could add multiple files that add elements, and repeated elements on the lists will not be repeatedly included on the parent script

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
# On this case, we want to add the equivalent to this:
#{"ProjectileName": {"GuaranteedBleedthrough": 0.1, "WhitelistFilename": ["Quantum", "QuantumTorpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"], "BlacklistFilename": ["AntiQuantum", "Quantumania"]}

ProjectileName = "maser"
ProjectileGuaranteedBleedthrough = 1.0
ProjectileWhitelistFilename = ["Maser", "MaserBeam"]  # Case-sensitive
ProjectileBlacklistName = ["not a maser", " not maser", " no maser", " anti-maser", "antimaser", "mimaser"]  # Case-insensitive
ProjectileBlacklistFilename = ["AntiMaser", "NotAMaser", "Turbomaser", "TurboMaser"]  # Case-sensitive
#ProjRacesImmune = ["Reaper"]

# Below here we have an example for beams
# {"BeamName": {"GuaranteedBleedthrough": 0.05, "WhitelistHardname": ["Ventral Phaser 1"], "BlacklistName": ["not a phaser", "notphaser", "laser", "nophaser"]}
BeamName = "maser"
BeamGuaranteedBleedthrough = 1.0
BeamWhitelistHardname = ["GARDIAN Maser 1", "GARDIAN Maser 2", "Maser Beam", "Maser beam"]
BeamBlacklistName = ["not a maser", "notmaser", "antimaser", "nomaser", "turbomaser", "turbo-maser"]
#BeamRacesImmune = ["Reaper"]