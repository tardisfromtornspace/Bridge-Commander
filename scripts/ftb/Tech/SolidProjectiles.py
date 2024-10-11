"""
#         SolidProjectiles
#         10th October 2024
#         Modification by Alex SL Gato, Greystar and JohnKuhns777 of ftb/Tech/SolidProjectiles.py, most likely by FoundationTechnologies team
#         Also based slightly on Turrets script by Alex SL Gato.
#################################################################################################################
# This tech update gives a torpedo or disruptor projectile the ability to fire a ship alongside it. Due to how base FoundationTech does not have a proper OnFire for projectiles fired from Pulse Weapon systems, the torpedo or disrupter needs to be fired from a Torpedo Launcher to work.
# The update to the original was made so the technology actually works in a cleaner manner, in order not to leave random flying ships floating invisible around the map and to fix an error with a casting.
# HOW-TO-ADD:
# At the bottom of your torpedo projectile file add this (Between the ### and ###), replacing the fields with proper values.
# If you want to combine multiple projectiel technologies that use FoundationTech.dOnFires and FoundationTech.dYields, then create a custom function inside the projectile file that calls the aforementioned technologies.
# Note that if a projectile has a torpedo model, the torpedo ship will not orient itself, but if the ship has a disruptor model, it will.
# Fields:
# - "sModel": literally the ship from scripts/Ships folder. That is, if we wanted a scripts/ships/ambassador ship to be deployed with the torpedo, then we make it "sModel" : "ambassador". Recommended to make the ship one without any warp engines or elements of the sort to avoid possible conflicts with certain warp or alternate FTL scripts.
# - "sScale": changes the model's size with respect to the original.
# - "sShield": value of 1 means shields will be in whatever state they are normally set when a non-player ship is added (which, in most cases, means shields up), value of 0 means shields down, value of 2 will guarantee shields. Default is 1.
# - "sCollide": represents status of collisions. 0 means it's like a ghost for weapons and collisions. -1 (or lesser) ensures it's like a ghost, removing the torpedo ship from the proximity manager fully. 1, if enabled, will attempt to keep some degree of tangibility, so weapons cannot pass through, but ships can. 2 will attempt to keep tangibility and collidability too but avoiding the parent ship colliding (in practice though, it is nearly identical to 1, without any of the potential glitches, so mode 1 is currently disabled). Any other positive or disabled value will make the ship fully collidable, which is totally NOT recommended. Please consider any configuration that restores tangibility will make the AI freak out for having incoming ships trying to collide with them. Default is 0.
# - "sHideProj": if you want the projectile whose torpedo ship is attached to visible (1) or not (0). Default is 0.
# - "sTargetable": if you want the vessel attached to the torpedo to be targetable by players (1) or not (0). Default is 1.
# TO-DO OPTION TO MAKE THE TORPEDO INVISIBLE!!! SetHidden
# - "sAI": imagine your torpedo vessel firing back. This is a dictionary with some fields:
# -- "AI": here you must include a CreateAI function to add an AI to make the ship act. Default is CreateAI from this file. Custom AIs need to be tailored so "def CreateAI" function has two fields, pShip and whoIattack, respectively.
# -- "Side": here you either indicate if you want your AI to be "Friendly", "Enemy", "Neutral" or "Tractor" compared with parent ship. Default is tractor group.
# -- "Team": here you either indicate if you want your ship to be on the "Friendly", "Enemy", "Neutral" or "Tractor" groups compared with parent ship. Default is tractor group.
###
import traceback

try:
	import FoundationTech
	import ftb.Tech.SolidProjectiles
	# The line below is a hypotehthical example if you want customized AI - uncomment and adjust accordingly if you want
	#import path.to.tailoredAI.tailoredAIfilename
	#myAIfunction = tailoredAIfilename.CreateAI
	# Remember, if you don't want AI, do not add the "sAI" field.
	#oFire = ftb.Tech.SolidProjectiles.Rocket('Spatial Projectiles', {"sModel" : "ambassador", "sScale" : 1.0, "sShield": 1, "sCollide": 0, "sHideProj": 0, "sTargetable": 1, "sAI": {"AI": myAIfunction, "Side": None, "Team": None}})
	oFire = ftb.Tech.SolidProjectiles.Rocket('Spatial Projectiles', {"sModel" : "ambassador", "sScale" : 1.0, "sShield": 1, "sCollide": 0, "sHideProj": 0, "sTargetable": 1}) 
	FoundationTech.dOnFires[__name__] = oFire
	FoundationTech.dYields[__name__] = oFire
except:
	print "Error with firing solid projectile"
	traceback.print_exc()
###
Known Bugs (ordered by priority):
- 1. [FIXED] With sCollide set to 1 with original functions enabled, ships can in fact crash the game if the player tries to end the simulation if and only if one of those ships is still active. In pro of cautiousness mode 1 is disabled.
- 2. Firing these torpedoes while at warp makes the targets unhittable with these torpedoes (as, the projectile does not collide with the targets). No other effects. Torps keep working correctly outside warp as intended.
- 3. Even when tangible, ONLY phasers can hit, no projectiles. 
- 4. Trying to tractor a torpedo ship may cause it to teleport.
- 5. Due to the nature of Warp mods (with Warp being a common set for all warp travels in general), if a ship enters Warp from system A to B, fires torpedoes while on the Warp set, leaves Warp and then rapidly enters Warp again, they may still see temporary previous solid projectiles.
- 6. While killing a torpedo ship causes no real issues, killing one of them with a phaser causes the vessel to teleport as a temporary dying ghost for a millisecond.
"""
#################################################################################################################
from bcdebug import debug
import App
import FoundationTech
import loadspacehelper
import MissionLib
import string
import traceback

#################################################################################################################
MODINFO = { "Author": "\"Alex SL Gato, Greystar, JohnKuhns777 and likely the ftb Team\" andromedavirgoa@gmail.com",
	    "Version": "0.2",
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
dShipsTorp = {} # Reverse dict for a thing

#Special AI for ship

def CreateAI(pShip, whoIattack): # We need a tailored function for us TO-DO
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	debug(__name__ + ", CreateAI")

	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, whoIattack)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait

# TO-DO CREATE AL ALTERNATIVE CLASS CALLED HERE THAT TAKES CARE OF ACTUAL THINGS WHIEL THE TORPS TAKE CARE OF ANOTHER
class AuxInitiater(FoundationTech.TechDef):
	def __init__(self, name, dict = None):
		debug(__name__ + ", __init__")
		FoundationTech.TechDef.__init__(self, name, dict)
		self.__dict__.update(dict)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.RemoveBroadcastHandler(TIME_TO_DELETE_TORP, self.pEventHandler, "RemoveTorp")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(TIME_TO_DELETE_TORP, self.pEventHandler, "RemoveTorp")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, self.pEventHandler, "RemoveTorp2")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_OBJECT_EXPLODING, self.pEventHandler, "RemoveTorp2")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_TORPEDO_EXITED_SET, self.pEventHandler, "RemoveTorp3") # TO-DO CHECK THIS ONE MAYBE?
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_TORPEDO_EXITED_SET, self.pEventHandler, "RemoveTorp3")

	def CreateTimer(self, pEvent, pTorp, pTorpID, delay = 0.0):
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

		return pTimer

	def CreateShip(self, pEvent, pTorp, pTorpID, sModel, sScale, sShield, sCollide, sHideProj, sTargetable, sAI):
		#print "Creating ship:", sModel, pTorp.GetContainingSet(), "SolidTorpedo"+str(pTorpID)
		#print "pTorp set is ", pTorp.GetContainingSet().GetName()

		pcName = "SolidTorpedo" + str(pTorpID)
		pSet = pTorp.GetContainingSet()

		pTorpShip = loadspacehelper.CreateShip(sModel, None, pcName, None) # Adding the ship to a set then changing its flags generates a glitch which causes the game to crash when a ship dies, warps out or the player reloads. Thus, we first create the ship, add the flags, and then we add it to the set.
		if not pTorpShip:
			print "Sorry, unable to add ship"
			return None

		# If we set the collision flags before adding it to the set, no more issues happen
		if sCollide <= 0:
			pTorpShip.SetCollisionFlags(0)
			#pTorpShip.SetCollisionsOn(0)
			pTorpShip.UpdateNodeOnly()
		else:
			pTorpShip.SetCollisionFlags(1)

		if not pSet.AddObjectToSet(pTorpShip, pcName):
			# Delete the ship.
			pDeletionEvent = App.TGEvent_Create()
			pDeletionEvent.SetEventType(App.ET_DELETE_OBJECT_PUBLIC)
			pDeletionEvent.SetDestination(pTorpShip)
			App.g_kEventManager.AddEvent(pDeletionEvent)

			return None

		pTorpShipA = App.ShipClass_GetObject(pSet, pcName)
		if not pTorpShipA:
			print "Sorry, unable to add ship"
			return None

		pTorpShipA.SetTranslateXYZ( 0, 0, 0)
		if sScale > 0.0 and sScale != 1.0:
			pTorpShipA.SetScale(sScale)
			
		if pTorpShipA.GetShields():
			if sShield == 0:
				pTorpShipA.GetShields().TurnOff()
			elif sShield == 2:
				pTorpShipA.GetShields().TurnOn()

		#TO-DO ADD AI OPTIONS?
		#pTorpShipA.ClearAI() #.SetAI(StarbaseNeutralAI.CreateAI(pShip))

		pShip = App.ShipClass_GetObjectByID(None, pTorp.GetParentID())
		if sCollide <= -1:
			pProxManager = pSet.GetProximityManager()
			if pProxManager:
				pProxManager.RemoveObject(pTorpShipA) # This removes the Subship from the proximity manager without causing a crash when a ship dies or changes set.
		#elif sCollide == 1: # This makes a strange combo - cannot be damaged by its own torpedo nor cannot be collided with, but now weapons can actually hit its hull.
		#	pTorpShip.SetCollisionFlags(0)
		#	pTorpShip.UpdateNodeOnly()
		elif sCollide == 2: # Ships are fully collidable
			if pShip:
				pShip.EnableCollisionsWith(pTorpShip, 0)
				pTorpShip.EnableCollisionsWith(pShip, 0)

		pTorpShipA.SetHidden(0) # guarantees the vessel is visible
		pTorpShipA.UpdateNodeOnly()

		#if sTargetable <= 0:
		#	pTorpShipA.SetTargetable(0)


		# OK so from what I gathered, for some reason, these vessels are not in any group, not even the tractor group!
		pMission = MissionLib.GetMission()
		pFriendlies     = None
		pEnemies        = None
		pNeutrals       = None
		pTractors       = None

		
		if pMission:
			#import Custom.QuickBattleGame.QuickBattle
			pFriendlies     = pMission.GetFriendlyGroup() 
			pEnemies        = pMission.GetEnemyGroup() 
			pNeutrals       = pMission.GetNeutralGroup()
			pNeutrals2      = App.ObjectGroup_FromModule("Custom.QuickBattleGame.QuickBattle", "pNeutrals2")
			pTractors       = pMission.GetTractorGroup()

			
			if pFriendlies.IsNameInGroup(pcName):
				pFriendlies.RemoveName(pcName)
			if pEnemies.IsNameInGroup(pcName):
				pEnemies.RemoveName(pcName)
			if pNeutrals.IsNameInGroup(pcName):
				pNeutrals.RemoveName(pcName)
			if pNeutrals2 and pNeutrals2.IsNameInGroup(pcName):
				pNeutrals2.RemoveName(pcName)
			if pTractors.IsNameInGroup(pcName):
				pTractors.RemoveName(pcName)

			parentAlignment = "None"
			parentTeam = None
			parentName = None
			if pShip:
				parentName = pShip.GetName()
				if pFriendlies.IsNameInGroup(parentName):
					parentTeam = pFriendlies
					parentAlignment = "pFriendlies"
				if pEnemies.IsNameInGroup(parentName):
					parentTeam = pEnemies
					parentAlignment = "pEnemies"
				if pNeutrals.IsNameInGroup(parentName):
					parentTeam = pNeutrals
					parentAlignment = "pNeutrals"
				if pNeutrals2 and pNeutrals2.IsNameInGroup(parentName):
					parentTeam = pNeutrals2
					parentAlignment = "pNeutrals2"
				if pTractors.IsNameInGroup(parentName):
					parentTeam = pTractors
					parentAlignment = "pTractors"

			# TO-DO AI HERE
			if sAI != None and sAI.has_key("AI"):
				if sAI.has_key("Team"):
					team = sAI["Team"]
					if team != None and pShip and parentTeam != None:
						if string.lower(team) == "friendly":
							parentTeam.AddName(pTorpShipA.GetName())
						elif string.lower(team) == "enemy":
							if parentAlignment != "None":
								if parentAlignment == "pFriendlies":
									pEnemies.AddName(pTorpShipA.GetName())
								elif parentAlignment == "pEnemies" or parentAlignment == "pNeutrals2":
									pFriendlies.AddName(pTorpShipA.GetName())
								elif parentAlignment == "pTractors":
									pNeutrals.AddName(pTorpShipA.GetName())
								else:
									pTractors.AddName(pTorpShipA.GetName())
							else:
								pTractors.AddName(pTorpShipA.GetName())
						elif string.lower(team) == "neutral":
							pNeutrals.AddName(pTorpShipA.GetName())
						else:
							pTractors.AddName(pTorpShipA.GetName())
					else:
						pTractors.AddName(pTorpShipA.GetName())
				else:
					pTractors.AddName(pTorpShipA.GetName())

				if sAI.has_key("Side"):
					side = sAI["Side"]
					if side != None and side != "None":
						ai = sAI["AI"] # function
						if ai == None:
							ai = CreateAI

						if parentAlignment != "None" and parentTeam != None:
							if string.lower(side) == "friendly":
								whoIattack = pTractors
								if parentAlignment == "pFriendlies":
									whoIattack = pEnemies
								elif parentAlignment == "pEnemies":
									whoIattack = pFriendlies
								elif parentAlignment == "pTractors" or parentAlignment == "pNeutrals2":
									whoIattack = pNeutrals

								pShip.SetAI(ai(pTorpShipA, whoIattack))
							
							elif string.lower(team) == "enemy":
								pShip.SetAI(ai(pTorpShipA, parentTeam))

							elif string.lower(team) == "neutral":
								pShip.SetAI(ai(pTorpShipA, pNeutrals))
							else:
								pShip.SetAI(ai(pTorpShipA, pTractors))
						else:
							pShip.SetAI(ai(pTorpShipA, pTractors))

			else:
				pTractors.AddName(pTorpShipA.GetName())

		pTorpShipA.UpdateNodeOnly()

		return pTorpShipA
					
	def RemoveTorp(self, pEvent):
		debug(__name__ + ", RemoveTorp")
		thisEventType = pEvent.GetEventType()
		pTorpID = pEvent.GetInt()
		if pTorpID:
			self.RemoveTorpAux(pEvent, pTorpID)

	def RemoveTorp3(self, pEvent):
		debug(__name__ + ", RemoveTorp3")
		pTorp = App.Torpedo_Cast(pEvent.GetDestination())
		
		pTorpID = pTorp.GetObjID()
		if pTorpID:
			self.RemoveTorpAux(pEvent, pTorpID)

	def RemoveTorpAux(self, pEvent, pTorpID):
		debug(__name__ + ", RemoveTorpAux")
		global dTorpShips, dShipsTorp
		if dTorpShips.has_key(pTorpID):
			try:
				if dTorpShips.has_key(pTorpID) and dTorpShips[pTorpID] != None and dTorpShips[pTorpID][1] != None:
					App.g_kTimerManager.DeleteTimer(dTorpShips[pTorpID][1].GetObjID())
					dTorpShips[pTorpID][1] = None
			except:
				print "Error on SolidProjectiles' RemoveTorpAux:"
				traceback.print_exc()

			pTorp = App.Torpedo_GetObjectByID(None, pTorpID)
			pTorpShip = App.ShipClass_GetObjectByID(None, dTorpShips[pTorpID][0])
			if pTorpShip:
				if dShipsTorp.has_key(dTorpShips[pTorpID][0]):
					del dShipsTorp[dTorpShips[pTorpID][0]]
				if pTorp:
					pTorp.DetachObject(pTorpShip)

				pSet = pTorpShip.GetContainingSet()
				if pSet:
					DeleteObjectFromSet(pSet, pTorpShip.GetName())
					pTorpShip.SetDeleteMe(1)

			del dTorpShips[pTorpID]

	def RemoveTorp2(self, pEvent):
		debug(__name__ + ", RemoveTorp2")
		global dTorpShips, dShipsTorp
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip:
			pTorpShipID = pShip.GetObjID()
			if pTorpShipID:
				pTorpShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
				if pTorpShip and dShipsTorp.has_key(pTorpShipID) and dShipsTorp[pTorpShipID] != App.NULL_ID:
					pTorpID = dShipsTorp[pTorpShipID]
					pTorp = App.Torpedo_GetObjectByID(None, pTorpID)
					if pTorp:
						pTorp.SetLifetime(0.0)
					del dShipsTorp[pTorpShipID]
					try:
						if dTorpShips.has_key(pTorpID) and dTorpShips[pTorpID] != None and dTorpShips[pTorpID][1] != None:
							App.g_kTimerManager.DeleteTimer(dTorpShips[pTorpID][1].GetObjID())
							dTorpShips[pTorpID][1] = None
					except:
						print "Error on SolidProjectiles' RemoveTorp2:"
						traceback.print_exc()

auxIniti = AuxInitiater("Solid Projectile helper", {})

class Rocket(FoundationTech.TechDef):
	def __init__(self, name, dict = None):
		debug(__name__ + ", __init__")
		FoundationTech.TechDef.__init__(self, name, dict)
		self.__dict__.update(dict)

		#loadspacehelper.PreloadShip(self.sModel, 6)

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
			pTimer = auxIniti.CreateTimer(pEvent, pTorp, pTorpID, delay)

			if not hasattr(self, "sScale") or self.sScale <= 0.0:
				self.sScale = 1.0
			if not hasattr(self, "sShield") or self.sShield <= 0.0:
				self.sShield = 1.0
			if not hasattr(self, "sCollide") or self.sCollide < -1:
				self.sCollide = 0
			if not hasattr(self, "sHideProj") or self.sHideProj <= 0:
				self.sHideProj = 0
			if self.sHideProj > 1:
				self.sHideProj = 1
			self.sHideProj = round(self.sHideProj)

			if not hasattr(self, "sTargetable") or self.sTargetable > 1:
				self.sTargetable = 1
			if self.sTargetable <= 0:
				self.sTargetable = 0
			self.sTargetable = round(self.sTargetable)

			if not hasattr(self, "sAI"):
				self.sAI = None
			elif self.sAI != None: # So it has an AI
				if not self.sAI.has_key("AI"):
					self.sAI["AI"] = None
				if not self.sAI.has_key("Side"):
					self.sAI["Side"] = "Tractor"
				if not self.sAI.has_key("Team"):
					self.sAI["Team"] = "Tractor"
				#"sAI": {"AI": None, "Side": None, "Team": None}

			pTorpShipA = auxIniti.CreateShip(pEvent, pTorp, pTorpID, self.sModel, self.sScale, self.sShield, self.sCollide, self.sHideProj, self.sTargetable, self.sAI)

			global dTorpShips, dShipsTorp

			pTorpShipID = pTorpShipA.GetObjID()
			dTorpShips[pTorpID] = [pTorpShipID, pTimer]
			dShipsTorp[pTorpShipID] = pTorpID

			pTorp.AttachObject(pTorpShipA)
			pTorp.SetHidden(self.sHideProj)
			pTorp.UpdateNodeOnly()
			#pTorpShipA.SetDeleteMe(1)
			#pSet.AddObjectToSet(pTorpShipA, pcName)

		except:
			print "Creating ship failed somehow..."
			traceback.print_exc()

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		debug(__name__ + ", OnYield")

		pTorpID = pTorp.GetObjID()
		pTorp = App.Torpedo_GetObjectByID(None, pTorpID)
		if not pTorp:
			return

		global dTorpShips, dShipsTorp

		if not (dTorpShips.has_key(pTorpID) and dTorpShips[pTorpID]):
			return

		pTorpShip = App.ShipClass_GetObjectByID(None, dTorpShips[pTorpID][0])
		if pTorpShip:
			if dShipsTorp.has_key(dTorpShips[pTorpID][0]):
				del dShipsTorp[dTorpShips[pTorpID][0]]
			pTorp.DetachObject(pTorpShip)

			pSet = pTorpShip.GetContainingSet()
			if pSet:
				DeleteObjectFromSet(pSet, pTorpShip.GetName())
				pTorpShip.SetDeleteMe(1)

		try:
			if dTorpShips.has_key(pTorpID) and dTorpShips[pTorpID] != None and dTorpShips[pTorpID][1] != None:
				App.g_kTimerManager.DeleteTimer(dTorpShips[pTorpID][1].GetObjID())
				dTorpShips[pTorpID][1] = None
		except:
			print "Error on SolidProjectiles' onYield"
			traceback.print_exc()

		del dTorpShips[pTorpID]


def DeleteObjectFromSet(pSet, sObjectName):
        if not MissionLib.GetShip(sObjectName):
                return

        #pSet.DeleteObjectFromSet(sObjectName)
	pSet.RemoveObjectFromSet(sObjectName)
        
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