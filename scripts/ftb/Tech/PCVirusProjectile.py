###############################################################################################################
#          PC Virus Projectile
#                                           by USS Frontier
###############################################################################################################
# PC/Computer Virus Projectiles are a sneaky captain's best friend. Upon hitting the HULL of their targets, 
# these projectiles will introduce a computer virus on the target ship, scrambling it's controls and turning
# the target ship to your side of the battle for some precious seconds.
#
# NOTE: Perhaps Breen Drainer Immunity somehow is preventing this from working on some ships... Not that it is a bad thing...
###############################################################################################################
# To add the PC Virus Projectile tech to a torpedo, add the following code at the end of the script:
# And remove the "#" symbols

#try:
#	import FoundationTech
#	import ftb.Tech.PCVirusProjectile
#
#	oFire = ftb.Tech.PCVirusProjectile.PCVirusWeaponDef('PCVirus Weapon', {"iTime": 60.0})
#	FoundationTech.dYields[__name__] = oFire
#except:
#	import sys
#	et = sys.exc_info()
#	error = str(et[0])+": "+str(et[1])
#	print "ERROR at script: " + __name__ +", details -> "+error

#########################################################################################################################

import App
import FoundationTech
import MissionLib

class PCVirusEvent(FoundationTech.FTBEvent):
	def __init__(self, source, when, pTargetID):
		self.pTargetID = pTargetID
		FoundationTech.FTBEvent.__init__(self, source, when)

	def __call__(self, now):
		pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(self.pTargetID))
		pPlayer = MissionLib.GetPlayer()
		if not pTarget:
			return

		ChangeShipGroup(pTarget, GetOppositeGroup( GetShipGroup(pTarget)) )
		if (pTarget.GetObjID() == pPlayer.GetObjID()):
			pTarget.ClearAI()	
		else:
			ResetShipAI(pTarget)

class PCVirusWeaponDef(FoundationTech.TechDef):

	def __init__(self, name, dict):
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.iTime = 60.0
		self.__dict__.update(dict)

	def IsDrainYield(self):
		return 1

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
			pPlayer = MissionLib.GetPlayer()
			pFromShipID = pTorp.GetParentID()
			pFromShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pFromShipID))
			pTarget = App.ShipClass_Cast(pEvent.GetDestination())
			#print "Attacker --->>>", pFromShip.GetName(), "// Target--->>>", pTarget.GetName()
			if (pEvent.IsHullHit() == 0):
				print "Must hit the hull to infect."
				return
			if (GetShipGroup(pTarget) == GetShipGroup(pFromShip)):
				print "Target is from the same group of the Attacker. Can't infect it."
				return
			if (pTarget.GetShipProperty().IsStationary() == 1):
				print "Can't infect with PC Virus a Station"
				return
			print "Target is succeptible to PC Virus infection, beggining to infect"	

			#print "Affecting Player. IN CONSTRUCTION"
			ChangeShipGroup(pTarget, GetGroup( GetShipGroup(pFromShip) ) )
			ResetShipAI(pTarget)
			print "Target infected. Initializing Timer."

			pInstance = FoundationTech.dShips[pFromShip.GetName()]		
			pTargetID = pTarget.GetObjID()
			ePlayerPC = PCVirusEvent(pInstance, self.iTime, pTargetID)
			FoundationTech.oEventQueue.Queue(ePlayerPC)

oPCVirusWeapon = PCVirusWeaponDef('PCVirus Weapon', {})

###################################
def GetShipGroup(pShip):
	pFriendlies = MissionLib.GetFriendlyGroup()
	pNeutrals = MissionLib.GetNeutralGroup()
	pEnemies = MissionLib.GetEnemyGroup()
	if pEnemies.IsNameInGroup(pShip.GetName()):  #ship is enemy
		return "Enemy"
	if pFriendlies.IsNameInGroup(pShip.GetName()):  #ship is friendly
		return "Friendly"
	if pNeutrals.IsNameInGroup(pShip.GetName()):   #ship is neutral
		return "Neutral"

def GetGroup(sName):
	if sName == "Friendly":
		return MissionLib.GetFriendlyGroup()
	if sName == "Neutral":
		return MissionLib.GetNeutralGroup()
	if sName == "Enemy":
		return MissionLib.GetEnemyGroup()

def GetOppositeGroup(sName):
	if sName == "Enemy":
		return MissionLib.GetFriendlyGroup()
	if sName == "Neutral":
		return MissionLib.GetNeutralGroup()
	if sName == "Friendly":
		return MissionLib.GetEnemyGroup()

def ChangeShipGroup(pShip, pGroup):
	if pGroup.IsNameInGroup(pShip.GetName()):
		return
	pOldGroup = GetGroup(GetShipGroup(pShip))
	pOldGroup.RemoveName(pShip.GetName())
	pGroup.AddName(pShip.GetName())

def ResetShipAI(pShip):
	try:
		import Custom.GalaxyCharts.GalaxyLIB
		Custom.GalaxyCharts.GalaxyLIB.ResetShipAI(pShip)
	except:
		if pShip.GetAI() != None:
			pShip.ClearAI()

		pFriendlies = MissionLib.GetFriendlyGroup()
		pEnemies = MissionLib.GetEnemyGroup()
		pNeutrals = MissionLib.GetNeutralGroup()

		if pEnemies.IsNameInGroup(pShip.GetName()):
			pAIenemyGroup = pFriendlies
			sAItoCheckTo = "QuickBattleAI"
		elif pFriendlies.IsNameInGroup(pShip.GetName()):
			pAIenemyGroup = pEnemies
			sAItoCheckTo = "QuickBattleFriendlyAI"
		else:   #elif pNeutrals.IsNameInGroup(pShip.GetName()):   #ship is neutral
			# forget resetting AI for a neutral ship
			print "Cancelled resetting, neutral ship."
			return 0

		try:
			pAIModule = __import__("QuickBattle." + sAI)
			try:
				pShip.SetAI(pAIModule.CreateAI(pShip, pAIenemyGroup))
			except:
				pShip.SetAI(pAIModule.CreateAI(pShip))
		except:
			pass