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

if __name__ == '__main__':
	unittest.main()