# Over here we'll make a wormhole cone and rotate it slowly to simulate inside wormhole graphics

# by USS Sovereign

# Imports
import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Variable
scale = 1000
# This is for cordys revision extra parts
scale2 = 900

# Just an object setup def
def WormholeSetObjects():
    global scale, scale2

    reload(DS9FXSavedConfig)

    if DS9FXSavedConfig.InsideWormholeModel == 1:
        # Get the set directly from the set file
        Worm = __import__("Systems.BajoranWormhole.BajoranWormhole1")   
        WormholeSet = Worm.GetSet()

        Wormhole = "Bajoran Wormhole Outer"
        pWormhole = loadspacehelper.CreateShip(DS9FXShips.Cone3, WormholeSet, Wormhole, "WormholeCone Position")

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet) 
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.2, 0)
        pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole.SetInvincible(1)
        pDS9FXWormhole.SetHurtable(0)
        pDS9FXWormhole.SetTargetable(0)
        pDS9FXWormhole.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole)
        
        pDS9FXWormhole.SetScale(scale) 

        Wormhole2 = "Bajoran Wormhole Inner"
        pWormhole2 = loadspacehelper.CreateShip(DS9FXShips.Cone4, WormholeSet, Wormhole2, "WormholeCone2 Position")

        pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, -0.2, 0)
        pDS9FXWormhole2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole2.SetInvincible(1)
        pDS9FXWormhole2.SetHurtable(0)
        pDS9FXWormhole2.SetTargetable(0)
        pDS9FXWormhole2.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole2)

        pDS9FXWormhole2.SetScale(scale) 


    elif DS9FXSavedConfig.InsideWormholeModel == 2:
        # Get the set directly from the set file
        Worm = __import__("Systems.BajoranWormhole.BajoranWormhole1")   
        WormholeSet = Worm.GetSet()

        Wormhole = "Bajoran Wormhole Outer"
        pWormhole = loadspacehelper.CreateShip(DS9FXShips.Cone9, WormholeSet, Wormhole, "WormholeCone Position")

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet) 
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.2, 0)
        pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole.SetInvincible(1)
        pDS9FXWormhole.SetHurtable(0)
        pDS9FXWormhole.SetTargetable(0)
        pDS9FXWormhole.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole)

        pDS9FXWormhole.SetScale(scale) 

        Wormhole2 = "Bajoran Wormhole Inner"
        pWormhole2 = loadspacehelper.CreateShip(DS9FXShips.Cone10, WormholeSet, Wormhole2, "WormholeCone2 Position")

        pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, -0.2, 0)
        pDS9FXWormhole2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole2.SetInvincible(1)
        pDS9FXWormhole2.SetHurtable(0)
        pDS9FXWormhole2.SetTargetable(0)
        pDS9FXWormhole2.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole2)

        pDS9FXWormhole2.SetScale(scale) 


    elif DS9FXSavedConfig.InsideWormholeModel == 3:
        # Get the set directly from the set file
        Worm = __import__("Systems.BajoranWormhole.BajoranWormhole1")   
        WormholeSet = Worm.GetSet()

        Wormhole = "Bajoran Wormhole Outer"
        pWormhole = loadspacehelper.CreateShip(DS9FXShips.Cone7, WormholeSet, Wormhole, "WormholeCone Position")

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet) 
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.2, 0)
        pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole.SetInvincible(1)
        pDS9FXWormhole.SetHurtable(0)
        pDS9FXWormhole.SetTargetable(0)
        pDS9FXWormhole.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole)

        pDS9FXWormhole.SetScale(scale) 

        Wormhole2 = "Bajoran Wormhole Inner"
        pWormhole2 = loadspacehelper.CreateShip(DS9FXShips.Cone8, WormholeSet, Wormhole2, "WormholeCone2 Position")

        pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, -0.2, 0)
        pDS9FXWormhole2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole2.SetInvincible(1)
        pDS9FXWormhole2.SetHurtable(0)
        pDS9FXWormhole2.SetTargetable(0)
        pDS9FXWormhole2.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole2)

        pDS9FXWormhole2.SetScale(scale) 


    elif DS9FXSavedConfig.InsideWormholeModel == 4:
        # Get the set directly from the set file
        Worm = __import__("Systems.BajoranWormhole.BajoranWormhole1")   
        WormholeSet = Worm.GetSet()

        Wormhole = "Bajoran Wormhole Outer"
        pWormhole = loadspacehelper.CreateShip(DS9FXShips.Cone5, WormholeSet, Wormhole, "WormholeCone Position")

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet) 
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.2, 0)
        pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole.SetInvincible(1)
        pDS9FXWormhole.SetHurtable(0)
        pDS9FXWormhole.SetTargetable(0)
        pDS9FXWormhole.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole)

        pDS9FXWormhole.SetScale(scale) 

        Wormhole2 = "Bajoran Wormhole Inner"
        pWormhole2 = loadspacehelper.CreateShip(DS9FXShips.Cone6, WormholeSet, Wormhole2, "WormholeCone2 Position")

        pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, -0.2, 0)
        pDS9FXWormhole2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole2.SetInvincible(1)
        pDS9FXWormhole2.SetHurtable(0)
        pDS9FXWormhole2.SetTargetable(0)
        pDS9FXWormhole2.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole2)        

        pDS9FXWormhole2.SetScale(scale)


    elif DS9FXSavedConfig.InsideWormholeModel == 5:
        # Get the set directly from the set file
        Worm = __import__("Systems.BajoranWormhole.BajoranWormhole1")   
        WormholeSet = Worm.GetSet()

        Wormhole = "Bajoran Wormhole Outer"
        pWormhole = loadspacehelper.CreateShip(DS9FXShips.Cone11, WormholeSet, Wormhole, "WormholeCone Position")

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.25, 0)
        pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole.SetInvincible(1)
        pDS9FXWormhole.SetHurtable(0)
        pDS9FXWormhole.SetTargetable(0)
        pDS9FXWormhole.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole)        

        pDS9FXWormhole.SetScale(scale) 

        Wormhole2 = "Bajoran Wormhole Inner"
        pWormhole2 = loadspacehelper.CreateShip(DS9FXShips.Cone12, WormholeSet, Wormhole2, "WormholeCone2 Position")

        pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.3, 0)
        pDS9FXWormhole2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole2.SetInvincible(1)
        pDS9FXWormhole2.SetHurtable(0)
        pDS9FXWormhole2.SetTargetable(0)
        pDS9FXWormhole2.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole2)        

        pDS9FXWormhole2.SetScale(scale)

        # Store location information
        pLocation = pDS9FXWormhole.GetWorldLocation()
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()

        Wormhole3 = "Bajoran Wormhole Extra 1"
        pWormhole3 = loadspacehelper.CreateShip(DS9FXShips.Cone13, WormholeSet, Wormhole3, "WormholeCone Position")

        pDS9FXWormhole3 = MissionLib.GetShip("Bajoran Wormhole Extra 1", WormholeSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.3, 0)
        pDS9FXWormhole3.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole3.SetInvincible(1)
        pDS9FXWormhole3.SetHurtable(0)
        pDS9FXWormhole3.SetTargetable(0)
        pDS9FXWormhole3.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole3)        

        pDS9FXWormhole3.SetScale(scale2)

        pDS9FXWormhole3.SetTranslateXYZ(pX, pY + 400, pZ + 400)
        pDS9FXWormhole3.UpdateNodeOnly() 

        Wormhole4 = "Bajoran Wormhole Extra 2"
        pWormhole4 = loadspacehelper.CreateShip(DS9FXShips.Cone13, WormholeSet, Wormhole4, "WormholeCone Position")

        pDS9FXWormhole4 = MissionLib.GetShip("Bajoran Wormhole Extra 2", WormholeSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.3, 0)
        pDS9FXWormhole4.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole4.SetInvincible(1)
        pDS9FXWormhole4.SetHurtable(0)
        pDS9FXWormhole4.SetTargetable(0)
        pDS9FXWormhole4.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole4)        

        pDS9FXWormhole4.SetScale(scale2)

        pDS9FXWormhole4.SetTranslateXYZ(pX, pY - 400, pZ - 400)
        pDS9FXWormhole4.UpdateNodeOnly() 

        Wormhole5 = "Bajoran Wormhole Extra 3"
        pWormhole5 = loadspacehelper.CreateShip(DS9FXShips.Cone13, WormholeSet, Wormhole5, "WormholeCone Position")

        pDS9FXWormhole5 = MissionLib.GetShip("Bajoran Wormhole Extra 3", WormholeSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.3, 0)
        pDS9FXWormhole5.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole5.SetInvincible(1)
        pDS9FXWormhole5.SetHurtable(0)
        pDS9FXWormhole5.SetTargetable(0)
        pDS9FXWormhole5.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole5)        

        pDS9FXWormhole5.SetScale(scale2)

        pDS9FXWormhole5.SetTranslateXYZ(pX, pY + 400, pZ - 400)
        pDS9FXWormhole5.UpdateNodeOnly() 

        Wormhole6 = "Bajoran Wormhole Extra 4"
        pWormhole6 = loadspacehelper.CreateShip(DS9FXShips.Cone13, WormholeSet, Wormhole6, "WormholeCone Position")

        pDS9FXWormhole6 = MissionLib.GetShip("Bajoran Wormhole Extra 4", WormholeSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.3, 0)
        pDS9FXWormhole6.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole6.SetInvincible(1)
        pDS9FXWormhole6.SetHurtable(0)
        pDS9FXWormhole6.SetTargetable(0)
        pDS9FXWormhole6.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole6)        

        pDS9FXWormhole6.SetScale(scale2)

        pDS9FXWormhole6.SetTranslateXYZ(pX, pY - 400, pZ + 400)
        pDS9FXWormhole6.UpdateNodeOnly() 

    else:
        # Get the set directly from the set file
        Worm = __import__("Systems.BajoranWormhole.BajoranWormhole1")   
        WormholeSet = Worm.GetSet()

        Wormhole = "Bajoran Wormhole Outer"
        pWormhole = loadspacehelper.CreateShip(DS9FXShips.Cone, WormholeSet, Wormhole, "WormholeCone Position")

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet) 
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.2, 0)
        pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole.SetInvincible(1)
        pDS9FXWormhole.SetHurtable(0)
        pDS9FXWormhole.SetTargetable(0)
        pDS9FXWormhole.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole)        

        pDS9FXWormhole.SetScale(scale) 

        Wormhole2 = "Bajoran Wormhole Inner"
        pWormhole2 = loadspacehelper.CreateShip(DS9FXShips.Cone2, WormholeSet, Wormhole2, "WormholeCone2 Position")

        pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, -0.2, 0)
        pDS9FXWormhole2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        pDS9FXWormhole2.SetInvincible(1)
        pDS9FXWormhole2.SetHurtable(0)
        pDS9FXWormhole2.SetTargetable(0)
        pDS9FXWormhole2.SetCollisionsOn(0)
        pProx = WormholeSet.GetProximityManager()
        pProx.RemoveObject(pDS9FXWormhole2)        

        pDS9FXWormhole2.SetScale(scale) 

