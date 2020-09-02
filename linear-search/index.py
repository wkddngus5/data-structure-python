import unittest

# Study tonight

# Linear search is a very basic and simple search algorithm.
# In Linear search, we search an element or value in a given array by traversing the array from the starting,
# till the desired element or value is found.

# As we learned in the previous tutorial that the time complexity of Linear search algorithm is O(n),
# we will analyse the same and see why it is O(n) after implementing it.



# Following are the steps of implementation that we will be following:

# 1. Traverse the array using a for loop.
# 2. In every iteration, compare the target value with the current value of the array.
# 	If the values match, return the current index of the array.
# 	If the values do not match, move on to the next array element.
# 3. If no match is found, return -1.

# To search the number 5 in the array given below,
# linear search will go step by step in a sequential order starting from the first element in the given array.


def linear_search(list, target):
	# step 1
	for index in range(len(list)):
		# step 2
		if list[index] == target:
			return index
	# step 3
	return -1

class Test(unittest.TestCase):
	def test1(self):
		list = [5, 34, 65, 12, 77, 35]
		target = 77
		self.assertEqual(linear_search(list, target), 4)

	def test2(self):
		list = [101, 392, 1, 54, 32, 22, 90, 93]
		target = 200
		self.assertEqual(linear_search(list, target), -1)

if __name__ == '__main__':
	unittest.main()
