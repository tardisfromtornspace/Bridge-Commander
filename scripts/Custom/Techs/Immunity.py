# Disable Immunity v1.0
#
# By:
#	MLeoDaalder
#
# Requirements:
#	Foundation Technologies (Version 20050510 or later)
#
# Installation:
#		Place this file in scripst\Custom\Techs
# dTechs configuration:
#   add:
#	"Disable Immunity": {Immunities}
#	where Immunities is one of the following:
#		"Power": MaxTimePrevented
#		"Sensor": MaxTimePrevented
#		"Cloak": MaxTimePrevented
#		"Shield": MaxTimePrevented
#		"Warp": MaxTimePrevented
#		"Impulse": MaxTimePrevented
#		"Phaser": MaxTimePrevented
#		"Torpedo": MaxTimePrevented
#		"Pulse": MaxTimePrevented
#	where MaxTimePrevented is a time in seconds which is the maximum ammount
#	of time the ship can prevent from getting dissabled, anything larger, and
#	it will be dissabled for the remaining ammount of time.
#
#	A ship can have multiple immunities (and diffrent maximum time per immunity)
#	they are added by adding a "," between 2 immunities (without the ")
#	It becomes like this (just an example):
#		"Disable Immunity": { "Power": 15, "Warp": 1, "Cloak": 10 }
#	As you can see, order doesn't matter.
#
#	When MaxTimePrevented is 0 then it will always be prevented
#
# Credits:
#	Dasher for his Foundation and FoundationTech
#		Making this all possible

import App
import FoundationTech

# This class is actually only used to store the ships preferences. :)
class Immunity(FoundationTech.TechDef):
	pass

oImmunity = Immunity("Disabler Immunity")
