from bcdebug import debug
# prototype Era Plugin - handmade


##########  GENERAL ERA INFORMATION  ##########

Name = "Post Dominion Wars"
Description = ["This is the Era between the end of Star Trek Nemesis and the Synthetic attack on Mars.", "The Post Dominion Wars era is the time comprised between Shinzon's attempt at destroying the Federation with the Reman Scimitar and immediately before the Synthetic terrorist attack on Mars. During that time, the Federation, Romulans and Klingons had finally reached a costly peace after the Dominion Wars, the Dominion withdrew from the Quadrant and all factions involved were trying to heal its scars, with the Cardassians in particular suffering the worst, and the Romulans detecting an unexpected shortening of their home system star. With the Alpha Quadrant no longer involved in that bloody war, exploration and peaceful contacts were once again resumed, with the invention of notable prototype advancements partially derived from the experience of the USS Voyager crew on the Delta Quadrant. It was at this time when it seemed the Federation was finally going to reach the furthest corners of the galaxy, paving a path for the events of the 26th Century's Azati Prime technologically speaking. The Ferengi are willing to join the Federation, while the Breen, now going on their own, still ocassionally raid neighboring worlds. ", "About some other 'minor' powers, not involved in the full-scale quadrant war: The Borg, excluding potential splintering factions, are supposedly defeated for good from a neurolitic virus. Species 8472 has a foothold in the Delta Quadrant. The Pak'leds have acquired enough technnology to be slightly beyond a mere nuisance. Any possible renegade Founders have not yet infiltrated the Federation well-enough to cause any incident. And the mysterious Vau N'Akat..."]
StardateRange = [56844.9, 61103.1]


########## RACE INFORMATION ##########

RaceInfo = {
	"Borg": {
		"peaceVal": 0.99,
	},
	"Breen": {
		"myEnemys": ["Cardassian", "Klingon", "Kessok", "Federation", "Romulan", "Borg", "8472"],
		"myFriendlys": ["Ferengi", "Dominion", "Sona"],
		"peaceVal": 0.35,
	},
	"Cardassian": {
		"myEnemys": ["Borg", "Sona", ],
		"myFriendlys": ["Kessok", "Ferengi", ],
		"peaceVal": 0.5,
	},
	"Dominion": {
		"myEnemys": ["Borg", "8472", ],
		"myFriendlys": ["Breen", "Ferengi", "Sona", ],
		"peaceVal": 0.48,
	},
	"Federation": {
		"myEnemys": ["Borg", ],
		"myFriendlys": ["Kessok", "Klingon", "Romulan", "Ferengi", "Sona", ],
		"peaceVal": 0.91,
	},
	"Ferengi": {
		"myFriendlys": ["Federation", ],
		"peaceVal": 0.91,
	},
	"Kessok": {
		"myFriendlys": ["Federation", ],
	},
	"Vau N'Akat": {
		"myEnemys": ["Federation", ],
		"peaceVal": 0.93,
	},
	"Romulan": {
		"myEnemys": ["Borg", "Breen", "8472", ],
		"myFriendlys": ["Federation", "Ferengi", ],
		"peaceVal": 0.41,
	},
	"Sona": {
		"myEnemys": [],
		"myFriendlys": ["Federation", "Dominion", ],
		"peaceVal": 0.92,
	},
}


########## SYSTEM INFORMATION ##########

SystemInfo = {

}