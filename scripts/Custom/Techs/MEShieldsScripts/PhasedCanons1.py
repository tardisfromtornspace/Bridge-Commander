# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 25th January 2026, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the MEShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/MEShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file adds Phase Canons to the list of guaranteed bleedthrough to ME Shields (according to the info about particle beam weapons from collectors "Being a particle beam weapon, it ignores kinetic barriers,"), according to MEShields in-script documentation. Due to the parent script implementation, we could add multiple files that add elements, and repeated elements on the lists will not be repeatedly included on the parent script.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
# On this case, we want to add the equivalent to this:
#{"ProjectileName": {"GuaranteedBleedthrough": 0.1, "WhitelistFilename": ["Quantum", "QuantumTorpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"], "BlacklistFilename": ["AntiQuantum", "Quantumania"]}

ProjectileName = "phased canon"
ProjectileGuaranteedBleedthrough = 0.8
ProjectileWhitelistFilename = ["PhasedCanon"]  # Case-sensitive
ProjectileBlacklistName = ["not a phased canon", "not phased canon", "no phased canon", ]  # Case-insensitive
ProjectileBlacklistFilename = []  # Case-sensitive
#ProjRacesImmune = ["Reaper"]

# Below here we have an example for beams
# {"BeamName": {"GuaranteedBleedthrough": 0.05, "WhitelistHardname": ["Ventral Phaser 1"], "BlacklistName": ["not a phaser", "notphaser", "laser", "nophaser"]}
BeamName = "phased canon"
BeamGuaranteedBleedthrough = 0.8
BeamWhitelistHardname = ["Phased Canon 1", "Phased Canon 2", "Phased Canon", "Lance phased canon"]
BeamBlacklistName = ["not a phased canon", "not phased canon", "no phased canon",]
#BeamRacesImmune = ["Reaper"]