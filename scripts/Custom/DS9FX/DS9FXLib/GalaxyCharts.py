# Galaxy Charts operations

from Custom.DS9FX.DS9FXLib import DS9FXMenuLib

TRUE = 1
FALSE = 0

def IsInstalled():
    pInstalled = DS9FXMenuLib.CheckModInstallation("Galaxy Charts")
    
    if pInstalled:
        return TRUE
    else:
        return FALSE

def GetGCVersion():
    try:
        from Custom.GalaxyCharts import Galaxy
        pVer = Galaxy.MOD_VERSION
        return pVer
    except:
        return None

def IsIncompatibleOn():
    pInstalled = IsInstalled()
    if not pInstalled:
        return FALSE

    pVer = GetGCVersion()
    if not pVer:
        return FALSE

    # 2.0 GC or a beta, so check for RAF and RDF
    if pVer > 1.0:
        try:
            from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import GalaxyChartsConfigValues
            
            pRAF = GalaxyChartsConfigValues.WarSimulator.UseWarSim
            pRDF = GalaxyChartsConfigValues.RandomDefenceForce.UseRDF
            
            if pRDF or pRAF == 1:
                return TRUE
            else:
                return FALSE
            
        except:
            return FALSE
        
    # 1.0 GC version, scan only for RDF
    else:
        try:
            from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import GalaxyChartsConfigValues
            
            pRDF = GalaxyChartsConfigValues.RandomDefenceForce.UseRDF
            
            if pRDF == 1:
                return TRUE
            else:
                return FALSE
            
        except:
            return FALSE            
