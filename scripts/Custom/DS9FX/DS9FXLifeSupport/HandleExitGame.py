# This just resets the life support dict when exiting the game

# by Sov

# Imports
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict

# Functions
def ResetLifeSupport():
    LifeSupport_dict.dCrew = {}
