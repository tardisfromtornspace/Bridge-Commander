from bcdebug import debug
# Power.py
# 2004 by Erik Andresen (Defiant) erik@vontaene.de
#
# Changes:
# ========
# -31.07.2005:
#  These Torp things should be finally fixed now
# -15.07.2005:
#  Fixed Torpedo instant reload
# -11.11.2004:
#  Work around for Pulse Turrets with a Recharge rate of 0: Use their cooldown time for Recharge rate.
# -14.11.2004:
#  testing with Shortcut key
# -7.11.2004:
#  Fixed Weapon when Power = 0
#  released as Version 0.4.1
# -6.11.2004:
#  Fixed Problem for Phasers when MinFiringCharge = MaxCharge
#  released as Version 0.4
#  fixed Impulse Engine setting
# -5.11.2004:
#  Fixed Tubes set to full load after Power was 0
#  Weapons could be receive damage now when Power > 150%
# -21.10.2004:
#  added Tractor beams
#  released as Version 0.3.
# -20.10.2004:
#  Torpedo Tubes now unloaded when no power.
# -18.10.2004:
#  Fixed shields when set to 0
# -17.10.2004:
#  Fixed Weapon reload time
#  Fix: Main Power changes now go with our settings
# -Version 0.2 ready!
# -16.10.2004:
#  Bugfixes: fixed Shields, lowered output needed for Repair System.
# -15.10.2004:
#  Version 0.1 is ready
# -14.10.1004:
#  started on Weapons
# -13.10.2004:
#  Shields, Saving done
# -12.10.2004:
#  Project started
#
# Todo:
# =====
# -stop flickering
#

MODINFO = {     "Author": "\"Defiant\" erik@vontaene.de",
                "Download": "http://defiant.homedns.org/~erik/STBC/Power/Power-current.zip",
                "Version": "0.5",
                "License": "BSD",
                "Description": "Advanced Power control for Bridge Commanders",
                "needBridge": 0
            }

import App
import MissionLib
import Lib.LibEngineering
import nt
import string
import math
from Libs.LibQBautostart import *

# too many globals!
pExtendedPowerWindow = None
ET_SHIELDS = {}
ET_NAME = {}
ET_SHIELDS[0] = Lib.LibEngineering.GetEngineeringNextEventType(), "Front"
ET_SHIELDS[1] = Lib.LibEngineering.GetEngineeringNextEventType(), "Rear"
ET_SHIELDS[2] = Lib.LibEngineering.GetEngineeringNextEventType(), "Top"
ET_SHIELDS[3] = Lib.LibEngineering.GetEngineeringNextEventType(), "Bottom"
ET_SHIELDS[4] = Lib.LibEngineering.GetEngineeringNextEventType(), "Left"
ET_SHIELDS[5] = Lib.LibEngineering.GetEngineeringNextEventType(), "Right"
ET_REPAIR = Lib.LibEngineering.GetEngineeringNextEventType()
ET_SAVE = Lib.LibEngineering.GetEngineeringNextEventType()
ET_LOAD = Lib.LibEngineering.GetEngineeringNextEventType()
ET_NAME[4] = Lib.LibEngineering.GetEngineeringNextEventType()
ET_REFRESH = Lib.LibEngineering.GetEngineeringNextEventType()
ET_WEAPON = Lib.LibEngineering.GetEngineeringNextEventType()
ET_TRACTOR = Lib.LibEngineering.GetEngineeringNextEventType()
TORPEDO_SET_TIMER = Lib.LibEngineering.GetEngineeringNextEventType()
ET_CLOSE = None
pShieldBars = {}
pRepairBar = None
Ships = {}
ET_NAME[0] = "Battle-Standard"
ET_NAME[1] = "Battle-Offensive"
ET_NAME[2] = "Battle-Defensive"
ET_NAME[3] = "Withdraw and Repair"
Switch = 0
pButtonSwitch = {}
DynamicPowerInterieur = {}
TorpsReady = {}
lockPowerWindow = 0


NonSerializedObjects = (
"pExtendedPowerWindow",
"pShieldBars",
"pRepairBar",
"Ships",
"pButtonSwitch",
"DynamicPowerInterieur",
"TorpsReady",
)

# class for saving, setting and loading settings
class ShipSettings:
        def __init__(self, pShip):
                debug(__name__ + ", __init__")
                self.MaxShields = {}
                self.ShieldChargePerSecond = {}
                self.PowerWanted = {}
                self.pShip = pShip
                self.oldPower = 1.0
                self.WeaponoldPower = 0.0
                self.Repair = 1.0
                self.RepairPowerPerSecond = self.pShip.GetRepairSubsystem().GetProperty().GetNormalPowerPerSecond()
                self.MaxRepairPoints = self.pShip.GetRepairSubsystem().GetProperty().GetMaxRepairPoints()
                self.pPhasers = {}
                self.pPulse = {}
                self.pTorp = {}
                self.AllWeapons = []
                self.ShieldStatus = {}
                self.forceshieldupdate = 0
		self.pTractor = {}
                
                # clycle all shields
                for Shield in range(App.ShieldClass.NUM_SHIELDS):
                        self.MaxShields[Shield] = self.pShip.GetShields().GetMaxShields(Shield)
                        self.ShieldChargePerSecond = self.pShip.GetShields().GetProperty().GetShieldChargePerSecond(Shield)
                        self.PowerWanted[Shield] = 1/6
                        self.ShieldStatus[Shield] = 1.0
                
                # add Phasers
                pPropSet = self.pShip.GetPropertySet()
                pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_PHASER_PROPERTY)
                if pShipSubSystemPropInstanceList:
                        iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
                        pShipSubSystemPropInstanceList.TGBeginIteration()
                        for i in range(iNumItems):
                                pInstance = pShipSubSystemPropInstanceList.TGGetNext()
                                pProperty = App.PhaserProperty_Cast(pInstance.GetProperty())
                                pName = pProperty.GetName().GetCString()
                                MaxCharge = pProperty.GetMaxCharge()
                                MaxDamage = pProperty.GetMaxDamage()
                                MaxDamageDistance = pProperty.GetMaxDamageDistance()
                                RechargeRate = pProperty.GetRechargeRate()
                                Value = 1.0
                                self.pPhasers[pName] = pProperty, MaxCharge, MaxDamage, MaxDamageDistance, RechargeRate, Value
                                self.AllWeapons.append(pName)
                        pShipSubSystemPropInstanceList.TGDoneIterating()
                        if self.pShip.GetPhaserSystem():
                                self.pPhasers[0] = self.pShip.GetPhaserSystem().GetProperty().GetNormalPowerPerSecond()
                
                # add Pulse Weapons
                pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_PULSE_WEAPON_PROPERTY)
                if pShipSubSystemPropInstanceList:
                        iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
                        pShipSubSystemPropInstanceList.TGBeginIteration()
                        for i in range(iNumItems):
                                pInstance = pShipSubSystemPropInstanceList.TGGetNext()
                                pProperty = App.PulseWeaponProperty_Cast(pInstance.GetProperty())
                                pName = pProperty.GetName().GetCString()
                                MaxCharge = pProperty.GetMaxCharge()
                                MaxDamage = pProperty.GetMaxDamage()
                                MaxDamageDistance = pProperty.GetMaxDamageDistance()
                                RechargeRate = pProperty.GetRechargeRate()
                                Value = 1.0
                                self.pPulse[pName] = pProperty, MaxCharge, MaxDamage, MaxDamageDistance, RechargeRate, Value
                                self.AllWeapons.append(pName)
                        pShipSubSystemPropInstanceList.TGDoneIterating()
                        if self.pShip.GetPulseWeaponSystem():
                                self.pPulse[0] = self.pShip.GetPulseWeaponSystem().GetProperty().GetNormalPowerPerSecond()

                # add Torpedos
                # found another way - this will add the Tube itself, not pTube.GetProperty()
                if self.pShip.GetTorpedoSystem():
                        for i in range(self.pShip.GetTorpedoSystem().GetNumChildSubsystems()):
                                pProperty = App.TorpedoTube_Cast(self.pShip.GetTorpedoSystem().GetChildSubsystem(i))
                                pName = pProperty.GetName()
                                ReloadDelay = pProperty.GetReloadDelay()
                                Value = 1.0
                                MaxReady = pProperty.GetMaxReady()
                                self.pTorp[pName] = pProperty, ReloadDelay, Value, MaxReady
                                self.AllWeapons.append(pName)

                        self.pTorp[0] = self.pShip.GetTorpedoSystem().GetProperty().GetNormalPowerPerSecond()

		# add Tractorbeams
                if self.pShip.GetTractorBeamSystem():
                        for i in range(self.pShip.GetTractorBeamSystem().GetNumChildSubsystems()):
                                pProperty = App.TractorBeamProjector_Cast(self.pShip.GetTractorBeamSystem().GetChildSubsystem(i))
                                pName = pProperty.GetName()
                                MaxDamage = pProperty.GetMaxDamage()
				MaxDamageDistance = pProperty.GetMaxDamageDistance()
                                Value = 1.0
                                self.pTractor[pName] = pProperty, MaxDamage, MaxDamageDistance, Value

                        self.pTractor[0] = self.pShip.GetTractorBeamSystem().GetProperty().GetNormalPowerPerSecond()

        def SetShieldStatus(self, i, Value):
                debug(__name__ + ", SetShieldStatus")
                self.ShieldStatus[i] = Value

        # Changing a Shield
        def SetShields(self, ShieldNum, Value):
                debug(__name__ + ", SetShields")
                if not self.pShip.GetShields().IsOn() and Value > 0:
                        for ShieldNum in range(App.ShieldClass.NUM_SHIELDS):
                                self.ShieldStatus[ShieldNum] = 0
                        return
                if Value > 2.0:
                        Value = 2.0
                elif Value == 0.0:
                        Value = 0.01
                oldValue = self.pShip.GetShields().GetSingleShieldPercentage(ShieldNum)
                self.pShip.GetShields().GetProperty().SetShieldChargePerSecond(ShieldNum, self.ShieldChargePerSecond * Value)
                self.pShip.GetShields().GetProperty().SetMaxShields(ShieldNum, self.MaxShields[ShieldNum] * Value)
                self.PowerWanted[ShieldNum] = Value/6
                self.ShieldStatus[ShieldNum] = Value
                
                normPower = 0
                for Shield in range(App.ShieldClass.NUM_SHIELDS):
                        normPower = normPower + self.PowerWanted[Shield]
                self.pShip.GetShields().SetCurShields(ShieldNum, self.pShip.GetShields().GetProperty().GetMaxShields(ShieldNum)*oldValue)
                self.pShip.GetShields().SetPowerPercentageWanted(normPower)
	
	def Save(self, Switch):
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
			file = __import__("saves.Power." + filename)
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
                Engines[Switch] = self.pShip.GetImpulseEngineSubsystem().GetPowerPercentageWanted()
                Sensors[Switch] = self.pShip.GetSensorSubsystem().GetPowerPercentageWanted()
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

	def Load(self, Switch):
		debug(__name__ + ", Load")
		filename = string.split(self.pShip.GetScript(), '.')[-1]
		dirlist = nt.listdir("scripts\Custom\QBautostart\saves\Power\\")
                fileexists = 0
                for file in dirlist:
                        if file == filename + ".py":
                                fileexists = 1
                                break
		if fileexists:
			file = __import__("saves.Power." + filename)
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
                                        self.pShip.GetImpulseEngineSubsystem().SetPowerPercentageWanted(file.Engines[Switch])
					self.pShip.GetWarpEngineSubsystem().SetPowerPercentageWanted(file.Engines[Switch])
                        if hasattr(file, "Sensors"):
                                if file.Sensors.has_key(Switch):
                                        self.pShip.GetSensorSubsystem().SetPowerPercentageWanted(file.Sensors[Switch])                        
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

        def SetRepair(self, Points):
                debug(__name__ + ", SetRepair")
                self.Repair = Points
                pRepair = self.pShip.GetRepairSubsystem().GetProperty()
                pRepair.SetMaxRepairPoints(self.MaxRepairPoints*self.Repair)
                if self.Repair > 1.0:
                        # expotentiel!
                        pRepair.SetNormalPowerPerSecond(self.RepairPowerPerSecond * math.exp(self.Repair*2))
                else:
                        pRepair.SetNormalPowerPerSecond(self.RepairPowerPerSecond * self.Repair)
        
        def GetRepair(self):
                debug(__name__ + ", GetRepair")
                return self.Repair
        
        def updateWeapon(self, Weapon, Value):
                debug(__name__ + ", updateWeapon")
                global TorpsReady
                
                if Value > 2.0:
                        Value = 2.0
                if self.pPhasers.has_key(Weapon):
                        pProperty, MaxCharge, MaxDamage, MaxDamageDistance, RechargeRate, ignoredValue = self.pPhasers[Weapon]
                        self.pPhasers[Weapon] = pProperty, MaxCharge, MaxDamage, MaxDamageDistance, RechargeRate, Value
                        pProperty.SetMaxCharge(MaxCharge * Value)
                        pProperty.SetMaxDamage(MaxDamage * Value)
                        pProperty.SetMaxDamageDistance(MaxDamageDistance * Value)
                        pProperty.SetRechargeRate(RechargeRate * Value)
                        while (pProperty.GetMaxCharge() < pProperty.GetMinFiringCharge()):
                                #print("damm...fixing miscalculation", pProperty.GetMaxCharge(), pProperty.GetMinFiringCharge())
                                pProperty.SetMaxCharge(pProperty.GetMaxCharge() + 0.001)
                        normPower = 0
                        cPhasers = len(self.pPhasers) - 1
                        for prob in self.pPhasers.keys():
                                if not prob:
                                        continue
                                normPower = normPower + self.pPhasers[prob][5] / cPhasers
                        self.pShip.GetPhaserSystem().SetPowerPercentageWanted(normPower)
                elif self.pPulse.has_key(Weapon):
                        pProperty, MaxCharge, MaxDamage, MaxDamageDistance, RechargeRate, ignoredValue = self.pPulse[Weapon]
                        self.pPulse[Weapon] = pProperty, MaxCharge, MaxDamage, MaxDamageDistance, RechargeRate, Value
                        pProperty.SetMaxCharge(MaxCharge * Value)
                        pProperty.SetMaxDamage(MaxDamage * Value)
                        pProperty.SetMaxDamageDistance(MaxDamageDistance * Value)
                        if Value != 0:
                                myRechargeRate = RechargeRate / Value
                                # Fix damm Hardpoints with a Recharge Rate of 0
                                if not RechargeRate and Value != 0:
                                        myRechargeRate = pProperty.GetCooldownTime() * Value
                        else:
                                myRechargeRate = 0
                        pProperty.SetRechargeRate(myRechargeRate)
                        normPower = 0
                        cPulse = len(self.pPulse) - 1
                        for prob in self.pPulse.keys():
                                if not prob:
                                        continue
                                normPower = normPower + self.pPulse[prob][5] / cPulse
                        self.pShip.GetPulseWeaponSystem().SetPowerPercentageWanted(normPower)
                elif self.pTorp.has_key(Weapon):
                        pProperty, ReloadDelay, oldValue, MaxReady = self.pTorp[Weapon]
                        self.pTorp[Weapon] = pProperty, ReloadDelay, Value, MaxReady
                        if Value != 0:
                                myRechargeRate = ReloadDelay * Value
                                if pProperty.GetProperty().GetMaxReady() != MaxReady:
                                        #if oldValue != 0:
                                        #        pProperty.SetNumReady(MaxReady)
                                        #else:
                                        # start a Timer to reset the torps
                                        # Create an event - it's a thing that will call this function
                                        #pTimerEvent = App.TGEvent_Create()
                                        #pTimerEvent.SetEventType(TORPEDO_SET_TIMER)
                                        #pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())
                                                
                                        #CounterTime = App.g_kUtopiaModule.GetGameTime() + myRechargeRate

                                        # Create a timer - it's a thing that will wait for a given time,then do something
                                        #pTimer = App.TGTimer_Create()
                                        #pTimer.SetTimerStart(ReloadDelay)
                                        #pTimer.SetDelay(0)
                                        #pTimer.SetDuration(0)
                                        #pTimer.SetEvent(pTimerEvent)
                                        #App.g_kTimerManager.AddTimer(pTimer)
                                        
                                        #TorpsReady[str(pTimerEvent)] = (pProperty, MaxReady)
                                        pProperty.GetProperty().SetMaxReady(MaxReady)
                                        
                                        pProperty.GetProperty().SetReloadDelay(myRechargeRate)
                        else:
                                myRechargeRate = 0
                                #pProperty.SetNumReady(0)
                                pProperty.GetProperty().SetMaxReady(0)
                        normPower = 0
                        cTorps = len(self.pTorp) - 1
                        for prob in self.pTorp.keys():
                                if not prob:
                                        continue
                                normPower = normPower + self.pTorp[prob][2] / cTorps
                        self.pShip.GetTorpedoSystem().SetPowerPercentageWanted(normPower)
        
        def GetWeapon(self, Weapon):
                debug(__name__ + ", GetWeapon")
                if self.pPhasers.has_key(Weapon):
                        if not self.pShip.GetPhaserSystem().IsOn():
                                return 0.0
                        return self.pPhasers[Weapon][5]
                elif self.pPulse.has_key(Weapon):
                        if not self.pShip.GetPulseWeaponSystem().IsOn():
                                return 0.0
                        return self.pPulse[Weapon][5]
                elif self.pTorp.has_key(Weapon):
                        if not self.pShip.GetTorpedoSystem().IsOn():
                                return 0.0
                        return self.pTorp[Weapon][2]
		else:
			return self.GetTractor(Weapon)
        
        def SetWeaponoldPower(self, Power):
                debug(__name__ + ", SetWeaponoldPower")
                self.WeaponoldPower = Power

	def updateTractor(self, Tractor, Value):
		debug(__name__ + ", updateTractor")
		pProperty, MaxDamage, MaxDamageDistance, ignoredValue = self.pTractor[Tractor]
		self.pTractor[Tractor] = pProperty, MaxDamage, MaxDamageDistance, Value
		pProperty.GetProperty().SetMaxDamage(MaxDamage*Value)
                # We are not allowed to update MaxDamageDistance in MP:
		pProperty.GetProperty().SetMaxDamageDistance(MaxDamageDistance*Value)
		normPower = 0
		for i in self.pTractor.keys():
			if i == 0:
				continue
			# just use the maximum for now
			if self.pTractor[i][3] > normPower:
				normPower = self.pTractor[i][3]
		self.pShip.GetTractorBeamSystem().SetPowerPercentageWanted(normPower)
	
	def GetTractor(self, Tractor):
		debug(__name__ + ", GetTractor")
		if not self.pTractor.has_key(Tractor):
			return None
		return self.pTractor[Tractor][3]


        # end class ShipSettings


def SetShields(ShieldNum, Value):
        debug(__name__ + ", SetShields")
        global Ships
        
        pPlayer = MissionLib.GetPlayer()
        if not Ships.has_key(str(pPlayer)):
               Ships[str(pPlayer)] = ShipSettings(pPlayer)
        
        Ships[str(pPlayer)].SetShields(ShieldNum, Value)
        if not pPlayer.GetShields().IsOn():
                Ships[str(pPlayer)].oldPower = 0
        else:
                Ships[str(pPlayer)].oldPower = pPlayer.GetShields().GetPowerPercentageWanted()
def SetShield0(pObject, pEvent):
        debug(__name__ + ", SetShield0")
        if not hasattr(pEvent, "GetFloat"):
                return
        SetShields(0, pEvent.GetFloat())
        pObject.CallNextHandler(pEvent)
def SetShield1(pObject, pEvent):
        debug(__name__ + ", SetShield1")
        if not hasattr(pEvent, "GetFloat"):
                return
        SetShields(1, pEvent.GetFloat())
        pObject.CallNextHandler(pEvent)
def SetShield2(pObject, pEvent):
        debug(__name__ + ", SetShield2")
        if not hasattr(pEvent, "GetFloat"):
                return
        SetShields(2, pEvent.GetFloat())
        pObject.CallNextHandler(pEvent)
def SetShield3(pObject, pEvent):
        debug(__name__ + ", SetShield3")
        if not hasattr(pEvent, "GetFloat"):
                return
        SetShields(3, pEvent.GetFloat())
        pObject.CallNextHandler(pEvent)
def SetShield4(pObject, pEvent):
        debug(__name__ + ", SetShield4")
        if not hasattr(pEvent, "GetFloat"):
                return
        SetShields(4, pEvent.GetFloat())
        pObject.CallNextHandler(pEvent)
def SetShield5(pObject, pEvent):
        debug(__name__ + ", SetShield5")
        if not hasattr(pEvent, "GetFloat"):
                return
        SetShields(5, pEvent.GetFloat())
        pObject.CallNextHandler(pEvent)
def SwitchName(pObject, pEvent):
	debug(__name__ + ", SwitchName")
	global Switch
        if not hasattr(pEvent, "GetInt"):
                return
	Switch = pEvent.GetInt()
def SaveConfig(pObject, pEvent):
	debug(__name__ + ", SaveConfig")
	global Switch, Ships
	pPlayer = MissionLib.GetPlayer()
	Ships[str(pPlayer)].Save(Switch)
def LoadConfig(pObject, pEvent):
	debug(__name__ + ", LoadConfig")
	global Switch, Ships
	pPlayer = MissionLib.GetPlayer()
	Ships[str(pPlayer)].Load(Switch)
def SetRepair(pObject, pEvent):
        debug(__name__ + ", SetRepair")
        global Ships
        if not hasattr(pEvent, "GetFloat"):
                return
        pPlayer = MissionLib.GetPlayer()
        Ships[str(pPlayer)].SetRepair(pEvent.GetFloat())
def SetWeapon(pObject, pEvent):
        debug(__name__ + ", SetWeapon")
        global Ships
        if not hasattr(pEvent, "GetFloat"):
                return
        pText = App.TGString()
        pPlayer = MissionLib.GetPlayer()
        # damm this casting was a pane!
        try:
                App.STNumericBar_Cast(pEvent.GetSource()).GetText().GetString(pText)
        except:
                return
        Ships[str(pPlayer)].updateWeapon(pText.GetCString(), pEvent.GetFloat())
        WStatus = 0
        PowerNeeded = 0
        cWeapons = 0
        if pPlayer.GetPhaserSystem():
                WStatus = pPlayer.GetPhaserSystem().IsOn()
        elif pPlayer.GetPulseWeaponSystem():
                WStatus = pPlayer.GetPulseWeaponSystem().IsOn()
        elif pPlayer.GetTorpedoSystem():
                WStatus = pPlayer.GetTorpedoSystem().IsOn()
        if pPlayer.GetPhaserSystem():
                PowerNeeded = PowerNeeded + pPlayer.GetPhaserSystem().GetPowerPercentageWanted()
                cWeapons = cWeapons + 1
        if pPlayer.GetPulseWeaponSystem():
                PowerNeeded = PowerNeeded + pPlayer.GetPulseWeaponSystem().GetPowerPercentageWanted()
                cWeapons = cWeapons + 1
        if pPlayer.GetTorpedoSystem():
                PowerNeeded = PowerNeeded + pPlayer.GetTorpedoSystem().GetPowerPercentageWanted()
                cWeapons = cWeapons + 1
        if cWeapons > 0:
                PowerNeeded = PowerNeeded / cWeapons
        
        if not WStatus:
                Ships[str(pPlayer)].SetWeaponoldPower(0)
        else:
                Ships[str(pPlayer)].SetWeaponoldPower(PowerNeeded)
def SetTractor(pObject, pEvent):
        debug(__name__ + ", SetTractor")
        global Ships
        pText = App.TGString()
        pPlayer = MissionLib.GetPlayer()
        try:
                App.STNumericBar_Cast(pEvent.GetSource()).GetText().GetString(pText)
        except:
                return
        Ships[str(pPlayer)].updateTractor(pText.GetCString(), pEvent.GetFloat())


# from MainMenu.MainMenu.CreateVolumeButton()
def CreateSliderBar(pName, eType, fValue, myColor, fWidth, fHeight=0.0364, RangeLow=0.0, RangeHigh=1.0):
        debug(__name__ + ", CreateSliderBar")
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pBar = App.STNumericBar_Create()

	pBar.SetRange(RangeLow, RangeHigh)
	pBar.SetKeyInterval(0.1)
	pBar.SetMarkerValue(1.0)
	pBar.SetValue(fValue)
	pBar.SetUseAlternateColor(0)
	pBar.SetUseButtons(0)

	pBar.SetNormalColor(myColor)
	pBar.SetEmptyColor(App.g_kSTMenu3Disabled)
	pText = pBar.GetText();
	pText.SetStringW(pName)

	pBar.Resize(fWidth, fHeight, 0)

	pEvent = App.TGFloatEvent_Create()
	pEvent.SetDestination(pOptionsWindow)
	pEvent.SetFloat(fValue)
	pEvent.SetEventType(eType)

	pBar.SetUpdateEvent(pEvent)

	return pBar


def CreateButton(myEvent, g_pPerson, Num, Name):
	debug(__name__ + ", CreateButton")
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(myEvent)
	pEvent.SetDestination(g_pPerson)
	pEvent.SetInt(Num)
	pButton = App.STButton_CreateW(Name, pEvent)
	return pButton


def UpdateDynamicPowerWindowInterieur(updategraphics):
        debug(__name__ + ", UpdateDynamicPowerWindowInterieur")
        global Ships, DynamicPowerInterieur
        pPlayer = MissionLib.GetPlayer()
        
        # test if Power Level for weapons was changed
        WStatus = 0
        PowerNeeded = 0
        cWeapons = 0
        if pPlayer.GetPhaserSystem():
                WStatus = pPlayer.GetPhaserSystem().IsOn()
        elif pPlayer.GetPulseWeaponSystem():
                WStatus = pPlayer.GetPulseWeaponSystem().IsOn()
        elif pPlayer.GetTorpedoSystem():
                WStatus = pPlayer.GetTorpedoSystem().IsOn()
                
        if pPlayer.GetPhaserSystem():
                PowerNeeded = PowerNeeded + pPlayer.GetPhaserSystem().GetPowerPercentageWanted()
                cWeapons = cWeapons + 1
        if pPlayer.GetPulseWeaponSystem():
                PowerNeeded = PowerNeeded + pPlayer.GetPulseWeaponSystem().GetPowerPercentageWanted()
                cWeapons = cWeapons + 1
        if pPlayer.GetTorpedoSystem():
                PowerNeeded = PowerNeeded + pPlayer.GetTorpedoSystem().GetPowerPercentageWanted()
                cWeapons = cWeapons + 1
        if cWeapons > 0:
                PowerNeeded = PowerNeeded / cWeapons
        
        if not WStatus:
               PowerNeeded = 0
        
        if (Ships[str(pPlayer)].WeaponoldPower != PowerNeeded):
                for myWeapon in range(len(Ships[str(pPlayer)].AllWeapons)):
                        Weapon = Ships[str(pPlayer)].AllWeapons[myWeapon]
                        if Ships[str(pPlayer)].WeaponoldPower != 0:
                                difference = Ships[str(pPlayer)].GetWeapon(Weapon) / Ships[str(pPlayer)].WeaponoldPower
                        else:
                                difference = 1
                        newStatus = difference * PowerNeeded
                        Ships[str(pPlayer)].updateWeapon(Weapon, newStatus)
                
                Ships[str(pPlayer)].SetWeaponoldPower(PowerNeeded)
        
        if updategraphics:
                for Weapon in DynamicPowerInterieur.keys():
                        if hasattr(DynamicPowerInterieur[Weapon], "SetValue"):
                                DynamicPowerInterieur[Weapon].SetValue(Ships[str(pPlayer)].GetWeapon(Weapon))
                                DynamicPowerInterieur[Weapon].Resize(0.2, 0.0364, 0)


# Weapons always have to be added dynamicly, cause different from ship to ship
def CreateDynamicPowerWindowInterieur():
        debug(__name__ + ", CreateDynamicPowerWindowInterieur")
        global pExtendedPowerWindow, DynamicPowerInterieur, ET_WEAPON, Ships, ET_TRACTOR
        
        pPlayer = MissionLib.GetPlayer()
        if not Ships.has_key(str(pPlayer)):
               Ships[str(pPlayer)] = ShipSettings(pPlayer)
        
        x = 0
        y = 0
        DynamicPowerInterieur['Phaser'] = App.TGParagraph_CreateW(App.TGString("Phaser control:"))
        pExtendedPowerWindow.AddChild(DynamicPowerInterieur['Phaser'], x, y, 0)
        
        # cycle weapon, grep its name and add to list
        pPropSet = pPlayer.GetPropertySet()
        pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_PHASER_PROPERTY)
        iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
        pShipSubSystemPropInstanceList.TGBeginIteration()
        for i in range(iNumItems):
                pInstance = pShipSubSystemPropInstanceList.TGGetNext()
                pProperty = pPlayer.GetSubsystemByProperty(App.PhaserProperty_Cast(pInstance.GetProperty()))
                pName = pProperty.GetName()
                y = y + 0.04
                Status = Ships[str(pPlayer)].GetWeapon(pName)
                if not Status:
                        Status = 0
                DynamicPowerInterieur[pName] = CreateSliderBar(App.TGString(pName), ET_WEAPON, Status, App.g_kEngineeringWeaponsColor, 0.2, 0.0364, 0.0, 2.0)
                pExtendedPowerWindow.AddChild(DynamicPowerInterieur[pName], x, y, 0)
        pShipSubSystemPropInstanceList.TGDoneIterating()
	
	y = y + 0.08
	DynamicPowerInterieur['Tractor'] = App.TGParagraph_CreateW(App.TGString("Tractor control:"))
	pExtendedPowerWindow.AddChild(DynamicPowerInterieur['Tractor'], x, y, 0)
	for pName in Ships[str(pPlayer)].pTractor.keys():
		if not pName:
			continue
                y = y + 0.04
		Status = Ships[str(pPlayer)].GetTractor(pName)
		DynamicPowerInterieur[pName] = CreateSliderBar(App.TGString(pName), ET_TRACTOR, Status, App.g_kEngineeringSensorsColor, 0.2, 0.0364, 0.0, 2.0)
		pExtendedPowerWindow.AddChild(DynamicPowerInterieur[pName], x, y, 0)

        x = 0.25
        y = 0
        DynamicPowerInterieur['Pulse'] = App.TGParagraph_CreateW(App.TGString("Pulse control:"))
        pExtendedPowerWindow.AddChild(DynamicPowerInterieur['Pulse'], x, y, 0)
        pPropSet = pPlayer.GetPropertySet()
        pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_PULSE_WEAPON_PROPERTY)
        iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
        pShipSubSystemPropInstanceList.TGBeginIteration()
        for i in range(iNumItems):
                pInstance = pShipSubSystemPropInstanceList.TGGetNext()
                pProperty = pPlayer.GetSubsystemByProperty(App.PulseWeaponProperty_Cast(pInstance.GetProperty()))
                pName = pProperty.GetName()
                y = y + 0.04
                Status = Ships[str(pPlayer)].GetWeapon(pName)
                if not Status:
                        Status = 0
                DynamicPowerInterieur[pName] = CreateSliderBar(App.TGString(pName), ET_WEAPON, Status, App.g_kEngineeringWeaponsColor, 0.2, 0.0364, 0.0, 2.0)
                pExtendedPowerWindow.AddChild(DynamicPowerInterieur[pName], x, y, 0)
        pShipSubSystemPropInstanceList.TGDoneIterating()

        y = y + 0.08
        DynamicPowerInterieur['Torpedo'] = App.TGParagraph_CreateW(App.TGString("Torpedo control:"))
        pExtendedPowerWindow.AddChild(DynamicPowerInterieur['Torpedo'], x, y, 0)
        pPropSet = pPlayer.GetPropertySet()
        pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_TORPEDO_TUBE_PROPERTY)
        iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
        pShipSubSystemPropInstanceList.TGBeginIteration()
        for i in range(iNumItems):
                pInstance = pShipSubSystemPropInstanceList.TGGetNext()
                pProperty = pPlayer.GetSubsystemByProperty(App.TorpedoTubeProperty_Cast(pInstance.GetProperty()))
                pName = pProperty.GetName()
                y = y + 0.04
                Status = Ships[str(pPlayer)].GetWeapon(pName)
                if not Status:
                        Status = 0
                DynamicPowerInterieur[pName] = CreateSliderBar(App.TGString(pName), ET_WEAPON, Status, App.g_kEngineeringWeaponsColor, 0.2, 0.0364, 0.0, 2.0)
                pExtendedPowerWindow.AddChild(DynamicPowerInterieur[pName], x, y, 0)
        pShipSubSystemPropInstanceList.TGDoneIterating()

        pExtendedPowerWindow.InteriorChangedSize()


def DestroyDynamicPowerWindowInterieur():
        debug(__name__ + ", DestroyDynamicPowerWindowInterieur")
        global pExtendedPowerWindow, DynamicPowerInterieur

        for key in DynamicPowerInterieur.keys():
                pExtendedPowerWindow.DeleteChild(DynamicPowerInterieur[key])
        DynamicPowerInterieur = {}
        

# static Interieur
def CreatePowerWindowInterieur():
        debug(__name__ + ", CreatePowerWindowInterieur")
        global pExtendedPowerWindow, ET_SHIELDS, pShieldBars, ET_SAVE, ET_LOAD, ET_NAME, pButtonSwitch, g_pBrex, pRepairBar, ET_REPAIR, ET_CLOSE
        
        x = 0.5
        y = 0
        pText = App.TGParagraph_CreateW(App.TGString("Shield control:"))
        pExtendedPowerWindow.AddChild(pText, x, y, 0)

        x = pText.GetRight() + 0.05
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_CLOSE)
        pEvent.SetDestination(g_pBrex)
        pEvent.SetInt(0)
        pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.13125, 0.034583)
        pExtendedPowerWindow.AddChild(pButton, x, y, 0)
        
        pShip = MissionLib.GetPlayer()
        if pShip.GetShields().IsOn():
                Status = pShip.GetShields().GetPowerPercentageWanted()
        else:
                Status = 0
        
        x = 0.5
        # cacle all shields
        for i in range(App.ShieldClass.NUM_SHIELDS):
                y = y + 0.04
                pShieldBars[i] = CreateSliderBar(App.TGString(ET_SHIELDS[i][1]), ET_SHIELDS[i][0], Status, App.g_kEngineeringShieldsColor, 0.2, 0.0364, 0.0, 2.0)
                pExtendedPowerWindow.AddChild(pShieldBars[i], x, y, 0)
        
        y = y + 0.08
        pRepairBar = CreateSliderBar(App.TGString("Repair Subsystem"), ET_REPAIR, 1.0, App.g_kEngineeringSensorsColor, 0.2, 0.0364, 0.0, 2.0)
        pExtendedPowerWindow.AddChild(pRepairBar, x, y, 0)
        
	y = 0.5
	pButtonSwitch[0] = CreateButton(ET_NAME[4], g_pBrex, 0, App.TGString(ET_NAME[0]))
	pExtendedPowerWindow.AddChild(pButtonSwitch[0], x, y, 0)
	y = y + 0.04
	pButtonSwitch[1] = CreateButton(ET_NAME[4], g_pBrex, 1, App.TGString(ET_NAME[1]))
	pExtendedPowerWindow.AddChild(pButtonSwitch[1], x, y, 0)
	y = y + 0.04
	pButtonSwitch[2] = CreateButton(ET_NAME[4], g_pBrex, 2, App.TGString(ET_NAME[2]))
	pExtendedPowerWindow.AddChild(pButtonSwitch[2], x, y, 0)
	y = y + 0.04
	pButtonSwitch[3] = CreateButton(ET_NAME[4], g_pBrex, 3, App.TGString(ET_NAME[3]))
	pExtendedPowerWindow.AddChild(pButtonSwitch[3], x, y, 0)

        y = y + 0.04
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_SAVE)
        pEvent.SetDestination(g_pBrex)
        pEvent.SetInt(0)
        pButton = App.STRoundedButton_CreateW(App.TGString("Save"), pEvent, 0.13125, 0.034583)
        pExtendedPowerWindow.AddChild(pButton, x, y, 0)
        x = pButton.GetRight() + 0.01
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_LOAD)
        pEvent.SetDestination(g_pBrex)
        pEvent.SetInt(0)
        pButton = App.STRoundedButton_CreateW(App.TGString("Load"), pEvent, 0.13125, 0.034583)
        pExtendedPowerWindow.AddChild(pButton, x, y, 0)
        
        # just somwthing to redraw window
        pExtendedPowerWindow.Layout()


# handle mouse clicks in empty space
def PassMouse(pWindow, pEvent):
        debug(__name__ + ", PassMouse")
        pWindow.CallNextHandler(pEvent)

        if not pEvent.EventHandled():
                pEvent.SetHandled()


# check for changed settings, resets itself
def RefreshTimer(pObject=None, pEvent=None):
        debug(__name__ + ", RefreshTimer")
        global pShieldBars, pExtendedPowerWindow, Ships, ET_REFRESH, pRepairBar
        updategraphics = 0
        if not pExtendedPowerWindow:
                return 0
        if pExtendedPowerWindow.IsVisible():
                updategraphics = 1
	
        dTimeLeft=0.5
        pPlayer = MissionLib.GetPlayer()
        if pPlayer:
                if not pPlayer.GetShields().IsOn():
                        newPower = 0
                else:
                        newPower = pPlayer.GetShields().GetPowerPercentageWanted()
                if not Ships.has_key(str(pPlayer)):
                        Ships[str(pPlayer)] = ShipSettings(pPlayer)
        
                if Ships[str(pPlayer)].forceshieldupdate and updategraphics:
                        for i in range(App.ShieldClass.NUM_SHIELDS):
                                pShieldBars[i].SetValue(Ships[str(pPlayer)].ShieldStatus[i])
                                pShieldBars[i].Resize(0.2, 0.0364, 0)
                        if Ships[str(pPlayer)].forceshieldupdate:
                                Ships[str(pPlayer)].oldPower = newPower
                                Ships[str(pPlayer)].forceshieldupdate = 0
        
                if (newPower != Ships[str(pPlayer)].oldPower):
                        if not Ships.has_key(str(pPlayer)):
                                Ships[str(pPlayer)] = ShipSettings(pPlayer)
                        for i in range(App.ShieldClass.NUM_SHIELDS):
                                if Ships[str(pPlayer)].oldPower != 0:
                                        difference = Ships[str(pPlayer)].ShieldStatus[i] / Ships[str(pPlayer)].oldPower
                                else:
                                        difference = 1
                                newStatus = difference * newPower
                                Ships[str(pPlayer)].SetShieldStatus(i, newStatus)
                                if updategraphics:
                                        pShieldBars[i].SetValue(Ships[str(pPlayer)].ShieldStatus[i])
                                        pShieldBars[i].Resize(0.2, 0.0364, 0)
                                Ships[str(pPlayer)].PowerWanted[i] = newPower / 6
                        Ships[str(pPlayer)].oldPower = newPower
        
                if updategraphics:
                        for i in range(App.ShieldClass.NUM_SHIELDS):
                                if Ships[str(pPlayer)].forceshieldupdate:
                                        pShieldBars[i].SetValue(Ships[str(pPlayer)].ShieldStatus[i])
                        pRepairBar.SetValue(Ships[str(pPlayer)].GetRepair())
                        pRepairBar.Resize(0.2, 0.0364, 0)
                
		if updategraphics:
                	UpdateDynamicPowerWindowInterieur(updategraphics)
        
                if pExtendedPowerWindow.IsVisible() and updategraphics:
                        pExtendedPowerWindow.Layout()

        pTimerEvent = App.TGEvent_Create()
        pTimerEvent.SetEventType(ET_REFRESH)
        pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())
        pTimer = App.TGTimer_Create()
        pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + 0.5)
        pTimer.SetDelay(0)
        pTimer.SetDuration(0)
        pTimer.SetEvent(pTimerEvent)
        App.g_kTimerManager.AddTimer(pTimer)
	return 0


def CreateExtendedPowerWindow(pObject=None, pEvent=None):
        debug(__name__ + ", CreateExtendedPowerWindow")
        global pExtendedPowerWindow, g_pBrex
        
        # Create the Engineering extra Window:
        pExtendedPowerWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Extended Power Window"), 0.0, 0.0, None, 1, 0.8, 0.8, App.g_kMainMenuBorderMainColor)
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pTacticalControlWindow.AddChild(pExtendedPowerWindow, 0.1, 0.1)

        pExtendedPowerWindow.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".PassMouse")
        pExtendedPowerWindow.SetNotVisible()
        
        CreatePowerWindowInterieur()

        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "RefreshTimer")
        pSequence.AppendAction(pAction, 2)
        pSequence.Play()


def UnlockTimer(pObject, pEvent):
        debug(__name__ + ", UnlockTimer")
        global lockPowerWindow
        lockPowerWindow = 0


def PowerWindowKey(pObject, pEvent):
        debug(__name__ + ", PowerWindowKey")
        global lockPowerWindow
        if lockPowerWindow:
                return
        # Lock against too fast key presses
        lockPowerWindow = 1
        PowerWindow(pObject, pEvent)
        # unlock using a Timer
        MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".UnlockTimer", App.g_kUtopiaModule.GetGameTime() + 1.0, 0, 0)
   

def PowerWindow(pObject, pEvent):
        debug(__name__ + ", PowerWindow")
        global pExtendedPowerWindow
        if not pExtendedPowerWindow:
                return

        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        if pExtendedPowerWindow.IsVisible():
                pTacticalControlWindow.MoveToBack(pExtendedPowerWindow)
                pExtendedPowerWindow.SetNotVisible()
                DestroyDynamicPowerWindowInterieur()
        else:
                pExtendedPowerWindow.SetVisible()
                pTacticalControlWindow.MoveToFront(pExtendedPowerWindow)
                # Not so agressiv to the front - only give us problems!
                pTacticalControlWindow.MoveTowardsBack(pExtendedPowerWindow)
                CreateDynamicPowerWindowInterieur()
                #RefreshTimer()


# Seperate from PowerWindow() - just for close, avoids trouble
def PowerWindowClose(pObject, pEvent):
        debug(__name__ + ", PowerWindowClose")
        global pExtendedPowerWindow

        if not pExtendedPowerWindow:
                return

        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        if pExtendedPowerWindow.IsVisible():
                pTacticalControlWindow.MoveToBack(pExtendedPowerWindow)
                pExtendedPowerWindow.SetNotVisible()
                DestroyDynamicPowerWindowInterieur()

        pObject.CallNextHandler(pEvent)


def WeaponFired(pObject, pEvent):
        debug(__name__ + ", WeaponFired")
        global Ships
	# just try it the hard way:
	pFiringWeapon = App.TractorBeamProjector_Cast(pEvent.GetSource())
	if not pFiringWeapon:
		pFiringWeapon = App.PhaserBank_Cast(pEvent.GetSource())
	if not pFiringWeapon:
		pFiringWeapon = App.PulseWeapon_Cast(pEvent.GetSource())
	if not pFiringWeapon:
		pFiringWeapon = App.TorpedoTube_Cast(pEvent.GetSource())
	# lets get the parent ship - we need the parent subsystem for this:
	ParentSubsystem = App.ShipSubsystem_Cast(pFiringWeapon.GetParentSubsystem())
	pShip = ParentSubsystem.GetParentShip()
	WeaponName = pFiringWeapon.GetName()
        if not Ships.has_key(str(pShip)):
                return
	PowerLevel = Ships[str(pShip)].GetWeapon(WeaponName)
        if not PowerLevel or PowerLevel <= 1.5:
                return
        # else randomly damage it:
        # 1. Do we damage it=
        myLevel = 200 - PowerLevel * 100 # 50...0
        RandNum = App.g_kSystemWrapper.GetRandomNumber(100)
        if RandNum < myLevel:
                # no damage
                return
        # 2. how much damage?
        myLevel = PowerLevel - 1.0
        WeaponCondition = pFiringWeapon.GetConditionPercentage()
        cDamage = WeaponCondition - myLevel / (App.g_kSystemWrapper.GetRandomNumber(49) + 1)
        if cDamage <= 0:
                pShip.DestroySystem(pFiringWeapon)
        else:
                pFiringWeapon.SetConditionPercentage(cDamage)


def SetTorpLoad(pObject, pEvent):
        debug(__name__ + ", SetTorpLoad")
        global TorpsReady
        
        if TorpsReady.has_key(str(pEvent)):
                pProperty = TorpsReady[str(pEvent)][0]
                NumReady = TorpsReady[str(pEvent)][1]
                pShip = pProperty.GetParentShip()
                pTorpSys = pShip.GetTorpedoSystem()
                
                TotalReady = 0
                for i in range(pTorpSys.GetNumChildSubsystems()):
                        curProperty = App.TorpedoTube_Cast(pTorpSys.GetChildSubsystem(i))
                        curNumReady = curProperty.GetNumReady()
                        TotalReady = TotalReady + curNumReady
                
                curTorpNumber = pTorpSys.GetCurrentAmmoTypeNumber()
                iNumTorps = pTorpSys.GetNumAvailableTorpsToType(curTorpNumber)
                
                if TotalReady + NumReady > iNumTorps:
                        NumReady = iNumTorps - TotalReady
                
                pProperty.SetNumReady(NumReady)
                
                del TorpsReady[str(pEvent)]

                # try to refresh the icons
                #pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                #pWeaponsDisplay = pTCW.GetWeaponsDisplay()
                #pTorpedoPane = App.TGPane_Cast(pWeaponsDisplay.GetNthChild(App.WeaponsDisplay.TORPEDO_PANE))
	        #for i in range(pTorpSys.GetNumChildSubsystems()):
		#        pTubeIcon = App.TGIcon_Cast(pTorpedoPane.GetNthChild(i))
                #
                #       if (pTubeIcon != None):
                #               kColor = App.NiColorA()
                #               kColor.r = 0.0
		#	        kColor.g = 1.0
		#	        kColor.b = 0.0
		#	        kColor.a = 0.0
		#	        pTubeIcon.SetColor(kColor)
                #pTorpedoPane.Layout()

def init():
        debug(__name__ + ", init")
        global g_pBrex, ET_SHIELDS, ET_NAME, ET_REFRESH, ET_REPAIR, ET_CLOSE, ET_WEAPON, ET_TRACTOR, TORPEDO_SET_TIMER
        
        if not Lib.LibEngineering.CheckActiveMutator("Advanced Power control"):
                return
        if not IsMultiplayerHostAlone():
                return

	pGame = App.Game_GetCurrentGame()
        pEpisode	        = pGame.GetCurrentEpisode()
        pMission	        = pEpisode.GetCurrentMission()
        ET_CLOSE                = Lib.LibEngineering.GetEngineeringNextEventType()
        pBridge = App.g_kSetManager.GetSet("bridge")
        g_pBrex = App.CharacterClass_GetObject(pBridge, "Engineer")
        Lib.LibEngineering.CreateMenuButton("Advanced Power control", "Engineer", __name__ + ".PowerWindow")
        # key bind
        #Lib.LibEngineering.AddKeyBind("Advanced Power control", __name__ + ".PowerWindowKey")
	import Custom.Autoload.APMMutator
	App.g_kEventManager.AddBroadcastPythonFuncHandler(Custom.Autoload.APMMutator.ET_KEY_EVENT, MissionLib.GetMission(), __name__ + ".PowerWindowKey")
	
        # sounds like the game sometimes crashes if we already create it here, so don't
        #CreateExtendedPowerWindow()
        # really bad work around!
        MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".CreateExtendedPowerWindow", App.g_kUtopiaModule.GetGameTime() + 2.0, 0, 0)
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_SHIELDS[0][0], pMission, __name__ + ".SetShield0")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_SHIELDS[1][0], pMission, __name__ + ".SetShield1")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_SHIELDS[2][0], pMission, __name__ + ".SetShield2")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_SHIELDS[3][0], pMission, __name__ + ".SetShield3")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_SHIELDS[4][0], pMission, __name__ + ".SetShield4")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_SHIELDS[5][0], pMission, __name__ + ".SetShield5")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_REPAIR, pMission, __name__ + ".SetRepair")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".PowerWindow")
        if g_pBrex:
	        g_pBrex.AddPythonFuncHandlerForInstance(ET_NAME[4], __name__ + ".SwitchName")
	        g_pBrex.AddPythonFuncHandlerForInstance(ET_SAVE, __name__ + ".SaveConfig")
                g_pBrex.AddPythonFuncHandlerForInstance(ET_LOAD, __name__ + ".LoadConfig")
                g_pBrex.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".PowerWindowClose")
	App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(ET_REFRESH, __name__ + ".RefreshTimer")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WEAPON, pMission, __name__ + ".SetWeapon")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_TRACTOR, pMission, __name__ + ".SetTractor")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_FIRED, pMission, __name__+".WeaponFired")
        App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(TORPEDO_SET_TIMER, __name__ + ".SetTorpLoad")


def exit():
        debug(__name__ + ", exit")
        global pExtendedPowerWindow, Ships, TorpsReady
        
        if pExtendedPowerWindow:
                pExtendedPowerWindow.KillChildren()
                pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
                pTacticalControlWindow.DeleteChild(pExtendedPowerWindow)
		pExtendedPowerWindow = None
        Ships = {}
        TorpsReady = {}


def Restart():
        debug(__name__ + ", Restart")
        global Ships
        Ships = {}
