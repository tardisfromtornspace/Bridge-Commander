from bcdebug import debug
# Carrier
# March 27, 2002
#
# by Evan Light aka sleight42
#
# All rights reserved
# Permission to redistribute this code as part of any other packaging requires
# the explicit permission of the author in advance.
##############################################################################

from Registry import Registry
import ftb.Ship

# TODO: Create a default launch group for people who don't care
class Carrier( ftb.Ship.Ship):
    "A Ship subclass that carries a series of launchers carrying other ships/objects" 

    def __init__( self, pShip):
        debug(__name__ + ", __init__")
        ftb.Ship.Ship.__init__( self, pShip)
        # TODO: change self.launchers to a Registry
        self.launchers = Registry()

    def AddLauncher( self, launcherName, launcher):
        debug(__name__ + ", AddLauncher")
        if( launcherName != None and launcher != None):
            self.launchers.Register( launcher, launcherName)

    def GetLauncher( self, launcherName):
        debug(__name__ + ", GetLauncher")
        if( launcherName != None and self.launchers.has_key( launcherName)):
            return self.launchers.GetName( launcherName)

    def GetLaunchers( self):
        debug(__name__ + ", GetLaunchers")
        return self.launchers

    def GetNumLaunches( self, launchName):
        debug(__name__ + ", GetNumLaunches")
        "Iterates over all of a Carriers launchers and tallies up the number of a particular Launch aboard"
        retval = 0
        if( launchName != None):
            for launcherName in self.launchers._keyList:
                launcher = self.launchers[launcherName]
                retval = retval + launcher.GetNumLaunches( launchName)
        return retval

    def HasMoreLaunches( self, shuttle): 
        debug(__name__ + ", HasMoreLaunches")
        return self.GetNumLaunches( shuttle)

    def GetLaunchType( self, launcherName):
        debug(__name__ + ", GetLaunchType")
        return self.launchers.GetName( launcherName).GetLaunchType()

    def NextLaunchType( self, launcherName):
        debug(__name__ + ", NextLaunchType")
        return self.launchers.GetName( launcherName).NextLaunchType()
        
    #def LaunchShip( self, shuttle, launcherName):
    #    debug(__name__ + ", LaunchShip")
    #    return self.Launchers.GetName( launcherName).LaunchShip( shuttle)

    #def LaunchShip( self, shuttle, launcherIndex):
    #    debug(__name__ + ", LaunchShip")
    #    return self.Launchers[launcherIndex].LaunchShip( shuttle)
