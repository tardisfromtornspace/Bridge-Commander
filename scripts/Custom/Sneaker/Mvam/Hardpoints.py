import App

# names explain themselves
def HardpointsSep (pPlayerOriginal, pPlayer, pMvamShips):
	#integrate pPlayer and pMvamShips. It'll just be easier
	pMvamShips.append(pPlayer)

	# get the property sets... 
	pPlayerSet = pPlayerOriginal.GetPropertySet()
	pMvamSet = []
	for i in range (len(pMvamShips)):
		pMvamSet.append(pMvamShips[i].GetPropertySet())

	# Grab all subsystems
	pPlayerList = pPlayerSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
	pMvamList = []
	for i in range (len(pMvamShips)):
		pMvamList.append(pMvamSet[i].GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY))

	#lets go through all the player items
	pPlayerList.TGBeginIteration()

	#for the record, I HATE how im doing this. its so damned inefficient... but it saves you guys a tonne of hp work
	for i in range(pPlayerList.TGGetNumItems()):
		# okay, we need subsystems of ALL the items on the player ship
		pPlayerProperty = App.SubsystemProperty_Cast(pPlayerList.TGGetNext().GetProperty())
		pPlayerSub = pPlayerOriginal.GetSubsystemByProperty(pPlayerProperty)

		#okay, start iterating in the mvam ships. basically, we go through each one looking for a match
		for j in range (len(pMvamShips)):
			pMvamList[j].TGBeginIteration()

			for k in range (pMvamList[j].TGGetNumItems()):
				#grab the properties n such
				pMvamProperty = App.SubsystemProperty_Cast(pMvamList[j].TGGetNext().GetProperty())
				pMvamSub = pMvamShips[j].GetSubsystemByProperty(pMvamProperty)

				#check if they are none. it'd be baddd if they were
				if (pPlayerSub != None and pMvamSub != None):
					if (pPlayerSub.GetName() == pMvamSub.GetName()):
						try:
							#standard damage transfering
							pMvamSub.SetConditionPercentage(pPlayerSub.GetConditionPercentage())
						except:
							#this is odd, but it could happen
							DoNothing = "Failed"

						#okay, if its the power core we're gonna havta have a wee lil talk to it
						if (pMvamSub.IsTypeOf(App.CT_POWER_SUBSYSTEM)):
							pPlayerPower = pPlayerOriginal.GetPowerSubsystem()
							pMvamPower = pMvamShips[j].GetPowerSubsystem()
							if (pPlayerPower and pMvamPower):
								pMvamPower.SetAvailablePower(pPlayerPower.GetAvailablePower())
								pMvamPower.SetMainBatteryPower(pPlayerPower.GetMainBatteryPower())
								pMvamPower.SetBackupBatteryPower(pPlayerPower.GetBackupBatteryPower())

						#now to check for shields and transfer over the charge
						elif (pMvamSub.IsTypeOf(App.CT_SHIELD_SUBSYSTEM)):
							#get all the shield classes
							pPlayerShields = App.ShieldClass_Cast(pPlayerSub)
							pMvamShields = App.ShieldClass_Cast(pMvamSub)

							if (pPlayerShields and pMvamShields):
								#get all shield facings
								kShieldFacings = [App.ShieldProperty.FRONT_SHIELDS, App.ShieldProperty.REAR_SHIELDS, App.ShieldProperty.TOP_SHIELDS, App.ShieldProperty.BOTTOM_SHIELDS, App.ShieldProperty.LEFT_SHIELDS, App.ShieldProperty.RIGHT_SHIELDS]

								#now, lets cycle through all the shields and set their charge
								for kFacing in kShieldFacings:
									fPct = pPlayerShields.GetSingleShieldPercentage(kFacing)
									pMvamShields.SetCurShields(kFacing, (pMvamShields.GetMaxShields(kFacing) * fPct))

						#check to transfer phaser charge
						elif (pMvamSub.IsTypeOf(App.CT_ENERGY_WEAPON)):
							#cast em all!
							pPlayerWeapon = App.EnergyWeapon_Cast(pPlayerSub)
							pMvamWeapon = App.EnergyWeapon_Cast(pMvamSub)
							if (pPlayerWeapon and pMvamWeapon):
								try:
									pMvamWeapon.SetChargeLevel(pPlayerWeapon.GetChargeLevel())
								except:
									DoNothing = "Failed"

						#check to transfer torpedo loads
						elif (pMvamSub.IsTypeOf(App.CT_TORPEDO_SYSTEM)):
							#load up proper torps. i want it all in a try-except just in case
							pPlayerTorpSys = App.TorpedoSystem_Cast(pPlayerSub)
							pMvamTorpSys = App.TorpedoSystem_Cast(pMvamSub)
							if (pPlayerTorpSys and pMvamTorpSys):
								for iType in range(pMvamTorpSys.GetNumAmmoTypes()):
									#grab the number of torps the player used so we can subtract it
									intNumTorps = pPlayerTorpSys.GetProperty().GetMaxTorpedoes(iType) / len(pMvamShips)
									pMvamTorpSys.LoadAmmoType(iType, -(intNumTorps + (intNumTorps - (pPlayerTorpSys.GetNumAvailableTorpsToType(iType) / len(pMvamShips)))))

	# save some memory here
	pPlayerList.TGDoneIterating()
	pPlayerList.TGDestroy()
	for i in range (len(pMvamShips)):
		pMvamList[i].TGDoneIterating()
		pMvamList[i].TGDestroy()

	return


def HardpointsRein (pPlayerOriginal, pPlayer, pMvamShips):
	#integrate pPlayer and pMvamShips. It'll just be easier
	pMvamShips.append(pPlayer)

	# get the property sets... 
	pPlayerSet = pPlayerOriginal.GetPropertySet()
	pMvamSet = []
	for i in range (len(pMvamShips)):
		pMvamSet.append(pMvamShips[i].GetPropertySet())

	# Grab all subsystems
	pPlayerList = pPlayerSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
	pMvamList = []
	for i in range (len(pMvamShips)):
		pMvamList.append(pMvamSet[i].GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY))

	#tally up the total number of torps...
	intTotalTorps = 0

	#lets go through all the player items
	pPlayerList.TGBeginIteration()

	#for the record, I HATE how im doing this. its so damned inefficient... but it saves you guys a tonne of hp work
	for i in range(pPlayerList.TGGetNumItems()):
		# okay, we need subsystems of ALL the items on the player ship
		pPlayerProperty = App.SubsystemProperty_Cast(pPlayerList.TGGetNext().GetProperty())
		pPlayerSub = pPlayerOriginal.GetSubsystemByProperty(pPlayerProperty)

		#okay, start iterating in the mvam ships. basically, we go through each one looking for a match
		for j in range (len(pMvamShips)):
			pMvamList[j].TGBeginIteration()

			for k in range (pMvamList[j].TGGetNumItems()):
				#grab the properties n such
				pMvamProperty = App.SubsystemProperty_Cast(pMvamList[j].TGGetNext().GetProperty())
				pMvamSub = pMvamShips[j].GetSubsystemByProperty(pMvamProperty)

				#check if they are none. it'd be baddd if they were
				if (pPlayerSub != None and pMvamSub != None):
					if (pPlayerSub.GetName() == pMvamSub.GetName()):
						try:
							#not so standard damage transfering
							if (pPlayerSub.GetConditionPercentage() == 1.0):
								pPlayerSub.SetConditionPercentage(pMvamSub.GetConditionPercentage())
							else:
								pPlayerSub.SetConditionPercentage((pPlayerSub.GetConditionPercentage() + pMvamSub.GetConditionPercentage()) / 2)
						except:
							#this is odd, but it could happen
							DoNothing = "Failed"

						#now to check for shields and transfer over the charge
						if (pMvamSub.IsTypeOf(App.CT_SHIELD_SUBSYSTEM)):
							#get the player shields... we need this for later, unfortunately
							pPlayerShields = App.ShieldClass_Cast(pPlayerSub)

						#okay, if its the power core we're gonna havta have a wee lil talk to it
						elif (pMvamSub.IsTypeOf(App.CT_POWER_SUBSYSTEM)):
							pPlayerPower = pPlayerOriginal.GetPowerSubsystem()
							pMvamPower = pMvamShips[j].GetPowerSubsystem()
							if (pPlayerPower and pMvamPower):
								if (pPlayerPower.GetAvailablePower() != pMvamPower.GetAvailablePower()):
									pPlayerPower.SetAvailablePower((pPlayerPower.GetAvailablePower() + pMvamPower.GetAvailablePower()) / 2)
								if (pPlayerPower.GetMainBatteryPower() != pMvamPower.GetMainBatteryPower()):
									pPlayerPower.SetMainBatteryPower((pPlayerPower.GetMainBatteryPower() + pMvamPower.GetMainBatteryPower()) / 2)
								if (pPlayerPower.GetBackupBatteryPower() != pMvamPower.GetBackupBatteryPower()):
									pPlayerPower.SetBackupBatteryPower((pPlayerPower.GetBackupBatteryPower() + pMvamPower.GetBackupBatteryPower()) / 2)

						#check to transfer phaser charge
						elif (pMvamSub.IsTypeOf(App.CT_ENERGY_WEAPON)):
							#cast em all!
							pPlayerWeapon = App.EnergyWeapon_Cast(pPlayerSub)
							pMvamWeapon = App.EnergyWeapon_Cast(pMvamSub)
							if (pPlayerWeapon and pMvamWeapon):
								pPlayerWeapon.SetChargeLevel(pMvamWeapon.GetChargeLevel())

						#check to transfer torpedo loads
						elif (pMvamSub.IsTypeOf(App.CT_TORPEDO_SYSTEM)):
							#grab the players torpedo system. we'll need it later
							pPlayerTorpSys = App.TorpedoSystem_Cast(pPlayerSub)

	#well... I'm lazy. so therefore, I'm doing torps after iteration rather then during
	pMvamTorpSys = []
	for i in range (len(pMvamShips)):
		if (pPlayerTorpSys.GetName() == pMvamShips[i].GetTorpedoSystem().GetName()):
			pMvamTorpSys.append(pMvamShips[i].GetTorpedoSystem())

	#check just to make sure... and then add up a total
	if (pPlayerTorpSys):
		#iterate through the torpedo systems and add up the total number of torpedoes
		intaTorpNum = [0,0,0,0,0,0,0,0]
		for i in range (len(pMvamTorpSys)):
			if (pMvamTorpSys[i]):
				for j in range (pMvamTorpSys[i].GetNumAmmoTypes()):
					intaTorpNum[j] = intaTorpNum[j] + pMvamTorpSys[i].GetNumAvailableTorpsToType(j)

		#now lets apply them to the player ship
		for i in range (pPlayerTorpSys.GetNumAmmoTypes()):
			pPlayerTorpSys.LoadAmmoType(i, -(pPlayerTorpSys.GetProperty().GetMaxTorpedoes(i) - intaTorpNum[i]))

	#grab the shields on all ships
	pMvamShields = []
	for i in range (len(pMvamShips)):
		pMvamShields.append(pMvamShips[i].GetShields())

	#get all shield facings
	kShieldFacings = [App.ShieldProperty.FRONT_SHIELDS, App.ShieldProperty.REAR_SHIELDS, App.ShieldProperty.TOP_SHIELDS, App.ShieldProperty.BOTTOM_SHIELDS, App.ShieldProperty.LEFT_SHIELDS, App.ShieldProperty.RIGHT_SHIELDS]

	#now, lets cycle through all the shields and set their charge
	for kFacing in kShieldFacings:
		intChargeTally = 0
		intCounter = 0
		for i in range (len(pMvamShips)):
			#i need a try in here.. it could fail entirely
			try:
				if (pMvamShields[i].GetName() == pPlayerShields.GetName()):
					intChargeTally = intChargeTally + pMvamShields[i].GetSingleShieldPercentage(kFacing)
					intCounter = intCounter + 1
			except:
				#something went wrong... maybe the shields dont exist on the mvam ship
				DoNothing = "OhWell"

		#make sure the player actually has shields...
		if (pPlayerShields and intCounter != 0):
			pPlayerShields.SetCurShields(kFacing, (pPlayerShields.GetMaxShields(kFacing) * (intChargeTally / intCounter)))


	# save some memory here
	pPlayerList.TGDoneIterating()
	pPlayerList.TGDestroy()
	for i in range (len(pMvamShips)):
		pMvamList[i].TGDoneIterating()
		pMvamList[i].TGDestroy()

	return


#this is used for temporary ship hardpoint transfering
def HardpointsTemp (pShip1, pShip2):
	# get the property sets...
	pShip1Set = pShip1.GetPropertySet()
	pShip2Set = pShip2.GetPropertySet()

	# Grab all subsystems
	pShip1List = pShip1Set.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
	pShip2List = pShip2Set.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)

	#lets go through all the player items
	pShip1List.TGBeginIteration()
	pShip2List.TGBeginIteration()
	for i in range(pShip1List.TGGetNumItems()):
		# okay, we need subsystems of ALL the items on both ships
		pShip1Property = App.SubsystemProperty_Cast(pShip1List.TGGetNext().GetProperty())
		pShip1Sub = pShip1.GetSubsystemByProperty(pShip1Property)
		pShip2Property = App.SubsystemProperty_Cast(pShip2List.TGGetNext().GetProperty())
		pShip2Sub = pShip2.GetSubsystemByProperty(pShip2Property)
		if (pShip1Sub != None):
			#maybe its only a property? it'd have no condition. just being careful here
			try:
				pShip1Sub.SetCondition(pShip2Sub.GetCondition())
			except:
				DoNothing = "Failed"

			#okay, if its the power core we're gonna havta have a wee lil talk to it
			if (pShip1Sub.IsTypeOf(App.CT_POWER_SUBSYSTEM)):
				#really, this isnt neccessary to do this here. but i will, just for kicks. it doesnt really matter
				pShip1Power = pShip1.GetPowerSubsystem()
				pShip2Power = pShip2.GetPowerSubsystem()

				pShip1Power.SetAvailablePower(pShip2Power.GetAvailablePower())
				pShip1Power.SetMainBatteryPower(pShip2Power.GetMainBatteryPower())
				pShip1Power.SetBackupBatteryPower(pShip2Power.GetBackupBatteryPower())

			#now to check for shields and transfer over the charge
			elif (pShip1Sub.IsTypeOf(App.CT_SHIELD_SUBSYSTEM)):
				#get all the shield classes
				pShip1Shields = App.ShieldClass_Cast(pShip1Sub)
				pShip2Shields = App.ShieldClass_Cast(pShip2Sub)

				#get all shield facings
				kShieldFacings = [App.ShieldProperty.FRONT_SHIELDS, App.ShieldProperty.REAR_SHIELDS, App.ShieldProperty.TOP_SHIELDS, App.ShieldProperty.BOTTOM_SHIELDS, App.ShieldProperty.LEFT_SHIELDS, App.ShieldProperty.RIGHT_SHIELDS]

				#now, lets cycle through all the shields and set their charge
				for kFacing in kShieldFacings:
					fPct = pShip2Shields.GetSingleShieldPercentage(kFacing)
					pShip1Shields.SetCurShields(kFacing, (pShip2Shields.GetMaxShields(kFacing) * fPct))

			#check to transfer phaser charge
			elif (pShip1Sub.IsTypeOf(App.CT_ENERGY_WEAPON)):
				#cast em all!
				pShip1Weapon = App.EnergyWeapon_Cast(pShip1Sub)
				pShip2Weapon = App.EnergyWeapon_Cast(pShip2Sub)

				#transfer charge
				pShip1Weapon.SetChargeLevel(pShip2Weapon.GetChargeLevel())

			#grab the torps
			elif (pShip1Sub.IsTypeOf(App.CT_TORPEDO_SYSTEM)):
				#get the torpedoes casted
				pShip1TorpSys = App.TorpedoSystem_Cast(pShip1Sub)
				pShip2TorpSys = App.TorpedoSystem_Cast(pShip2Sub)

				#lets transfer the torps
				for iType in range(pShip1TorpSys.GetNumAmmoTypes()):
					pShip1TorpSys.LoadAmmoType(iType, -(pShip2TorpSys.GetProperty().GetMaxTorpedoes(iType) - pShip2TorpSys.GetNumAvailableTorpsToType(iType)))

	# save some memory here
	pShip1List.TGDoneIterating()
	pShip1List.TGDestroy()
	pShip2List.TGDoneIterating()
	pShip2List.TGDestroy()