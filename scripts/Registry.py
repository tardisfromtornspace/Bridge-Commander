from bcdebug import debug
# Registry class
# November 2001
# By Daniel B. Houghton, all rights reserved


#########################################################
# Registry classes
# The Registry maintains a list of loaded objects by name and in an ordered list.
# It is meant to keep track of prototypes, although it has potential uses in property maps.
# - DH

class Registry:
	def __init__(self):
		debug(__name__ + ", __init__")
		self._keyList = {}
		self._arrayList = []

	def Register(self, obj, name):
		debug(__name__ + ", Register")
		self._keyList[name] = obj
		for i in range(0, len(self._arrayList)):
			if self._arrayList[i] == name:
				return i				# Return offset of current placement
		else:
			self._arrayList.append(name)
		return len(self._arrayList) - 1   # Return array size as it was before

	def Remove(self, what):
		debug(__name__ + ", Remove")
		if self._keyList.has_key(what):
			self._arrayList.remove(what)
			del self._keyList[what]

	def __len__(self):
		debug(__name__ + ", __len__")
		return len(self._arrayList)
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return self.List()

	def __getitem__(self, i):
		#debug(__name__ + ", __getitem__")
		try:	idx = int(i)
		except ValueError:
			return self._keyList[i]
		return self._keyList[self._arrayList[idx]]

	#def __iter__(self):
	#	debug(__name__ + ", __iter__")
	#	return self._arrayList.iteritems()

	def has_key(self, key):
		debug(__name__ + ", has_key")
		return self._keyList.has_key(key)

	def GetName(self, i):
		debug(__name__ + ", GetName")
		if self._keyList.has_key(i):
			return self._keyList[i]
		return None

	def List(self, col = 1):
		debug(__name__ + ", List")
		i = 0
		end = len(self._arrayList)
		width = 80 / col
		retval = ''
		for key in self._arrayList:
			if (i != end and i % col == 0):  retval = retval + '\r'
			i = i + 1
			retval = retval + ("%s%s" % (key, (' ' * (width - len(key)))))
		return retval

	def ListNumbered(self, col = 1, width = 80):
		debug(__name__ + ", ListNumbered")
		i = 0
		end = len(self._arrayList)
		# width /= (col + 4)
		width = (width / col) - col
		retval = ""
		for key in self._arrayList:
			i = i + 1
			retval = retval +  ('%3d) %s%s' % (i, key, (' ' * (width - len(key)))))
			if (i != end and i % col == 0):  retval = retval + '\r'
		return retval


class IntHashRegistry(Registry):
	def __init__(self):
		debug(__name__ + ", __init__")
		Registry.__init__(self)
		self._hashList = {}

	def Register(self, obj, name):
		debug(__name__ + ", Register")
		Registry.Register(self, obj, name)
		self._hashList[int(obj)] = obj

	def Remove(self, what):
		debug(__name__ + ", Remove")
		if self._hashList.has_key(what):
			Registry.Remove(self, self._hashList[what.__repr__()])
			del self._hashList[what]
		else:
			del self._hashList[self._keyList[what]]
			Registry.Remove(self, what)

	def __getitem__(self, i):
		debug(__name__ + ", __getitem__")
		try:	idx = hash(i)
		except ValueError:
			return self._keyList[i]
		if self._hashList.has_key(idx):
			return self._hashList[idx]
		return None
