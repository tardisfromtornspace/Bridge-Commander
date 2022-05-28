### Okay, Chances are if you're reading this then you're interested in making an MVAM ship. So I will lay out what to do
### in some easy steps. Good luck, and remember to be patient and read thoroughly :)

### 1) First off, you need ships. Sorry, but I don't have the ability to split up an existing ship for you, so you'll
###    either have to make them yourself or have someone else do it. You will need the full (combined) ship plus the
###    seperated models.
#
### 2) You may want to adjust the hardpoints to each of the ship files. Remember that if one subsystem name equals the
###    subsystem name on the combined ship, then it's damage amount will be transfered to the other. If you,
###    for example, don't want the shields status of the combined ship to be transfered over to the seperated ship, you
###    just simply name it something other then what it's called on the combined ship.
#
### 3) Now you need a plugin file. Copy one of the plugin files that came with the Mvam Infinite (either GalaxyMvam.py or
###    PrometheusMvam.py) and paste it into the same directory as you copied it from(scripts/Custom/Autoload/Mvam). Rename
###    your new plugin file to whatever you want (I suggest: ShipnameMvam.py). Please don't overwrite anyone's mod, or my
###    own... also keep in mind that you NEVER put anything but the plugin file into the scripts/Custom/Autoload/Mvam
###    directory.
#
### 4) Modify the plugin file for your ships. Change only the lines below a "###TO CHANGE:". Always keep names in order
###    (IE: combined ship, seperated ship #1, seperated ship #2, seperated ship #3, etc).
#
### 5) Package all the files needed into a zip file, keeping things in the proper directory's. Remember to include the
###    plugin file, ship models, ship hardpoints, misc sound files you used, and anything else. DON'T include ANY
###    of the Mvam Infinite files (which means you shouldn't modify them AT ALL). I may want to release patches to this
###    if needed later on, and i don't want to have to contend with alternate versions floating around. If you want
###    something changed, email me at sneaker98@hotmail.com and let me know about what you would like modified). Also,
###    if you require assistance with the plugin or anything else, email me and I'll see what I can do.
#
### Readme Note: If you don't credit me in your readme, I will take action. You are modifying the code that I created in
###              my own spare time. This literally took months to get working and I don't expect to be overlooked. Also,
###              notify the users that they require the Mvam Infinite in order for your mod plugin to work.
#
### Final Note: Eventually, I may make a pretty GUI for all this... still not sure if I'll ever get the time.

#required import. Don't touch this...
import App


###TO CHANGE: what ships are in this? start with the full ship, then the ones that seperate
MvamShips = ["AsuranSatellite", "Satellite"]


#this is to make things less confusing... don't touch this ;)
MvamDirections = []
MvamDistances = []
MvamReinDirections = []
MvamReinDistances = []
for i in range (len(MvamShips) - 1):
	MvamDirections.append(App.TGPoint3())
	MvamDistances.append(App.TGPoint3())
	MvamReinDirections.append(App.TGPoint3())
	MvamReinDistances.append(App.TGPoint3())


###TO CHANGE: these are all the buttons used. Keep them in the order that you named them first (ie: saucer sep for the
############# saucer, then stardrive, etc). Note: For the reintegration button, make sure you have "$Rein" at the VERY
############# end, so I know what it is. Dont worry, that part wont show in game.
IconNames = ["Activate", "Deactivate$Rein"]


###TO CHANGE: This is the hardest part. You need to find the offset of the new ship models as opposed to the
############# original integrated model. Using MPE greatly assists in this, you can use it to compare a point on the
############# combined model to a point on the seperated one. Use PrometheusMvam.py to give you an idea of how this
############# works, as the MvamGalaxy models were positioned all around the same central point entirely for the purpose
############# of seperating (doing this isn't recommended as it makes ships turn very oddly). So this is what you do:
############# 1) Open up two instances of MPE. One for the combined ship, and the other to see a seperated ship.
#############    REMEMBER: MPE's model scale needs to be set to 0.01. To check this, go to Edit -> Options. The model
#############    scale is shown in the third text box.
############# 2) You need to pick a point that you can see on both the combined ship and the seperated ship. For
#############    example, I used the top of the bridge on the prometheus to find the offset for the saucer section, since
#############    I can clearly see it on both models
############# 3) For each XYZ point you're given after selecting the point on both ships, subtract the value on the
#############    combined ship from the value on the seperated ship. IE: If you're given (3.5, 4.0, 4.1) on the
#############    combined ship and (2.0, 2.5, 2.3) on the seperated ship, you'd do: 3.5 - 2.0 for the X, 4.0 - 2.5 for
#############    the Y, and 4.1 - 2.3 for the Z.
############# 4) Repeat for each seperated ship, using a different point each time of course. Remember to record the
#############    results of your calculations and put them below. Be as accurate as possible, as you can see I have done.
MvamDistances[0].SetXYZ(0.0, 0.0, 0.0)


###TO CHANGE: This is the direction you want the seperated ship to go during the seperation sequence. It's all X, Y, Z.
############# Remember, its in the order you name them. 0 = the first ship, 1 = the second ship, etc etc. Now, the first
############# number is to the left (so a negative number would send a ship to the right.. you get the idea), the second
############# number is to go forward, and the last number is to go up. So a 0.0, 1.0, 1.0 would send a ship on a heading
############# of forward and up, or about a positive 45 degree pitch (i use the word pitch lightly, it doesnt twist or turn
############# the model whatsoever, it's just the direction it moves)
MvamDirections[0].SetXYZ(0.0, 1.0, 0.0)


###TO CHANGE: This is the speed you want each ship to go. 1.0 is about 600 km/h on the speed display ingame for the
############# prometheus. Remember, its in the same order as the ships.. ie [ship1, ship2, ship3, ship4]
MvamSpeeds = [1.0]


###TO CHANGE: This is the reintegrating distance. Basically, this where each ship starts off at the beginning
############# of the reintegration custscene. I found the values for the Prometheus models by doing the following, NOTE,
############# You need to have the seperation sequence working properly to get this to work properly as well:
############# 1) Get the XYZ world location of the seperated ships before they start moving. Use the "PreSeperate" def
#############    below to get these values. The following bits of code can get you started:
#############    Get a ship by name: pShip1 = App.ShipClass_GetObject (pSet, "MvamPrometheusSaucer")
#############    Print location: print 'X=', pShip1.GetWorldLocation().GetX(), 'Y=', pShip1.GetWorldLocation().GetY(), etc
############# 2) Get the world location of the seperated ships AFTER they've done the cutscene. Use the "PostSeperate" def
#############    below to get these XYZ values.
############# 3) Go ingame and perform the seperation sequence so that the XYZ values of step 1 and 2 are output to the
#############    console. Write down these values.
############# 4) Subtract the XYZ values you got in the second step from the XYZ values you got in the first. Write down
#############    the numbers you get as a result.
############# 5) Flip the sign (+/-) of the new value's Y number. Ie: If you got Y=4.56345, it's now Y=-4.56345.
############# 6) Add these new XYZ values (there were 3 sets of them for the prometheus) to the values in MvamDistances.
#############    This is because you want the ship to reintegrate to the spot it would be on the combined ship. Write down
#############    the result of this calculation into the variables below, keeping the order of the ships like you should
#############    have been doing throughout this plugin.
MvamReinDistances[0].SetXYZ(0.0, 0.0, 0.0)


###TO CHANGE: This is the reintegration heading. If you used the 6 step guide in MvamReinDistances, you would simply
############# take the value in MvamDirections two steps above; switch the +/- sign on the Z value for each; and put it
############# in the appropriate spot below. Remember to keep the proper order of the ships.
MvamReinDirections[0].SetXYZ(0.0, 1.0, 0.0)


###TO CHANGE: This is how fast each ship is going during the reintegration sequence. If you used the 6 step guide in
############# MvamReinDistances, you simple use the same speed values you used in MvamSpeeds three steps above.
MvamReinSpeeds = [1.0]


###TO CHANGE: this is the name of your music! It's the file in sfx/music. REMEMBER to include this file in your plugin if
############# you've used your own.
MusicName = "MvamGalaxy"


###TO CHANGE: this is the name of the seperating sound. it's the file in sfx/Explosions. REMEMBER to include this file
############# if it's different then what I have. Leave blank ("") if you don't want a sound
SoundName = "collision2"


###TO CHANGE: this is the name of the bridge sound during seperation. it's the file in sfx/. REMEMBER to include this
############# file too, if you decide to have one. Leave blank ("") if you don't want a sound
BridgeSoundName = ""


###TO CHANGE: this is the sound when the ships reintegrate. I allowed two different sounds just in case, and keep in mind
############# that the file for this is in sfx/Explosions. REMEMBER to include this file too, if you decide to have one.
############# Leave blank ("") if you don't want a sound.
ReinSoundName = "collision2"


###TO CHANGE: this is the name of the bridge sound during reintegration. it's the file in sfx/. REMEMBER to include this
############# file too, if you decide to have one. Leave blank ("") if you don't want a sound
BridgeReinSoundName = ""


###TO CHANGE: this is the name of the ai you want to use. Unless you want it doing something REAL special, use what i have.
############# Remember to include the ai file if you use something different then what i have. For reference, the MvamAI
############# is just a basic attack plus collision avoidance. IF you make your own AI (and want computer controlled
############# ships to seperate as well), then base it on the MvamAI so it'll go through certain scripts that detect when
############# the ai ship should seperate
MvamAiName = "Custom.Sneaker.Mvam.MvamAI"


###TO CHANGE: if you want your integrated ship to have the ability to seperate when it's under computer control, set it
############# to 1. If not, set it to 0.
AiSepAbility = 1


###TO CHANGE: name the following def's EXACTLY what the seperated mvam ships are called. You need to have as many def's
############# as you have ships seperating (we aren't counting the integrated ship).
def Satellite(pObject, pEvent):


	# get the player
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	snkMvamModule = __import__ (__name__)
	# check if its our full ship
	if (pPlayer.GetScript() == "ships." + snkMvamModule.ReturnMvamShips()[0]):
		import Custom.Sneaker.Mvam.Seperation


###TO CHANGE: change the last word in quotes in the next line to the name of the def. (ie: "MvamGalaxySaucer")
		Custom.Sneaker.Mvam.Seperation.Seperation(snkMvamModule, "Satellite")


	pObject.CallNextHandler(pEvent)


###OPTIONAL CHANGE: This is the reintegrate sequence. You really don't need to touch this
def Reintegrate(pObject, pEvent):
	#get the base variables
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	snkMvamModule = __import__ (__name__)
	#check to see if all the ships are still around in the set. start a counter
	intCounter = 0
	for i in range((len(snkMvamModule.ReturnMvamShips())) - 1):
		if (App.ShipClass_GetObject(pSet, snkMvamModule.ReturnMvamShips()[i + 1]) == None):
			#make sure we're not skipping the player ship
			if (pPlayer.GetScript() != "ships." + snkMvamModule.ReturnMvamShips()[i + 1]):
				#NOW it's bad. something isnt right, so notify the counter
				intCounter = intCounter + 1
	#alright, if this is a legit reintegrate, intCounter will equal 0
	if (intCounter == 0):
		import Custom.Sneaker.Mvam.Reintegration
		Custom.Sneaker.Mvam.Reintegration.Reintegration(snkMvamModule)
	pObject.CallNextHandler(pEvent)


###OPTIONAL CHANGE: If you set AiSepAbility to equal 1 then you might want to have a specific condition on when the AI
################### seperates. Returning 1 means it seperates, returning 0 means it doesn't.
def CheckSeperate (pShip):
	#grab base values for use later
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pSet = pShip.GetContainingSet()
	pEnemies = pMission.GetEnemyGroup()
	pFriendlies = pMission.GetFriendlyGroup()
	snkAiRanSep = App.g_kSystemWrapper.GetRandomNumber(5)

	#is the ship an enemy?
	if (pEnemies.IsNameInGroup(pShip.GetName())):
		#seperate if we're outnumbered 3 to 1
		if ((pFriendlies.GetNumActiveObjects() >= (pEnemies.GetNumActiveObjects() * 3)) and (snkAiRanSep == 4)):
			return 1
		#seperate if we're targetting a HUGE ship (a la the Enterprise D vs. Borg). make sure the ai has a target
		try:
			if (pShip.GetTarget().GetRadius() > 20.0):
				return 1
		except:
			DoNothing = 0
		#seperate if 50% damaged and outnumbered 2 to 1
		if ((pShip.GetHull().GetConditionPercentage() <= 0.5) and (pFriendlies.GetNumActiveObjects() >= (pEnemies.GetNumActiveObjects() * 2)) and (snkAiRanSep == 4)):
			return 1

	#the ship is a friendly or neutral
	else:
		#seperate if we're outnumbered 3 to 1
		if ((pEnemies.GetNumActiveObjects() >= (pFriendlies.GetNumActiveObjects() * 3)) and (snkAiRanSep == 4)):
			return 1
		#seperate if we're targetting a HUGE ship (a la the Enterprise D vs. Borg). make sure the ai has a target
		try:
			if (pShip.GetTarget().GetRadius() > 20.0):
				return 1
		except:
			DoNothing = 0
		#seperate if 50% damaged and outnumbered 2 to 1
		if ((pShip.GetHull().GetConditionPercentage() <= 0.5) and (pEnemies.GetNumActiveObjects() >= (pFriendlies.GetNumActiveObjects() * 2)) and (snkAiRanSep == 4)):
			return 1
	return 0


###OPTIONAL CHANGE: The next four def's are for before and after both the seperation and reintegration sequences,
################### respectively. I really can't think of what someone would want to do with them as of this second, but
################### it's my job to keep it as dynamic as possible. Oh, The def names say where each one is called,
################### really. ALWAYS return 0. If you don't want the AI to use the changes, you might want to have a check
################### for it (eg: if (pShip.GetName() == "Player"): )

#pShip is the integrated ship just before ANYTHING is done
def PreScripts(pAction, pShip):
	#these are the base values... very useful. they are commented out since I dont use them right now
	#pGame = App.Game_GetCurrentGame()
	#pEpisode = pGame.GetCurrentEpisode()
	#pMission = pEpisode.GetCurrentMission()
	#pSet = pShip.GetContainingSet()

	return 0


#pShip is the seperated ship just before the seperation cutscene
def PreSeperate(pAction, pShip):
	#these are the base values... very useful. they are commented out since I dont need them right now
	#pGame = App.Game_GetCurrentGame()
	#pEpisode = pGame.GetCurrentEpisode()
	#pMission = pEpisode.GetCurrentMission()
	#pSet = pShip.GetContainingSet()

	return 0

#pShip is the seperated ship just after the seperation cutscene
def PostSeperate(pAction, pShip):
	#these are the base values... very useful. they are commented out since I dont need them right now
	#pGame = App.Game_GetCurrentGame()
	#pEpisode = pGame.GetCurrentEpisode()
	#pMission = pEpisode.GetCurrentMission()
	#pSet = pShip.GetContainingSet()

	return 0

#pShip is the seperated ship just before the reintegration cutscene
def PreReintegrate(pAction, pShip):
	#these are the base values... very useful. they are commented out since I dont need them right now
	#pGame = App.Game_GetCurrentGame()
	#pEpisode = pGame.GetCurrentEpisode()
	#pMission = pEpisode.GetCurrentMission()
	#pSet = pShip.GetContainingSet()

	return 0

#pShip is integrated ship just after the reintegration cutscene
def PostReintegrate(pAction, pShip):
	#these are the base values... very useful. they are commented out since I dont need them right now
	#pGame = App.Game_GetCurrentGame()
	#pEpisode = pGame.GetCurrentEpisode()
	#pMission = pEpisode.GetCurrentMission()
	#pSet = pShip.GetContainingSet()

	return 0


###OPTIONAL CHANGE: I REALLY don't recommend modifying the following, they are for the cutscene. VERY touchy... I
################### can with all honesty say that I don't know for sure what they all do. Changing one changes the others
################### and it just gets so damned complicated. I used the warp-in camera position with a few modifications.
################### The best advice I can give is to try to think of the values as a "range" in which the camera could be.
################### The more of a "range" you have, the less likely you'll get a repeated camera movement.

def ReturnCameraValues ():
	#this is as far as I can tell mostly useless
	AwayDistance1 = -1.0
	AwayDistance2 = 100000.0

	#this is the true viewing distance from the ship. probably the most useful. Also, it controls which SIDE of the
	#ship you're going to view. As far as I can tell, it looks like: if both numbers are negative, it's going to view
	#from behind; and if both numbers are positive it'll view from the front
	ForwardOffset = -5.0
	SideOffset = -5.0

	#NOTE: The next two sets of numbers need the lowest value on the top and the highest on the bottom.
	###### The game WILL freeze if you do this wrong, trust me.
	#something to do with where the camera rotates around the ship (horizontal values... more or less)
	RangeAngle1 = 230.0
	RangeAngle2 = 310.0

	#looks to be how far the camera can go up and down while "rotating" around the ship (vertical values... more or less)
	RangeAngle3 = -20.0
	RangeAngle4 = 20.0

	return [AwayDistance1, ForwardOffset, SideOffset, RangeAngle1, RangeAngle2, RangeAngle3, RangeAngle4, AwayDistance2]

###OPTIONAL CHANGE: How long would you like the seperation cutscene to play? Remember, 1.0 is about a half a second
def ReturnCameraSepLength ():
	return 5.0

###OPTIONAL CHANGE: How long would you like the reintegration cutscene to play? Remember that changing this value will
################### affect how your ships come together in the reintegration cutscene, since they aren't timed to exactly
################### how long the cutscene plays.
def ReturnCameraReinLength ():
	return 3.0


### DON'T TOUCH ANYTHING PAST HERE. THEY RETURN VALUES TO THE MVAM PROGRAM. MODIFY AT YOUR OWN RISK ###
def LoadDynamicMusic ():
	#load in the sound
	import DynamicMusic
	App.g_kMusicManager.LoadMusic("sfx/Music/" + MusicName + ".mp3", MusicName, 2.0)
	DynamicMusic.dsMusicTypes[MusicName] = MusicName
	return
def ReturnMvamShips ():
	return MvamShips
def ReturnMvamDirections ():
	return MvamDirections
def ReturnMvamDistances ():
	return MvamDistances
def ReturnMvamSpeeds ():
	return MvamSpeeds
def ReturnMvamReinDirections ():
	return MvamReinDirections
def ReturnMvamReinDistances ():
	return MvamReinDistances
def ReturnMvamReinSpeeds ():
	return MvamReinSpeeds
def ReturnMusicName ():
	return MusicName
def ReturnSoundName ():
	return SoundName
def ReturnBridgeSoundName ():
	return BridgeSoundName
def ReturnReinSoundName ():
	return ReinSoundName
def ReturnBridgeReinSoundName ():
	return BridgeReinSoundName
def ReturnMvamAiName ():
	return MvamAiName
def ReturnAiSepAbility ():
	return AiSepAbility
def ReturnIconNames ():
	return IconNames
def ReturnModuleName ():
	return __name__
