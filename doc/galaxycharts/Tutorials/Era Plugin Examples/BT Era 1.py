# prototype Era Plugin - handmade


##########  GENERAL ERA INFORMATION  ##########

Name = "BetaTest Example 1"
Description = ["Example Number ONE for Beta Testing.", "Modifies Romulan and Federation race attributes, and Romulus System attributes."]
StardateRange = [55555.1, 66666.0]


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

}