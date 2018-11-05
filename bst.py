class BinarySearchTree():

	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None

	def insert(self, insertee):
		if insertee.value <= self.value:
			if self.left == None:
				self.left = insertee
				insertee.parent = self
				return
			else:
				return self.left.insert(insertee)
		if insertee.value > self.value:
			if self.right == None:
				self.right = insertee
				insertee.parent = self
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

	def traverse_pre_order(self, values = []):
		values.append(self.value)
		if self.left != None:
			values = self.left.traverse_pre_order(values)
		if self.right != None:
			values = self.right.traverse_pre_order(values)
		return values

	def traverse_in_order(self, values = []):
		if self.left != None:
			values = self.left.traverse_in_order(values)
		values.append(self.value)
		if self.right != None:
			values = self.right.traverse_in_order(values)
		return values