################################################################################
# PROJECT GOAT: Autoload File
# by Bridge Commander Scripters: The New Generation
#
# [Summary Deleted]
#
# v0.1 by Wowbagger - 5 May 2006
#       --Made the basic file.  Pretty simple.  All the cool stuff is in
#       LoadAtmospheres.  This is just the mutator.
#
# v0.2.1 by Wowbagger - 26 January 2007
#       --Edited the file to remove references to ********, aka Project Goat,
#       prior to release to USS Frontier for use in GravityFX.
#       --Thanks to a consultation with Frontier, this exact file will be used
#       in GravityFX, and, when Project Goat is finally released, we'll be able
#       to just write straight over this version with the new one.
#
# v0.2.1 Release Approved - 26 January 2007
#       -- This script is hereby authorized by BCS:TNG for use in USS Frontier's
#       GravityFX mod.  All other standard restrictions and permission rules
#       apply.  (Read: Don't use this without our express written permission.)
################################################################################
# QUOTE OF THE DAY:
#   "That's it!  You are all sequestered!"
#   "Excuse me, judge?  Do you even know what sequestered *means*?"
#   "I believe it involves shackles and some sort of hot poker."
#   "No, it doesn't!"
#   "Oh.  Well, in that case, you're all gonna be shackled and hot-pokered.
#            Now let's start this trial!"
#
#   --Sam and Judge Chalmers, on TV's "Lies and Disorder"; The Strangerhood #13. 
################################################################################

import App
import Foundation
import QuickBattle.QuickBattle

# Note to USS Frontier: if you can find a way to get rid of this MutatorDef,
# you're welcome to do it.  It's been long enough since I did an Autoload file
# that I don't remember whether you can create an OverrideDef without passing
# it a mode.
mode = Foundation.MutatorDef("Planet Classification Script")

# NanoFX Override
Foundation.OverrideDef('OverrideNanoAtmosphere', 'Custom.NanoFXv2.SpecialFX.AtmosphereFX.CreateAtmosphereFX', 'Custom.EarthFX.scripts.EFX_AtmosphereOverrides.OverrideNanoFX', dict = { "modes": [ mode ] } )

## Rest of file removed for BCS:TNG secrecy purposes.  We are t3h sneaky.
