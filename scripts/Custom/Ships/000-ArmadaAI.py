import App
import Foundation
import F_FedAttackLightCruiser

sMutatorName = "new AI (needs restart)"

# remove '#' to enable in the line below
#mode = Foundation.MutatorDef(sMutatorName)


def CheckActiveMutator(MutatorName):
	Foundation.LoadConfig()
	for i in Foundation.mutatorList._arrayList:
		fdtnMode = Foundation.mutatorList._keyList[i]
		if fdtnMode.IsEnabled() and (fdtnMode.name == MutatorName):
			return 1
	return 0


if CheckActiveMutator(sMutatorName):
	Foundation.FedShipDef = F_FedAttackLightCruiser.FedAttackLightCruiserAI
