import Foundation
import nt


###############################################################################
## Get File Names with extension from path sFolderPath
###############################################################################
def GetFileNames(sFolderPath, extension):
	import string
	sFileList = nt.listdir(sFolderPath)

	retList = []

	for i in sFileList:
		s = string.split(string.lower(i), '.')
		ext = s[-1]

		if extension == ext:
			retList.append(i)

	retList.sort()
	return retList


Foundation.GetFileNames = GetFileNames
GetFileNames = None


def IsDir(sFolder):
	return (nt.stat(sFolder)[0] & 0170000) == 0040000

Foundation.IsDir = IsDir
IsDir = None


## Basic class from SFN ported to Python 1.5.2.  Written by Daniel Rollings, AKA Dasher42.

class Flags:
	"""A generic long bitvector.  Accessors maintain integrity of the >32 bit size.
	"""
	def __init__(self, val = 0):
		self._value = long(val)

	def __repr__(self):
		return str(self._value)

	def __long__(self):
		return self._value

	def __int__(self):
		return self._value

	def List(self, registry):
		out = []
		for i in range(0, len(registry)):
			if self[i]:
				out.append(registry[i])
		return string.join(out, ', ');

	def __iand__(self, other):
		return self._value & long(other)

	def __ixor__(self, other):
		return self._value ^ long(other)

	def __ior__(self, other):
		return self._value | long(other)

	def Toggle(self, num):
		if long(num) >= 1024:	# Manual limits imposed because extremely high precisions cause slowdown
			raise IndexError	# and could be a sign of buggy code.
		self._value = self._value ^ long(1 << long(num))

	def Set(self, num):
		if long(num) >= 1024:	# Manual limits imposed because extremely high precisions cause slowdown
			raise IndexError	# and could be a sign of buggy code.
		self._value = self._value | long(1 << long(num))

	def UnSet(self, num):
		if long(num) >= 1024:	# Manual limits imposed because extremely high precisions cause slowdown
			raise IndexError	# and could be a sign of buggy code.
		self._value = self._value & long(1 << long(num))

	def Clear(self):
		self_value = long(0)

	def __getitem__(self, i):
		return self._value & long(1 << long(i))

	# This is experimental
	def __setitem__(self, i, val):
		if val:
			self._value = self._value | long(1 << long(i))
		else:
			self._value = self._value & long(1 << long(i))
		return self._value


import Foundation
Foundation.Flags = Flags
