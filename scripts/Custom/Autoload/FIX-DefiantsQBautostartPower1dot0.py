# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 1st April 2025
# By Alex SL Gato
# Power.py 0.5 by Defiant -> no subsystems fix
# Changes:
# ========
# - 01.04.2025 (version 0.6):
#  As of Power.py 0.5 from 31.07.2005, load and Save take certain subsystems like Sensors and Warp Engine subsystems as granted if impulse systems are present, something which on certain mod packs or ships with impulse engines but no warp control system could cause problems. This has been corrected on this patch on the Load and Save functions, with very minute changes.
#
# The original readme of Power.py had this.
"""
BSD style:
Copyright (c) 2004 Defiant // Erik Andresen
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. The name of the author may not be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"THIS MATERIAL IS NOT MADE OR SUPPORTED BY ACTIVISION."

LIMITATION ON DAMAGES. IN NO EVENT WILL ACTIVISION BE LIABLE FOR SPECIAL,
INCIDENTAL OR CONSEQUENTIAL DAMAGES RESULTING FROM POSSESSION, USE OR
MALFUNCTION OF THE PROGRAM OR PROGRAM UTILITIES, INCLUDING DAMAGES TO
PROPERTY, LOSS OF GOODWILL, COMPUTER FAILURE OR MALFUNCTION AND, TO THE
EXTENT PERMITTED BY LAW, DAMAGES FOR PERSONAL INJURIES, EVEN IF ACTIVISION
HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
"""


#################################################################################################################
#
MODINFO = { "Author": "\"Erik Andresen (Defiant)\" erik@vontaene.de (original) and \"Alex SL Gato\" andromedavirgoa@gmail.com (modified patch)",
	    "Version": "0.6",
	    "License": "All Rights Reserved to Defiant (BSD), LGPL from Alex SL Gato changes",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

from bcdebug import debug
import App
import nt
import string
import traceback

banana = None

global myGoodPlugin
myGoodPlugin = "Custom.QBautostart.Power"

necessaryToUpdate = 0
try:
	try:
		banana = __import__(myGoodPlugin, globals(), locals())

		if banana != None:
			if hasattr(banana, "MODINFO"):
				if banana.MODINFO.has_key("Version") and banana.MODINFO["Version"] < MODINFO["Version"]:
					necessaryToUpdate = 1

	except:
		print "FIX-DefiantsQBautostartPower1dot0: Error, could not load " + str(myGoodPlugin) + ":"
		traceback.print_exc()
		necessaryToUpdate = 0
except:
    print "Unable to find FoundationTech.py install"
    pass

if banana != None and necessaryToUpdate:
	# This theoretically should give us all functions and their globals... but it doesn't somehow
	from Custom.QBautostart.Power import *
	originalSave = banana.ShipSettings.Save
	originalLoad = banana.ShipSettings.Load
	originalInit = banana.init

	def NewSave(self, Switch):
                debug(__name__ + ", Save")
                ShieldStatus = {}
                Repair = {}
                pPhasers = {}
                pPulse = {}
                pTorp = {}
                Engines = {}
                Sensors = {}
		Tractors = {}
		filename = string.split(self.pShip.GetScript(), '.')[-1]
		dirlist = nt.listdir("scripts\Custom\QBautostart\saves\Power\\")
                fileexists = 0
                for file in dirlist:
                        if file == filename + ".py":
                                fileexists = 1
                                break
                # if file exist, we have to rescue our old settings!
		if fileexists:
			#### ASL CHANGE - THIS IS TOTALLY UNRELATED WITH THE ACTUAL FIX, it is an adaptation I had to do for it to work with the patch ####
			global myGoodPlugin
			if __name__ == myGoodPlugin:
				file = __import__("saves.Power." + filename)
			else:
				file = __import__("Custom.QBautostart.saves.Power." + filename)
			#file = __import__("saves.Power." + filename)
			#### END OF ASL CHANGES ####
                        reload(file)
                        if hasattr(file, "ShieldStatus"):
			        ShieldStatus = file.ShieldStatus
                        if hasattr(file, "Repair"):
                                Repair = file.Repair
                        if hasattr(file, "pPhasers"):
                                pPhasers = file.pPhasers
                        if hasattr(file, "pPulse"):
                                pPulse = file.pPulse
                        if hasattr(file, "pTorp"):
                                pTorp = file.pTorp
                        if hasattr(file, "Engines"):
                                Engines = file.Engines
                        if hasattr(file, "Sensors"):
                                Sensors = file.Sensors
                        if hasattr(file, "Tractors"):
                                Tractors = file.Tractors
                        nt.remove("scripts\Custom\QBautostart\saves\Power\\" + filename + ".py")
                # now override at "Switch"
		ShieldStatus[Switch] = self.ShieldStatus
                Repair[Switch] = self.Repair
		myPhasers = {}
		for Phaser in self.pPhasers.keys():
                        if Phaser != 0:
        			myPhasers[Phaser] = self.pPhasers[Phaser][5]
		pPhasers[Switch] = myPhasers
		myPulse = {}
		for Pulse in self.pPulse.keys():
                        if Pulse != 0:
			        myPulse[Pulse] = self.pPulse[Pulse][5]
		pPulse[Switch] = myPulse
		myTorps = {}
		for Torp in self.pTorp.keys():
                        if Torp != 0:
			        myTorps[Torp] = self.pTorp[Torp][2]
		pTorp[Switch] = myTorps
		#### ALEX SL GATO CHANGES ####	
                Engines[Switch] = 0
		if self.pShip.GetImpulseEngineSubsystem() != None:
			Engines[Switch] = self.pShip.GetImpulseEngineSubsystem().GetPowerPercentageWanted()
                Sensors[Switch] = 0
		if self.pShip.GetSensorSubsystem() != None:
			Sensors[Switch] = self.pShip.GetSensorSubsystem().GetPowerPercentageWanted()
		#### END OF ALEX SL GATO CHANGES ####
		myTractors = {}
		for Tractor in self.pTractor.keys():
                        if Tractor != 0:
			        myTractors[Tractor] = self.pTractor[Tractor][3]
		Tractors[Switch] = myTractors
		
                # and save to file
		file = nt.open("scripts\Custom\QBautostart\saves\Power\\" + filename + ".py", nt.O_CREAT | nt.O_RDWR)
		nt.write(file, "ShieldStatus = " + repr(ShieldStatus) + "\n")
                nt.write(file, "Repair = " + repr(Repair) + "\n")
		nt.write(file, "pPhasers = " + repr(pPhasers) + "\n")
		nt.write(file, "pPulse = " + repr(pPulse) + "\n")
		nt.write(file, "pTorp = " + repr(pTorp) + "\n")
                nt.write(file, "Engines = " + repr(Engines) + "\n")
                nt.write(file, "Sensors = " + repr(Sensors) + "\n")
		nt.write(file, "Tractors = " + repr(Tractors) + "\n")
		nt.close(file)

	def NewLoad(self, Switch):
		debug(__name__ + ", Load")
		filename = string.split(self.pShip.GetScript(), '.')[-1]
		dirlist = nt.listdir("scripts\Custom\QBautostart\saves\Power\\")
                fileexists = 0
                for file in dirlist:
                        if file == filename + ".py":
                                fileexists = 1
                                break
		if fileexists:
			#### ASL CHANGE - THIS IS TOTALLY UNRELATED WITH THE ACTUAL FIX, it is an adaptation I had to do for it to work with the patch ####
			global myGoodPlugin
			if __name__ == myGoodPlugin:
				file = __import__("saves.Power." + filename)
			else:
				file = __import__("Custom.QBautostart.saves.Power." + filename)
			#file = __import__("saves.Power." + filename)
			#### END OF ASL CHANGES ####
                        reload(file)
                        normPower = 0
                        if hasattr(file, "ShieldStatus"):
                                if file.ShieldStatus.has_key(Switch):
			                self.ShieldStatus = file.ShieldStatus[Switch]
                                        
                                        normPower = 0
                                        for ShieldNum in range(App.ShieldClass.NUM_SHIELDS):
                                                Value = self.ShieldStatus[ShieldNum]
                                                self.SetShields(ShieldNum, Value)
                                        self.forceshieldupdate = 1
                        self.oldPower = normPower
                        if hasattr(file, "Repair"):
                                if file.Repair.has_key(Switch):
                                        self.Repair = file.Repair[Switch]
                                        self.SetRepair(self.Repair)
                        if hasattr(file, "pPhasers"):
                                if file.pPhasers.has_key(Switch):
                                        for Phaser in self.pPhasers.keys():
                                                if (Phaser != 0):
					                pProperty, MaxCharge, MaxDamage, MaxDamageDistance, RechargeRate, Value = self.pPhasers[Phaser]
                                                        Value = file.pPhasers[Switch][Phaser]
                                                        self.pPhasers[Phaser] = pProperty, MaxCharge, MaxDamage, MaxDamageDistance, RechargeRate, Value
                                                        self.updateWeapon(Phaser, Value)
                        if hasattr(file, "pPulse"):
                                if file.pPulse.has_key(Switch):
                                        for Pulse in self.pPulse.keys():
                                                if (Pulse != 0):
					                pProperty, MaxCharge, MaxDamage, MaxDamageDistance, RechargeRate, Value = self.pPulse[Pulse]
                                                        Value = file.pPulse[Switch][Pulse]
                                                        self.pPulse[Pulse] = pProperty, MaxCharge, MaxDamage, MaxDamageDistance, RechargeRate, Value
                                                        self.updateWeapon(Pulse, Value)
                        if hasattr(file, "pTorp"):
                                if file.pTorp.has_key(Switch):
                                        for Torp in self.pTorp.keys():
                                                if (Torp != 0):
					                pProperty, ReloadDelay, Value, MaxReady = self.pTorp[Torp]
                                                        Value = file.pTorp[Switch][Torp]
                                                        self.pTorp[Torp] = pProperty, ReloadDelay, Value, MaxReady
                                                        self.updateWeapon(Torp, Value)
                        if hasattr(file, "Engines"):
                                if file.Engines.has_key(Switch):
					#### ALEX SL GATO CHANGES ####
					if self.pShip.GetImpulseEngineSubsystem() != None:
                                        	self.pShip.GetImpulseEngineSubsystem().SetPowerPercentageWanted(file.Engines[Switch])
					if self.pShip.GetWarpEngineSubsystem() != None:
						self.pShip.GetWarpEngineSubsystem().SetPowerPercentageWanted(file.Engines[Switch])
					#### END OF ALEX SL GATO CHANGES ####


                        if hasattr(file, "Sensors"):
				#### ALEX SL GATO CHANGES ####
                                if file.Sensors.has_key(Switch) and self.pShip.GetSensorSubsystem() != None:
                                        self.pShip.GetSensorSubsystem().SetPowerPercentageWanted(file.Sensors[Switch])
				#### END OF ALEX SL GATO CHANGES ####                       
                        if hasattr(file, "Tractors"):
                                if file.Tractors.has_key(Switch):
                                        for Tractor in self.pTractor.keys():
                                                if (Tractor != 0):
                                                        Value = file.Tractors[Switch][Tractor]
                                                        self.updateTractor(Tractor, Value)
                        WStatus = 0
                        PowerNeeded = 0
                        cWeapons = 0
                        if self.pShip.GetPhaserSystem():
                                WStatus = self.pShip.GetPhaserSystem().IsOn()
                        elif self.pShip.GetPulseWeaponSystem():
                                WStatus = self.pShip.GetPulseWeaponSystem().IsOn()
                        elif self.pShip.GetTorpedoSystem():
                                WStatus = self.pShip.GetTorpedoSystem().IsOn()
                        if self.pShip.GetPhaserSystem():
                                PowerNeeded = PowerNeeded + self.pShip.GetPhaserSystem().GetPowerPercentageWanted()
                                cWeapons = cWeapons + 1
                        if self.pShip.GetPulseWeaponSystem():
                                PowerNeeded = PowerNeeded + self.pShip.GetPulseWeaponSystem().GetPowerPercentageWanted()
                                cWeapons = cWeapons + 1
                        if self.pShip.GetTorpedoSystem():
                                PowerNeeded = PowerNeeded + self.pShip.GetTorpedoSystem().GetPowerPercentageWanted()
                                cWeapons = cWeapons + 1
                        if cWeapons > 0:
                                PowerNeeded = PowerNeeded / cWeapons
        
                        if not WStatus:
                                PowerNeeded = 0
                        self.WeaponoldPower = PowerNeeded
        
		else:
			print("Unable to load config for", filename)

	banana.ShipSettings.Save = NewSave
	banana.ShipSettings.Load = NewLoad

	# Having to re-do the init because the importing needed for monkey-patching leads to the globals being instantiated, and on this case being instantiated before QBautostart leads to those getting wrong values. Ugh, how I hate contorting like a pretzel to update a script without directly editing the source file!
	def NewInit():
		reload (banana)
		banana.ShipSettings.Save = NewSave
		banana.ShipSettings.Load = NewLoad
		originalInit()

	banana.init = NewInit
