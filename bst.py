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

	def traverse_post_order(self, values = []):
		if self.left != None:
			values = self.left.traverse_post_order(values)
		if self.right != None:
			values = self.right.traverse_post_order(values)
		values.append(self.value)
		return values

	def delete(self, target_node):
		# replacement_node = None

		# if target_node.right != None or target_node.left != None:
		# 	if target_node.right != None:
		# 		replacement_node = target_node.right
		# 		while(replacement_node.left != None):
		# 			replacement_node = replacement_node.left	

		# 		if replacement_node.right != None:
		# 			target_node.right.parent = target_node.parent
		# 			target_node.parent.left = target_node.right
		# 			replacement_node.right = target_node.right
		# 		else:
		# 			target_node.parent.left = replacement_node

		# 	else:
		# 		replacement_node = target_node.left
		# 		while(replacement_node.right != None):
		# 			replacement_node = replacement_node.right

		# 		if replacement_node.left != None:
		# 			target_node.left.parent = target_node.parent
		# 			target_node.parent.right = target_node.left
		# 			replacement_node.left = target_node.left
		# 		else:
		# 			target_node.parent.right = replacement_node

		# 	replacement_node.parent = target_node.parent

		# else:
		# 	if target_node.value <= target_node.parent.value:
		# 		target_node.parent.left = None
		# 	else:
		# 		target_node.parent.right = None
		
		







		# if replacement_node.right != None:
		# 	replacement_node.right.parent = replacement_node.parent
		# 	replacement_node.parent.left = replacement_node.right
		
		

		# if target_node.value <= target_node.parent.value:
		# 	target_node.parent.left = replacement_node
		# else:
		# 	target_node.parent.right = replacement_node

		# if target_node.left != None:
		# 	target_node.left.parent = replacement_node
		# if target_node.right != None:
		# 	target_node.right.parent = replacement_node

		"""
		OLD
		"""

		if target_node.left == None and target_node.right == None:
			if target_node.value < target_node.parent.value:
				target_node.parent.left = None
			else:
				target_node.parent.right = None

		elif (target_node.left != None and target_node.right == None) or (target_node.left == None and target_node.right != None):
			if target_node.value <= target_node.parent.value:
				if target_node.left != None and target_node.right == None:
					target_node.left.parent = target_node.parent
					target_node.parent.left = target_node.left
				elif target_node.left == None and target_node.right != None:
					target_node.right.parent = target_node.parent
					target_node.parent.left = target_node.right
		
			else:
				if target_node.left != None and target_node.right == None:
					target_node.left.parent = target_node.parent
					target_node.parent.right = target_node.left
				elif target_node.left == None and target_node.right != None:
					target_node.right.parent = target_node.parent
					target_node.parent.right = target_node.right

		else:
			replacement_node = None
			replacement_node = target_node.right
			while(replacement_node.left != None):
				replacement_node = replacement_node.left

			if replacement_node.right != None:
				replacement_node.right.parent = replacement_node.parent
				replacement_node.parent.left = replacement_node.right

			if replacement_node != target_node.right:
				replacement_node.right = target_node.right
				target_node.right.parent = replacement_node

			replacement_node.left = target_node.left
			target_node.left.parent = replacement_node

			replacement_node.parent = target_node.parent
			if target_node.value <= target_node.parent.value:
				target_node.parent.left = replacement_node
			else:
				target_node.parent.right = replacement_node
