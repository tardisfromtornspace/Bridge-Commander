# Adds a name to an affiliation group

# by Sov

# Imports
import App
import MissionLib

# Functions
def AddNames():
    lGroups = [MissionLib.GetEnemyGroup(), MissionLib.GetFriendlyGroup(), MissionLib.GetNeutralGroup(), App.ObjectGroup()]
    i = 0
    for group in lGroups:
        if group:
                i = i + 1
                if not group.GetNameTuple():
                    group.AddName("This ship doesn't exist: " + str(i))
