# Console Logger
#
# by MLeo
#
# This console logger is an entirely selfsufficent logger with no big impact other than disk writing, so no periodic hickups after a big (or loads) of print statements in a short time
# Check for the logs in scripts/Custom/Logs/ if you sort the directory/map/folder by date (descending) then the newest log is at the top.
# There are 3 types of logs, input (what you type into the console), output (what print statements do) and the "console" log, which is what appears on the console, in the same order as the console.
# For (script) Support, please include the console log in your thread
#
# Scratch part of the earlier part, this will only log output, since input appears to be too difficult for now.

import App
import nt
import time


currentTime = time.localtime(time.time())

sPrefix= "%04d%02d%02d_%02d%02d%02d"%(currentTime[:6])

output = nt.open("scripts/Custom/Logs/%s_output.log" %sPrefix, nt.O_CREAT|nt.O_WRONLY|nt.O_TRUNC)

class ConsolePipe:
	def __init__(self, next, name):
		self.__next = next
		self.__name = name
		setattr(sys, name, self)
	def write(self, s):
		setattr(sys, self.__name, self.__next)
		self.__next.write(s)
		self.__next.flush()
		setattr(sys, self.__name, self)
		global output
		nt.write(output, s)
	def writelines(self, l):
		r = string.joinfields(l, '')
		self.write(r)
	def __getattr__(self, name):
		return getattr(self.__next, name)

import sys

s = sys.stdout.getvalue()
nt.write(output, s)# Get the current values

ConsolePipe(sys.stderr, "stderr")
ConsolePipe(sys.stdout, "stdout")

