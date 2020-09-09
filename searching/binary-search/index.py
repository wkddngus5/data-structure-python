import unittest

# Study tonight

# Binary Search is applied on the sorted array or list of large size.
# It's time complexity of O(log n) makes it very fast as compared to other sorting algorithms.
# The only limitation is that the array or list of elements must be sorted for the binary search algorithm to work on it.



# Following are the steps of implementation that we will be following:

# 1. Start with the middle element:
# 	If the target value is equal to the middle element of the array, then return the index of the middle element.
# 	If not, then compare the middle element with the target value,
# 		If the target value is greater than the number in the middle index, then pick the elements to the right of the middle index, and start with Step 1.
# 		If the target value is less than the number in the middle index, then pick the elements to the left of the middle index, and start with Step 1.
# 2. When a match is found, return the index of the element matched.
# 3. If no match is found, then return -1


def binary_search(list, target):
	list_length = len(list)

	head_index = 0
	tail_index = list_length - 1

	# step 1
	while (head_index <= tail_index):
		middle_index = int((head_index + tail_index) / 2)
		if (list[middle_index] > target):
			tail_index = middle_index -1
			continue
		if (list[middle_index] < target):
			head_index = middle_index + 1
			continue
		# step 2
		return middle_index
	# step 3
	return -1

class Test(unittest.TestCase):
	def test1(self):
		list = [13, 21, 54, 81, 90]
		target = 81
		self.assertEqual(binary_search(list, target), 3)

	def test2(self):
		list = [13, 21, 54, 81, 90]
		target = 200
		self.assertEqual(binary_search(list, target), -1)

if __name__ == '__main__':
	unittest.main()
