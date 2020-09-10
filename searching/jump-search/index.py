import unittest
import math

# Study tonight

# Jump Search Algorithm is a relatively new algorithm for searching an element in a sorted array.

# The fundamental idea behind this searching technique is to search fewer number of elements compared to linear search algorithm (which scans every element in the array to check if it matches with the element being searched or not). This can be done by skipping some fixed number of array elements or jumping ahead by fixed number of steps in every iteration.

# Lets consider a sorted array A[] of size n, with indexing ranging between 0 and n-1, and element x that needs to be searched in the array A[]. For implementing this algorithm, a block of size m is also required, that can be skipped or jumped in every iteration. Thus, the algorithm works as follows:

# Iteration 1: if (x==A[0]), then success, else, if (x > A[0]), then jump to the next block.
# Iteration 2: if (x==A[m]), then success, else, if (x > A[m]), then jump to the next block.
# Iteration 3: if (x==A[2m]), then success, else, if (x > A[2m]), then jump to the next block.
# At any point in time, if (x < A[km]), then a linear search is performed from index A[(k-1)m] to A[km]


def linear_search(list, target):
	# step 1
	for index in range(len(list)):
		# step 2
		if list[index] == target:
			return index
	# step 3
	return -1

def jump_search(list, target):
	block_size = int(math.sqrt(len(list)))
	index = 0
	while(list[index] < target):
		if (list[index] == target):
			return index
		index += block_size
		if ( index >= len(list)):
			break
		

	block_index = linear_search(list[index - block_size:index], target)
	if (block_index == -1):
		return -1
	return index - block_size + block_index



class Test(unittest.TestCase):
	def test1(self):
		list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 55, 77, 89, 101, 201, 256, 780]
		target = 77 
		self.assertEqual(jump_search(list, target), 10)

	def test2(self):
		list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 55, 77, 89, 101, 201, 256, 780]
		target = 200
		self.assertEqual(jump_search(list, target), -1)

	def test3(self):
		list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 55, 77, 89, 101, 201, 256, 780]
		target = 900
		self.assertEqual(jump_search(list, target), -1)

if __name__ == '__main__':
	unittest.main()