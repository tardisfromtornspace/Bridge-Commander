from bcdebug import debug
##########################################################################################################################
#        Race Plugin script   (created by the Race Plugin Creator Tool (v1.0.0.0)
###########
# this script sets up a race and info about her that some mods like Construct, Distress Signal (Distress call), and
# Galaxy Charts uses, to get a race's ship, escorts, and other things.
##########################################################################################################################

########
##  Name of this race
sName = "8472"

########
## List of strings containing the names of the enemy races  (put a "ALL" to make it enemy to everybody)
lEnemies = ["ALL", "Borg", "Kessok", "Federation", "Breen", "Cardassian", "Dominion", "Ferengi", "Klingon", "Romulan", "Sona", ]

########
## List of strings containing the names of the friendly races
lFriendlies = []

########
## a float representing the peace value  (in the range of 0 to 1, being 1 the most peacefull races )
fPeaceValue = 0.00

########
## the name of the ship selecting menu (you know, in QuickBattle), in which we can look for ships to add to this race
sLookInMenu = "8472 Ships"

########
## list of the ship script name  of ships of this race, to be added manually (that is, besides looking in the above 
## mentioned menu)
lDefaultShips = ["CA8472", ]

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
"F4E23",
"F2B74",
"F5Y10",
"F7O98",
"F8G65",
"F5V63",
"F6R53",
"F1Q32",
"F6F54",
"F1M36",
"F1N76",
"F6D20",
"F9G98",
"F7N76",
"F9M94",
"F1F89",
"F5H18",
"F4M85",
"F2H44",
"F0S13",
"F0Y67",
"F8J54",
"F5KHY",
"F6G88",
"F4L09",
"F3P86",
"F4T65",
"F9M76",
"F1A87",
"F8Z36",
"F7F84",
"F9I81",
]

## We are all done now. The Races script will take care of setting up the RaceInfo objects.
