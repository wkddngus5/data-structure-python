import unittest

# Selection sort is conceptually the most simplest sorting algorithm.
# This algorithm will first find the smallest element in the array and swap it with the element in the first position,
# then it will find the second smallest element and swap it with the element in the second position,
# and it will keep on doing this until the entire array is sorted.

# It is called selection sort because it repeatedly selects the next-smallest element and swaps it into the right place.



# Following are the steps involved in selection sort(for sorting a given array in ascending order):

# 1. Starting from the first element, we search the smallest element in the array, and replace it with the element in the first position.
# 2. We then move on to the second position, and look for smallest element present in the subarray, starting from index 1, till the last index.
# 3. We replace the element at the second position in the original array, or we can say at the first position in the subarray, with the second smallest element.
# 4. This is repeated, until the array is completely sorted.



# Worst Case Time Complexity [ Big-O ]: O(n2)



def selection_sort(list):
	for index in range(len(list)):
		smallest_index = index
		for index2 in range(index + 1, len(list)):
			smallest_index = smallest_index if list[smallest_index] < list[index2] else index2
		if smallest_index != index:
			temp = list[smallest_index]
			list[smallest_index] = list[index]
			list[index] = temp

class Test(unittest.TestCase):
	def test1(self):
		list = [5, 1, 6, 2, 4, 3]
		copy_list = list[:]

		selection_sort(list)
		copy_list.sort()
		self.assertEqual(list, copy_list)

if __name__ == '__main__':
	unittest.main()
