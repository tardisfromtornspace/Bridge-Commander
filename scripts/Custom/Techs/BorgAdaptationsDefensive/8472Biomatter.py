# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 15 June 2023, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used along with the BorgAdaptation Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/BorgAdaptationsDefensive
def defenseCounterRdm(): # Establishes a random factor - values must be >= 0. The greater the value, the more range can happen between sessions.
	return 650000
def defenseCounter(): # Establishes the minimum number of strikes before it adapts, stacking along the random value above - please notice some weapons deal multi-strikes. Values must be >= 0
	return 1950000