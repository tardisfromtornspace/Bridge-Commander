#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 22.02.2009                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'destiny'
iconName = 'Destiny'
longName = 'Destiny'
shipFile = 'destiny' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 773
SubMenu = "Ancient Ships/Bases"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Destiny',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.Destiny = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })
Foundation.ShipDef.Destiny.fCrew = 80

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Destiny.hasTGLName = 1
# Foundation.ShipDef.Destiny.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Destiny.desc = "Destiny is a ship in the Ancient fleet, constructed and launched around 50 million years ago from Earth. The Ancients launched several automated ships prior to Destiny, each with the purpose of constructing and seeding Stargates throughout the numerous galaxies they crossed, with Destiny itself planned to follow in their path to explore those planets. Destiny has traversed at least 38 different galaxies. After beginning this process, the Ancients initially planned to wait until the ship reached a sufficient distance from Earth to board it. However, because of other endeavors, like ascension, they never followed through on the plan. Because of this, Destiny has continued on a pre-programmed path on its journey throughout the stars, alone, for millions of years. With the arrival of a Tau'ri expedition in 2009, Destiny has a new crew. Destiny is capable of faster than light travel (FTL) but not by means of hyperdrive engines. The FTL drive spans the full rear of the ship. It predates the Ancient Technology Activation gene security feature featured in the outposts and in Lantean technology, instead having an incredibly complex master code based on an advanced Ancient DNA sequence. This access code is required for access to systems such as navigation and advanced power management, but not for basic weapon and shield control. The Destiny has a great deal of advanced technology at her disposal, ranging from the Stargate and Shuttles, to Energy weapons, the Faster-Than-Light engine, to the Solar Power Collectors and the all-important Energy shields. Destiny reactors are fueled by absorbing and storing stellar material through a series of ram scoops on the underside of each wing. To accomplish this, Destiny dives into the photosphere of a star, absorbing material during its fly-through. The shields allow matter to pass through for the ram scoops to collect while keeping the ship completely protected from the intense conditions. However, large, hot stars (such as Blue giants) are more than the Destiny's protective capabilities can fully handle. Destiny can still use these stars to recharge though not without incurring some degree of damage and putting great strain on its shields. Both shields and weapons might get their power from the same source at the moment due to damaged relays, and so the ship may have automatically diverted more power to one and less to the other to keep it balanced to allow both to run at the same time. The shield strength can also be attenuated to allow things to pass through them. Destiny's shields constantly change frequencies in the hope of matching enemy fire; the closer the frequency, the less damage Destiny takes. While this makes the shields less effective against specific types of energy weapons, it provides better general protection overall. However, Destiny's programming can be overridden to allow the shields to be set to a specific frequency, or at least relatively close to it, to provide better protection against that specific type of energy weapon. Unfortunately, doing so leaves the ship vulnerable to all other types of attacks."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Destiny.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Destiny.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
