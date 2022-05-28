import App

###############################################################################
#	Cloaked Firing
#	
#	The Cloaked Firing Plugin
###############################################################################

def CloakPlugin (pShipType, pCloakingShipName):

##########################Don't Edit Above This Line###########################

        pNormalScript = "ships.Reman Scimitar"
        pPlayerScript = "ships.Reman ScimitarP"
        pComputScript = "ships.Reman ScimitarAI"

        # Cloaking Limitations - Ways It Can Be Detected Where 0 = No and 1 = Yes

        # Shields Down While Cloaked
        pShieldsDown = "0"

	# Phasers Down While Cloaked
	pPhasersDown = "0"

	# Pulse Weapons Down While Cloaked
	pPulseDown = "0"

	# Torpedoes Down While Cloaked
	pTorpedoesDown = "0"

        # Probes Detect Cloaked Ship - Not Implemented
        pProbeDetection = "0"

        # Scan Area Detects Cloaked Ships Briefly - Not Implemented
        pScanDetection = "0"

	# Can Be Detected By Neutron Radiation
	pNeutronDetection = "0"

##########################Don't Edit Below This Line###########################

        if (pCloakingShipName == "0"):
                pass
        else:
                import Custom.TechnologyExpansion.Scripts.CloakedFiring.CloakActivate
                g_CloakedShipPlugins = Custom.TechnologyExpansion.Scripts.CloakedFiring.CloakActivate.g_CloakedShipPlugins
                g_CloakedShipPlugins[str(pCloakingShipName)] = pShieldsDown, pPhasersDown, pPulseDown, pTorpedoesDown, pProbeDetection, pScanDetection, pNeutronDetection

        if (pShipType == "P"):
                pLoadScript = pPlayerScript
                return (pShipType, pLoadScript)
        elif (pShipType == "AI"):
                pLoadScript = pComputScript
                return (pShipType, pLoadScript)
        elif (pShipType == "C"):
                pLoadScript = pNormalScript
                return (pShipType, pLoadScript)
        else:
                print ("Something Went Really Wrong")
