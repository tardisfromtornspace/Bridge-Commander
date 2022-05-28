import App
from Custom.QBautostart.Libs.Races import Races


dIcons = {
"Sona": 'Data/Icons/Races/Sona.tga',
"8472": 'Data/Icons/Races/8472.tga',
"Ferengi": 'Data/Icons/Races/Ferengi.tga',
"Borg": 'Data/Icons/Races/Borg.tga',
"Romulan": 'Data/Icons/Races/Romulan.tga',
"Dominion": 'Data/Icons/Races/Dominion.tga',
"Federation": 'Data/Icons/Races/Federation.tga',
"Klingon": 'Data/Icons/Races/Klingon.tga',
"Cardassian": 'Data/Icons/Races/Cardassian.tga',
"Breen": 'Data/Icons/Races/Breen.tga',
}

def LoadRacesIcons(RacesIcons = None):
	if not RacesIcons:
		RacesIcons = App.g_kIconManager.CreateIconGroup("RacesIcons")
		App.g_kIconManager.AddIconGroup(RacesIcons)

	i=1
	for key in dIcons.keys():
		file = dIcons[key]
		kTextureHandle = RacesIcons.LoadIconTexture(file)
		RacesIcons.SetIconLocation(i, kTextureHandle, 0, 0, 128, 128)
		Races[key].RaceIcon = i
		
		i = i+1
		