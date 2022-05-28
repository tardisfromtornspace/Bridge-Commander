import App

###############################################################################
#	Cloaked Firing
#	
#	The Cloaked Firing Plugin
###############################################################################

def CloakPlugin (pShipType, pCloakingShipName):

##########################Don't Edit Above This Line###########################

        pNormalScript = "ships.Klingon Bird Of Prey"
        pPlayerScript = "ships.Klingon Bird Of PreyP"
        pComputScript = "ships.Klingon Bird Of PreyAI"

        # Cloaking Limitations Where 0 = No and 1 = Yes

        # Shields Down While Cloaked
        pShieldsDown = "1"

	# Phasers Down While Cloaked
	pPhasersDown = "1"

	# Pulse Weapons Down While Cloaked
	pPulseDown = "1"

	# Torpedoes Down While Cloaked
	pTorpedoesDown = "0"

        # Probes Detect Cloaked Ship
        pProbeDetection = "1"

        # Scan Area Detects Cloaked Ships Briefly
        pScanDetection = "0"

	# Can Be Detected By Neutron Radiation
	pNeutronDetection = "1"
	
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
