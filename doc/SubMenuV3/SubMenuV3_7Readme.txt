Sub Menu Ship Selection mod V3.7

By MLeo Daalder


About this version:
This isn't unfortunatly V4. But some people reported bugs in V3 (more than a year after it's release), 
so I thought I fix those. I have started work on V4 (a long time ago) but one of it's intended features 
isn't cooperating (see the Features for the future section), so I've ported one of the intended features
to this version, namely, alphabetic sorting of menu's and ships.
The version number is 3.7 because 3.5 is the alphabetic sorting, and I've applied 2 fixes which upped it to 3.7.


Requirements:
The Foundation. And that's all.
But the effects of the new functions of this mod shall only be seen when you have MVAM Infinity installed.
And then only when you have the MVAM plugin for the ships which are using this mod.


What are the functions so far?
Sub Menu's in the ship selection screen. (In V1)
Sub Menu's to the Sub Menu's (to any level). (In V2)
MVAM based Sub Menu's. (New in V3)
Alphabetic sorting. (New in V3.5)
Ability to exclude a ship from being listed. (New in V3.5)
Ability to exclude a MVAM ship from it's menu (or remove the entire menu all together). (New in V3.5)


Features for the future:
Allowing the end user to sort his/her menu's by hand (moving ship entries up and down, within their current menu though).


Alphabetic sorting of menu's:
This is done automagicly and can't currently be influenced.
There is one "problem" with it, it's that it uses the non TGL name of the ship, so the Cardasian Hybrid is listed before
the Galor, this is because the Hybrid's name is internally CardHybrid, which comes before Galor.


How to make your MVAM capable ships use this:
It already does this automaticly. :)

If you want to disable the MVAM menu for all the ships, add this to your parent (integrated) ship plugin:
bMvamMenu = 0
You can also use None instead of 0, but 0 is more natural (in absence of true and false keywords).

You can now also exclude a sub ship from that list, you can do that by adding the same bMvamMenu to that subship plugin.

You can add bMvamMenu in the same way as you do SubMenu and SubSubMenu (more about this in "Using the previous features").


A new feature I've added in the last minute is a feature targetted at Mission scripters, that want to use the ShipDef
mechanism in Foundation for diffrent ships (to use FoundationTechnologies for example) but not let them show in the menu.
This can be done by adding the attribute "Do not display" (with the spaces, use the first method or the second method, 
second way as explained in the next sections), if this attribute is not 0 or None then the ship is omitted from the menu.



Using the previous features:

General instructions:
Getting the ships instance:
The ships instance is a variable where the ships instance is stored, it can be found if you find the ShipDef line and take the part before the =
For example:

Foundation.ShipDef.YourShip = Foundation.FedShipDef(abbrev, species, {<Configuration>})

Here Foundation.ShipDef.YourShip is the ships instance, this is where you will do your configuration on.
<Configuration> is not the actual text, it generally holds the additional configuration in the following format:
{"Key 1": "Value 1", "Key 2": "Value 2", ...}

The ... is placed there because there can be any number of key->value pairs. The keys and values can be variables, but are
in the example shown as text (strings).
The structure they are contained in is known as a dictionary.
The key->value pairs are separated by comma's (,).

Adding attributes and configuration to the ships instance:
This can be done in 2 ways, some of the possible configuration could be done easier in the first way than in the second way
but both are always possible.

The first way of adding attributes (which will be used as configuration) is by adding it in the configuration dictionary.
For instance:
{<Other Configuration>, "Attribute 1": "Value of Attribute 1", "Attribute 2": "Value of Attribute 2"}

If you need to add additional key->value pairs, just put the cursor of your file editor before the } and
any other character (apart for ,) and add: 
, "Another attribute": "Value of Another attribute"

The other way consists of getting the ships instance and adding it directly as attribute:
Foundation.ShipDef.YourShip.NewAttribute = "Value of NewAttribute"

If your new attribute must contain a space, it's also possible:
Foundation.ShipDef.YourShip.__dict__["New Attribute with spaces"] = "Value of New Attribute with spaces"


The values of the attributes don't need to be text (strings created by putting text between "" or '') 
they can be numbers (both integers and floating point), objects, lists, tuples, dictionaries, even functions and classes.

Note for scripters: this does not work for variables gotten out of App! They are reference/shadow/proxy objects.


Adding a submenu to a ship:
This is done by using either way as explained in the previous section.
The attribute is SubMenu and it's value can be a string (which is the name of the submenu)
or a list of sub menu's (like this: ["Sub menu 1", "Sub menu 2", "Sub menu 3"]). 
There isn't a limit to the number of sub menu's, but 6 can be considerd extreme, this is because the menu's and buttons
get shorter with each level. Experiment, and you will see what I mean. also, on higher resolutions, the text can become
bigger.

Another note, the list method is fine for post V1 versions of SubMenu, but the end user will get a BSOD if you use this
if the end user has V1 installed, preferably use the following section for additional sub menu's or for all your submenu's.


Adding additional sub menu's to a ship:
As before, this is done by using either way as explained in the "Adding attributes and configuration to the ships instance"
section.

The relevant attribute is SubSubMenu and it's value can be a string (name of sub menu)
or a list of sub menu's (see previous section, just with the SubSubMenu attribute).
If the plugin has a SubMenu attribute, that first is done, and additionally the SubSubMenu is added.
You can also only have the SubSubMenu and leave out the SubMenu.


As with my previous mods when this mod is not installed, the modifications to the ship plugin are not used.


Credits:
Dasher42 for his Foundation, of which this is a mild modification.
Sneaker98 for his MVAM Infinity, or this mod wouldn't have a reason to exist. ;)
And for making me make this mod do it's stuff automaticly.
Mark (Ignis) for asking me more than a year ago to make the menu's sort.


Licence:
You may include this mod with your own mod. But credits must atleast be given to Dasher42!
If you want to publish a mod which has a modified version of this mod (or a modification of this mod) 
then I would like to know first due to compatibility reasons (I would like to see the modification myself).
