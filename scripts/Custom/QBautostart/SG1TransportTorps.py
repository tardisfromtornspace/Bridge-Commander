#########################################################
#       SG1 Transport Torps Variant
#
#           by USS Sovereign
#
#
#   A specialized version for SG Pack.
#
#
#   Permissions: Only to be used in SG1 Pack. Don't steal
#   the code... you know the drill.
#########################################################

# Presets
DamageDoneByTorp = 100000
TransportDelayTime = 3
AvailableTorps = 5
SuccessRate = 100
TransportValue = 100

# globals and imports and same old stuff over here

import App
import Libs.LibEngineering
import MissionLib
import string
pMain = None
pTransportButton = None
pAvailableTorpsButton = None
TorpedoBlowUpTimer = None
AvailTorpsTimer = None
TorpedoCount = AvailableTorps


# just to make sure it loads in MP

MODINFO = {     "Author": "\"USS Sovereign\" uss882000@yahoo.co.uk",
                "Version": "0.1.3",
                "License": "GPL",
                "Description": "Transport Torpedo and damage any targeted subsystem",
                "needBridge": 0
            }


# Start a ship check to determine if we need to build a menu actually
def init():
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        # When you change a player ship then initiate the script
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".ShipCheck")
    
# I got the list of HP's that are supposed to have these torps so let's add them here
def ShipCheck(pObject, pEvent):
        global AvailableTorps, TorpedoCount
        
        # grab some values
        pPlayer = MissionLib.GetPlayer()

        
        # With each ET_SET_PLAYER Event reset the torp counter
        TorpedoCount = AvailableTorps
        
        # just to be safe delete the menu
        RemoveMenu()

        # Ship checks using the list given to me. 
        if (GetShipType(pPlayer) == "Daedalus"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "DSC304Daedalus"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "Korolev"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "DSC304Korolev"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "Odyssey"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "DSC304Odyssey"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "OdysseyRefit"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "DSC304OdysseyRefit"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "OdysseyUpgrade"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "DSC304OdysseyUpgrade"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "Apollo"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "DSC304Apollo"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "PrometheusRefit"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "X303Refit"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "PrometheusUpgrade"):
                    BuildMenu()

        elif (GetShipType(pPlayer) == "X303RefitUpgrade"):
                    BuildMenu()

        else:
                    return
# define buttons

def BuildMenu():
	global pMain, pTransportButton, pAvailableTorpsButton, AvailableTorps
    	
    	# we use the tactical menu for this option ;)
    	
	pBridge = App.g_kSetManager.GetSet('bridge')
	pFelixMenu = Libs.LibEngineering.GetBridgeMenu("Tactical")
	pMain = App.STMenu_CreateW(App.TGString("Transport Nukes"))
	pFelixMenu.PrependChild(pMain)
	
	# we need 2 buttons 
	
	pAvailableTorpsButton = Libs.LibEngineering.CreateMenuButton("Nuke Count: " + str(AvailableTorps), "Tactical", __name__ + ".Nothing", 0, pMain)
	pTransportButton = Libs.LibEngineering.CreateMenuButton("Transport", "Tactical", __name__ + ".TransportTorps", 0, pMain)

	pAvailableTorpsButton.SetEnabled()
	pTransportButton.SetEnabled()
	# just for fun lol

	# i don't want to overflow the console anymore :)
	
	# print "BCS: TNG - Transport Torpedo v0.1 Loaded! Congratulations!"

# some things we need to do before we actually beam over the torpedo to the enemy ship
	
def TransportTorps(pObject, pEvent):
        global TorpedoCount, TransportValue
    
        # get some values
        
 	pPlayer = MissionLib.GetPlayer()
 	pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
 	pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        # qb and qbr end combat handelers
        
        pSaffiQB = GetMenuButton("Commander", "End Combat")
        pSaffiQBR = GetQBRMenuButton("Commander", "Configure")

        # qb restart function, pretty much standard in BCS: TNG's mods
        
	if pSaffiQB:
                pSaffiQB.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".TransportTorpReset")

        # qbr restart function

        if pSaffiQBR:
                pSaffiQBR.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".TransportTorpReset")

        # restart really works now in both qb versions

        # App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pMission, __name__ + ".TransportTorpReset")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ShipExploding")
 	
 	# no target?! no beaming
 	
 	if not pTarget:
 	    return

        # too great distance?! no beaming
        
 	if PlTgtDistance(pTarget) > 350:
            return

        # cloaked?! no beaming

        if pPlayer.IsCloaked():
            return

        # no more torps?! no beaming

        if TorpedoCount == 0:
            return

        # Immune to the transport torps?
        if (GetShipType(pTarget) == "OriWarship"):
            return
            
        # if shield value is below certain ammount, you can then beam those torpedoes nicely and will work every time ;)
        # i chose value of 1800, why? well it's more realistic this way. in tng shows shields are not always offline for
        # someone to transport through them.

        # okay changed the value to 1500. 1800 is too high and 1500 maybe, will do some research further.

        # wowbagger mentioned something about even further reducing this value but it is evidental that small ships have weak shields
        # so they don't need to be down for you to be able to transport through them. at least i've seen this in the shows.

        
 	if (pTarget.GetShields() != None):
		if (pTarget.GetShields().GetCurShields(App.ShieldClass.FRONT_SHIELDS) < TransportValue):
                    DamageEnemy(None, None)
                    # recalibrating transporter sir
                    pTransportButton.SetDisabled()
                    
		elif (pTarget.GetShields().GetCurShields(App.ShieldClass.REAR_SHIELDS) < TransportValue):
                    DamageEnemy(None, None)
                    # recalibrating transporter sir
                    pTransportButton.SetDisabled()
				
		elif (pTarget.GetShields().GetCurShields(App.ShieldClass.TOP_SHIELDS) < TransportValue):
                    DamageEnemy(None, None)
                    # recalibrating transporter sir
                    pTransportButton.SetDisabled()
				
		elif (pTarget.GetShields().GetCurShields(App.ShieldClass.BOTTOM_SHIELDS) < TransportValue):
                    DamageEnemy(None, None)
                    # recalibrating transporter sir
                    pTransportButton.SetDisabled()
				
		elif (pTarget.GetShields().GetCurShields(App.ShieldClass.LEFT_SHIELDS) < TransportValue):
                    DamageEnemy(None, None)
                    # recalibrating transporter sir
                    pTransportButton.SetDisabled()
				
		elif (pTarget.GetShields().GetCurShields(App.ShieldClass.RIGHT_SHIELDS) < TransportValue):
                    DamageEnemy(None, None)
                    # recalibrating transporter sir
                    pTransportButton.SetDisabled()
				
		else:
                    return				


# thanks to defiant's marines mod for this one ;) 

def PlTgtDistance(pObject):
	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()

# we damage our target with this one, even frindlies. The user will answer for his crimes I don't care

def DamageEnemy(pObject, pEvent):
        global TransportDelayTime, TorpedoBlowUpTimer, AvailTorpsTimer
        
        # first say the line lowering shields ;) and flicker shields if they are online of course
        
        pPlayer = MissionLib.GetPlayer()
        pShields = pPlayer.GetShields()

        # bugfix although the menu is at tactical the brex has to say the line lowering shields not brex
        # my fault sorry about that
        if (pShields.IsOn() and not pShields.IsDisabled()):   
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()
            Database = pMission.SetDatabase("data/TGL/Bridge Crew General.tgl")
            pSequence = App.TGSequence_Create()
            pSet = App.g_kSetManager.GetSet("bridge")
            pEngineer = App.CharacterClass_GetObject(pSet, "Engineer")
            pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, Database))
            pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, 5))
            pSequence.Play()

        # play the transport sound no matter if shields are online or not
        
        Sound = App.TGSound_Create("sfx/Custom/SG1TransportTorpedo/Transport.wav", "Transport", 0)
	Sound.SetSFX(0)
	Sound.SetInterface(1)
	App.g_kSoundManager.PlaySound("Transport")

        # we need 2 timers one that damages targeted subsystem and one that calls for availtorp function

        AvailTorpsTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".AvailTorps", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)


        # add a timer then the torpedo blows up and damages the targeted subsystem 

        TorpedoBlowUpTimer = MissionLib.CreateTimer(Libs.LibEngineering.GetEngineeringNextEventType(), __name__ + ".BlowUp", App.g_kUtopiaModule.GetGameTime() + TransportDelayTime, 0, 0)
        
# the subsystem finally blows up, booooooooooooom

def BlowUp(pObject, pEvent):
        global DamageDoneByTorp, SuccessRate, pTargetedSysCon, TargetedSys, pTarget

        # again grab some values we need and define damage done by a torpedo
         
        pPlayer = MissionLib.GetPlayer()
        pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    	pTargetedSys = pPlayer.GetTargetSubsystem()
    	pTargetedSysCon = pTargetedSys.GetCondition()

        # define damage done by a torpedo and if it should blow up or not 50% chance

        Percentage = 1
        DmgSelector = 1

        # This is from BCS: TB v1.1 version of Tr. Torps
        if GetRandomRate(Percentage) < SuccessRate:
            Calculation = pTargetedSysCon - DamageDoneByTorp
            
            if (Calculation <= 0.01):
		pTarget.DestroySystem(pTargetedSys)
	    else:
                pTargetedSys.SetCondition(pTargetedSysCon - DamageDoneByTorp)

            # play the explosion sfx sound
            Sound = App.TGSound_Create("sfx/Custom/SG1TransportTorpedo/TrTorpExplosion.wav", "explosion", 0)
            Sound.SetSFX(0)
            Sound.SetInterface(1)
            App.g_kSoundManager.PlaySound("explosion")

            # we randomize where damage occurs with random choice
            # you have 8 to choose from :)
            # excuse me BC has 8 to choose from
            # enough i think

            if GetRandomNumber(DmgSelector) == 1:
                AddDamage1(pTarget)
            
            elif GetRandomNumber(DmgSelector) == 2:
                AddDamage2(pTarget)

            elif GetRandomNumber(DmgSelector) == 3:
                AddDamage3(pTarget)

            elif GetRandomNumber(DmgSelector) == 4:
                AddDamage4(pTarget) 

            elif GetRandomNumber(DmgSelector) == 5:
                AddDamage5(pTarget)

            elif GetRandomNumber(DmgSelector) == 6:
                AddDamage6(pTarget)

            elif GetRandomNumber(DmgSelector) == 7:
                AddDamage7(pTarget)

            elif GetRandomNumber(DmgSelector) == 8:
                AddDamage8(pTarget)


        # done with transporter recalibrations
        
        pTransportButton.SetEnabled()

        

# get a random number for percentage

def GetRandomRate(Number):
        return App.g_kSystemWrapper.GetRandomNumber(99) + Number

# get a random number for damage selector 8 to choose from but this is way much better. must compliment wowbagger on an excellent idea ;)

def GetRandomNumber(Number2):
        return  App.g_kSystemWrapper.GetRandomNumber(7) + Number2
        

# the name says it all

def Nothing(pObject, pEvent):
        return 				 	 	

# now we move onto the torpedo count part of the script 

def AvailTorps(pObject, pEvent):
        global AvailableTorps, pAvailableTorpsButton, TorpedoCount

        TorpedoCount = TorpedoCount - 1
 
        pAvailableTorpsButton.SetName(App.TGString("Nuke Count: " + str(TorpedoCount)))

# we need to reset our torp count ;)

def TransportTorpReset(pObject, pEvent):
        global AvailableTorps, pTransportButton, TorpedoCount

        # just to be on the safe side we will issue the order to reenable the button
        # who knows what BC might think of next
        
        pTransportButton.SetEnabled()

        TorpedoCount = AvailableTorps

        pAvailableTorpsButton.SetName(App.TGString("Nuke Count: " + str(TorpedoCount)))

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        # reset our end combat handelers

        pSaffiQB = GetMenuButton("Commander", "End Combat")
        pSaffiQBR = GetQBRMenuButton("Commander", "Configure")
        
        if pSaffiQB:
                pSaffiQB.RemoveHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".TransportTorpReset")

        if pSaffiQBR:
                pSaffiQBR.RemoveHandlerForInstance(App.ET_ST_BUTTON_CLICKED, __name__ + ".TransportTorpReset")
            
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ShipExploding")
        # App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_PLAYER, pMission, __name__ + ".TransportTorpReset")


# we use random damage codes to apply visual damage

# add visual damage 1, the explosions inside the ship are huge and cause many external breaches

def AddDamage1(pThingToDamage):
	pThingToDamage.AddObjectDamageVolume(-0.346769, 0.505777, 0.211104, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.391424, 0.292077, 0.136891, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.480019, 0.478436, 0.055110, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.491906, -0.009849, 0.036503, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.410636, -0.320572, 0.163709, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.033209, -0.662447, 0.254643, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.088509, -1.154540, 0.234934, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.273566, -1.192976, 0.216826, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.311354, -0.558230, 0.230304, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.222401, 0.425513, 0.261027, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.059797, 0.854007, 0.315946, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.056210, 1.548879, 0.118923, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.010570, 1.840008, -0.062665, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.004918, 1.929916, -0.118732, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.001939, 1.938382, -0.123910, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.255125, 1.524279, -0.107981, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.340457, 0.871074, 0.058321, 0.400000, 300.000000)

# add visual damage 2

def AddDamage2(pThingToDamage):
	pThingToDamage.AddObjectDamageVolume(0.000847, 1.163047, 0.295946, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.447814, 0.288307, 0.028379, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.234699, 0.027302, 0.259706, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.335636, -1.328933, 0.166836, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.347983, -0.744068, 0.144445, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.532026, 0.467509, -0.147177, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.482553, -0.298320, -0.226326, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.351669, -0.343077, -0.383422, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.278125, 0.289238, -0.398746, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.178232, 1.112100, -0.162443, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.134755, 0.889398, -0.217919, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.205823, 0.698926, -0.398746, 0.400000, 300.000000)

# add visual damage 3

def AddDamage3(pThingToDamage):
	pThingToDamage.AddObjectDamageVolume(0.296626, 1.243148, -0.134832, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.126445, 1.415870, -0.158072, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.067971, -0.037120, -0.398747, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.149664, 0.196479, -0.398746, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.121442, -0.420599, -0.398748, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.147468, -0.721491, -0.003603, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.034781, -0.636699, -0.041525, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.103933, -1.060943, -0.001106, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.072679, -1.187713, -0.001000, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.037587, -1.391599, -0.000836, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.128441, 0.075653, -0.398749, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.128440, 0.075653, -0.398747, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.071726, 0.209187, -0.398747, 0.400000, 300.000000)

# add visual damage 4

def AddDamage4(pThingToDamage):
	pThingToDamage.AddObjectDamageVolume(-0.345813, -0.685381, -0.614542, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.302524, -0.706135, -0.631574, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.146801, -0.782789, -0.676372, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.455602, -0.667914, -0.574382, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.572804, -0.813001, -0.547154, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.193804, -0.733335, -0.662817, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.214107, -0.574814, -0.642235, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.611432, -0.572691, -0.529461, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.070807, -0.379312, -0.635533, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.030613, -0.145652, -0.346971, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.005559, -0.121254, -0.283762, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.034129, -0.964541, 0.066513, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.036802, -1.037225, 0.000659, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.507236, -0.634171, 0.328817, 0.400000, 300.000000)

# add visual damage 5

def AddDamage5(pThingToDamage):
        pThingToDamage.AddObjectDamageVolume(0.929057, -0.201515, 0.400643, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.801802, -0.304561, 0.388759, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.666115, -0.397717, 0.373515, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.213361, -0.245429, 0.359157, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.851782, -0.351260, 0.371372, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.809756, 0.016150, 0.454896, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.587137, 0.397876, 0.526805, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.541201, 0.492356, 0.540685, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.375059, 0.726711, 0.576656, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.046282, 3.098201, 0.357073, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.042288, 2.960103, 0.394244, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.345629, 2.530174, 0.479749, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.685705, 1.910513, 0.545903, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.490639, 2.268348, 0.517067, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.136996, 2.856081, 0.419813, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.636938, 1.985357, 0.541501, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.804660, 1.689765, 0.553807, 0.400000, 300.000000)

# add visual damage 6

def AddDamage6(pThingToDamage):
        pThingToDamage.AddObjectDamageVolume(-1.137933, 1.015570, 0.528061, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.279356, 0.771891, 0.498532, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.346444, 0.670076, 0.481998, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.428968, 0.523097, 0.458471, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.649349, 0.111432, 0.362016, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.500440, 0.353440, 0.428241, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.018135, 1.258580, 0.545868, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(1.778010, 0.915723, 0.282265, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(1.753688, 1.235525, 0.282169, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(1.699858, 1.313243, 0.282100, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(1.376720, 1.519782, 0.215094, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(1.442958, 1.516261, 0.229245, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(2.141679, 1.319118, 0.282607, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.940048, 1.834173, 0.162829, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.694127, 1.926775, 0.143619, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.669067, 2.031247, 0.158117, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.787049, -2.450481, -0.479406, 0.400000, 300.000000)

# add visual damage 7

def AddDamage7(pThingToDamage):
        pThingToDamage.AddObjectDamageVolume(0.472988, -2.582106, -0.479406, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.332775, -2.606269, -0.479406, 0.400000, 300.000000)
        pThingToDamage.AddObjectDamageVolume(1.491975, -2.752262, -0.185564, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(1.492164, -2.546745, -0.185347, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(1.519967, -2.418399, -0.174117, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(1.537456, -2.011956, -0.106467, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(1.493736, -1.214339, -0.124618, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.293176, -0.893505, 0.057163, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.465843, -1.078616, 0.047023, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.517567, -1.529963, 0.029249, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.506633, -1.556521, 0.051007, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.383068, -1.955101, -0.400695, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.405347, -1.597944, -0.332310, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.434705, -1.311026, -0.304137, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.491449, -2.187363, -0.479408, 0.400000, 300.000000)

# add visual damage 8

def AddDamage8(pThingToDamage):
	pThingToDamage.AddObjectDamageVolume(1.871296, 1.205940, 0.423314, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.622082, 1.532477, 0.096169, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-0.887656, 1.790044, 0.149888, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.070588, 2.159536, 0.236573, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.110948, 2.139911, 0.240968, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.290856, 2.453246, 0.282340, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(0.151287, -2.431957, -0.520467, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.152492, -2.776111, -0.496844, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.225880, -2.674515, -0.449059, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.392438, -3.107039, -0.173366, 0.400000, 300.000000)
	pThingToDamage.AddObjectDamageVolume(-1.426545, -3.150084, -0.167093, 0.400000, 300.000000)


# also a standard in BCS: TNG scripts

def ShipExploding(pObject, pEvent):
                pPlayer = App.Game_GetCurrentGame().GetPlayer()

                # Get the ship that is exploding.
                pShip = App.ShipClass_Cast(pEvent.GetDestination())
                if (pShip != None):
                        iShipID = pShip.GetObjID()
                        if pPlayer and pShip.GetName() == pPlayer.GetName():
                                # It's us.  Reset.
                                TransportTorpReset(None, None)

def RemoveMenu():
        g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/TransportNuke.tgl")
        pBridge = App.g_kSetManager.GetSet("bridge")
        g_pPerson = App.CharacterClass_GetObject(pBridge, "Tactical")
        pMenu = g_pPerson.GetMenu()
	if (pMenu != None):
		pButton = pMenu.GetSubmenu("Transport Nukes")
		if (pButton != None):
			pMenu.DeleteChild(pButton)


# It returns currently used Ship HP
def GetShipType(pShip):
                if pShip.GetScript():
                        return string.split(pShip.GetScript(), '.')[-1]
                return None
            

# below this point stuff needed for our end combat handelers

# From the Menu Cleanup Brigade Lib, by Wowbagger - good job
# why mess with what works and we are all BCS: TNG, needed for a restart function just prints commented out

def GetMenuButton(sMenuName, sButtonName):
        pMenu = GetBridgeMenu(sMenuName)
        if not pMenu:
                return

        # Grab the starting button.    
        pButton = pMenu.GetButton(sButtonName)
        if not pButton:
                pButton = pMenu.GetSubmenu(sButtonName)
                if not pButton: 
                        return
        return pButton


# From ATP_GUIUtils:

def GetBridgeMenu(menuName):
	pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	if(pDatabase is None):
		return
	return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))

# get the qbr menu button 

def GetQBRMenuButton(sMenuName, sButtonName):
        pMenu = GetBridgeMenu(sMenuName)
        if not pMenu:
                return

        # Grab the starting button.    
        pButton = pMenu.GetButton(sButtonName)
        if not pButton:
                pButton = pMenu.GetSubmenu(sButtonName)
                if not pButton: 
                        return
        return pButton


# From ATP_GUIUtils to get qbr button modified by USS Sovereign

def GetQBRBridgeMenu(menuName):
	pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/QBRrestart.tgl")
	if(pDatabase is None):
		return
	return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))


# That's it folks.

# USS Sovereign signing out!

