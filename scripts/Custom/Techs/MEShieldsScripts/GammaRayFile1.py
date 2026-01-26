# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 17th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the MEShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/MEShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file adds gamma-rays (a type of invisible laser, which ME barriers excluding reapers cannot even block partially) to the list of guaranteed bleedthrough to ME Shields, according to MEShields in-script documentation. Due to the parent script implementation, we could add multiple files that add elements, and repeated elements on the lists will not be repeatedly included on the parent script

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
# On this case, we want to add the equivalent to this:
#{"ProjectileName": {"GuaranteedBleedthrough": 0.1, "WhitelistFilename": ["Quantum", "QuantumTorpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"], "BlacklistFilename": ["AntiQuantum", "Quantumania"]}

ProjectileName = "gamma-ray"
ProjectileGuaranteedBleedthrough = 1.0
ProjectileWhitelistFilename = ["gamma-ray", "gamma ray"]  # Case-sensitive
ProjectileBlacklistName = ["not a gamma-ray", " not gamma-ray", " no gamma-ray", " anti-gamma-ray", "antigamma-ray"]  # Case-insensitive
ProjectileBlacklistFilename = ["Antigamma-ray", "Notagamma-ray", "Turbogamma-ray", "Turbogamma-Ray"]  # Case-sensitive
#ProjRacesImmune = ["Reaper"]

# Below here we have an example for beams
# {"BeamName": {"GuaranteedBleedthrough": 0.05, "WhitelistHardname": ["Ventral Phaser 1"], "BlacklistName": ["not a phaser", "notphaser", "laser", "nophaser"]}
BeamName = "gamma-ray"
BeamGuaranteedBleedthrough = 1.0
BeamWhitelistHardname = ["Gamma Ray 1", "Gamma Ray 2", "Gamma Ray 3", "Gamma Ray 4", "Gamma Ray 5", "Gamma Ray 6", "Gamma Ray 7", "Gamma Ray 8", "Gamma Ray 9", "Gamma Ray 10", "Gamma Ray 11", "Gamma Ray 12", "Gamma Ray 13", "Gamma Ray 14", "Gamma Ray 15", "Gamma Ray 16", "Gamma Ray 17", "Gamma Ray 18", "Gamma Ray 19", "Gamma Ray 20"]
BeamBlacklistName = ["not a gamma-ray", "notgamma-ray", "antigamma-ray", "nogamma-ray", "turbogamma-ray"]
#BeamRacesImmune = ["Reaper"]