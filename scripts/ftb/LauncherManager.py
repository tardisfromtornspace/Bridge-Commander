#
# LauncherManager
#
# by Evan Light aka sleight42
# All Rights Reserved
#
# This module acts as a Factory and repository of ftb.Launcher.Launcher objects 
# and it's subclasses.
##################################################################

import App
import Registry
import MissionLib
import ftb.Launcher

launcherRegistry = Registry.Registry()

def GetLauncherBySystem( pSystem):
    return launcherRegistry.GetName( pSystem.this)

def GetLauncher( launcherName, pShip):
    retval = None
    if (launcherName != None):
        sOEPName = launcherName + " OEP"
        #print "sOEPName:", sOEPName
        pProperty = GetPropertyByName( pShip, sOEPName, \
                                       App.CT_OBJECT_EMITTER_PROPERTY)
        #print sOEPName, "property:", pProperty
        pSystem = MissionLib.GetSubsystemByName( pShip, launcherName)
        #print "system:", pSystem
        if not pSystem:
            return
        retval = launcherRegistry.GetName( pSystem.this)
        if (retval == None):
            retval = ftb.Launcher.Launcher( pSystem, pProperty, pShip)
            launcherRegistry.Register(retval, pSystem.this)
    return retval

def GetPropertyByName( pShip, propertyName, cPropType):
    retval = None
    pPropSet = pShip.GetPropertySet()
    pEmitterInstanceList = pPropSet.GetPropertiesByType( cPropType)
    pEmitterInstanceList.TGBeginIteration()
    iNumItems = pEmitterInstanceList.TGGetNumItems()
    pLaunchProperty = None
    for i in range(iNumItems):
        pInstance = pEmitterInstanceList.TGGetNext()
        # Check to see if the property for this instance is a shuttle
        # emitter point.
        pProperty = pInstance.GetProperty()
        if (pProperty != None):
            if( not pProperty.GetName().CompareC( propertyName, 1)):
                retval = pProperty
                break
    pEmitterInstanceList.TGDoneIterating()
    pEmitterInstanceList.TGDestroy()
    return retval
