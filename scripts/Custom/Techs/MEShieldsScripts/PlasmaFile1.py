# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 17th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the MEShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/MEShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file adds Quantum torpedoes to the list of guaranteed bleedthrough to ME Shields, according to MEShields in-script documentation. Due to the parent script implementation, we could add multiple files that add elements, and repeated elements on the lists will not be repeatedly included on the parent script

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
# On this case, we want to add the equivalent to this:
#{"ProjectileName": {"GuaranteedBleedthrough": 0.1, "WhitelistFilename": ["Quantum", "QuantumTorpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"], "BlacklistFilename": ["AntiQuantum", "Quantumania"]}

ProjectileName = "plasma"
ProjectileGuaranteedBleedthrough = 0.5
ProjectileWhitelistFilename = ["Plasma", "PlasmaCannon"]  # Case-sensitive
ProjectileBlacklistName = ["not a plasma", " not plasma", " no plasma", " anti-plasma", "antilplasma", "plasmatic", "cataplasma",]  # Case-insensitive
ProjectileBlacklistFilename = ["AntiPlasma", "NotAPlasma", ]  # Case-sensitive
#ProjRacesImmune = ["Reaper"]

# Below here we have an example for beams
# {"BeamName": {"GuaranteedBleedthrough": 0.05, "WhitelistHardname": ["Ventral Phaser 1"], "BlacklistName": ["not a phaser", "notphaser", "laser", "nophaser"]}
BeamName = "plasma"
BeamGuaranteedBleedthrough = 0.5
BeamWhitelistHardname = ["Plasma Cannon", "Plasma Canon", "Plasma Round", "Plasma Beam", "Plasma beam"]
BeamBlacklistName = ["not a plasma", " not plasma", " no plasma", " anti-plasma", "antilplasma", "plasmatic", "cataplasma",]
#BeamRacesImmune = ["Reaper"]