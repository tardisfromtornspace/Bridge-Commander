# On Exit Game kill the GUI's

def Exiting():
        from Custom.DS9FX.DS9FXLib import DS9FXMissionLib

        DS9FXMissionLib.Quit()

        from Custom.DS9FX.DS9FXScan import ProvideShipInfo

        ProvideShipInfo.Quitting()

        from Custom.DS9FX.DS9FXScan import ProvidePlayerInfo

        ProvidePlayerInfo.Quitting()

        from Custom.DS9FX.DS9FXScan import ProvidePlanetInfo

        ProvidePlanetInfo.Quitting()

        from Custom.DS9FX.DS9FXScan import ProvideRegionInfo

        ProvideRegionInfo.Quitting()

        from Custom.DS9FX.DS9FXLifeSupport import HandleTransportCrew

        HandleTransportCrew.Quitting()

        from Custom.DS9FX.DS9FXLifeSupport import CaptureShip
        
        CaptureShip.Quitting()

        from Custom.DS9FX.DS9FXLifeSupport import ShipRecovery
   
        ShipRecovery.Quitting()
        
        from Custom.DS9FX.DS9FXMissions import MissionStatus
        
        MissionStatus.Quit()
        
        from Custom.DS9FX.DS9FXMissions import MissionQuitHelper

        MissionQuitHelper.Exiting()
