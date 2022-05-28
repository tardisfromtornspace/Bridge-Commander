import App
import Foundation

#mode = Foundation.MutatorDef("Shuttle View Bridge Plugin")

class ShuttleView(Foundation.BridgePluginDef):
    def __call__(self, Plug, pBridgeSet, oBridgeInfo):
        # Camera setup(s)
        #print "ShuttleView start"
        if oBridgeInfo.__dict__.has_key("ViewScreenCamera"):
            #print "Has key"
            pOldCamera = App.CameraObjectClass_GetObject(None, "ViewScreenCamera")
            if pOldCamera:
                pOldCamera.GetContainingSet().DeleteCameraFromSet("ViewScreenCamera")
            pViewScreen = pBridgeSet.GetViewScreen()
            pCamera = pViewScreen.GetRemoteCam()
            print "Old Camera", pCamera
            if (not oBridgeInfo.__dict__.has_key("pOrgCamera")) and pCamera != None:# (oBridgeInfo.__dict__.has_key("pOrgCamera") and oBridgeInfo.pOrgCamera == None):
                oBridgeInfo.pOrgCamera = pCamera
            pPlayerPos = oBridgeInfo.pShip.GetWorldLocation()
            x = pPlayerPos.GetX()
            y = pPlayerPos.GetY()
            z = pPlayerPos.GetZ()
            if oBridgeInfo.ViewScreenCamera.has_key("Position"):
                x = oBridgeInfo.ViewScreenCamera["Position"][0]
                y = oBridgeInfo.ViewScreenCamera["Position"][1]
                z = oBridgeInfo.ViewScreenCamera["Position"][2]
            pCamera = App.CameraObjectClass_Create(x,y,z,1.55,0,0,1, "ViewScreenCamera")

            import Camera
            Camera.PlaceCameraInPlayerSet(pCamera, oBridgeInfo.pShip)
            Camera.KeepCameraInPlayerSet(pCamera)
            if Camera.__dict__.has_key(oBridgeInfo.ViewScreenCamera["Mode"][0]):
                toApply = (pCamera,)
                for toEval in oBridgeInfo.ViewScreenCamera["Mode"][1]:
                    toApply = toApply + (eval(toEval),)
                toApply = toApply + (1,)
                # The above works...
                #print toApply
                apply(Camera.__dict__[oBridgeInfo.ViewScreenCamera["Mode"][0]], toApply)
            if oBridgeInfo.ViewScreenCamera.has_key("Extra Commands"):
                exec(oBridgeInfo.ViewScreenCamera["Extra Commands"])
            pViewScreen.SetRemoteCam(pCamera)
        else:
            #print "Doesn\'t has the key, revert to default Camera"
            if oBridgeInfo.__dict__.has_key("pOrgCamera"):
                pViewScreen = pBridgeSet.GetViewScreen()
                pViewScreen.SetRemoteCam(oBridgeInfo.pOrgCamera)
                del oBridgeInfo.__dict__["pOrgCamera"]
                pOldCamera = App.CameraObjectClass_GetObject(None, "ViewScreenCamera")
                if pOldCamera:
                    pOldCamera.GetContainingSet().DeleteCameraFromSet("ViewScreenCamera")
        #print "Done with ShuttleView"

oShuttleView = ShuttleView("Shuttle View Bridge Plugin")#, dict = {"modes": [mode]})
