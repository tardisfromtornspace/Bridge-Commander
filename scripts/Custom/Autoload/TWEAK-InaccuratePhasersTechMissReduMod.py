# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 21st July 2025
# VERSION 0.1
# By Alex SL Gato
#
# Changes: 
# - This file is related to the FoolTargeting Tech and makes all phasers to not miss. EDITED: It will only apply the reduced formula for now.

from bcdebug import debug
import App


necessaryToUpdate = 0
FoolTargeting = None
try:
	import Foundation
	import FoundationTech
	necessaryToUpdate = 1
except:
	print "Unable to find fTech"
	necessaryToUpdate = 0
	pass

if necessaryToUpdate == 1:
	try:
		FoolTargeting = __import__("Custom.Techs.FoolTargeting")
	except:
		FoolTargeting = None
	if FoolTargeting != None and hasattr(FoolTargeting,"ApplyPseudoMonkeyPatch") and hasattr(FoolTargeting,"necessaryToUpdate") and hasattr(FoolTargeting,"basicMissMult"):
			FoolTargeting.ApplyPseudoMonkeyPatch()
			FoolTargeting.necessaryToUpdate = 0
			FoolTargeting.basicMissMult = 1.0 # EDITED FOR CUSTOM USE, IT WAS 0.0
			print "Patched FoolTargeting to not miss from regular InaccurateFire"