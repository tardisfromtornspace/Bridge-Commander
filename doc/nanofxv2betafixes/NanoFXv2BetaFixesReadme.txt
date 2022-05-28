NanoFXv2 Beta fixes by MLeo Daalder
Original author: NanoByte (NanoFX itself)

Requirements:
	Have NanoFXv2 Beta (correctly) installed.

Installation:
	Place the contents of the zip in your root BC directory.
	Remind to preserve file paths when you unzip it.
	All files should be placed correctly afterwards.

Bug descriptions:
	Cloak bug:
		Blinkers still visible after you cloaked (on both player and AI ships).
		Can be exploited if you have good eyes.
	Fix used:
		Hide the Static and Dynamic lights when a ship cloaks
		And remove the clock that controls the blinking

	MVAM bug:
		The static blinkers would shift 0.1 on the Y axis when (atleast) the player
		reintegrated.
		Untested if this also happens to AI ships, but it was never said
	Fix used:
		Move the static blinkers by -0.1 on teh Y axis when the player reintegrates.
		Detecting the player reintegrating is a slight problem, since no events are
		fired when that happens.
		Solution to this is to attach an event listener on the reintegration button.
		With that we hit another kink. Though not a large one.
		It appears to be the case that CreateBlinkerFX get's called 4 times for the player

	Warp when cloaked bug:
		When you start/end warp cloaked, the ship will turn totally opaque
		when you enter or leave the warpset.
	Fix used:
		When the ship get's unhidden (through HideShip function in WarpFX.py)
		I'll check if the ship has a cloaking device and if so,
		then I'll quickly recloak (InstantDecloak and InstantCloak) the ship

	Ship destroyed bug:
		When a ship with blinkers get destroyed, the blinkers stay behind.
	Fix used:
		Hide the blinkers and static lights, then delete them.

Credits:
	NanoByte for NanoFXv2 (and his permission to release this)
	Sneaker  for MVAM (Infinite)
	Defiant  for giving me an idea when I was stuck
	Mark (Ignis) for beta testing it and reminding me of the Ship destroyed bug
	The people on BCU for bringing me these problems
