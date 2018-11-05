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

	def test_insert_many_small_large_and_equal_values_in_correct_locations(self):
		"""
		Many inserted nodes all end up in correct locations.
		"""
		bst = BinarySearchTree(100)
		small_child_1 = BinarySearchTree(20)
		small_child_2 = BinarySearchTree(30)
		small_child_3 = BinarySearchTree(10)
		large_child_1 = BinarySearchTree(110)
		large_child_2 = BinarySearchTree(130)
		large_child_3 = BinarySearchTree(120)
		equal_child = BinarySearchTree(100)
		bst.insert(small_child_1)
		bst.insert(small_child_2)
		bst.insert(small_child_3)
		bst.insert(large_child_1)
		bst.insert(large_child_2)
		bst.insert(large_child_3)
		bst.insert(equal_child)
		self.assertEqual(small_child_1, bst.left)
		self.assertEqual(small_child_2, small_child_1.right)
		self.assertEqual(small_child_3, small_child_1.left)
		self.assertEqual(large_child_1, bst.right)
		self.assertEqual(large_child_2, large_child_1.right)
		self.assertEqual(large_child_3, large_child_2.left)
		self.assertEqual(equal_child, small_child_2.right)

	"""
	Finding
	"""

	def test_find_root_value_returns_root(self):
		"""
		Using find for root's value returns the root.
		"""
		bst = BinarySearchTree(100)
		self.assertEqual(bst, bst.find(100))

	def test_find_smallest_leaf_node(self):
		"""
		The smallest leaf node can be found.
		"""
		bst = BinarySearchTree(100)
		child_1 = BinarySearchTree(20)
		child_2 = BinarySearchTree(10)
		child_3 = BinarySearchTree(150)
		bst.insert(child_1)
		bst.insert(child_2)
		bst.insert(child_3)
		self.assertEqual(child_2, bst.find(10))

	def test_find_largest_leaf_node(self):
		"""
		The largest leaf node can be found.
		"""
		bst = BinarySearchTree(100)
		child_1 = BinarySearchTree(110)
		child_2 = BinarySearchTree(120)
		child_3 = BinarySearchTree(50)
		bst.insert(child_1)
		bst.insert(child_2)
		bst.insert(child_3)
		self.assertEqual(child_2, bst.find(120))

if __name__ == '__main__':
	unittest.main()