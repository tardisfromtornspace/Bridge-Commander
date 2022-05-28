#!/usr/bin/python

import App
import nt

def Go():
	file = nt.open("scripts/Custom/EventTypes.txt", nt.O_WRONLY | nt.O_APPEND | nt.O_CREAT)
	for sKey in App.__dict__.keys():
		if sKey[:3] == "ET_":
			nt.write(file, "%s = %d\n" % (sKey, App.__dict__[sKey]))
	nt.close(file)

