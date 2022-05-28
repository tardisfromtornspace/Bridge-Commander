# prototype Era Plugin - handmade


##########  GENERAL ERA INFORMATION  ##########

Name = "BetaTest Example 4"
Description = ["Example Number FOUR for Beta Testing.", "Modifies Romulan, Cardassian, Kessok, Breen, Klingon, Ferengi, Federation and Dominion race attributes. Also modifies systems Romulus, Sol and Deep Space attributes."]
StardateRange = [99999.1, 123456.0]


########## RACE INFORMATION ##########

RaceInfo = {

"Romulan": {
	"myFriendlys": [ ],
	"isEnemyToAll": 1,
	"myShips": ["Galaxy", "Sovereign", "Akira", "Nebula", "Defiant", "BirdOfPrey"],
	"peaceVal": 0.0,
},

"Federation": {
	"myFriendlys": [ ],
	"isEnemyToAll": 1,
	"myShips": ["Warbird", "BirdOfPrey", "Galor", "Keldon", "CardHybrid"],
	"peaceVal": 0.0,
},

"Dominion": {
	"myFriendlys": [ ],
	"isEnemyToAll": 1,
	"myShips": ["Vorcha", "DomBB", "DomBC", "Shuttle", ],
	"myEscorts": {
		"Vorcha": ["Shuttle", "Shuttle", ],
		"DomBB": ["DomBC", "DomBC", ],
	},
	"peaceVal": 0.0,
},

"Ferengi": {
	"myFriendlys": [ ],
	"isEnemyToAll": 1,
	"myShips": ["Marauder", "BirdOfPrey", "Breen", "cOWP", ],
	"myEscorts": {
		"Marauder": ["BirdOfPrey", "BirdOfPrey", ],
	},
	"peaceVal": 0.0,
},

"Cardassian": {
	"myFriendlys": [ ],
	"isEnemyToAll": 1,
	"myShips": ["PeragrineF1", "bug", ],
	"myEscorts": {
		"bug": ["bug", "bug", ],
		"PeragrineF1": ["PeragrineF1", "PeragrineF1", ],
	},
	"peaceVal": 0.0,
},

"Breen": {
	"myFriendlys": [ ],
	"isEnemyToAll": 1,
	"peaceVal": 0.0,
},

"Klingon": {
	"myFriendlys": [ ],
	"isEnemyToAll": 1,
	"peaceVal": 0.0,
},

"Kessok": {
	"myFriendlys": [ ],
	"isEnemyToAll": 1,
	"peaceVal": 0.0,
},

}


########## SYSTEM INFORMATION ##########

SystemInfo = {

"Romulus": {
	"Description": "Romulus, home-world of the Romulan Empire. In this beta test era, it do not have any strategical, economical or defensive values.",
	"Sets": {
		"Romulus": {
			"Description": "Romulus, home-world of the Romulan Empire. In this beta test era, it do not have any strategical, economical or defensive values.",
			"Economy": 0,
			"StrategicValue": 0,
			"DefaultDefence": 0,
		},
	},
},

"Deep Space": {
	"Description": "In this BetaTest Era, this system is crowded with Dominion forces...",
	"ControllingEmpire": "Dominion",
	"Sets": {
		"Deep Space": {
			"Description": "Lots of dominion in this bizarre era.",
			"Economy": 100,
			"StrategicValue": 100,
			"DefaultDefence": 0,
		},
	},
},

"Sol": {
	"Description": "In this BetaTest Era, this system was bought by the Ferengi...",
	"ControllingEmpire": "Ferengi",
},

}