Skinning and Damaging Tool V2.0

By MLeoDaalder (MLeoDaalder@netscape.net)

Summary:
Credits
Requirements
Installation
What is this mod for?
Known Bugs
Included Stuff
Tutorial

Credits:
Dasher42 for his Foundation!
This mod wouldn't be possible wihtout it! 
The Foundation Triggers are a large part of the core!

Requirements:
1. Foundation and the Foundation Triggers by Dasher42 
(included in seperate zip, not needed when you have NanoFX 2.0 Beta installed)
2. Activation of the mutator (named "Skinning And Damaging Tool").
And if you want to see it in action...
3. Load a game with a couple of Romulan WarBirds and yourself in Fed/Rom WarBird (and maybe a STWTBD WarBird, see below)

Installation:
1. Drop the scripts directory included in this zip in your BC-Root directory
2. Activate the mutator.

What is this mod for?
To reduce download size for big mods, to be more precise:
You have a fleet mod, like 10 Galaxy class ships, each with there own Registry and Hard Points.
Now, each Galaxy is 10 MB large, so you would need to download 100 MB. 
Let's say that the Registry texture is 1 MB large. If you could use 1 model, and have 10 diffrent
registry textures you would only need 19 MB instead of 100 MB, that is a reduction of 71%(!).
And what if you have a mission, where you just got out of a battle, but you are called to another again, 
before you could repair the visible damage?

Well, in both cases you can use my mod to do just that, to swap textures and add damage in QB!

Known Bugs:
One bug I encounterd was when I tried the STWTBD WarBird as the player ship, I exploded twice. And then BC crashed.
Another was when I added the changes in the ship plugin itself. The trigger class isn't there yet, and you need to
import the file, so it won't find the required function and give you a black screen with cursor...

Included stuff:
1. This readme
2. The mod itself
3. Trigger Foundation by Dasher42


Tutorial:
1. Overal setup
2. How to swap textures
3. How to add damage
4. How to create a HP that uses another as template (file size reduction when only small changes (like Shields are 10% stronger than the template)

1. Overal setup.

There are 3 ways of setting this up.
1.1. With your ship file
1.2. With your ships plugin
1.3. Same as 2 with diffrent approach

1.1. With the ship file.
Now, get your ship file, so in scripts/ships/YourShip.py
Open this file and go to the bottom.
Add a new line and add all the way at the beginning:

import Custom.Autoload.SDT
ThingsToChange = {}
Custom.Autoload.SDT.AddShipToChange(ThingsToChange)

You need to know the path of your ship.
It is mostlikely ships/YourShip.py (this is the file you are making the change).
Now add between the {} signs:
"Script": "Path To Script without BC-Root and scripts"

This is the bare bones setup, and it doesn't changes anything.

1.2 With your ships plugin file
Open your ships plugin file (usually scripts/Custom/Ships/YourShip.py).
At the bottom add this:
def SDTEntry(self):
	retval = {}
	return retval

Foundation.ShipDef.YourShip.__dict__["SDT Entry"] = SDTEntry

1.3 With your ships plugin file diffrent approach
Open your ships plugin file (usually scripts/Custom/Ships/YourShip.py).
At the bottom add this:
Foundation.ShipDef.YourShip.__dict__["SDT Entry"] = {}

2. How to swap textures

First do tutorial 1. Overal setup on the ship you wish to change a texture.
Now, set your cursor between the {} signs (and if there is (like if you have done 1.1) behind the last " sign.
Add a comma (,)) and press Enter.
Now for textures you need to add:
"Textures": [["Old Texture, and no path or tga", "New Texture, this time, include path, so from the BC-Root"]]}

And that is one textures swapped. If you were to add another texture, you do this:

"Textures": [	["Old Texture, and no path or tga", "New Texture, this time, include path, so from the BC-Root"],
		["Another Old Texture", "Another New Texture"]]}

It is not a requirement to add enters and tabs and such, but it is more clean, and easier to see.
And replace the text with their proper values. And make sure the paths and other text are between "" signs!


Note: If you wish to add both textures and damage you simply do that. You can do it in 2 ways.
1. You simply do the proces of 1 twice, one with textures and one with damage.
2. You add:
"Textures": [Changed Textures],
"Damage": [Damages added]
}



3. How to add damage

There are 2 ways for this.

0. First do tutorial 1. Overal setup on the ship you wish to add damage.
Now, set your cursor between the {} signs.
(Add a comma (,) and press Enter if neccesary)


1. Way 1
Now for damage you need to add:
"Damage": [[x, y, z, radius, damage]]}

And for more damage holes:
"Damage": [	[x1, y1, z1, radius1, damage1],
		[x2, y2, z2, radius2, damage2]]}

It is not a requirement to add enters and tabs and such, but it is more clean, and easier to see.
And make sure you add values, and not "x1", and "x2" as if they are predefined.
You can get these values in 2 ways, use the Damage Tool in the SDK and copy and change the values to this format,
or use the MPE tp aquire the x, y and z values and a bit of trial and error.

2. Way 2
You can use the Damage Tool (included) in the SDK to add damage and let it produce a file with all the damage set up (it produces a file with a function called AddDamage).
You can either take this file and place it somewhere in BC scripts or (most handy I would think) copy the content (remove the import App),
to the ship file and paste it *BEFORE* the following:

The syntax is:
"DamageFunction": Function
Function is the real name of the function, no "" signs or anything.
If you where to import the file from somewhere, let's say ship in scripts, where the file is called: "ShipDamage"
Then the syntax for only the damage would be:

import Custom.Autoload.SDT
import ships.ShipDamage
ThingsToChange = {	"Scripts": "ships.ShipFile",
			"DamageFunction": ships.ShipDamage.AddDamage
		}
Custom.Autoload.SDT.AddShipToChange(ThingsToChange)




Note: If you wish to add both textures and damage you simply do that. You can do it in 2 ways.
1. You simply do the proces of 1 twice, one with textures and one with damage.
2. You add:
"Textures": [Changed Textures],
"Damage": [Damages added]
}



4. How to create a HP that uses another as template

This is something I have figured out of the examples already included in BC (to be more precise the 2 Sovereigns, the Sovereign is a template for the Enterprise)...

You simply add this:
ParentPropertyScript = "ships.Hardpoints.TemplateFile"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.TemplateFile", globals(), locals(), ['*'])
	reload(ParentModule)

Where TemplateFile is the ship you wish to base the HardPoints off.
Now for each subsystem you wish to change something off you simply add the subsystem again, but with the same name.

You can also do this by loading the model in MPE, goto "Property" in the menu bar and select "Parent Script".
Instructions are there as well.



Hope this helps a lot of 56kb people!

If you have questions, contact me at MLeoDaalder@netscape.net
And make sure you check out the examples I have included!

Or ask at dynamic3.gamespy.com/~bridgecommander/phpBB
And make sure you post in either the script forum or the Technical Support forum, or PM me (username is MLeoDaalder).
