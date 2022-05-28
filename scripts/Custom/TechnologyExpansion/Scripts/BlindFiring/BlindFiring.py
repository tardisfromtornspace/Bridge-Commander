from bcdebug import debug
# Imports
import App
import MissionLib
import Bridge.BridgeUtils
#import QuickBattle.QuickBattle
import loadspacehelper

# Start Of Blind Fire User Adjustable Settings

# How often the location of the targets is updated - in 30 second increments (1 = 30 seconds, 2 = 60 seconds, etc.)
resetdelay = 1
# How fast the fire points move
firepointspeed = 8
# Speed of the Mouse Pick fire
iMousePickSense = 50

# End Of Blind Fire User Adjustable Settings

REMOVE_POINTER_FROM_SET = 190
BLIND_FIRE_R = App.UtopiaModule_GetNextEventType()
BLIND_FIRE_Z = App.UtopiaModule_GetNextEventType()
BLIND_FIRE_D = App.UtopiaModule_GetNextEventType()
BLIND_FIRE_V = App.UtopiaModule_GetNextEventType()
BLIND_FIRE_A = App.UtopiaModule_GetNextEventType()
BLIND_FIRE_F = App.UtopiaModule_GetNextEventType()
BLIND_FIRE_P = App.UtopiaModule_GetNextEventType()
BLIND_FIRE_S = App.UtopiaModule_GetNextEventType()
BLIND_FIRE_M = App.UtopiaModule_GetNextEventType()
BLIND_FIRE_FIXED = App.UtopiaModule_GetNextEventType()
CEASE_FIRE = App.UtopiaModule_GetNextEventType()
pOn = 0


def BFCreateMenu(pSpecialMenu):
        #global BLIND_FIRE_R, BLIND_FIRE_Z, BLIND_FIRE_D, BLIND_FIRE_V, BLIND_FIRE_A, BLIND_FIRE_F, BLIND_FIRE_P, BLIND_FIRE_S, CEASE_FIRE, BLIND_FIRE_M
	#this import is copied from sleight's FTB framework. Used in TGL bypass
	debug(__name__ + ", BFCreateMenu")
	import Custom.TechnologyExpansion.Scripts.GUIUtils

	#grab the database of strings
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/TechnologyExpansion.tgl")

        # Setup Our Button Instances
        #BLIND_FIRE_R = App.Game_GetNextEventType()
        #BLIND_FIRE_Z = App.Game_GetNextEventType()
        #BLIND_FIRE_D = App.Game_GetNextEventType()
        #BLIND_FIRE_V = App.Game_GetNextEventType()
        #BLIND_FIRE_A = App.Game_GetNextEventType()
        #BLIND_FIRE_F = App.Game_GetNextEventType()
        #BLIND_FIRE_P = App.Game_GetNextEventType()
        #BLIND_FIRE_S = App.Game_GetNextEventType()
        #BLIND_FIRE_M = App.Game_GetNextEventType()
        #CEASE_FIRE = App.Game_GetNextEventType()

	# Create the Blind Fire menu
	pBlindFireName = pDatabase.GetString("CloakedFiring")
	pBlindFireName.SetString("Blind Fire")
	pBlindFireMenu = App.STCharacterMenu_CreateW(pBlindFireName)
	pSpecialMenu.AddChild(pBlindFireMenu)

        # Add the individual buttons for the various coordinations to the Blind Fire menu
	pBlindFireR = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Random Coordinates", BLIND_FIRE_R, pSpecialMenu, 1)
	pBlindFireMenu.AddChild(pBlindFireR)
	pBlindFireZ = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Zero Elevation", BLIND_FIRE_Z, pSpecialMenu, 1)
	pBlindFireMenu.AddChild(pBlindFireZ)
	pBlindFireD = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Dorsal Sweep", BLIND_FIRE_D, pSpecialMenu, 1)
	pBlindFireMenu.AddChild(pBlindFireD)
	pBlindFireV = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Ventral Sweep", BLIND_FIRE_V, pSpecialMenu, 1)
	pBlindFireMenu.AddChild(pBlindFireV)
	pBlindFireA = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Aft Sweep", BLIND_FIRE_A, pSpecialMenu, 1)
	pBlindFireMenu.AddChild(pBlindFireA)
	pBlindFireF = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Forward Sweep", BLIND_FIRE_F, pSpecialMenu, 1)
	pBlindFireMenu.AddChild(pBlindFireF)
	pBlindFireP = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Port Sweep", BLIND_FIRE_P, pSpecialMenu, 1)
	pBlindFireMenu.AddChild(pBlindFireP)
	pBlindFireS = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Starboard Sweep", BLIND_FIRE_S, pSpecialMenu, 1)
	pBlindFireMenu.AddChild(pBlindFireS)
	pBlindFireM = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Pick Mouse", BLIND_FIRE_M, pSpecialMenu, 1)
	pBlindFireMenu.AddChild(pBlindFireM)
	pBlindFireFixed = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Fixed Ahead", BLIND_FIRE_FIXED, pSpecialMenu, 1)
	pBlindFireMenu.AddChild(pBlindFireFixed)
	pCeaseFire = Custom.TechnologyExpansion.Scripts.GUIUtils.CreateIntButton("Cease Fire", CEASE_FIRE, pSpecialMenu, 1)
	pBlindFireMenu.AddChild(pCeaseFire)

        # Run a definition depending on the button pressed
	App.g_kEventManager.AddBroadcastPythonFuncHandler(BLIND_FIRE_R, MissionLib.GetMission(), __name__ + ".BlindFireR")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(BLIND_FIRE_Z, MissionLib.GetMission(), __name__ + ".BlindFireZ")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(BLIND_FIRE_D, MissionLib.GetMission(), __name__ + ".BlindFireD")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(BLIND_FIRE_V, MissionLib.GetMission(), __name__ + ".BlindFireV")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(BLIND_FIRE_A, MissionLib.GetMission(), __name__ + ".BlindFireA")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(BLIND_FIRE_F, MissionLib.GetMission(), __name__ + ".BlindFireF")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(BLIND_FIRE_P, MissionLib.GetMission(), __name__ + ".BlindFireP")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(BLIND_FIRE_S, MissionLib.GetMission(), __name__ + ".BlindFireS")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(BLIND_FIRE_M, MissionLib.GetMission(), __name__ + ".BlindFireM")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(BLIND_FIRE_FIXED, MissionLib.GetMission(), __name__ + ".BlindFireFixed")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(CEASE_FIRE, MissionLib.GetMission(), __name__ + ".CeaseFire")
	
	App.g_kLocalizationManager.Unload(pDatabase)

# Below are the definitions for the various fire sequences - its a messy setup but it works

def BlindFireR(pObject, pEvent, pType="R"):
	debug(__name__ + ", BlindFireR")
	print "Calling BF Random"
        BlindFire(pType)
def BlindFireZ(pObject, pEvent, pType="Z"):
        debug(__name__ + ", BlindFireZ")
        BlindFire(pType)
def BlindFireD(pObject, pEvent, pType="D"):
        debug(__name__ + ", BlindFireD")
        BlindFire(pType)
def BlindFireV(pObject, pEvent, pType="V"):
        debug(__name__ + ", BlindFireV")
        BlindFire(pType)
def BlindFireA(pObject, pEvent, pType="A"):
        debug(__name__ + ", BlindFireA")
        BlindFire(pType)
def BlindFireF(pObject, pEvent, pType="F"):
        debug(__name__ + ", BlindFireF")
        BlindFire(pType)
def BlindFireP(pObject, pEvent, pType="P"):
        debug(__name__ + ", BlindFireP")
        BlindFire(pType)
def BlindFireS(pObject, pEvent, pType="S"):
        debug(__name__ + ", BlindFireS")
        BlindFire(pType)
def BlindFireM(pObject, pEvent, pType="M"):
	debug(__name__ + ", BlindFireM")
	global pOn
	if pOn == 0:
                pOn = 1
        else:
                pOn = 0
        NewFirePointM(pType)
def BlindFireFixed(pObject, pEvent, pType="Fixed"):
	debug(__name__ + ", BlindFireFixed")
	global pOn
	if pOn == 0:
                pOn = 1
        else:
                pOn = 0
        NewFirePointM(pType)
def BlindFire(pType):
	debug(__name__ + ", BlindFire")
	global pOn
	pOn = 1
	NewFirePoint(pType)
def CeaseFire(pObject, pEvent):
	debug(__name__ + ", CeaseFire")
	global pOn
	pOn = 0
	NewFirePoint()

def NewFirePoint(pType="S"):
        debug(__name__ + ", NewFirePoint")
        global pOn
        global gType
        gType = pType
        pShip = MissionLib.GetPlayer()
        pSet = pShip.GetContainingSet()

        global pNewFirePoint1
        global pNewFirePoint2
        global pNewFirePoint3
        global pNewFirePoint4
        global pNewFirePoint5
        global pNewFirePoint6
        global pNewFirePoint7
        global pNewFirePoint8
        global pNewFirePoint9
        global pNewFirePoint10
        global resetdelay
        resetdelay = 1

        # Try to remove any existing fire points from the game

        pFirePoint = []
        pFirePoint[:0] = ["FirePoint1" + pShip.GetName()]
        pFirePoint[:0] = ["FirePoint2" + pShip.GetName()]
        pFirePoint[:0] = ["FirePoint3" + pShip.GetName()]
        pFirePoint[:0] = ["FirePoint4" + pShip.GetName()]
        pFirePoint[:0] = ["FirePoint5" + pShip.GetName()]
        pFirePoint[:0] = ["FirePoint6" + pShip.GetName()]
        pFirePoint[:0] = ["FirePoint7" + pShip.GetName()]
        pFirePoint[:0] = ["FirePoint8" + pShip.GetName()]
        pFirePoint[:0] = ["FirePoint9" + pShip.GetName()]
        pFirePoint[:0] = ["FirePoint10" + pShip.GetName()]

        for i in pFirePoint:
            pFirePointNumeral = i
            try:
                pSet.RemoveObjectFromSet(pFirePointNumeral)
            except:
                pass

        # Create our new fire points
	pNewFirePoint1 = loadspacehelper.CreateShip("Firepoint", pSet, "FirePoint1" + pShip.GetName(), "", 0)
	pNewFirePoint2 = loadspacehelper.CreateShip("Firepoint", pSet, "FirePoint2" + pShip.GetName(), "", 0)
	pNewFirePoint3 = loadspacehelper.CreateShip("Firepoint", pSet, "FirePoint3" + pShip.GetName(), "", 0)
        pNewFirePoint4 = loadspacehelper.CreateShip("Firepoint", pSet, "FirePoint4" + pShip.GetName(), "", 0)
        pNewFirePoint5 = loadspacehelper.CreateShip("Firepoint", pSet, "FirePoint5" + pShip.GetName(), "", 0)
        pNewFirePoint6 = loadspacehelper.CreateShip("Firepoint", pSet, "FirePoint6" + pShip.GetName(), "", 0)
        pNewFirePoint7 = loadspacehelper.CreateShip("Firepoint", pSet, "FirePoint7" + pShip.GetName(), "", 0)
        pNewFirePoint8 = loadspacehelper.CreateShip("Firepoint", pSet, "FirePoint8" + pShip.GetName(), "", 0)
        pNewFirePoint9 = loadspacehelper.CreateShip("Firepoint", pSet, "FirePoint9" + pShip.GetName(), "", 0)
        pNewFirePoint10 = loadspacehelper.CreateShip("Firepoint", pSet, "FirePoint10" + pShip.GetName(), "", 0)

        # Remove them from the proximity manager
	pProx = pSet.GetProximityManager()
	pSet.SetProximityManagerActive(1)
	pProx.RemoveObject(pNewFirePoint1)
	pProx.RemoveObject(pNewFirePoint2)
	pProx.RemoveObject(pNewFirePoint3)
	pProx.RemoveObject(pNewFirePoint4)
	pProx.RemoveObject(pNewFirePoint5)
	pProx.RemoveObject(pNewFirePoint6)
	pProx.RemoveObject(pNewFirePoint7)
	pProx.RemoveObject(pNewFirePoint8)
	pProx.RemoveObject(pNewFirePoint9)
	pProx.RemoveObject(pNewFirePoint10)

        # Make sure they are not targetable by us
        pNewFirePoint1.SetTargetable (0)
        pNewFirePoint2.SetTargetable (0)
        pNewFirePoint3.SetTargetable (0)
        pNewFirePoint4.SetTargetable (0)
        pNewFirePoint5.SetTargetable (0)
        pNewFirePoint6.SetTargetable (0)
        pNewFirePoint7.SetTargetable (0)
        pNewFirePoint8.SetTargetable (0)
        pNewFirePoint9.SetTargetable (0)
        pNewFirePoint10.SetTargetable (0)
        
        #...or anyone else
        #for i in pFirePoint:
            #pFirePointNumeral = i
            #pNeutral.RemoveName(pFirePointNumeral)

        BeginFiringSequence (pShip, pSet, pType)

        return 0


def NewFirePointM(pType):
        debug(__name__ + ", NewFirePointM")
        global pOn, gType, resetdelay, pNewFirePoint1
        gType = pType
        pShip = MissionLib.GetPlayer()
        pSet = pShip.GetContainingSet()
        resetdelay = 0.01
        
        pNewFirePoint1 = MissionLib.GetShip("FirePoint1" + pShip.GetName())
        if not pNewFirePoint1:
                pNewFirePoint1 = loadspacehelper.CreateShip("Firepoint", pSet, "FirePoint1" + pShip.GetName(), "", 0)
                #pNewFirePoint1.SetTargetable(0)
                
        FirePointLocation(pNewFirePoint1, pShip, pType)
        sTarget = "FirePoint1" + pShip.GetName()
        
        if pOn == 0:
                RemoveFirepoint(pSet, "FirePoint1" + pShip.GetName())
        
        SetTargetM(pShip, pSet, pType, sTarget)


def BeginFiringSequence (pShip, pSet, pType):
        debug(__name__ + ", BeginFiringSequence")
        global pOn
        global pNewFirePoint1
        global pNewFirePoint2
        global pNewFirePoint3
        global pNewFirePoint4
        global pNewFirePoint5
        global pNewFirePoint6
        global pNewFirePoint7
        global pNewFirePoint8
        global pNewFirePoint9
        global pNewFirePoint10
        pPlayerName = MissionLib.GetPlayer().GetName()
    
        FirePointLocation(pNewFirePoint1, pShip, pType)
        FirePointLocation(pNewFirePoint2, pShip, pType)
	FirePointLocation(pNewFirePoint3, pShip, pType)
	FirePointLocation(pNewFirePoint4, pShip, pType)
	FirePointLocation(pNewFirePoint5, pShip, pType)
	FirePointLocation(pNewFirePoint6, pShip, pType)
	FirePointLocation(pNewFirePoint7, pShip, pType)
	FirePointLocation(pNewFirePoint8, pShip, pType)
	FirePointLocation(pNewFirePoint9, pShip, pType)
        FirePointLocation(pNewFirePoint10, pShip, pType)
	
        pRandom = App.g_kSystemWrapper.GetRandomNumber(10)
        if (pOn == 0):
                Cleanup(pSet)
        else:
                if (pRandom < 1):
                        pRandom = 1
                if (pRandom == 1):
                        pTarget = "FirePoint1" + pPlayerName
                elif (pRandom == 2):
                        pTarget = "FirePoint2" + pPlayerName
                elif (pRandom == 3):
                        pTarget = "FirePoint3" + pPlayerName
                elif (pRandom == 4):
                        pTarget = "FirePoint4" + pPlayerName
                elif (pRandom == 5):
                        pTarget = "FirePoint5" + pPlayerName
                elif (pRandom == 6):
                        pTarget = "FirePoint6" + pPlayerName
                elif (pRandom == 7):
                        pTarget = "FirePoint7" + pPlayerName
                elif (pRandom == 8):
                        pTarget = "FirePoint8" + pPlayerName
                elif (pRandom == 9):
                        pTarget = "FirePoint9" + pPlayerName
                elif (pRandom == 10):
                        pTarget = "FirePoint10" + pPlayerName
                else:
                        print ("Something Went Wrong")

                SetTarget (pShip, pSet, pType, pTarget)

        return 0
        
def FirePointLocation(pNewFirePoint, pShip, pType):
	debug(__name__ + ", FirePointLocation")
	pPlayer = MissionLib.GetPlayer()
	vLocation = pShip.GetWorldLocation()
	pShipX = vLocation.GetX()
	pShipY = vLocation.GetY()
	pShipZ = vLocation.GetZ()
	kLocation = App.TGPoint3()
	pGame = App.Game_GetCurrentGame()
	kForward = pShip.GetWorldForwardTG()
	kUp = pShip.GetWorldUpTG()
	kRight = pShip.GetWorldRightTG()
	iDist = 300

	if (pType == "R"):
                X = ((App.g_kSystemWrapper.GetRandomNumber(300) - 150.0))
                Y = ((App.g_kSystemWrapper.GetRandomNumber(300) - 150.0))
                Z = ((App.g_kSystemWrapper.GetRandomNumber(300) - 150.0))
        elif (pType == "Z"):
                iMx = App.g_kSystemWrapper.GetRandomNumber(600) - 300
                iMy = App.g_kSystemWrapper.GetRandomNumber(600) - 300
		
                X = iMx * kForward.GetX() + iMy * kRight.GetX()
                Y = iMx * kForward.GetY() + iMy * kRight.GetY()
                Z = iMx * kForward.GetZ() + iMy * kRight.GetZ()
        elif (pType == "D"):
                iMx = App.g_kSystemWrapper.GetRandomNumber(600) - 300
                iMy = App.g_kSystemWrapper.GetRandomNumber(600) - 300
		
                X = iMx * kForward.GetX() + iMy * kRight.GetX() + iDist * kUp.GetX()
                Y = iMx * kForward.GetY() + iMy * kRight.GetY() + iDist * kUp.GetY()
                Z = iMx * kForward.GetZ() + iMy * kRight.GetZ() + iDist * kUp.GetZ()
        elif (pType == "V"):
                iMx = App.g_kSystemWrapper.GetRandomNumber(600) - 300
                iMy = App.g_kSystemWrapper.GetRandomNumber(600) - 300
		
                X = iMx * kForward.GetX() + iMy * kRight.GetX() + -iDist * kUp.GetX()
                Y = iMx * kForward.GetY() + iMy * kRight.GetY() + -iDist * kUp.GetY()
                Z = iMx * kForward.GetZ() + iMy * kRight.GetZ() + -iDist * kUp.GetZ()
        elif (pType == "A"):
                iMx = App.g_kSystemWrapper.GetRandomNumber(600) - 300
                iMy = App.g_kSystemWrapper.GetRandomNumber(600) - 300
		
                X = -iDist * kForward.GetX() + iMx * kRight.GetX() + iMy * kUp.GetX()
                Y = -iDist * kForward.GetY() + iMx * kRight.GetY() + iMy * kUp.GetY()
                Z = -iDist * kForward.GetZ() + iMx * kRight.GetZ() + iMy * kUp.GetZ()
        elif (pType == "F"):
                iMx = App.g_kSystemWrapper.GetRandomNumber(600) - 300
                iMy = App.g_kSystemWrapper.GetRandomNumber(600) - 300
		
                X = iDist * kForward.GetX() + iMx * kRight.GetX() + iMy * kUp.GetX()
                Y = iDist * kForward.GetY() + iMx * kRight.GetY() + iMy * kUp.GetY()
                Z = iDist * kForward.GetZ() + iMx * kRight.GetZ() + iMy * kUp.GetZ()
        elif (pType == "P"):
                iMx = App.g_kSystemWrapper.GetRandomNumber(600) - 300
                iMy = App.g_kSystemWrapper.GetRandomNumber(600) - 300
		
                X = iMx * kForward.GetX() + -iDist * kRight.GetX() + iMy * kUp.GetX()
                Y = iMx * kForward.GetY() + -iDist * kRight.GetY() + iMy * kUp.GetY()
                Z = iMx * kForward.GetZ() + -iDist * kRight.GetZ() + iMy * kUp.GetZ()
        elif (pType == "S"):
                iMx = App.g_kSystemWrapper.GetRandomNumber(600) - 300
                iMy = App.g_kSystemWrapper.GetRandomNumber(600) - 300
		
                X = iMx * kForward.GetX() + iDist * kRight.GetX() + iMy * kUp.GetX()
                Y = iMx * kForward.GetY() + iDist * kRight.GetY() + iMy * kUp.GetY()
                Z = iMx * kForward.GetZ() + iDist * kRight.GetZ() + iMy * kUp.GetZ()
        elif (pType == "M"):
                pGame = App.Game_GetCurrentGame()
                pCam = pGame.GetPlayerCamera()
                kForward = pCam.GetWorldForwardTG()
                kUp = pCam.GetWorldUpTG()
                kRight = pCam.GetWorldRightTG()
		
                iMx = App.g_kInputManager.GetMousePos().x * iMousePickSense - iMousePickSense / 2
                iMy = App.g_kInputManager.GetMousePos().y * -iMousePickSense + iMousePickSense / 2
		iDist = 300

                X = iDist * kForward.GetX() + iMx * kRight.GetX() + iMy * kUp.GetX()
                Y = iDist * kForward.GetY() + iMx * kRight.GetY() + iMy * kUp.GetY()
                Z = iDist * kForward.GetZ() + iMx * kRight.GetZ() + iMy * kUp.GetZ()
		
		# this should make sure we see the firepoint even if sensors are disabled
		#if pPlayer and not pPlayer.GetTarget():
		#	pPlayer.SetTarget(pNewFirePoint.GetName())
	elif (pType == "Fixed"):
                iMx = 0.5
                iMy = 0.5
		
                X = iDist * kForward.GetX() + iMx * kRight.GetX() + iMy * kUp.GetX()
                Y = iDist * kForward.GetY() + iMx * kRight.GetY() + iMy * kUp.GetY()
                Z = iDist * kForward.GetZ() + iMx * kRight.GetZ() + iMy * kUp.GetZ()
        else:
                print ("Houstan, We Have A Problem")

	kLocation.SetXYZ(pShipX + X, pShipY + Y, pShipZ + Z)

        #pNewFirePoint.AlignToVectors(pShip.GetWorldForwardTG(), pShip.GetWorldUpTG())
        pNewFirePoint.SetTranslate(kLocation)
        pNewFirePoint.UpdateNodeOnly()

        # part below not needed?!?
	#vImpPointP = App.TGPoint3()
	#vImpPointP.SetXYZ(5.0, 0.0, 0.0)

	#try:
        #        pShip.AttachObject(pNewFirePoint)
        #        pNewFirePoint.SetImpulse(firepointspeed, vImpPointP, App.ShipClass.DIRECTION_MODEL_SPACE)
        #except:
        #        pass

        return 0

def SetTarget (pShip, pSet, pType, pTarget):
        debug(__name__ + ", SetTarget")
        pWeaponSystem = pShip.GetPhaserSystem()
	if not pWeaponSystem:
		return 1
	vSubsystemOffset = App.TGPoint3()
	vSubsystemOffset.SetXYZ(0, 0, 0)
	pTargetClass = App.ObjectClass_GetObject(pSet, pTarget)
	pWeaponSystem.StartFiring(pTargetClass, vSubsystemOffset)

        #App.g_kEventManager.AddBroadcastPythonFuncHandler(QuickBattle.QuickBattle.ET_END_SIMULATION,App.Game_GetCurrentGame(), __name__ + ".Terminate")

        global pSeq
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "Delay"), resetdelay)
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "BeginFiringResequence"))
        MissionLib.QueueActionToPlay(pSeq)

        # App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_POWER_CONTROL_REFRESH_TIMER, pMission, __name__ + ".BeginFiringResequence" )

        return 0


def SetTargetM(pShip, pSet, pType, sTarget):
        debug(__name__ + ", SetTargetM")
        pWeaponSystem = pShip.GetPhaserSystem()
	vSubsystemOffset = App.TGPoint3()
	vSubsystemOffset.SetXYZ(0, 0, 0)
	sTargetClass = App.ObjectClass_GetObject(pSet, sTarget)
        pShip.SetTarget(sTarget)
	#pWeaponSystem.StartFiring(sTargetClass, vSubsystemOffset)

        #App.g_kEventManager.AddBroadcastPythonFuncHandler(QuickBattle.QuickBattle.ET_END_SIMULATION,App.Game_GetCurrentGame(), __name__ + ".Terminate")

        global pSeq
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "Delay"), resetdelay)
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "BeginFiringResequenceM"))
        MissionLib.QueueActionToPlay(pSeq)
        return 0


def Delay(pAction):
        debug(__name__ + ", Delay")
        return 0


def RemoveFirepoint(pSet, FirePointName):
        debug(__name__ + ", RemoveFirepoint")
        pSet.RemoveObjectFromSet(FirePointName)
        
        # send clients to remove this object
        if App.g_kUtopiaModule.IsMultiplayer():
                # Now send a message to everybody else that the score was updated.
                # allocate the message.
                pMessage = App.TGMessage_Create()
                pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                # Setup the stream.
                kStream = App.TGBufferStream()		# Allocate a local buffer stream.
                kStream.OpenBuffer(256)				# Open the buffer stream with a 256 byte buffer.
	
                # Write relevant data to the stream.
                # First write message type.
                kStream.WriteChar(chr(REMOVE_POINTER_FROM_SET))

                # Write the name of killed ship
                for i in range(len(FirePointName)):
                        kStream.WriteChar(FirePointName[i])
                # set the last char:
                kStream.WriteChar('\0')

                # Okay, now set the data from the buffer stream to the message
                pMessage.SetDataFromStream(kStream)

                # Send the message to everybody but me.  Use the NoMe group, which
                # is set up by the multiplayer game.
                pNetwork = App.g_kUtopiaModule.GetNetwork()
                if not App.IsNull(pNetwork):
                        if App.g_kUtopiaModule.IsHost():
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                        else:
                                pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

                # We're done.  Close the buffer.
                kStream.CloseBuffer()


def Cleanup (pSet):
        debug(__name__ + ", Cleanup")
        pPlayerName = MissionLib.GetPlayer().GetName()
        
        RemoveFirepoint(pSet, "FirePoint1" + pPlayerName)
        RemoveFirepoint(pSet, "FirePoint2" + pPlayerName)
        RemoveFirepoint(pSet, "FirePoint3" + pPlayerName)
        RemoveFirepoint(pSet, "FirePoint4" + pPlayerName)
        RemoveFirepoint(pSet, "FirePoint5" + pPlayerName)
        RemoveFirepoint(pSet, "FirePoint6" + pPlayerName)
        RemoveFirepoint(pSet, "FirePoint7" + pPlayerName)
        RemoveFirepoint(pSet, "FirePoint8" + pPlayerName)
        RemoveFirepoint(pSet, "FirePoint9" + pPlayerName)
        RemoveFirepoint(pSet, "FirePoint10" + pPlayerName)


def Terminate (pObject, pEvent):
        debug(__name__ + ", Terminate")
        global pOn
        pOn = 0
        return 0

def BeginFiringResequenceM(pAction):
        debug(__name__ + ", BeginFiringResequenceM")
        global pOn
        global gType
        global pNewFirePoint1
        pShip = MissionLib.GetPlayer()
        pSet = pShip.GetContainingSet()

        if (pOn == 1):
    
                FirePointLocation(pNewFirePoint1, pShip, gType)
	
                pPlayerName = pShip.GetName()
                
                sTarget = "FirePoint1" + pPlayerName

                SetTargetResequenceM(pShip, pSet, sTarget)

        else:

                pass

        return 0


def BeginFiringResequence (pAction):
        debug(__name__ + ", BeginFiringResequence")
        global pOn
        global gType
        global pNewFirePoint1
        global pNewFirePoint2
        global pNewFirePoint3
        global pNewFirePoint4
        global pNewFirePoint5
        global pNewFirePoint6
        global pNewFirePoint7
        global pNewFirePoint8
        global pNewFirePoint9
        global pNewFirePoint10
        pShip = MissionLib.GetPlayer()
        pSet = pShip.GetContainingSet()

        if (pOn == 1):
    
                FirePointLocation(pNewFirePoint1, pShip, gType)
                FirePointLocation(pNewFirePoint2, pShip, gType)
                FirePointLocation(pNewFirePoint3, pShip, gType)
                FirePointLocation(pNewFirePoint4, pShip, gType)
                FirePointLocation(pNewFirePoint5, pShip, gType)
                FirePointLocation(pNewFirePoint6, pShip, gType)
                FirePointLocation(pNewFirePoint7, pShip, gType)
                FirePointLocation(pNewFirePoint8, pShip, gType)
                FirePointLocation(pNewFirePoint9, pShip, gType)
                FirePointLocation(pNewFirePoint10, pShip, gType)
	
                pPlayerName = pShip.GetName()
                pRandom = App.g_kSystemWrapper.GetRandomNumber(10)
                
                if (pRandom < 1):
                        pRandom = 1
                if (pRandom == 1):
                        pTarget = "FirePoint1" + pPlayerName
                elif (pRandom == 2):
                        pTarget = "FirePoint2" + pPlayerName
                elif (pRandom == 3):
                        pTarget = "FirePoint3" + pPlayerName
                elif (pRandom == 4):
                        pTarget = "FirePoint4" + pPlayerName
                elif (pRandom == 5):
                        pTarget = "FirePoint5" + pPlayerName
                elif (pRandom == 6):
                        pTarget = "FirePoint6" + pPlayerName
                elif (pRandom == 7):
                        pTarget = "FirePoint7" + pPlayerName
                elif (pRandom == 8):
                        pTarget = "FirePoint8" + pPlayerName
                elif (pRandom == 9):
                        pTarget = "FirePoint9" + pPlayerName
                elif (pRandom == 10):
                        pTarget = "FirePoint10" + pPlayerName
                else:
                        print ("Something Went Wrong")

                SetTargetResequence (pShip, pSet, pTarget)

	else:
		print ("BlindFire not active")
		pass

        return 0

def SetTargetResequence (pShip, pSet, pTarget):
        debug(__name__ + ", SetTargetResequence")
        pWeaponSystem = pShip.GetPhaserSystem()
	if not pWeaponSystem:
		return 1
	vSubsystemOffset = App.TGPoint3()
	vSubsystemOffset.SetXYZ(0, 0, 0)
	pTargetClass = App.ObjectClass_GetObject(pSet, pTarget)
	pWeaponSystem.StartFiring(pTargetClass, vSubsystemOffset)
        global pSeq
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "Delay"), resetdelay)
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "BeginFiringResequence"))
        MissionLib.QueueActionToPlay(pSeq)


def SetTargetResequenceM(pShip, pSet, pTarget):
        debug(__name__ + ", SetTargetResequenceM")
        pWeaponSystem = pShip.GetPhaserSystem()
	vSubsystemOffset = App.TGPoint3()
	vSubsystemOffset.SetXYZ(0, 0, 0)
	pTargetClass = App.ObjectClass_GetObject(pSet, pTarget)
	#pWeaponSystem.StartFiring(pTargetClass, vSubsystemOffset)
        global pSeq
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "Delay"), resetdelay)
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "BeginFiringResequenceM"))
        MissionLib.QueueActionToPlay(pSeq)


def CreateKeys(mode):
        #global BLIND_FIRE_R, BLIND_FIRE_Z, BLIND_FIRE_D, BLIND_FIRE_V, BLIND_FIRE_A, BLIND_FIRE_F, BLIND_FIRE_P, BLIND_FIRE_S, CEASE_FIRE, BLIND_FIRE_M
        debug(__name__ + ", CreateKeys")
        KeyBindingsConfig = __import__ ("Custom.TechnologyExpansion.Scripts.BlindFiring.LoadMenu")
        KeyBindingsConfig.AddKeyBind("Random Coordinates", BLIND_FIRE_R, 1, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Zero Elevation", BLIND_FIRE_Z, 1, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Dorsal Sweep", BLIND_FIRE_D, 1, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Ventral Sweep", BLIND_FIRE_V, 1, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Aft Sweep", BLIND_FIRE_A, 1, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Forward Sweep", BLIND_FIRE_F, 1, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Port Sweep", BLIND_FIRE_P, 1, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Starboard Sweep", BLIND_FIRE_S, 1, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Cease Fire", CEASE_FIRE, 1, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
        KeyBindingsConfig.AddKeyBind("Pick Mouse", BLIND_FIRE_M, 1, App.KeyboardBinding.GET_INT_EVENT, "Ship", mode)
