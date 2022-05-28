from bcdebug import debug
# LauncherGroup
# April 18, 2002
#
# by Evan Light aka sleight42
#
# All rights reserved
# Permission to redistribute this code as part of any other packaging requires
# the explicit permission of the author in advance.
##############################################################################

from Registry import Registry
import Launcher

SINGLE = 1
ALL = 42
LAUNCH_MODE = [SINGLE, ALL]

class LauncherGroup:
    "A proxy to manage an arbitrary group of Launchers"

    def __init__( self):
        debug(__name__ + ", __init__")
        self.Launchers = Registry()
        self.sLaunchType = None
        self.iCurrentLauncherIdx = 0
        self.iCurrentLaunchIdx = 0
        self.eLaunchMode = SINGLE

    def AddLauncher( self, launcherName, launcher):
        debug(__name__ + ", AddLauncher")
        if( launcherName != None and launcher != None):
            self.Launchers.Register( launcher, launcherName)

    #def GetLauncher( self, launcherName):
    #    debug(__name__ + ", GetLauncher")
    #    retval = None
    #    if( launcherName != None and self.Launcher._keyList.has_key( launcherName)):
    #        retval = self.Launchers.GetName( launcherName)
    #    return retval

    #def RemoveLauncher( self, launcherName):
    #    debug(__name__ + ", RemoveLauncher")
    #    retval = None
    #    if( launcherName != None and self.Launchers._keyList.has_key( launcherName)):
    #        retval = self.Launchers.GetName( launcherName)
    #        self.Remove( launcherName)
    #    return retval

    def GetLaunchers( self):
        debug(__name__ + ", GetLaunchers")
        return self.Launchers._arrayList

    def GetNumLaunches( self, launchName): 
        debug(__name__ + ", GetNumLaunches")
        retval = 0
        totalComplement = self.GetComplement()
        if( totalComplement._keyList.has_key( launchName)):
            retval = totalComplement.GetName( launchName)
        return retval

    def HasMoreLaunches( self, launchName):
        debug(__name__ + ", HasMoreLaunches")
        return self.GetNumLaunches( launchName)

    def SetLaunchMode( self, mode):
        debug(__name__ + ", SetLaunchMode")
        AssertMode( mode)
        self.eLaunchMode = mode

    def GetLaunchType( self):
        debug(__name__ + ", GetLaunchType")
        if( self.sLaunchType == None):
            totalComplement = self.GetComplement()
            self.sLaunchType = totalComplement._keyList.keys()[0]
        return self.sLaunchType

    def NextLaunchType( self):
        debug(__name__ + ", NextLaunchType")
        totalComplement = self.GetComplement()
        retval = None
        if( self.sLaunchType == None):
            self.GetLaunchType()
        else:
            keys = totalComplement._keyList.keys()
            startingIdx = keys.index( self.sLaunchType)
            index = startingIdx
            while( 1):
                if( len( keys) - 1 == index):
                    index = 0 
                elif( index < len( keys) -1):
                    index = index + 1
                if( totalComplement[keys[index]] > 0):
                    retval = keys[index]
                    self.sLaunchType = retval
                    break
                if( index == startingIdx):
                    # we've cycled the whole dict.  we're out of ships
                    break
        return retval
        
    def LaunchShip( self, launch):
        debug(__name__ + ", LaunchShip")
        "Launch a ship(s) of 'launch' type from a contained Launcher"
        if( len( self.Launchers) > 0):
            if( self.eLaunchMode == SINGLE):
                self.LaunchFromOneLauncher( launch)
            elif( self.eLaunchMode == ALL):
                self.LaunchFromAllLaunchers( launch)

    def LaunchFromOneLauncher( self, launch):
        debug(__name__ + ", LaunchFromOneLauncher")
        "Launch a single ship and advance the launcher index"
        launched = 0
        numLaunchers = len( self.Launchers)
        count = 0
        currentIndex = self.iCurrentLaunchIdx
        while( not launched and count < numLaunchers):
            count = count + 1
            complement = self.GetComplement()
            bTimer = complement.GetName( launch) - 1
            launched = \
                self.Launchers[currentIndex].LaunchShip( launch, bTimer)
            if( launched == 1):
                break
            if( currentIndex < len( self.Launchers) - 1):
                currentIndex = currentIndex + 1
            else:
                currentIndex = 0
        self.iCurrentLaunchIdx = currentIndex

    def LaunchFromAllLaunchers( self, launch):
        debug(__name__ + ", LaunchFromAllLaunchers")
        "Try to launch a ship of 'launch' type from all launchers"
        for launcher in self.Launchers:
            complement = self.GetComplement()
            bTimer = complement.GetName( launch) - 1
            launcher.LaunchShip( launch, bTimer)

    def GetComplement( self):
        # NOTE: Use of this method considered ugly
        # TODO: Figure out a better way of doing this than computing it here
        debug(__name__ + ", GetComplement")
        totalComplement = Registry()
        for launcher in self.Launchers:
            complement = launcher.GetComplement()
            for key in complement._keyList.keys():
                val = 0
                if( totalComplement._keyList.has_key( key)):
                    val = totalComplement.GetName( key)
                count = complement.GetName( key).count
                updatedVal = val + count
                totalComplement.Register( updatedVal, key)
        return totalComplement

    def Equals( self, other):
        debug(__name__ + ", Equals")
        "KLUGE: Compares the launchers in this group to a passed in launcher"
        retval = 0
        for launcher in self.Launchers:
            if launcher == other:
                retval = 1
                break
        return retval

def AssertMode( mode):
    debug(__name__ + ", AssertMode")
    bMatch = 0
    for launchMode in LAUNCH_MODE:
        if( launchMode == mode):
            bMatch = 1
            break
    if( bMatch == 0):
        # We may print an error, but not raise one! -Defiant
        print("ValueError in LauncherGroup.AssertMode: mode is not of legal type")
