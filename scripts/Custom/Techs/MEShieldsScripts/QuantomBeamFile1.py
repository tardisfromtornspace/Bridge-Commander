# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 25th January 2026, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the MEShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/MEShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file adds "quantom" ("Quantom Gravimetric Drive") to the list of guaranteed bleedthrough to ME Shields (according to the info about particle beam weapons from collectors "Being a particle beam weapon, it ignores kinetic barriers,"), according to MEShields in-script documentation. Due to the parent script implementation, we could add multiple files that add elements, and repeated elements on the lists will not be repeatedly included on the parent script.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
# On this case, we want to add the equivalent to this:
#{"ProjectileName": {"GuaranteedBleedthrough": 0.1, "WhitelistFilename": ["Quantum", "QuantumTorpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"], "BlacklistFilename": ["AntiQuantum", "Quantumania"]}

#ProjectileName = "quantom" # Commented because it is a quantom beam and there are too many typos to trust a quantum torpedo out there...
#ProjectileGuaranteedBleedthrough = 0.4
#ProjectileWhitelistFilename = ["PhasedQuantom"]  # Case-sensitive
#ProjectileBlacklistName = ["not a quantom", "not quantom", "no quantom", "not a phased quantom", "not phased quantom", "no phased quantom", "not a phase quantom", "not phase quantom", "no phase quantom",]  # Case-insensitive
#ProjectileBlacklistFilename = []  # Case-sensitive
#ProjRacesImmune = ["Reaper"]

# Below here we have an example for beams
# {"BeamName": {"GuaranteedBleedthrough": 0.05, "WhitelistHardname": ["Ventral Phaser 1"], "BlacklistName": ["not a phaser", "notphaser", "laser", "nophaser"]}
BeamName = "quantom"
BeamGuaranteedBleedthrough = 0.65
BeamWhitelistHardname = ["Quantom"]
BeamBlacklistName = ["not a quantom", "not quantom", "no quantom", "not a phased quantom", "not a phased quantom", "no phased quantom", "not a phase quantom", "not phase quantom", "no phase quantom", "quantomania",]
#BeamRacesImmune = ["Reaper"]