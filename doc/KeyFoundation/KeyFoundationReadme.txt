Key Foundation Readme + Example

A Foundation Extension by MLeoDaalder

This Foundation Extension will allow a modder to add buttons to the Key Configuration.
This without going to the tedious process of editing MainMenu.KeyboardConfig (trust me, it is tedious)!

And (if all goes well) it will eliminate any diffrent versions, if this mod is (going to be) widely used.


I call it a Foundation Extension, because it uses the Foundation (by Dasher42), but it doesn't change
Foundation.py or any similar file. Apart from the Foundation, this mod is a standalone mod.

How to install this.

Just drop the contents of this zip in the root (main) Bridge Commander directory.
This will install 2 things. The Extension, and an example mod.

The example mod will serve as an example on how to use the Extension. The example will allow you to keep
zoomed at your target. It is located in the Camera Controls (you will have to activate the mutator 
called: "Fix Zoom On Target" for this).
Then you can go to the Controls, Camera, and select your key for it.





How to add keys.

First, create your file.

Set it up as you want and place it in scripts.Custom.Autoload

You might have there some Event Types as globals, now these make it possible to add keys.
First of all, import Foundation (you mostlikely already have this).
At the bottom of your script add:

yourET = Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("Name On Key", "Name Of Event Type", Event Type, Keyboard Binding Type, Keyboard Binding Type Value, "Menu", dict = {"modes": [mode]}))


Let's go over this.

Foundation, Foundation is the Foundation by Dasher42. I've added g_kKeyBucket from an external file.

	g_kKeyBucket, g_kKeyBucket is the class instance (a value) that I've added to the Foundation. I call it a bucket, because 
	every new key should be added to it (or be placed in it). Or it won't work (not without editing KeyboardConfig).

		AddKeyConfig(), AddKeyConfig() is a function (or member) of the class. Of which the instance is g_kKeyBucket.

			Foundation, see above.

			KeyConfig, KeyConfig is a class I added to the Foundation through an external file.

				"Name On Key", this is a simple string variable, it can be anything.
				This is shown on the button in the Key Config.

				"Name Of Event Type", this is how your Event Type is called. So if you create your Event Type
				through ET_EVENT_TYPE = App.... then this should be called ET_EVENT_TYPE

				Event Type, this is a variable. It is the event type you wich to let it called.

				Keyboard Binding Type, this is a variable inside the App. Here is a list of what it can be:
					App.KeyboardBinding.GET_EVENT
					App.KeyboardBinding.GET_INT_EVENT
					App.KeyboardBinding.GET_BOOL_EVENT
					App.KeyboardBinding.GET_FLOAT_EVENT
					0

				Keyboard Binding Type Value, this is a value. It is dependant on Keyboard Binding Type.
					0
					Any real number (0, 1, -1, 100, 13435358353)
					0 (False) or 1 (True)
					Any number (1.0035353, -0.000024374)
					0

				"Menu", this is the name of the menu you wish to add your key to, possible values are:
					"General", all misc key bindings
					"Menu", all menu key bindings
					"Ship", all ship bindings
					"Camera", all camera bindings

				dict = {"modes": [mode]}, this is needed for the Foundation, and my mod. mode is a global
				variable in your script. It contains the button in the mutator list. If it is active, then
				the button will be detected and used in the control config.



Licence:

You may include the KeyFoundation in your mod. You may edit it for your own, but DO NOT RELEASE IT WITHOUT MY AGREEMENT.
I'm hoping that their won't be any diffrent versions of this. Or it will make this mod useless!


Credits:
Dasher42, for his Foundation, and his Foundation Triggers (that is how I learned how to make an Extension for the Foundation)

