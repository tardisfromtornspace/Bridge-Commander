import App

def Initialize(pGame):
    'Called Initialize and activate our Game'
    SetupMusic(pGame)
    import LoadTacticalSounds
    LoadTacticalSounds.LoadSounds()
    App.g_kSetManager.ClearRenderedSet()
    pGame.LoadEpisode('Custom.QuickBattleGame.QuickBattleEpisode')


def SetupMusic(pGame):
    import DynamicMusic
    DynamicMusic.Initialize(pGame, (('sfx/Music/EpisGen2.mp3', 'Starting Ambient'), ('sfx/Music/Starbase12.mp3', 'Starbase12 Ambient'), ('sfx/Music/Nebula 1.mp3', 'Nebula Ambient'), ('sfx/Music/Panic-9a.mp3', 'Cbt Panic 1'), ('sfx/Music/Panic-9b.mp3', 'Cbt Panic 2'), ('sfx/Music/Panic-9c.mp3', 'Cbt Panic 3'), ('sfx/Music/Panic-9d.mp3', 'Cbt Panic 4'), ('sfx/Music/Panic-9e.mp3', 'Cbt Panic 5'), ('sfx/Music/Panic-9f.mp3', 'Cbt Panic 6'), ('sfx/Music/Panic-9g.mp3', 'Cbt Panic 7'), ('sfx/Music/Neutral-10i.mp3', 'Cbt Neutral 1'), ('sfx/Music/Neutral-10b.mp3', 'Cbt Neutral 2'), ('sfx/Music/Neutral-10c.mp3', 'Cbt Neutral 3'), ('sfx/Music/Neutral-10d.mp3', 'Cbt Neutral 4'), ('sfx/Music/Neutral-10e.mp3', 'Cbt Neutral 5'), ('sfx/Music/Neutral-10f.mp3', 'Cbt Neutral 6'), ('sfx/Music/Neutral-10g.mp3', 'Cbt Neutral 7'), ('sfx/Music/Neutral-10h.mp3', 'Cbt Neutral 8'), ('sfx/Music/Neutral-10a.mp3', 'Cbt Neutral 9'), ('sfx/Music/Confident-11a.mp3', 'Cbt Confident 1'), ('sfx/Music/Confident-11b.mp3', 'Cbt Confident 2'), ('sfx/Music/Confident-11c.mp3', 'Cbt Confident 3'), ('sfx/Music/Confident-11d.mp3', 'Cbt Confident 4'), ('sfx/Music/Confident-11e.mp3', 'Cbt Confident 5'), ('sfx/Music/Confident-11f.mp3', 'Cbt Confident 6'), ('sfx/Music/Confident-11g.mp3', 'Cbt Confident 7'), ('sfx/Music/Failure-8d.mp3', 'Lose'), ('sfx/Music/Success-12.mp3', 'Win'), ('sfx/Music/Transition 13.mp3', 'EnemyBlewUp'), ('sfx/Music/Transition 14.mp3', 'PlayerBlewUp')), (), (('Combat Panic', ('Cbt Panic 1', 'Cbt Panic 2', 'Cbt Panic 3', 'Cbt Panic 4', 'Cbt Panic 5', 'Cbt Panic 6', 'Cbt Panic 7')), ('Combat Neutral', ('Cbt Neutral 1', 'Cbt Neutral 2', 'Cbt Neutral 3', 'Cbt Neutral 4', 'Cbt Neutral 5', 'Cbt Neutral 6', 'Cbt Neutral 7', 'Cbt Neutral 8', 'Cbt Neutral 9')), ('Combat Confident', ('Cbt Confident 1', 'Cbt Confident 2', 'Cbt Confident 3', 'Cbt Confident 4', 'Cbt Confident 5', 'Cbt Confident 6', 'Cbt Confident 7'))), DynamicMusic.StandardCombatMusic)


def Terminate(pGame):
    import DynamicMusic
    DynamicMusic.Terminate(pGame)
    App.g_kSetManager.DeleteAllSets()

