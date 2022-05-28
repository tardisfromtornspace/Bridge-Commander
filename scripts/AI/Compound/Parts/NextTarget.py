from bcdebug import debug
import App
import MissionLib

def CreateAI(pShip, pTargets):
        debug(__name__ + ", CreateAI")
        print("Getting next Target")
        pTargetGroup = App.ObjectGroup_ForceToGroup(pTargets)
        pSet = pShip.GetContainingSet()
        lTargets = pTargetGroup.GetActiveObjectTupleInSet(pSet)
        
        for DamObject in lTargets:
                pTarget = App.ShipClass_Cast(DamObject)
                if not pTarget:
                        continue
                
                if pTarget.IsDead() or pTarget.IsDying() or not pTarget.IsTargetable():
                        continue
                
                pShip.SetTarget(pTarget.GetName())
                return
        
        pShip.SetTarget(None)
        
