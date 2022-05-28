Changes to this file was necessary for the new Player AI to
function properly. If the new Player AI is used with any 
other mods that uses this same file, then the changes listed
below must be included, and by doing so, should not cause 
any conflicts between mods.

def UsePlayerSettings(self, bDisableOnly = 0):
		self.SetAttackDisabled(bDisableOnly) # Default = not bDisableOnly
		self.SetAttackWithoutValidSubsystems(bDisableOnly) # Default = not bDisableOnly
		self.bHighPower = bDisableOnly # Default = not bDisableOnly
		self.bChangePowerSetting = 0
		self.bHullSelectedChooseAlternate = bDisableOnly