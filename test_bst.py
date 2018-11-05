# Run me with `python -m unittest test_bst`

import unittest
from bst import BinarySearchTree

class TestTree(unittest.TestCase):

	"""
	Initialization
	"""

	def test_instantiation(self):
		"""
		A BinarySearchTree exists.
		"""
		try:
			BinarySearchTree()
		except NameError:
			self.fail("Could not instantiate BinarySearchTree.")

	def test_instantiation_with_value(self):
		"""
		A BST can be instantiated with a value.
		"""
		fake_value = "FAKE"
		bst = BinarySearchTree(fake_value)
		self.assertEqual(fake_value, bst.value)

	def test_has_left_and_right_initially_none(self):
		"""
		BST has left and right values that start out as None.
		"""
		bst = BinarySearchTree()
		self.assertEqual(None, bst.left)
		self.assertEqual(None, bst.right)

	"""
	Insertion
	"""

	def test_insert_smaller_values_as_left(self):
		"""
		Child nodes smaller than the root are inserted on the left.
		"""
		bst = BinarySearchTree(100)
		child = BinarySearchTree(50)
		bst.insert(child)
		self.assertEqual(child, bst.left)

	def test_insert_larger_values_as_right(self):
		"""
		Child nodes larger than the root are inserted on the right.
		"""
		bst = BinarySearchTree(100)
		child = BinarySearchTree(150)
		bst.insert(child)
		self.assertEqual(child, bst.right)

if __name__ == '__main__':
	unittest.main()