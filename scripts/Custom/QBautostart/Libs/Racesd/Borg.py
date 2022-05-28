from bcdebug import debug
##########################################################################################################################
#        Race Plugin script   (created by the Race Plugin Creator Tool (v1.0.0.0)
###########
# this script sets up a race and info about her that some mods like Construct, Distress Signal (Distress call), and
# Galaxy Charts uses, to get a race's ship, escorts, and other things.
##########################################################################################################################

########
##  Name of this race
sName = "Borg"

########
## List of strings containing the names of the enemy races  (put a "ALL" to make it enemy to everybody)
lEnemies = ["ALL", "Kessok", "Klingon", "Federation", "Romulan", "Cardassian", "Ferengi", "Breen", "Dominion", "8472", "Sona", ]

########
## List of strings containing the names of the friendly races
lFriendlies = []

########
## a float representing the peace value  (in the range of 0 to 1, being 1 the most peacefull races )
fPeaceValue = 0.00

########
## the name of the ship selecting menu (you know, in QuickBattle), in which we can look for ships to add to this race
sLookInMenu = "Borg Ships"

########
## list of the ship script name  of ships of this race, to be added manually (that is, besides looking in the above 
## mentioned menu)
lDefaultShips = ["BorgDiamond", "LowCube", "sphere", "CUBE", "TacticalCube", "TNGBorgCube", "Borg", "BorgCube", "Cube", "VoyagerCube", ]

########
## dictionary showing the escorts of a ship class  (for a example, check the Dominion race script)
## "ship class to be escorted": list of ship classes that escort it
dEscorts = {
}

########
## list of the ship script name of starbase ships of this race, to be added manually (that is, besides looking in the
## above mentioned menu)
lDefaultBases = []

########
## the name of the ship selecting menu (you know, in QuickBattle), in which we can look for ships to add to this race
sInitialShipBuild = ""

########
## Dictionary of resources of this race
## "resource name": amount of resources
dResources = {
}

########
## A list of names of ships of this race
lShipNames = [
"A923-02324",
"A923-98746",
"L923-64456",
"C923-02555",
"A923-15345",
"A923-02133",
"A923-19275",
"A923-16554",
"D923-98744",
"A923-53985",
"A923-98743",
"U923-15485",
"A923-02335",
"A923-02335",
"R923-32366",
"A923-02555",
"A923-98445",
"A923-08267",
"F923-98765",
"A923-75656",
"S923-18479",
"A923-55649",
"U923-11523",
"A923-63545",
"I472-18644",
"I472-48746",
"I472-16471",
"I472-05641",
"A472-68464",
"I472-12844",
"I472-78416",
"S472-16841",
"I472-48541",
"I472-85104",
"V472-56160",
"I472-63155",
"I472-04645",
"I472-45614",
"I472-05646",
"I472-78911",
"O472-46844",
"I472-78916",
"I472-16104",
"I472-96461",
"L472-75161",
"I472-91464",
"K472-48941",
"I472-46514",
]

## We are all done now. The Races script will take care of setting up the RaceInfo objects.
