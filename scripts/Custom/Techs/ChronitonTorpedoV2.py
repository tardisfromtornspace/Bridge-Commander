#################################################################################################################
#	Filename :	PhasedTorpedoV1.py      Original Author  : Graham Spencer
#       Version  :      1.02000                 Last Modified by : 2010 JB
#	Created  :	06 Feb 2008
#
#       *1* Create the torpedo you want to be phased
#       *2* set its damage to however much you want to do to the target's shields on impact
#       *3* Make a copy of that file in the same folder, use the same name but add _P to the end.  eg.  Torp.py   Torp_P.py
#       *4* Set the damage in that copy to your true yield (how much damage you want to do on hull impact)
#       *5* Open your original torp file that you created in *1*
#       *6* Add " from Custom.Techs.PhasedTorpedoV1 import * " (without quotes) to your torp file, you can put it under "import App"
#       *7* Add torp from *1* to your ship
#
#       Version History:
#       1.01 - changed pVector scaling method from fixed number to target radius based - GS  7 Feb 08
#       1.02 - seperated code for pulse & torpedo to help reduce pulse lag - GS  10 Feb 08
#       1.03 - 
#
#################################################################################################################

import App

def TargetHit(pObject, pEvent):
	pTorp = App.Torpedo_Cast(pEvent.GetSource())

	if pEvent.IsHullHit() :
		CreateTorp(pEvent, pTorp.GetModuleName() + '_P', 1)
		return
	else:
		CreateTorp(pEvent, pTorp.GetModuleName() + '_P', 0)
		return
	return

def NiToTG(Ni):
	TG = App.TGPoint3()
	TG.SetXYZ(Ni.x, Ni.y, Ni.z)
	return TG

def CreateTorp(pEvent, sTorpPath, HullHit):

	pTorp           = App.Torpedo_Cast(pEvent.GetSource())
	pTarget         = App.ShipClass_Cast(pEvent.GetDestination())
	pShipID         = pTorp.GetParentID()
	pSet            = pTorp.GetContainingSet()
	pVector         = pTorp.GetVelocityTG()
	pVector2        = pTorp.GetVelocityTG()         ## there is probably a better way..
	pVector.Scale( (0.06 * pTarget.GetRadius()) / pTorp.GetLaunchSpeed() )
	pHitPoint       = NiToTG( pTorp.GetWorldLocation() )    ## pEvent.GetWorldHitPoint is somtimes way off (2 or 3 torpedo widths on a stationary target)

	if pTorp.GetGuidanceLifeTime() < 2.0 :
		if HullHit == 1:
			pHitPoint.Subtract(pVector)
			pTorp2 = App.Torpedo_Create(sTorpPath,pHitPoint)
			pTorp2.SetHidden(1)
			pTorp2.SetDamage( pTorp2.GetDamage() - pTorp.GetDamage() )      ## to prevent dealing hull damage equal to pTorp dmg + pTorp2 dmg
		else:
			pTorp.SetLifetime(0)
			pHitPoint.Add(pVector)
			pTorp2 = App.Torpedo_Create(sTorpPath,pHitPoint)
		pTorp2.SetVelocity(pVector2)
		pSet.AddObjectToSet(pTorp2, None)
		return pTorp2

	else:
		pShip = App.ShipClass_GetObjectByID(None, pShipID)

		if HullHit == 1:
			pHitPoint.Subtract(pVector)
			pTorp2 = App.Torpedo_Create(sTorpPath,pHitPoint)
			pTorp2.SetHidden(1)
			pTorp2.SetDamage( pTorp2.GetDamage() - pTorp.GetDamage() )
		else:
			pTorp.SetLifetime(0)
			pHitPoint.Add(pVector)
			pTorp2 = App.Torpedo_Create(sTorpPath,pHitPoint)

		pTargetID = pTorp.GetTargetID()
		pTorp2.SetTarget(pTargetID)
		pTargetSubsystem = pShip.GetTargetSubsystem()
		IDTargetSubsystem = pTargetSubsystem.GetObjID()
		pSubsystem = App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(IDTargetSubsystem))
		pTorp2.SetTargetOffset(pSubsystem.GetPosition())
		pSet.AddObjectToSet(pTorp2, None)
		pTorp2.SetVelocity(pVector2)
		return pTorp2

	return
