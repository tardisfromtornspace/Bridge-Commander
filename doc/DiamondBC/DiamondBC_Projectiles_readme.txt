DiamondBC Projectiles v1
by MLeo Daalder

Diamond Bridge Commander (or DiamondBC for short) is a series of, usually, little mods that all have the common purpose to make Bridge Commander more robust, to the point of being as hard as a diamond. It is about taking away the corner cases of the Bridge Commander scripting system that when triggered, which at the very least, only provide a small warning in the console, but could have as much impact as actually crashing BC, or somewhere in between, as a black screen. And DiamondBC aims to take these problems away, or at the very least, soften the blow.

Projectiles is one of those mods, its aim, to make BC _not_ crash when a projectile (be it a torpedo or a pulse) isn't found or doesn't contain all required functions for a projectile. When a ship loads such a faulty projectile, it will replace that projectile with a completely safe one, itself. Which is the one and only projectile we can rely on to be present in your BC installation when you install this mod (which is a single file). If Projectiles encounters a missing projectile, then it will report so in the console. So if any of your ships suddenly fire photon torpedoes (they only look like that) Or the torpedo is suddenly named "ProjectileSubstitute", take a look in the console and see what the missing projectile is and create a thread on bc-central.com in the Technical Support forum with the subject "Missing projectile: {projectilename}" and replace {projectilename} with the actual projectile name as reported in the console.

The only requirement is the Foundation, and even then it only needs it to load itself into BC, you do not need to activate any mutators to enable this mod.

To install this mod, the archive you just downloaded is entirely formatted for easy installation, just copy the scripts directory you found into your BC directory (the same place where you can find the STBC executable).
If your archive program didn't properly handle (sub) directories/folders/maps, then the DiamondBC_Projectiles.py needs to be copied to scripts/Custom/Autoload/

Any questions and problems should be directed to MLeoDaalder+DiamondBC _AT_ gmail _DOT_ com or through a PM on bc-central.com, if you experience a black screen or a crash after installation (meaning, a black screen or crash caused by this mod), create a thread in the Technical Support forum on bc-central.com and, if you can manage it, a console report would be nice.

It should be noted that this mod won't (shouldn't) cause any problems and can be safely installed even if you don't experience crashes caused by missing projectile files. Installing this makes your BC future proof for that one instance where you did install a ship that didn't list their dependancies correctly.

Modders may include this two files (this readme and the script itself) in their own mods, but honestly, you include all the required projectile files, right?