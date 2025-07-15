# File: Z (Python 1.5)

import App
MvamShips = [
    'ZZBorgSC',
    'ZZBCube',
    'ZZBSphere']
MvamDirections = []
MvamDistances = []
MvamReinDirections = []
MvamReinDistances = []
for i in range(len(MvamShips) - 1):
    MvamDirections.append(App.TGPoint3())
    MvamDistances.append(App.TGPoint3())
    MvamReinDirections.append(App.TGPoint3())
    MvamReinDistances.append(App.TGPoint3())

IconNames = [
    'Cube',
    'Sphere',
    'Reintegrate$Rein']
MvamDistances[0].SetXYZ(0.0, 0.1, 0.0)
MvamDistances[1].SetXYZ(0.0, 0.1, 0.0)
MvamDirections[0].SetXYZ(0.0, 1.0, 0.0)
MvamDirections[1].SetXYZ(0.0, -1.0, 0.0)
MvamSpeeds = [
    3.0,
    0.0]
MvamReinDistances[0].SetXYZ(0.0, 7.7, 0.0)
MvamReinDistances[1].SetXYZ(0.0, 0.0, 0.0)
MvamReinDirections[0].SetXYZ(0.0, -1.0, 0.0)
MvamReinDirections[1].SetXYZ(0.0, 1.0, 0.0)
MvamReinSpeeds = [
    3.0,
    0.0]
MusicName = ''
SoundName = ''
BridgeSoundName = ''
ReinSoundName = ''
BridgeReinSoundName = ''
MvamAiName = 'Custom.Sneaker.Mvam.MvamAI'
AiSepAbility = 1

def ZZBCube(pObject, pEvent):
    pGame = App.Game_GetCurrentGame()
    pPlayer = pGame.GetPlayer()
    snkMvamModule = __import__(__name__)
    if pPlayer.GetScript() == 'ships.' + snkMvamModule.ReturnMvamShips()[0]:
        import Custom.Sneaker.Mvam.Seperation
        Custom.Sneaker.Mvam.Seperation.Seperation(snkMvamModule, 'ZZBCube')
    
    pObject.CallNextHandler(pEvent)


def ZZBSphere(pObject, pEvent):
    pGame = App.Game_GetCurrentGame()
    pPlayer = pGame.GetPlayer()
    snkMvamModule = __import__(__name__)
    if pPlayer.GetScript() == 'ships.' + snkMvamModule.ReturnMvamShips()[0]:
        import Custom.Sneaker.Mvam.Seperation
        Custom.Sneaker.Mvam.Seperation.Seperation(snkMvamModule, 'ZZBSphere')
    
    pObject.CallNextHandler(pEvent)


def Reintegrate(pObject, pEvent):
    pGame = App.Game_GetCurrentGame()
    pPlayer = pGame.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    snkMvamModule = __import__(__name__)
    intCounter = 0
    for i in range(len(snkMvamModule.ReturnMvamShips()) - 1):
        if App.ShipClass_GetObject(pSet, snkMvamModule.ReturnMvamShips()[i + 1]) == None:
            if pPlayer.GetScript() != 'ships.' + snkMvamModule.ReturnMvamShips()[i + 1]:
                intCounter = intCounter + 1
            
        
    
    if intCounter == 0:
        import Custom.Sneaker.Mvam.Reintegration
        Custom.Sneaker.Mvam.Reintegration.Reintegration(snkMvamModule)
    
    pObject.CallNextHandler(pEvent)


def CheckSeperate(pShip):
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    pSet = pShip.GetContainingSet()
    pEnemies = pMission.GetEnemyGroup()
    pFriendlies = pMission.GetFriendlyGroup()
    snkAiRanSep = App.g_kSystemWrapper.GetRandomNumber(5)
    if pEnemies.IsNameInGroup(pShip.GetName()):
        if pFriendlies.GetNumActiveObjects() >= pEnemies.GetNumActiveObjects() * 3 and snkAiRanSep == 4:
            return 1
        
        
        try:
            if pShip.GetTarget().GetRadius() > 20.0:
                return 1
        except:
            DoNothing = 0

        if pShip.GetHull().GetConditionPercentage() <= 0.5 and pFriendlies.GetNumActiveObjects() >= pEnemies.GetNumActiveObjects() * 2 and snkAiRanSep == 4:
            return 1
        
    elif pEnemies.GetNumActiveObjects() >= pFriendlies.GetNumActiveObjects() * 3 and snkAiRanSep == 4:
        return 1
    
    
    try:
        if pShip.GetTarget().GetRadius() > 20.0:
            return 1
    except:
        DoNothing = 0

    if pShip.GetHull().GetConditionPercentage() <= 0.5 and pEnemies.GetNumActiveObjects() >= pFriendlies.GetNumActiveObjects() * 2 and snkAiRanSep == 4:
        return 1
    
    return 0


def PreScripts(pAction, pShip):
    return 0


def PreSeperate(pAction, pShip):
    return 0


def PostSeperate(pAction, pShip):
    return 0


def PreReintegrate(pAction, pShip):
    return 0


def PostReintegrate(pAction, pShip):
    return 0


def ReturnCameraValues():
    AwayDistance1 = -1.0
    AwayDistance2 = 100000.0
    ForwardOffset = -5.0
    SideOffset = -5.0
    RangeAngle1 = 230.0
    RangeAngle2 = 310.0
    RangeAngle3 = -20.0
    RangeAngle4 = 20.0
    return [
        AwayDistance1,
        ForwardOffset,
        SideOffset,
        RangeAngle1,
        RangeAngle2,
        RangeAngle3,
        RangeAngle4,
        AwayDistance2]


def ReturnCameraSepLength():
    return 5.0


def ReturnCameraReinLength():
    return 3.0


def LoadDynamicMusic():
    import DynamicMusic
    App.g_kMusicManager.LoadMusic('sfx/Music/' + MusicName + '.mp3', MusicName, 2.0)
    DynamicMusic.dsMusicTypes[MusicName] = MusicName
    return None


def ReturnMvamShips():
    return MvamShips


def ReturnMvamDirections():
    return MvamDirections


def ReturnMvamDistances():
    return MvamDistances


def ReturnMvamSpeeds():
    return MvamSpeeds


def ReturnMvamReinDirections():
    return MvamReinDirections


def ReturnMvamReinDistances():
    return MvamReinDistances


def ReturnMvamReinSpeeds():
    return MvamReinSpeeds


def ReturnMusicName():
    return MusicName


def ReturnSoundName():
    return SoundName


def ReturnBridgeSoundName():
    return BridgeSoundName


def ReturnReinSoundName():
    return ReinSoundName


def ReturnBridgeReinSoundName():
    return BridgeReinSoundName


def ReturnMvamAiName():
    return MvamAiName


def ReturnAiSepAbility():
    return AiSepAbility


def ReturnIconNames():
    return IconNames


def ReturnModuleName():
    return __name__

