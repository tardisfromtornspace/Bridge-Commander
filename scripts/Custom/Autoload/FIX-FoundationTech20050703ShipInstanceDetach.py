# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 30th April 2024
# By Alex SL Gato
# FoundationTech.py by Dasher and the Foundation Technologies team -> ShipInstance.DetachShipTechs and ShipInstance.DetachTechs fix
#
# Changes: 
# - As of FoundationTech 20050703:
# -- ShipInstance.DetachTechs uses a "for i in self.lTechs" to then remove the i from such lTechs. This seems to lead to strange behaviour where some techs listed on lTechs are never called, specially when more complex technologies are called. This has been corrected on this patch.
# -- ShipInstance.DetachShipTechs and ShipInstance.DetachTechs are sequential and not single-error proof, that is, they iterate over the ship technologies and have no try-catch blocks around those tech Detach functions, so if a new technology on a ship breaks something during its own Detach, the error will prevent any tech after that to detach from that ship. This has been corrected as well, so now does not only keep detaching unrelated technologies from the list, but will also catch those exceptions and print the traceback, something modders and new users will appreciate.
# -- Any Detach function was only called when an object was destroyed, not when an object was deleted (such as, for example, ending Simulation, or some more esoteric ways to remove a ship), giving cleanup issues.


from bcdebug import debug
import App
import FoundationTech
import Foundation
import traceback

necessaryToUpdate = 0
try:

	if hasattr(Foundation,"version"):
		if int(Foundation.version[0:8]) < 20231231: # we are gonna assume the 2023 version and previous versions lack this
			necessaryToUpdate = 1
	else:
		necessaryToUpdate = 1 # the oldest versions have a signatre, except maybe some prototypes	

except:
    print "Unable to find FoundationTech.py install"
    pass

if necessaryToUpdate:
	original1 = FoundationTech.ShipInstance.DetachTechs
	original2 = FoundationTech.ShipInstance.DetachShipTechs
	originalNonSerializedObjects = FoundationTech.NonSerializedObjects
	if originalNonSerializedObjects:
		tempNonSerializedObjects = list(originalNonSerializedObjects)
		tempNonSerializedObjects.append("oRemoveDeletedShip")
		oRemoveDeletedShip = FoundationTech.RemoveShip('RemoveShip', App.ET_OBJECT_DELETED, FoundationTech.dMode)
		FoundationTech.oRemoveShip = oRemoveDeletedShip
		NewNonSerializedObjects = tuple(tempNonSerializedObjects)
		FoundationTech.NonSerializedObjects = NewNonSerializedObjects


	def NewDetachTechs(self):
		debug(__name__ + ", DetachTechs")
		if self.pShipID:
			try:
				self.DetachShipTechs()
			except:
				print "Error in FoundationTech.DetachTechs:"
				traceback.print_exc()

		tempTechs = []
		for i in self.lTechs:
			tempTechs.append(i)

		for i in tempTechs:
			try:
				i.Detach(self)
			except:
				print "Error in FoundationTech.DetachTechs:"
				traceback.print_exc()

		del tempTechs

	def NewDetachShipTechs(self):
		debug(__name__ + ", DetachShipTechs")
		tempTechs = []
		for i in self.lTechs:
			tempTechs.append(i)

		for i in tempTechs:
			try:
				i.DetachShip(self.pShipID, self)
			except:
				print "Error in FoundationTech.DetachShipTechs:"
				traceback.print_exc()
		del tempTechs

	if original1 != None:
		FoundationTech.ShipInstance.DetachTechs = NewDetachTechs
	if original2 != None:
		FoundationTech.ShipInstance.DetachShipTechs = NewDetachShipTechs
	print "Updated FoundationTech.ShipInstance Detach-related fixes"
