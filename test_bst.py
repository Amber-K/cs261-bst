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

	def test_has_left_right_and_parent_initially_none(self):
		"""
		BST has left, right, and prev values that start out as None.
		"""
		bst = BinarySearchTree()
		self.assertEqual(None, bst.left)
		self.assertEqual(None, bst.right)
		self.assertEqual(None, bst.parent)

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
		equal_child = BinarySearchTree(100)
		large_child_1 = BinarySearchTree(110)
		large_child_2 = BinarySearchTree(130)
		large_child_3 = BinarySearchTree(120)
		bst.insert(small_child_1)
		bst.insert(small_child_2)
		bst.insert(small_child_3)
		bst.insert(equal_child)
		bst.insert(large_child_1)
		bst.insert(large_child_2)
		bst.insert(large_child_3)
		self.assertEqual(small_child_1, bst.left)
		self.assertEqual(small_child_2, small_child_1.right)
		self.assertEqual(small_child_3, small_child_1.left)
		self.assertEqual(equal_child, small_child_2.right)
		self.assertEqual(large_child_1, bst.right)
		self.assertEqual(large_child_2, large_child_1.right)
		self.assertEqual(large_child_3, large_child_2.left)

	def test_insertee_has_parent_matching_previous_node(self):
		"""
		When inserted, a node's parent value becomes the node before it.
		"""
		bst = BinarySearchTree(100)
		child_1 = BinarySearchTree(20)
		child_2 = BinarySearchTree(30)
		child_3 = BinarySearchTree(10)
		bst.insert(child_1)
		bst.insert(child_2)
		bst.insert(child_3)
		self.assertEqual(bst, child_1.parent)
		self.assertEqual(child_1, child_2.parent)
		self.assertEqual(child_1, child_3.parent)

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

	def test_find_node_at_complex_location(self):
		"""
		Nodes can be found in complicated locations.
		"""
		bst = BinarySearchTree(100)
		child_1 = BinarySearchTree(10)
		child_2 = BinarySearchTree(130)
		child_3 = BinarySearchTree(110)
		child_4 = BinarySearchTree(120)
		bst.insert(child_1)
		bst.insert(child_2)
		bst.insert(child_3)
		bst.insert(child_4)
		self.assertEqual(child_3, bst.find(110))

	def test_find_value_without_node(self):
		"""
		None is returned when no node has the correct value.
		"""
		bst = BinarySearchTree(100)
		self.assertEqual(None, bst.find(50))
		self.assertEqual(None, bst.find(150))

	"""
	Traversal
	"""

	def test_pre_order_traversal(self):
		"""
		Pre-order traversals return lists of BST values in pre-order.
		"""
		bst = BinarySearchTree(100)
		small_child_1 = BinarySearchTree(20)
		small_child_2 = BinarySearchTree(30)
		small_child_3 = BinarySearchTree(10)
		large_child_1 = BinarySearchTree(110)
		large_child_2 = BinarySearchTree(130)
		large_child_3 = BinarySearchTree(120)
		bst.insert(small_child_1)
		bst.insert(small_child_2)
		bst.insert(small_child_3)
		bst.insert(large_child_1)
		bst.insert(large_child_2)
		bst.insert(large_child_3)
		self.assertEqual([100, 20, 10, 30, 110, 130, 120], bst.traverse_pre_order())

	def test_in_order_traversal(self):
		"""
		In-order traversals return lists of BST values in-order.
		"""
		bst = BinarySearchTree(100)
		small_child_1 = BinarySearchTree(20)
		small_child_2 = BinarySearchTree(30)
		small_child_3 = BinarySearchTree(10)
		large_child_1 = BinarySearchTree(110)
		large_child_2 = BinarySearchTree(130)
		large_child_3 = BinarySearchTree(120)
		bst.insert(small_child_1)
		bst.insert(small_child_2)
		bst.insert(small_child_3)
		bst.insert(large_child_1)
		bst.insert(large_child_2)
		bst.insert(large_child_3)
		self.assertEqual([10, 20, 30, 100, 110, 120, 130], bst.traverse_in_order())

	def test_post_order_traversal(self):
		"""
		Post-order traversals return lists of BST values in post-order.
		"""
		bst = BinarySearchTree(100)
		small_child_1 = BinarySearchTree(20)
		small_child_2 = BinarySearchTree(30)
		small_child_3 = BinarySearchTree(10)
		large_child_1 = BinarySearchTree(110)
		large_child_2 = BinarySearchTree(130)
		large_child_3 = BinarySearchTree(120)
		bst.insert(small_child_1)
		bst.insert(small_child_2)
		bst.insert(small_child_3)
		bst.insert(large_child_1)
		bst.insert(large_child_2)
		bst.insert(large_child_3)
		self.assertEqual([10, 30, 20, 120, 130, 110, 100], bst.traverse_post_order())

	"""
	Deletion
	"""

	def test_delete_leaf_node(self):
		"""
		Delete removes leaf nodes correctly.
		"""
		bst = BinarySearchTree(100)
		small_child_1 = BinarySearchTree(20)
		small_child_2 = BinarySearchTree(10)
		equal_child = BinarySearchTree(100)
		large_child = BinarySearchTree(150)
		bst.insert(small_child_1)
		bst.insert(small_child_2)
		bst.insert(equal_child)
		bst.insert(large_child)
		bst.delete(small_child_2)
		bst.delete(equal_child)
		bst.delete(large_child)
		self.assertEqual(small_child_1, bst.left)
		self.assertEqual(None, small_child_1.left)
		self.assertEqual(None, small_child_1.right)
		self.assertEqual(None, bst.right)

	def test_delete_node_with_single_child(self):
		"""
		Delete removes nodes with single children correctly.
		"""
		bst = BinarySearchTree(100)
		small_child = BinarySearchTree(50)
		equal_child = BinarySearchTree(100)
		large_child_1 = BinarySearchTree(110)
		large_child_2 = BinarySearchTree(120)
		bst.insert(small_child)
		bst.insert(equal_child)
		bst.insert(large_child_1)
		bst.insert(large_child_2)
		bst.delete(small_child)
		bst.delete(large_child_1)
		self.assertEqual(equal_child, bst.left)
		self.assertEqual(bst, equal_child.parent)
		self.assertEqual(large_child_2, bst.right)
		self.assertEqual(bst, large_child_2.parent)

	def test_delete_node_with_two_children(self):
		"""
		Delete removes nodes with two children correctly.
		"""
		bst = BinarySearchTree(100)
		small_child_1 = BinarySearchTree(20)
		small_child_2 = BinarySearchTree(10)
		small_child_3 = BinarySearchTree(30)
		large_child_1 = BinarySearchTree(120)
		large_child_2 = BinarySearchTree(110)
		large_child_3 = BinarySearchTree(130)
		large_child_4 = BinarySearchTree(122)
		large_child_5 = BinarySearchTree(123)
		bst.insert(small_child_1)
		bst.insert(small_child_2)
		bst.insert(small_child_3)
		bst.insert(large_child_1)
		bst.insert(large_child_2)
		bst.insert(large_child_3)
		bst.insert(large_child_4)
		bst.insert(large_child_5)
		bst.delete(small_child_1)
		bst.delete(large_child_1)
		self.assertEqual(bst, small_child_3.parent)
		self.assertEqual(small_child_3, bst.left)

		self.assertEqual(small_child_3, small_child_2.parent)
		self.assertEqual(small_child_2, small_child_3.left)
		
		self.assertEqual(bst, large_child_4.parent)
		self.assertEqual(large_child_4, bst.right)

		self.assertEqual(large_child_4, large_child_2.parent)
		self.assertEqual(large_child_2, large_child_4.left)

		self.assertEqual(large_child_4, large_child_3.parent)
		self.assertEqual(large_child_3, large_child_4.right)

		self.assertEqual(large_child_3, large_child_5.parent)
		self.assertEqual(large_child_5, large_child_3.left)


if __name__ == '__main__':
	unittest.main()