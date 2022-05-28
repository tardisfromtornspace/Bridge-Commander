# by USS Sovereign

# Imports
import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips
from Custom.DS9FX.DS9FXCometFX.DS9FXIntroCometFX import StartGFX, CreateGFX
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig


# Just an object setup def
def DS9SetObjects():
        # Get the set directly from the set file
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")   
        DS9Set = DS9.GetSet()
        pProx = DS9Set.GetProximityManager()

        reload (DS9FXSavedConfig)
        if DS9FXSavedConfig.CometSelection == 1:

                # Comet creation
                Comet = "Comet Alpha"
                pComet = loadspacehelper.CreateShip(DS9FXShips.Comet, DS9Set, Comet, "Comet Location")

                pDS9FXComet = MissionLib.GetShip("Comet Alpha", DS9Set)

                if DS9FXSavedConfig.CometAlphaTrail == 1:
                        from Custom.DS9FX.DS9FXCometFX.LibComet import CometTrail

                        CometTrail(pDS9FXComet)

                else:
                        StartGFX()
                        for i in range(1):
                                CreateGFX(pDS9FXComet)

                # Give the object movement effect
                import Custom.DS9FX.DS9FXAILib.DS9FXCometAI

                DS9FXComet = App.ShipClass_Cast(pDS9FXComet)

                DS9FXComet.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXCometAI.CreateAI(DS9FXComet))
                pDS9FXComet.SetInvincible(1)
                pDS9FXComet.SetHurtable(0)

        else:
                pass


        if DS9FXSavedConfig.WormholeSelection == 1:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole, DS9Set, Wormhole, "Wormhole Location")

                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
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
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole3, DS9Set, Wormhole, "Wormhole Location")

                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
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
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole4, DS9Set, Wormhole, "Wormhole Location")

                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
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
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole5, DS9Set, Wormhole, "Wormhole Location")

                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
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
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole6, DS9Set, Wormhole, "Wormhole Location")

                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
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
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole7, DS9Set, Wormhole, "Wormhole Location")

                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
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
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole8, DS9Set, Wormhole, "Wormhole Location")

                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
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
                pWormhole = loadspacehelper.CreateShip(DS9FXShips.Wormhole2, DS9Set, Wormhole, "Wormhole Location")

                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
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
        pNav = loadspacehelper.CreateShip(DS9FXShips.Distortion, DS9Set, Navpoint, "Wormhole Location")

        pNavpoint = MissionLib.GetShip(Navpoint, DS9Set) 

        pNavpoint.SetInvincible(1)
        pNavpoint.SetHurtable(0)
        pNavpoint.SetHidden(1)
        pNavpoint.SetTargetable(0)
        pNavpoint.SetCollisionsOn(0)
        pProx.RemoveObject(pNavpoint)

