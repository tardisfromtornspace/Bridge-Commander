###############################################################################
#	Filename:	PoleronTorp.py
#	By:		edtheborg
#       Updated:        LJ 2007 - Added ability to make the target swap teams.
###############################################################################
# This torpedo uses the FTA mod...
#
# it actually passes through shields and damages whatever subsystem it was
# targeted at
#
# please refer to the bottom of this file for details on changing effects
###############################################################################

import App
import MissionLib
pWeaponLock = {}

###############################################################################
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(84.0 / 255.0, 67.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.2) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLifetime():
        return 15
#        return 6

def GetLaunchSpeed():
	return(50)

def GetLaunchSound():
	return("Replicator Missile")

def GetPowerCost():
        return (10.0)
#	return(500.0)

def GetName():
	return("Replicator Missile")

def GetDamage():
	return 0.00001

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 1500

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.00001

def GetGuidanceLifetime():
	return 5.0
#	return 1.0

def GetMaxAngularAccel():
	return 1.5

def TargetHit(pObject, pEvent):
	global pWeaponLock
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if (pTorp==None) or (pShip==None):
                return
	try:
		id=pTorp.GetObjID()
		pSubsystem=pWeaponLock[id]
		del pWeaponLock[id]
	except:
		pSubsystem=pShip.GetHull()
	if (pSubsystem==None):
		return
	Dmg=pSubsystem.GetMaxCondition()*GetPercentage()
	if (Dmg<GetMinDamage()):
		Dmg=GetMinDamage()
	if (pSubsystem.GetCondition()>Dmg):
		pSubsystem.SetCondition(pSubsystem.GetCondition()-Dmg)
	else:
                pShip.DestroySystem(pSubsystem)
        
        ####################################################################
        ## Make the ship flip sides. LJ
        pTorpedo        = App.Torpedo_Cast(pEvent.GetSource())
        pVictim         = App.ShipClass_Cast(pEvent.GetDestination())

        ## Check we haven't hit a planet or something daft
        if (pTorpedo == None) or  pVictim == None:
                return

        ## Get the attacker from the torpedo
        pAttacker       = App.ShipClass_GetObjectByID(pTorpedo.GetContainingSet(), pTorpedo.GetParentID())
        if pAttacker == None:
                return
        
        ## Make the victim switch to the side of the attacker
        import MissionLib
        pMission        = MissionLib.GetMission() 
        pFriendlies     = pMission.GetFriendlyGroup() 
        pEnemies        = pMission.GetEnemyGroup() 
        pGroup          = pMission.GetNeutralGroup()

        ## Check the friendlys and enemy group for our attacter
        if pFriendlies.IsNameInGroup(pAttacker.GetName()):
                pGroup = pFriendlies
        elif pEnemies.IsNameInGroup(pAttacker.GetName()):
                pGroup = pEnemies

        ## Add the victim ship to the new group
        pSequence = App.TGSequence_Create()
        for i in range(5):
                pMakeFriend     = App.TGScriptAction_Create(__name__, "SwapTeam", pVictim, pFriendlies)
                pMakeEnemy      = App.TGScriptAction_Create(__name__, "SwapTeam", pVictim, pEnemies)                           
                pSequence.AddAction(pMakeEnemy, App.TGAction_CreateNull(), 1.0*((i)*1.8) + 30.0)
                pSequence.AddAction(pMakeFriend, App.TGAction_CreateNull(), 2.0*((i)*1.8) + 30.0)
                
        pSwapFinalTeam  = App.TGScriptAction_Create(__name__, "SwapTeam", pVictim, pGroup)
        pAIChangeAction = App.TGScriptAction_Create(__name__, "ChangeAI", pVictim)
        pSequence.AppendAction(pSwapFinalTeam)
        pSequence.AppendAction(pAIChangeAction)
        pSequence.Play()
        #pGroup.AddName(pVictim.GetName())
        ## Clear AI
        #pAIModule = __import__("QuickBattle.QuickBattleAI")
        #pVictim.SetAI(pAIModule.CreateAI(pVictim), 0, 0)
        #pVictim.ClearAI()
        ####################################################################
	return

def WeaponFired(pObject, pEvent):
	global pWeaponLock
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	pTube=App.TorpedoTube_Cast(pEvent.GetDestination())
	if (pTorp==None) or (pTube==None):
		return
	pShip=pTube.GetParentShip()
	if (pShip==None):
		return
	try:
		pWeaponLock[pTorp.GetObjID()]=pShip.GetTargetSubsystem()
	except:
		return
	return


def ChangeAI(pAction, pShip):
        pShip.ClearAI()
        return 0

def SwapTeam(pAction, pShip, pGroup):
        pMission        = MissionLib.GetMission() 
        pFriendlies     = pMission.GetFriendlyGroup() 
        pEnemies        = pMission.GetEnemyGroup() 
        pNeutrals       = pMission.GetNeutralGroup()
        pFriendlies.RemoveName(pShip.GetName())
        pEnemies.RemoveName(pShip.GetName())
        pNeutrals.RemoveName(pShip.GetName())
        pGroup.AddName(pShip.GetName())
        return 0
