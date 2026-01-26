# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 17th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the MEShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/MEShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file adds uv-rays (a type of invisible laser, which ME barriers excluding reapers cannot even block partially) to the list of guaranteed bleedthrough to ME Shields, according to MEShields in-script documentation. Due to the parent script implementation, we could add multiple files that add elements, and repeated elements on the lists will not be repeatedly included on the parent script

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
# On this case, we want to add the equivalent to this:
#{"ProjectileName": {"GuaranteedBleedthrough": 0.1, "WhitelistFilename": ["Quantum", "QuantumTorpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"], "BlacklistFilename": ["AntiQuantum", "Quantumania"]}

ProjectileName = "uv-ray"
ProjectileGuaranteedBleedthrough = 1.0
ProjectileWhitelistFilename = ["uv-ray", "uv ray"]  # Case-sensitive
ProjectileBlacklistName = ["not an uv-ray", " not uv-ray", " no uv-ray", " anti-uv-ray", "antiuv-ray"]  # Case-insensitive
ProjectileBlacklistFilename = ["Antiuv-ray", "Notanuv-ray", "Turbouv-ray", "Turbouv-Ray"]  # Case-sensitive
#ProjRacesImmune = ["Reaper"]

# Below here we have an example for beams
# {"BeamName": {"GuaranteedBleedthrough": 0.05, "WhitelistHardname": ["Ventral Phaser 1"], "BlacklistName": ["not a phaser", "notphaser", "laser", "nophaser"]}
BeamName = "uv-ray"
BeamGuaranteedBleedthrough = 1.0
BeamWhitelistHardname = ["Ultraviolet Ray 1", "Ultraviolet Ray 2", "Ultraviolet Ray 3", "Ultraviolet Ray 4", "Ultraviolet Ray 5", "Ultraviolet Ray 6", "Ultraviolet Ray 7", "Ultraviolet Ray 8", "Ultraviolet Ray 9", "Ultraviolet Ray 10", "Ultraviolet Ray 11", "Ultraviolet Ray 12", "Ultraviolet Ray 13", "Ultraviolet Ray 14", "Ultraviolet Ray 15", "Ultraviolet Ray 16", "Ultraviolet Ray 17", "Ultraviolet Ray 18", "Ultraviolet Ray 19", "Ultraviolet Ray 20"]
BeamBlacklistName = ["not an uv-ray", "notuv-ray", "antiuv-ray", "nouv-ray", "turbouv-ray"]
#BeamRacesImmune = ["Reaper"]