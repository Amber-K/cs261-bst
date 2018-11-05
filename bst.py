class BinarySearchTree():

	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, insertee):
		self.left = insertee
		self.right = insertee