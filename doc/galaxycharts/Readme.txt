------------------------------------------------------------------------------
               Galaxy Charts  v2.0

                                by USS Frontier
------------------------------------------------------------------------------

----------------------------------
 Brief New Features List   (changes from GC v1)
----------------------------------

- New Major feature: Custom Travelling Method Plugin System
	- Extending on GC v1's Travelling system, with this now people can easily create and add to their BC fully functional travelling methods, just by adding the travelling method plugin (a simple script) to a folder specific for these plugins. And to change a existing travelling method just gotta edit it's plugin.
	- All travelling methods this way can benefit of all the nice things GC introduced to BC, like dropping out of travel, changing course, selecting speed, real distances and ETA, and so on... 
	- The simple Warp from GC v1 is implemented this way already. And this mod also has another travelling method called "Enhanced Warp" which is twice as fast as regular warp, just for fun and to see what this system can make :P
	- You can create ship-based travelling methods (like warp, slipstream, etc) and non-ship-based methods (like the graviton catapult or transwarp hub from Voyager). And with the amount of options/stuff of the travelling method which you can change by the plugin, the possibilities are endless. You can pretty much create and add to BC most (if not all) travelling methods you can think off.
	- A little menu in the Helm menu which lists the travelling methods you can use allows you to select which travelling method you'll use. AI ships will auto select which method to use to travel based on circunstances.

- Other new features extending the Travelling system:
	- Restriction system: systems can now be restricted to only be accessible by the specified travelling methods. System Analysis can tell you the restriction of a system.
	- Now when the player tries to travel and for some reason it doesn't work, a message box will appear showing the reason (besides it being logged as it were before). 
	- Added a "Drop Out of Travel" button (which does the same thing than it's counterpart in Stellar Cartography) to the Helm menu.
	- Added a "Emergency Travel Out" button on the Helm Menu, which when clicked will immediately set course for the nearest friendly system and engage travel there using the selected travelling method or a useable one if the selected one can't be engaged.

- New major feature implemented: the Galactic War Simulator
	- Besides various UMM configuration values, this feature can be toggled ON/OFF in GC's config menu in UMM. 
	- Changes the operation of some normal GC features, such as RDF and the Galaxy Map.
	- Ships of X race can conquer systems from enemy races by attacking them, and defeating it's defence forces (Random Defence Force - RDF).
	- Races will periodically attack their enemies. (Random Attack Force - RAF)
	- Basic Economy running: each race gains each second the sum of it's systems Economy value as "Funds". These funds are the basic (and only) resouce used in the war: to buy ships and etc.
	- Ships now carry a price tag, depending of it's systems and so. To be able to add ships to the game (either by a RAF, RDF, on some other means), it's race will need to have that amount of funds available to pay for the ship.
	- RAF and RDF amount of ships and classes of ships to use are now "randomly" calculated based on attacking/defending system importance.
	- System in the Galaxy Map receive a different color coding: green->player region / blue->selected destination / yellow->neutral system red->hostile system / light blue->allied system
	- Ships will be divided in fleets, and their behavior in the game, thanks to a new AI, will be much more "intelligent". Ships will follow the lead ship of their fleet, coordinate fire with the lead ship, try to dock in a base to repair/resupply if needed, and more.
	- The player always commands his fleet, which can be seen, with details of each ship's actions, in a little "Fleet Status" windows which appears in your screen's top-right corner when in tactical view.
	- Saving System: users can save the game to continue playing another time, selecting the saved game to load in UMM.

- Added Strategic Command GUI, available when the War Sim is online, which contain various features:
	- 'news system' allows to you to easily check whats going on in the galaxy
	- 'War/Race Stats' allow you to easily check how races are compared to each other and the personal stats of the player (like how many kills, deaths, playing time, and so on).
	- 'database' allows you to have a majorly detailed look at the characteristics of any ship class of your race.
	- 'System Development' allows you to develop and improve the sets/systems that belong to your race, by placing or selling starbases, or improving the set's economic value / strategic value / default defence value
	- 'Military Command' allows you to take control of your race's diplomatic negotiations and military fleet, to offer peace treaties or order attack on enemy systems.

- And also made several tweaks and fixes in the code from GC v1.


------------------------------------------
 For more, complete, Information:
------------------------------------------
Read the "Full Readme" document, included in this mod.
It is a 21 page long document, detailing all aspects of this mod, such as features, installation notes, requirements, and more.


----------------------------------
 Brief Features List   (from GC v1)
----------------------------------
- Organization of BC's star-systems into a galaxy. With real distances and so.  (by using a system plugin, more on this later)
- A Galaxy Map interface in-game, which has the features:
	- lets you see a map of the galaxy, with all star-systems in your install.
	- shows their names, if the user wants so.
	- dynamic, and optional, grid divides the galaxy into sectors.
	- accessible from the Helm menu and from the Science menu, thru the button "Stellar Cartography".
	- enables selection of your destination by clicking in one of the regions in the map.
	- shows time you'll need to travel from your location to your destination.
	- 'shortcut' button to open the Warp Speed Selector Window, in which you select your warp speed, and can see the cruise and max warp speeds of your ship.
	- and more!
- A System Analysis interface in-game, which has the features:
	- lets you see a complete analysis of your selected destination system and it's contained sets, or the system you're on now, depending of your distance to it, and the power of the sensor system of your ship.
	- Some examples of the information showned are: controlling empire of the system, description, contained sets, strategical importance and economical importance of each set, and many more!
	- accessible from the button "System Analysis", in the Galaxy Map.
- New, improved, more canon, Warp travel system, with things like:
	- full warp battle allowed (all weapons).
	- able to tow a ship thru warp.
	- able to change destination while warping.
	- able to change warp speed while warping.
	- ETA (estimated time to arrive) is based on warp speed and distance to destination.
	- dropping out of warp, anywhere, is possible (for player AND  AI ships). Done thru the button "Drop Out of Warp" in the Galaxy Map.
	- dynamic star streaks (user can change their attributes, like speed, distance and more, in Galaxy Charts's UMM configuration menu)
	- improved warping in and warping out GFX sequences
	- and more!
- New "Warping" AIs (mainly to be compatible with the new warp travel system), so AI ships will still follow you, or their target, thru warp.
- New System Plugin  system, which allows extensive information about a system and it's sets to be configured, like description, location in the galaxy, and many more.
- New Race Plugin  system, which allows extensive information about a race to be configured.
- New Era Plugin  system, which allows the configuration of a era in BC, which will them overwrite System and Race plugin values, to match the era in which the user has selected. The user can select the era going to the "Era Selection" UMM menu, and selecting one of the era plugins that are listed there.
- A Chronological Info interface in-game, accessible from the Science menu, which allows the user to see the description of the currently selected era.
- Random Defence Force (RDF) feature, which makes a race defend it's territories if they are invaded by a ship belonging to a enemy race. Waves of ships will warp in to the system that is invaded to defend it. Highly configurable thru Galaxy Charts UMM configuration menu.
- New In-System Warp  system: now all ships, when trying to intercept a target which is more than 900 kilometers away, will enter a low-warp speed inside the system (including the warp effects) which is about 6 times faster than normal intercept speed. After passing the 900km distance, ships will disengage in-system warp and proceed at normal intercept speed towards the target, until reaching a distance of 50km.
- High user customization possible, for various areas of the mod, using UMM (Unified Main Menu modification)
- Includes a modified version of the mod CWS 2 (Change Warp Speed 2), used to select your ship's warp speed.


------------------------
 Requirements
------------------------
- Bridge Commander Patch 1.1 is required.
  Download link:  http://bridgecommander.filefront.com/file/Bridge_Commander_Patch;2374


- Foundation is required.
  Foundation is the base of modding BC, it is the mod which, literally, enables mods.
  Foundation is installed by 1 program, Bridge Commander Universal Tool (aka BCSMC), or in short, BCUT.  (BCMP, BCMI and old versions of BCSMC are outdated)
	BCUT v1.5.5 (Full): http://bridgecommander.filefront.com/file/Bridge_Commander_Universal_Tool;99364
	

- Unified Main Menu (UMM), is optional, and highly recommended.
  UMM allows the user to easily configure various parts of this mod in the game's Main Menu configuration pane.
  Download link for UMM:  http://bridgecommander.filefront.com/file/Unified_Main_Menu;56343


Note that the mod-pack Kobayashi Maru 1 full (in short: KM1), contains both of these requirements (Foundation and UMM).


-----------------------------
 Installation Notes
-----------------------------
This mod is pretty much a stand-alone mod, so it can be installed directly on Bridge Commander, or on top Galaxy Charts v1.0.

Also, if you plan on (or already had) installing DS9FX Xtended, make sure you install that mod AFTER GC v2, since it overwrites a couple scripts.

Other than that, old installation notes from GC v1.0 apply:

Before installing this mod, install the 2 required requirements (BC 1.1 patch and Foundation, at this exact order), mentioned above in the "Requirements".
The optional requirement, Unified Main Menu, can be installed later without problems.

This mod overwrites key scripts of GravityFX (by me), CWS 2 (Change Warp Speed 2, by USS Sovereign) and Distress Signal (by Defiant)
So, in other words, besides installing the requirements, install this mod AFTER installing:
- GravityFX
- CWS2
- Distress Signal (or the KM mod)
OR, if you're also use the mod-pack Kobayashi Maru 1.0, just install this after installing it.

Then, install this mod manually, by extracting the files, copying and pasting the contents of the folder "Manual Installation" folder of this mod's pack, to your BC directory (overwrite all if Windows ask it).
Unfortunately there is no automatic installer for this.

It's also recommended that if you do have GravityFX, you install this mod as well, because it has a few fixes for GravityFX.

Finally, after installing everything, turn on the mutator “USS Frontier’s Galaxy Charts” in the Mutator menu. 


-------------------------------------------------
 Bugs / Known Problems
-------------------------------------------------
None that I know of. This mod has been in beta testing for some time, in various BC "builds". But mainly on a KM1 based install.
But nothing's perfect so if you find anything wrong, well check the Contact section below :)


-----------------------------
 Contact 
-----------------------------
Contact me either by PM or by posting in the Galaxy Charts forum over at the BCS:TNG forums (link: http://bcs-tng.com/forums/)
The Galaxy Charts forum is a child forum of the Final Frontier Production forum, which contains all of my projects.
Direct link to Galaxy Charts forum:  http://bcs-tng.com/forums/index.php?board=53.0

For support relating to this mod, go over the child Galaxy Charts Tech Support sub-forum, in the Galaxy Charts forum, mentioned above.


------------------------
 Credits   (for GCv2)
------------------------	
- Jb06 and Limey, which kinda shared a beta testing team with me :D
- To all the beta testers which were managing to beta test not only this but the DQP pack too :P
- USS Sovereign for a bit of support and his help in making our mods (GCv2 and DS9FX Xtended) more compatible than their previous versions.
- Kirk, because he remembers :D
- To all those people who gave ideas and comments over at the forums.
- And finally, to you, user, for downloading and using this mod!


------------------------
 Copyright
------------------------
THIS MATERIAL IS NOT MADE, DISTRIBUTED, OR SUPPORTED BY Activision TM & (C) INTERPLAY & PARAMOUNT PICTURES.

Star Trek, Star Trek: The Next Generation, Star Trek: Deep Space Nine, Star Trek: Voyager
and related properties are Registered Trademarks of Paramount Pictures
registered in the United States Patent and Trademark Office.
All original designs are copyright © Paramount Pictures.
No infringement of Paramount's copyrights is intended.


------------------------
 Distribution
------------------------
All files in this .rar file are for personal use only and cannot be bought or sold. They also cannot be modified or released in any way without the author's permission.