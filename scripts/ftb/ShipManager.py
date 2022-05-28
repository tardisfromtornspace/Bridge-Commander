from bcdebug import debug
#
# ShipManager
#
# by Evan Light aka sleight42
# All Rights Reserved
#
# This module acts as a Factory and repository of ftb.Ship.Ship objects 
# and it's subclasses.
##################################################################

import App
import Registry
import MissionLib
import ftb.Ship
import ftb.Carrier
import traceback
import sys

classRegistry = Registry.Registry()
shipRegistry = Registry.Registry()
lGetShipShowErrorDone = []

def GetShip(pShip):
    debug(__name__ + ", GetShip")
    global lGetShipShowErrorDone
    retval = None
    if (pShip != None):
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if( pShip != None):
            retval = shipRegistry.GetName(str(pShip.GetObjID()) + pShip.GetName())
            if (retval == None):
		try:
                	shipClass = GetShipClass(pShip.GetShipProperty().GetShipName())
                	retval = shipClass(pShip)
                	shipRegistry.Register(retval, str(pShip.GetObjID()) + pShip.GetName())
		except AttributeError:
			if not pShip.GetName() in lGetShipShowErrorDone:
				print "Shuttle Launching Error: ship %s has no Shuttle launching points" % pShip.GetName()
				lGetShipShowErrorDone.append(pShip.GetName())
			return retval
    return retval


def RemoveShip(pShip):
        debug(__name__ + ", RemoveShip")
        pShip = App.ShipClass_Cast(pShip)
        if pShip:
                shipRegistry.Remove(str(pShip.GetObjID()) + pShip.GetName())


def RegisterShipClass(className, shipClass):
    debug(__name__ + ", RegisterShipClass")
    if (className == None):
        print("ValueError in ftb.ShipManager.RegisterShipClass() - className cannot be None") # we may print an error
    if (shipClass == None):
        print("ValueError in ftb.ShipManager.RegisterShipClass() - shipClass cannot be None") # but we do not raise one!
    classRegistry.Register(shipClass, className)


def GetShipClass(className):
    debug(__name__ + ", GetShipClass")
    retval = classRegistry.GetName(className)
    if (retval == None):
        retval = ftb.Ship.Ship
    return retval


# Based off of Dasher's LoadExtraPlugins based off of Banbury's GetShipList()
# ;) sleight42
def LoadExtraPlugins(dir = 'scripts\\Custom\\Carriers\\'):
    debug(__name__ + ", LoadExtraPlugins")
    import nt
    import string

    list = nt.listdir(dir)
    list.sort()

    dotPrefix = string.join(string.split(dir, '\\')[1:], '.')

    for plugin in list:
        s = string.split(plugin, '.')
        pluginFile = ''
        # We don't want to accidentally load the wrong ship.
        # Indexing by -1 lets us be sure we're grabbing the extension. -Dasher42
        if len(s) > 1 and \
           ( s[-1] == 'pyc' or s[-1] == 'py'):
            pluginFile = s[0]
        else:
            continue

        try:
            pModule = __import__(dotPrefix + pluginFile)
        except:
            print "Error Loading Carrier", dotPrefix + pluginFile
            errtype, errinfo, errtrace = sys.exc_info()
            fulltrace = traceback.print_exc(errtrace)
            if fulltrace:
            	print("Traceback: %s") % (fulltrace)

LoadExtraPlugins()
