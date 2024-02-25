"""
wild rift item value analyzer

takes item's
name, cost, effect

effect may be a list of objects?

Ex)
Amplifying Tome
500
[ability power ]

"""


class item:
	def __init__(self, name, cost, effect):
		self.name = name
		self.cost = cost
		self.effect = effect

