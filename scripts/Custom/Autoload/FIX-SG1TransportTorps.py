# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 12th April 2025
# By Alex SL Gato
# SG1 Transport Torps Variant.py 0.1.3 by USS Sovereign -> missing SG 2.0 and new ships fix
# Changes:
# ========
# - 12.04.2025 (version 0.1.4):
#  As of SG1 Transport Torps Variant.py 0.1.3, the script works nicely, but does not include some of the stock vessels from Stargate Pack 2.0 and 3.0 that should have this, plus a patch was needed to cover extra ships, too
#

#################################################################################################################
#
MODINFO = { "Author": "\"USS Sovereign\" uss882000@yahoo.co.uk (original) and \"Alex SL Gato\" andromedavirgoa@gmail.com (this patch)",
	    "Version": "0.1.4",
	    "License": "All Rights Reserved to USS Sovereign for the original file 'Only to be used in SG1 Pack. Don't steal the code... you know the drill.', LGPL for this Autoload patch file in particular",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

from bcdebug import debug
import App
import nt
import string
import traceback

banana = None

global myGoodPlugin
myGoodPlugin = "Custom.QBautostart.SG1TransportTorps"

necessaryToUpdate = 0
try:
	try:
		banana = __import__(myGoodPlugin, globals(), locals())

		if banana != None:
			if hasattr(banana, "MODINFO"):
				if banana.MODINFO.has_key("Version") and banana.MODINFO["Version"] < MODINFO["Version"]:
					necessaryToUpdate = 1

	except:
		print "FIX-SG1TransportTorps: Error, could not load " + str(myGoodPlugin) + ":"
		traceback.print_exc()
		necessaryToUpdate = 0
except:
    print "Unable to find FoundationTech.py install"
    pass

if banana != None and necessaryToUpdate:
	# This theoretically should give us all functions and their globals... but it doesn't somehow
	from Custom.QBautostart.SG1TransportTorps import *
	originalShipCheck = banana.ShipCheck

# The updated function, to include the new vessels
	def NewShipCheck(pObject, pEvent):
		global AvailableTorps, TorpedoCount
	
		# grab some values
		pPlayer = MissionLib.GetPlayer()

	
		# With each ET_SET_PLAYER Event reset the torp counter
		TorpedoCount = AvailableTorps
	
		# just to be safe delete the menu
		RemoveMenu()

		# Ship checks using the list given to me. 
		if (GetShipType(pPlayer) == "Daedalus"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304Daedalus"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304DaedalusRefit"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304DaedalusRefitS"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "Korolev"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304Korolev"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "Odyssey"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304Odyssey"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "OdysseyRefit"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304OdysseyRefit"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "OdysseyUpgrade"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304OdysseyUpgrade"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "Apollo"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304Apollo"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304ApolloRefit"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304ApolloRefitS"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304SunTzu"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304SunTzuRefit"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "DSC304SunTzuRefitS"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "PrometheusRefit"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "X303Refit"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "PrometheusUpgrade"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "X303RefitUpgrade"):
			BuildMenu()

		elif (GetShipType(pPlayer) == "X303Upgrade"):
			BuildMenu()

		else:
			return

	banana.ShipCheck = NewShipCheck
