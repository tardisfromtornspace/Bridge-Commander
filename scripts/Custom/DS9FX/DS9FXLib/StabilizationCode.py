# Code which removes ships from a set, it's a memory cleaner basically

# by USS Sovereign

# Imports
import App
import MissionLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Vars
Timer = None
bWatcher = 0

# Start the code
def StartUp():
        global Timer, bWatcher

        if not bWatcher:
                Timer = StartUpTimer()  
        else:    
                return

# Remove dying ship & repeat the timer based event
class StartUpTimer:
        def __init__(self):
                global bWatcher
                bWatcher = 1
                self.pTimer = None
                self.__Timing__()

        def __Timing__(self):
                if not self.pTimer:
                        self.pTimer = App.PythonMethodProcess()
                        self.pTimer.SetInstance(self)
                        self.pTimer.SetFunction("__Update__")
                        self.pTimer.SetDelay(1)
                        self.pTimer.SetPriority(App.TimeSliceProcess.LOW)

        def __Update__(self, fTime):
                # Option shut down???
                reload(DS9FXSavedConfig)
                if not DS9FXSavedConfig.StabilizeBC == 1:
                        return 0

                # From QuickBattle.py
                pSets = App.g_kSetManager.GetAllSets()
                for pSet in pSets:
                        for kShip in pSet.GetClassObjectList(App.CT_DAMAGEABLE_OBJECT):
                                pShip = kShip.GetObjID()
                                pPlayer = MissionLib.GetPlayer()
                                if not pPlayer:
                                        continue

                                pPlayer = pPlayer.GetObjID()
                                if not pShip == pPlayer:
                                        if kShip.IsDead():
                                                try:
                                                        kShip.SetDeleteMe(1)
                                                except:
                                                        pass

                                                try:
                                                        App.g_kLODModelManager.Purge()
                                                except:
                                                        pass

                                                try:
                                                        App.g_kModelManager.Purge()
                                                except:
                                                        pass


