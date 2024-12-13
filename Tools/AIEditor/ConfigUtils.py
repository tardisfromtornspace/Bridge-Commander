try:
    from Tkinter import *
except:
    from tkinter import *

class EditTextDialog(Toplevel):
	def __init__(self, pParent, pSetTextFunc, sText):
		# Base class init
		Toplevel.__init__(self, pParent)

		self.focus_set()

		self.pSetTextFunc = pSetTextFunc

		# Create a text box so our text can be edited:
		self.pText = Text(self, font=(("Courier"), "10"), height=40, width=80, tabs="24p")
		self.pText.pack(side=TOP, fill=BOTH, anchor=NW, expand=YES)
		# Fill the text entry box with our existing text...
		self.pText.insert(END, sText)

		# Add an OK button.
		Button(self, text="Ok", command=self.Ok).pack(side=BOTTOM, anchor=W)

		# Key bindings.
		self.pText.bind("<Return>", lambda event, self=self: self.HandleNewline(event))

	def Ok(self):
		self.pSetTextFunc( self.pText.get(0.0, END) )
		self.destroy()

	def HandleNewline(self, event):
		text = self.pText
		try:
			first = text.index("sel.first")
			last = text.index("sel.last")
		except TclError:
			first = last = None

		if first and last:
			text.delete(first, last)
			text.mark_set("insert", first)

		line = text.get("insert linestart", "insert")
		# Get the indentation of the previous line.
		i, n = 0, len(line)
		while i < n and line[i] in " \t":
			i = i+1
		indent = line[:i]

		# Check the last character of the previous line, to see
		# if the next line should be indented further.
		lastchar = text.get("insert -1c")
		if lastchar == ":":
			if not indent:
				indent = "\t"
			else:
				indent = indent + "\t"

		# Insert the newline and indentation.
		text.insert("insert", "\n" + indent)
		text.see("insert")
		return "break"

class ConfigurationDialog(Toplevel):
	def __init__(self, pOutput, pAI, **dOptions):
		# Base class init
		Toplevel.__init__(self, pOutput)

		self.focus_set()

		# Member variable setup
		self.pOutput = pOutput
		self.pAI = pAI

		# Create things so the user can change our name
		pFrame = Frame(self)
		pFrame.pack(side=TOP, anchor=W, pady=2, fill=X, expand=NO)
		self.sNameVar = StringVar()
		Label(pFrame, text="Name:").pack(side=LEFT)
		pNameEntry = Entry(pFrame, width=40, textvariable=self.sNameVar)
		pNameEntry.pack(side=LEFT)
		pNameEntry.bind("<KeyPress>", self.NameKey)
		self.sNameVar.set(self.pAI.GetName())

		# Create a "Copy" button.
		Button(pFrame, text="Copy", command=self.Copy).pack(side=RIGHT)

		# Add a checkbox for setting the AI interruptable or not.
		self.bInterruptable = IntVar()
		Checkbutton(self, text="Interruptable", variable=self.bInterruptable).pack(side=TOP, anchor=W)
		self.bInterruptable.set(self.pAI.bInterruptable)

		# Let the user delete this item.
		pFrame = Frame(self)
		pFrame.pack(side=BOTTOM, anchor=W, pady=8, fill=X)
		Button(pFrame, text="Ok", command=self.Ok).pack(side=LEFT)
		Button(pFrame, text="Delete", command=self.DeleteAI).pack(side=RIGHT)

		# Advanced feature:  Edit Post-AI text:
		try:
			if dOptions["EditPostAIText"]:
				Button(pFrame, text="Edit Post-AI text", command=self.EditPostAIText).pack(side=RIGHT)
		except KeyError:
			pass

	def NameKey(self, event):
		# Check if the character is one of the characters
		# we'll allow in a name.  If not, we need to return
		# "break", so the event isn't propogated any further.
		import string
		try:
			auxVariable = string.find(string.digits + string.letters, event.keysym)
		except:
			auxVariable = (string.digits + string.ascii_letters).find(event.keysym)
		if -1 == auxVariable:
			# Didn't find it.  Check for special keys.
			if not (event.keysym in ( "BackSpace", "Tab", "underscore", "Left", "Right", "Home", "End" )):
				# It's not a special key.  Don't propogate
				# this event.
				return "break"


	def Ok(self):
		self.Apply()
		self.destroy()

	def Apply(self):
		# Set our name..
		self.pAI.SetName( self.sNameVar.get() )

		# Set our interruptable flag.
		self.pAI.bInterruptable = self.bInterruptable.get()

	def DeleteAI(self):
		print("Deleting " + self.pAI.GetName())
		self.pOutput.RemoveEntity(self.pAI)
		self.pAI = None
		self.destroy()

	def EditPostAIText(self):
		EditTextDialog(self, self.pAI.SetPostEntitySaveText, self.pAI.sPostEntitySaveText)

	def Copy(self):
		self.Apply()

		pCopy = self.pAI.CreateCopy()
		self.pAI.pOutput.AddEntityDirect(pCopy)

		self.destroy()

	def __del__(self):
		# Cleanup.
		self.destroy()



