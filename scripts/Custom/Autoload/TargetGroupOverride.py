# This should help get rid of this file

# 2004 by Defiant - erik@vontaene.de
# Overwriting All AIs
# I hate it, but the only thing we could do...

#import App
#import Appc
#import MissionLib
#import Foundation
#
#mode = Foundation.MutatorDef("Targetgroup override")
#pEnemies = None
#pFriendlies = None
#
#class TargetGroup:
#        def __init__(self, Group):
#                self.Targets = App.ObjectGroupWithInfo()
#                pMission = MissionLib.GetMission()
#                print("group:", Group)
#                if Group == "Enemy":
#                        self.realGroup = pMission.GetEnemyGroup()
#                elif Group == "Friendly":
#                        self.realGroup = pMission.GetFriendlyGroup()
#        def AddName(self, ShipName):
#                self.realGroup.AddName(ShipName)
#                self.Targets[ShipName] = {"Priority" : 1.0}
#        def RemoveName(self, ShipName):
#                self.realGroup.RemoveName(ShipName)
#                del self.Targets[ShipName]
#        def IsNameInGroup(self, ShipName):
#                return self.Targets.IsNameInGroup(ShipName)
#        def GetNameTuple(self):
#                return self.Targets.GetNameTuple()
#        def RemoveAllNames(self):
#                self.Targets.RemoveAllNames()
#                self.realGroup.RemoveAllNames()
#        def GetNumActiveObjects(self):
#                return self.Targets.GetNumActiveObjects()
#        def GetActiveObjectTupleInSet(self, pSet):
#                return self.Targets.GetActiveObjectTupleInSet(pSet)
#        def __repr__(self):
#                return str(self.Targets)
#        def __getattr__(self):
#                return self.Targets
#        def SetPriority(self, ShipName, Priority):
#                if Priority > 0.0:
#                        self.Targets[ShipName] = {"Priority" : Priority}
#                else:
#                        del self.Targets[ShipName]
#
#
#def GetEnemyGroup():
#        global pEnemies
#        if not pEnemies:
#                print("Warning: Group override is active!")
#                pEnemies = TargetGroup("Enemy")
#                #pEnemies.AddName("This ship probably wont exist")
#        return pEnemies
#
#
#def GetFriendlyGroup():
#        global pFriendlies
#        if not pFriendlies:
#                print("Warning: Group override is active!")
#                pFriendlies = TargetGroup("Friendly")
#                #pEnemies.AddName("This ship probably wont exist")
#        return pFriendlies
#
#
#def ObjectGroup_FromModule(*args, **kwargs):
#        global pEnemies, pFriendlies
#        if args[1] == "pEnemies":
#                return pEnemies.Targets
#        elif args[1] == "pFriendlies":
#                return pFriendlies.Targets
#        val = apply(Appc.ObjectGroup_FromModule,args,kwargs)
#        if val: val = App.ObjectGroupPtr(val)
#        return val
#
#def ObjectGroup_ForceToGroup(lpTargets):
#        global pEnemies, pFriendlies
#        val = Appc.ObjectGroup_ForceToGroup(lpTargets)
#        if not val:
#                if pEnemies:
#                        if str(lpTargets[0]) == str(pEnemies.Targets):
#                                val = pEnemies.Targets
#                if pFriendlies:
#                        if str(lpTargets[0]) == str(pFriendlies.Targets):
#                                val = pFriendlies.Targets
#        # Last chance before failure:
#        try:
#                if not val:
#                        if str(lpTargets[0][0]) == str(pEnemies.Targets):
#                                val = pEnemies.Targets
#                        if str(lpTargets[0][0]) == str(pFriendlies.Targets):
#                                val = pFriendlies.Targets
#        except:
#                pass
#        return val
#
#
#Foundation.OverrideDef.EnemyTargetGroup = Foundation.OverrideDef("TargetGroup", "MissionLib.GetEnemyGroup", __name__ + ".GetEnemyGroup", dict = { "modes": [ mode ] } )
#Foundation.OverrideDef.EnemyTargetGroup = Foundation.OverrideDef("TargetGroup", "MissionLib.GetFriendlyGroup", __name__ + ".GetFriendlyGroup", dict = { "modes": [ mode ] } )
#Foundation.OverrideDef.EnemyTargetGroup = Foundation.OverrideDef("TargetGroup", "App.ObjectGroup_FromModule", __name__ + ".ObjectGroup_FromModule", dict = { "modes": [ mode ] } )
#Foundation.OverrideDef.EnemyTargetGroup = Foundation.OverrideDef("TargetGroup", "App.ObjectGroup_ForceToGroup", __name__ + ".ObjectGroup_ForceToGroup", dict = { "modes": [ mode ] } )
