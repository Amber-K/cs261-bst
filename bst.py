class BinarySearchTree():

	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, insertee):
		if insertee.value <= self.value:
			if self.left == None:
				self.left = insertee
				return
			else:
				self.left.insert(insertee)
		if insertee.value > self.value:
			if self.right == None:
				self.right = insertee
			else:
				self.right.insert(insertee)

	def find(self, value):
		return self