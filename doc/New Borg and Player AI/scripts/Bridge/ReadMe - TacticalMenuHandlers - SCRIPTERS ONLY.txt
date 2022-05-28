Changes to this file was necessary for the new Player AI to
function properly. If the new Player AI is used with any 
other mods that uses this same file, then the changes listed
below must be included, and by doing so, should not cause 
any conflicts between mods.

def CheckSubsystemTargeting():
-
-
-
-
	if pTargetingButton.IsChosen() == 1:
		#debug(__name__ + ": Checking subsystem targeting...Autotargeting.")
		# We're autotargeting.  Ensure that the script has a
		# list of target subsystems.
#Uncoment for default setting#		iRestored = 0
#Uncoment for default setting#		for pScript in lFireScripts:
			# Make sure the script has a list of target subsystems.
#Uncoment for default setting#			if not pScript.HasSubsystemTargets():
				# It doesn't have any subsystem targets.  Add some.
#Uncoment for default setting#				pScript.RestoreSubsystemTargets()
#Uncoment for default setting#				iRestored = iRestored + 0 # Default = 1
		#debug(__name__ + ": Checking subsystem targeting...%d systems restored" % iRestored)
#Uncoment for default setting#	else:
		#debug(__name__ + ": Checking subsystem targeting...Not autotargeting.")
		# Not autotargeting.  Make sure the fire scripts have no
		# targets.