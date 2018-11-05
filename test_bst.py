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

if __name__ == '__main__':
	unittest.main()