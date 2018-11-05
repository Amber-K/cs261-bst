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
				return self.left.insert(insertee)
		if insertee.value > self.value:
			if self.right == None:
				self.right = insertee
				return
			else:
				return self.right.insert(insertee)

	def find(self, value):
		if value == self.value:
			return self
		elif value < self.value:
			if self.left == None:
				return None
			else:
				return self.left.find(value)
		else:
			if self.right == None:
				return None
			else:
				return self.right.find(value)