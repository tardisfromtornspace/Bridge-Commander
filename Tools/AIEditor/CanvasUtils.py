sNextUniqueTagBase = "Tag"
iNextUniqueTagNumber = 0

def GetUniqueTagName():
	"Get a unique tag name."
	global sNextUniqueTagBase, iNextUniqueTagNumber

	sTag = sNextUniqueTagBase + str(iNextUniqueTagNumber)
	iNextUniqueTagNumber = iNextUniqueTagNumber + 1

	return sTag

class DraggableCanvasIcon:
	"""An icon that can be added to a Canvas.  It knows how to
	draw itself on the canvas, and knows how to drag itself around."""
	def __init__(self, parent, posX = 50, posY = 50):
		# Setup basic variables.
		self.pParent = parent
		self.vPos = (posX, posY)
		self.vLastDragPos = None

		# We need to get a unique tag name for our graphics.
		self.sTag = GetUniqueTagName()

		# Create our graphics, because they don't exist yet.
		# Actually, we shouldn't call this here.  Inherited
		# classes need to do it on their own.
		#self.CreateGraphics()

		# Done for now.

	def __del__(self):
		# Cleanup.  Delete anything from the canvas that's
		# associated with our tag..
		self.pParent.delete(self.sTag)

	def GetMainTag(self):
		return self.sTag
	
	def CreateGraphics(self):
		"""Create our graphics, and make sure everything we make
		that we want to be moved automatically has the self.sTag
		tag."""
		# We're an abstract parent class.  We do nothing.
		pass

	def Redraw(self):
		"""Refresh any graphics that aren't automatically refreshed
		by the parent class (any graphics bits that aren't associated
		with our main tag."""
		# We're an abstract parent class.  We do nothing.
		pass

	def MoveTo(self, iXPos, iYPos):
		"Move ourselves to the specified position."
		# Find the difference between our current position and the
		# new position.
		vDiff = (iXPos - self.vPos[0], iYPos - self.vPos[1])
		
		# Set our new position
		self.vPos = (iXPos, iYPos)
		
		# Move our graphics, based on our tag.
		self.pParent.move(self.sTag, vDiff[0], vDiff[1])
		
		# Refresh our graphics, for anything that doesn't move
		# with our tag.
		self.Redraw()

	def DragButtonDown(self, event):
		"""Whatever the drag button is, it's been clicked on us.
		Start dragging ourselves."""
		self.vLastDragPos = (event.x, event.y)
		self.pParent.grab_set()

	def DragButtonDragged(self, event):
		"""Drag button is down while the cursor is being
		dragged along...  Drag our graphics around."""
		assert(self.vLastDragPos)

		vDiff = (event.x - self.vLastDragPos[0], event.y - self.vLastDragPos[1])
		self.MoveTo(self.vPos[0] + vDiff[0], self.vPos[1] + vDiff[1])
		self.vLastDragPos = (event.x, event.y)

	def DragButtonUp(self, event):
		"""Drag button has been released.  Stop dragging."""
		self.vLastDragPos = None
		self.pCanvas.grab_release()

