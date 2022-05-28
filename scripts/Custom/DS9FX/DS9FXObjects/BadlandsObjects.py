# We load our Badlands Vortexes here...

# by USS Sovereign

# Imports
import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Vortex size in game
vortexSize = 18
vortexSize2 = 11

# Load objects by checking settings
def BadlandsSetObjects():
    # Grab the set
    Badlands = __import__("Systems.DS9FXBadlands.DS9FXBadlands1")
    BadlandsSet = Badlands.GetSet()        
    pProx = BadlandsSet.GetProximityManager()
    
    reload(DS9FXSavedConfig)

    if DS9FXSavedConfig.BadlandsVortexVariant == 1:
        reload(DS9FXSavedConfig)
        
        # High setting
        if DS9FXSavedConfig.BadlandsVortex == 3:
            # Many objects to load, iterate through them and their locations
            iCount = 0
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex3, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize) 

                # Finally increase the iCount by 2... We actually use 2 models so that's why we increase the number by 2
                iCount = iCount + 2
                if iCount > 56:
                    break

            # 2nd Model, the same procedure...
            iCount = 1
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex4, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize2) 

                # Finally increase the iCount by 2... We actually use 2 models so that's why we increase the number by 2
                iCount = iCount + 2
                if iCount > 56:
                    break

        # Med setting
        elif DS9FXSavedConfig.BadlandsVortex == 2:
            # Fewer objects to load, iterate through them and their locations
            iCount = 0
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex3, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize) 

                # Finally increase the iCount by 4...
                iCount = iCount + 4
                if iCount > 56:
                    break

            # 2nd Model, the same procedure...
            iCount = 1
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex4, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize2) 

                # Finally increase the iCount by 4...
                iCount = iCount + 4
                if iCount > 56:
                    break
            
        # Low setting
        elif DS9FXSavedConfig.BadlandsVortex == 1:
            # Fewer objects to load, iterate through them and their locations
            iCount = 0
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex3, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize) 

                # Finally increase the iCount by 6...
                iCount = iCount + 6
                if iCount > 56:
                    break

            # 2nd Model, the same procedure...
            iCount = 1
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex4, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize2) 

                # Finally increase the iCount by 6...
                iCount = iCount + 6
                if iCount > 56:
                    break
                        
        # None
        else:
            return


    else:
        reload(DS9FXSavedConfig)
        
        # High setting
        if DS9FXSavedConfig.BadlandsVortex == 3:
            # Many objects to load, iterate through them and their locations
            iCount = 0
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize) 

                # Finally increase the iCount by 2... We actually use 2 models so that's why we increase the number by 2
                iCount = iCount + 2
                if iCount > 56:
                    break

            # 2nd Model, the same procedure...
            iCount = 1
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex2, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize2) 

                # Finally increase the iCount by 2... We actually use 2 models so that's why we increase the number by 2
                iCount = iCount + 2
                if iCount > 56:
                    break

        # Med setting
        elif DS9FXSavedConfig.BadlandsVortex == 2:
            # Fewer objects to load, iterate through them and their locations
            iCount = 0
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize) 

                # Finally increase the iCount by 4...
                iCount = iCount + 4
                if iCount > 56:
                    break

            # 2nd Model, the same procedure...
            iCount = 1
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex2, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize2) 

                # Finally increase the iCount by 4...
                iCount = iCount + 4
                if iCount > 56:
                    break
            
        # Low setting
        elif DS9FXSavedConfig.BadlandsVortex == 1:
            # Fewer objects to load, iterate through them and their locations
            iCount = 0
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize) 

                # Finally increase the iCount by 6...
                iCount = iCount + 6
                if iCount > 56:
                    break

            # 2nd Model, the same procedure...
            iCount = 1
            strPos = "Vortex "
            
            while not iCount > 56:
                strName = strPos + str(iCount)
                pObj = loadspacehelper.CreateShip(DS9FXShips.Vortex2, BadlandsSet, strName, strName)

                pObject = MissionLib.GetShip(strName, BadlandsSet)
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0, 0.33)
                pObject.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                pObject.SetInvincible(1)
                pObject.SetHurtable(0)
                pObject.SetTargetable(0)
                pObject.SetCollisionsOn(0)
                pProx.RemoveObject(pObject)
                pObject.SetScale(vortexSize2) 

                # Finally increase the iCount by 6...
                iCount = iCount + 6
                if iCount > 56:
                    break
                        
        # None
        else:
            return
