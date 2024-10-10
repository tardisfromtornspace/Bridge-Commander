"""
#         SolidProjectiles
#         10th October 2024
#         Modification by Alex SL Gato of ftb/Tech/SolidProjectiles.py, most likely by FoundationTechnologies team
#         Also based slightly on Turrets script by Alex SL Gato.
#################################################################################################################
# This tech update gives a torpedo or disruptor projectile the ability to fire a ship alongside it. Due to how base FoundationTech does not have a proper OnFire for projectiles fired from Pulse Weapon systems, the torpedo or disrupter needs to be fired from a Torpedo Launcher to work.
# The update to the original was made so the technology actually works in a cleaner manner, in order not to leave random flying ships floating invisible around the map and to fix an error with a casting.
# HOW-TO-ADD:
# At the bottom of your torpedo projectile file add this (Between the ### and ###), replacing the fields with proper values:
# Note that if a projectile has a torpedo model, the torpedo ship will not orient itself, but if the ship has a disruptor model, it will.
# Fields:
# - "sModel": literally the ship from scripts/Ships folder. That is, if we wanted a scripts/ships/ambassador ship to be deployed with the torpedo, then we make it "sModel" : "ambassador". Recommended to make the ship one without any warp engines or elements of the sort to avoid possible conflicts with certain warp or alternate FTL scripts.
###
import traceback

try:
	import FoundationTech
	import ftb.Tech.SolidProjectiles
	oFire = ftb.Tech.SolidProjectiles.Rocket('Spatial Projectiles', {"sModel" : "ambassador"})
	FoundationTech.dOnFires[__name__] = oFire
	FoundationTech.dYields[__name__] = oFire
except:
	print "Error when firing solid projectile"
	traceback.print_exc()
###
Known Bugs (ordered by priority):
-1. Unfortunately, like the original, after firing, the game will crash every time you try to get out of the system, nearly every time you try to end Simulation, and nearly every time a ship dies.
"""
#################################################################################################################
from bcdebug import debug
import App
import FoundationTech
import loadspacehelper
import MissionLib
import traceback

#################################################################################################################
MODINFO = { "Author": "\"Alex SL Gato and likely the ftb Team\" andromedavirgoa@gmail.com",
	    "Version": "0.02",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#################################################################################################################

REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209
TIME_TO_DELETE_TORP = App.UtopiaModule_GetNextEventType() #Maybe App.ET_TORPEDO_EXITED_SET could work?

dTorpShips = {}

class Rocket(FoundationTech.TechDef):
	def __init__(self, name, dict = None):
		debug(__name__ + ", __init__")
		FoundationTech.TechDef.__init__(self, name, dict)
		self.__dict__.update(dict)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.RemoveBroadcastHandler(TIME_TO_DELETE_TORP, self.pEventHandler, "RemoveTorp")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(TIME_TO_DELETE_TORP, self.pEventHandler, "RemoveTorp")

	def OnFire(self, pEvent, pTorp):
		debug(__name__ + ", OnFire")
		#print 'SolidTorpedoTorpedo.OnFire'

		pTorpID = pTorp.GetObjID()
		if not pTorpID:
			return
		try:
			delay = pTorp.GetLifetime() - 0.25
			if delay < 0.0:
				delay = 0.0

			pEvent2 = App.TGIntEvent_Create()
			pEvent2.SetEventType(TIME_TO_DELETE_TORP)
			pEvent2.SetSource(pEvent.GetSource())
			pEvent2.SetDestination(pEvent.GetDestination())
			pEvent2.SetInt(int(pTorpID))

			pTimer = App.TGTimer_Create()
			pTimer.SetTimerStart( App.g_kUtopiaModule.GetGameTime()+delay )
			pTimer.SetDelay(0)
			pTimer.SetDuration(0)
			pTimer.SetEvent(pEvent2)

			App.g_kTimerManager.AddTimer(pTimer)

			#print "Creating ship:", self.sModel, pTorp.GetContainingSet(), "SolidTorpedo"+str(pTorpID)
			#print "pTorp set is ", pTorp.GetContainingSet()
			pcName = "SolidTorpedo" + str(pTorpID)
			pSet = pTorp.GetContainingSet()
			pTorpShip = loadspacehelper.CreateShip(self.sModel, pSet, pcName, "")
			pTorpShipA = App.ShipClass_GetObject(pSet, pcName)
			if not pTorpShipA:
				print "Sorry, unable to add ship"
				return

			pTorpShipA.SetCollisionFlags(0)
			pTorpShipA.UpdateNodeOnly()
			pTorpShipA.SetTranslateXYZ( 0, 0, 0)

			#pTorpShipA.ClearAI() #.SetAI(StarbaseNeutralAI.CreateAI(pShip))

			#pProxManager = pSet.GetProximityManager()
			#if pProxManager:
			#	pProxManager.RemoveObject(pTorpShipA) # This removes the Subship from the proximity manager without causing a crash when a ship dies or changes set
			pTorpShipA.UpdateNodeOnly()

			# pTorpShipA.SetHailable(0) TO-DO ADD A CUSTOM OPTION?

			"""
			pMission = MissionLib.GetMission()
			pFriendlies     = None
			pEnemies        = None
			pNeutrals       = None
			pTractors       = None

			if pMission:
				pFriendlies     = pMission.GetFriendlyGroup() 
				pEnemies        = pMission.GetEnemyGroup() 
				pNeutrals       = pMission.GetNeutralGroup()
				pTractors       = pMission.GetTractorGroup()

				pFriendlies.RemoveName(pTorpShipA.GetName())
				pEnemies.RemoveName(pTorpShipA.GetName())
				pNeutrals.RemoveName(pTorpShipA.GetName())
				pTractors.RemoveName(pTorpShipA.GetName())
				pTractors.AddName(pTorpShipA.GetName())

			pTorpShipA.UpdateNodeOnly()
			"""

			global dTorpShips

			dTorpShips[pTorpID] = [pTorpShip, pTimer]

			pTorp.AttachObject(pTorpShipA)
			pTorp.UpdateNodeOnly()


		except:
			print "Creating ship failed somehow..."
			traceback.print_exc()

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		debug(__name__ + ", OnYield")

		pTorpID = pTorp.GetObjID()
		pTorp = App.Torpedo_GetObjectByID(None, pTorpID)
		if not pTorp:
			return

		global dTorpShips

		if not (dTorpShips.has_key(pTorpID) and dTorpShips[pTorpID]):
			return


		pTorpShip = App.ShipClass_GetObjectByID(None, dTorpShips[pTorpID][0].GetObjID())
		if pTorpShip:
			pTorp.DetachObject(pTorpShip)

			pSet = pTorpShip.GetContainingSet()
			if pSet:
				DeleteObjectFromSet(pSet, pTorpShip.GetName())

		try:
			App.g_kTimerManager.DeleteTimer(dTorpShips[pTorpID][1].GetObjID())
			del dTorpShips[pTorpID][1]
		except:
			print "Error on SolidProjectiles' onYield"
			traceback.print_exc()

		del dTorpShips[pTorpID]

	def RemoveTorp(self, pEvent):
		debug(__name__ + ", RemoveTorp")
		global dTorpShips

		thisEventType = pEvent.GetEventType()
		pTorpID = pEvent.GetInt()

		if dTorpShips.has_key(pTorpID):
			try:
				App.g_kTimerManager.DeleteTimer(dTorpShips[pTorpID][1].GetObjID())
				del dTorpShips[pTorpID][1]

			except:
				print "Error on SolidProjectiles' RemoveTorp"
				traceback.print_exc()

			pTorp = App.Torpedo_GetObjectByID(None, pTorpID)
			pTorpShip = App.ShipClass_GetObjectByID(None, dTorpShips[pTorpID][0].GetObjID())
			if pTorpShip:
				if pTorp:
					pTorp.DetachObject(pTorpShip)

				pSet = pTorpShip.GetContainingSet()
				if pSet:
					DeleteObjectFromSet(pSet, pTorpShip.GetName())

			del dTorpShips[pTorpID]

def DeleteObjectFromSet(pSet, sObjectName):
        if not MissionLib.GetShip(sObjectName):
                return

        pSet.DeleteObjectFromSet(sObjectName)
	#pSet.RemoveObjectFromSet(sObjectName)
        
        # send clients to remove this object
        if App.g_kUtopiaModule.IsMultiplayer():
                # Now send a message to everybody else that the score was updated.
                # allocate the message.
                pMessage = App.TGMessage_Create()
                pMessage.SetGuaranteed(1)                # Yes, this is a guaranteed packet
                        
                # Setup the stream.
                kStream = App.TGBufferStream()                # Allocate a local buffer stream.
                kStream.OpenBuffer(256)                                # Open the buffer stream with a 256 byte buffer.
        
                # Write relevant data to the stream.
                # First write message type.
                kStream.WriteChar(chr(REMOVE_POINTER_FROM_SET))

                # Write the name of killed ship
                for i in range(len(sObjectName)):
                        kStream.WriteChar(sObjectName[i])
                # set the last char:
                kStream.WriteChar('\0')

                # Okay, now set the data from the buffer stream to the message
                pMessage.SetDataFromStream(kStream)

                # Send the message to everybody but me.  Use the NoMe group, which
                # is set up by the multiplayer game.
                pNetwork = App.g_kUtopiaModule.GetNetwork()
                if not App.IsNull(pNetwork):
                        if App.g_kUtopiaModule.IsHost():
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                        else:
                                pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

                # We're done.  Close the buffer.
                kStream.CloseBuffer()
        return 0