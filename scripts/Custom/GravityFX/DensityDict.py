DensityDict = {
"DEFAULT": [0.1, 10.0],
"Blue Gas": [0, 0],
"Class-B": [4.7, 6.5],
"Class-C": [1.0, 3.0],
"Class-D": [6.0, 8.0],
"Class-E": [3.2, 5.3],
"Class-F": [3.5, 5.7],
"Class-H": [4.0, 6.5],
"Class-I": [0.65, 2.5],
"Class-J": [0.8, 2.7],
"Class-K": [3.0, 5.5],
"Class-M": [4.5, 6.0],
"Class-N": [4.8, 6.3],
"Class-O": [4.3, 5.8],
"Class-P": [4.2, 5.6],
"Class-S": [0.8, 2.9],
"Class-T": [0.9, 2.9],
"H-Class": [4.6, 6.2],
"Io-Class": [0, 0],
"Luminious": [0, 0],
"N-Class 1": [0, 0],
"N-Class 2": [0, 0],
"Ringed": [0, 0],
"Y-Class": [4.9, 6.25]
}

def AddPlanetClass(name, minDensity, maxDensity):
	global DensityDict
	DensityDict[name] = [minDensity, maxDensity]

def GetClasses():
	return keys()

def keys():
	return DensityDict.keys()

def GetAllDensityRanges():
	return values()

def values():
	return DensityDict.values()

def GetDensityRange(className):
	if DensityDict.has_key(className):
		return DensityDict[className]
	else:
		return []

def has_key(key):
	return DensityDict.has_key(key)