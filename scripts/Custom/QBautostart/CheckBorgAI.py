from Custom.QBautostart.Libs.LibEngineering import CreateInfoBox

s = """
Your Kobayashi Maru Installation detected a broken Borg AI.\n
\n
Please reinstall the AI files or contact support.
"""


def init():
	import AI.Compound.BorgAttack
	if hasattr(AI.Compound.BorgAttack, "BuilderCreate56"):
		# detected broken Borg AI
		CreateInfoBox(s)

