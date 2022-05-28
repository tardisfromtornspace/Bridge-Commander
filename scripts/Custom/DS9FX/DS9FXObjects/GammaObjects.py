# Just like the DS9Objects.py this holds info about all objects that are located in the set

# by USS Sovereign

# Imports
import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig


# Just an object setup def
def GammsSetObjects():
        # Grab the system name from the set file
        Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
        GammaSet = Gamma.GetSet()
        pProx = GammaSet.GetProximityManager()

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.WormholeSelection == 1:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole, GammaSet, Wormhole, "Wormhole Location")
                
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)
                pDS9FXWormhole.SetCollisionsOn(0)
                pProx.RemoveObject(pDS9FXWormhole)

                pDS9FXWormhole.SetScale(0.01) 

        elif DS9FXSavedConfig.WormholeSelection == 2:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole3, GammaSet, Wormhole, "Wormhole Location")
                
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)
                pDS9FXWormhole.SetCollisionsOn(0)
                pProx.RemoveObject(pDS9FXWormhole)

                pDS9FXWormhole.SetScale(0.01) 

        elif DS9FXSavedConfig.WormholeSelection == 3:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole4, GammaSet, Wormhole, "Wormhole Location")
                
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)
                pDS9FXWormhole.SetCollisionsOn(0)
                pProx.RemoveObject(pDS9FXWormhole)
               
                pDS9FXWormhole.SetScale(0.01)

        elif DS9FXSavedConfig.WormholeSelection == 4:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole5, GammaSet, Wormhole, "Wormhole Location")
                
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)
                pDS9FXWormhole.SetCollisionsOn(0)
                pProx.RemoveObject(pDS9FXWormhole)

                pDS9FXWormhole.SetScale(0.01)

        elif DS9FXSavedConfig.WormholeSelection == 5:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole6, GammaSet, Wormhole, "Wormhole Location")
                
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)
                pDS9FXWormhole.SetCollisionsOn(0)
                pProx.RemoveObject(pDS9FXWormhole)

                pDS9FXWormhole.SetScale(0.01)                

        elif DS9FXSavedConfig.WormholeSelection == 6:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole7, GammaSet, Wormhole, "Wormhole Location")
                
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)
                pDS9FXWormhole.SetCollisionsOn(0)
                pProx.RemoveObject(pDS9FXWormhole)

                pDS9FXWormhole.SetScale(0.01)
                
                
        elif DS9FXSavedConfig.WormholeSelection == 7:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole8, GammaSet, Wormhole, "Wormhole Location")
                
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)
                pDS9FXWormhole.SetCollisionsOn(0)
                pProx.RemoveObject(pDS9FXWormhole)

                pDS9FXWormhole.SetScale(0.01)                

        else:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole2, GammaSet, Wormhole, "Wormhole Location")
                
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)
                pDS9FXWormhole.SetCollisionsOn(0)
                pProx.RemoveObject(pDS9FXWormhole)

                pDS9FXWormhole.SetScale(0.01)

        Navpoint = "Bajoran Wormhole Navpoint"
        pNav = loadspacehelper.CreateShip(DS9FXShips.Distortion, GammaSet, Navpoint, "Wormhole Location")
                
        pNavpoint = MissionLib.GetShip(Navpoint, GammaSet) 

        pNavpoint.SetInvincible(1)
        pNavpoint.SetHurtable(0)
        pNavpoint.SetHidden(1)
        pNavpoint.SetTargetable(0)
        pNavpoint.SetCollisionsOn(0)
        pProx.RemoveObject(pNavpoint)
