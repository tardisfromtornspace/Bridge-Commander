# prototype Era Plugin - handmade


##########  GENERAL ERA INFORMATION  ##########

Name = "BetaTest Example 3"
Description = ["Example Number THREE for Beta Testing.", "Modifies Romulan, Ferengi, Federation and Dominion race attributes. Also modifies systems Romulus, Sol and Deep Space attributes."]
StardateRange = [77777.1, 88888.0]


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