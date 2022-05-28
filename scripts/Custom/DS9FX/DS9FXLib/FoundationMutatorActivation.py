# by Sov

# It either disables or enables all Foundation Mutators

# Imports
import Foundation
from Custom.DS9FX.DS9FXLib import FoundationMutatorFix
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Functions
def EnableMutators():
    mtList = Foundation.mutatorList
    for mt in mtList._keyList.values():
        mt.Enable()

    Foundation.SaveConfig()
    Foundation.LoadConfig()

    reload(DS9FXSavedConfig)
    iSetting = DS9FXSavedConfig.AutoMutatorBackup
    if iSetting == 1:
        FoundationMutatorFix.SaveBackup(bSilent = 0)

    print "DS9FX: Enabling all mutators..."
    
def DisableMutators():
    mtList = Foundation.mutatorList
    for mt in mtList._keyList.values():
        mt.Disable()

    Foundation.SaveConfig()
    Foundation.LoadConfig()

    reload(DS9FXSavedConfig)
    iSetting = DS9FXSavedConfig.AutoMutatorBackup
    if iSetting == 1:
        FoundationMutatorFix.SaveBackup(bSilent = 0)

    print "DS9FX: Disabling all mutators..."
