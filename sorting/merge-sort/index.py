import unittest

# Merge Sort follows the rule of Divide and Conquer to sort a given set of numbers/elements, recursively, hence consuming less time.


# It is also called partition-exchange sort. This algorithm divides the list into three main parts:

# Elements less than the Pivot element
# Pivot element(Central element)
# Elements greater than the pivot element
# Pivot element can be any element from the array, it can be the first element, the last element or any random element. In this tutorial,
# we will take the rightmost element or the last element as pivot.

# 1. After selecting an element as pivot, which is the last index of the array in our case, we divide the array for the first time.
# 2. In quick sort, we call this partitioning. It is not simple breaking down of array into 2 subarrays,
# 	but in case of partitioning, the array elements are so positioned that all the elements smaller than the pivot will be
# 	on the left side of the pivot and all the elements greater than the pivot will be on the right side of it.
# 3. And the pivot element will be at its final sorted position.
# 4. The elements to the left and right, may not be sorted.
# 5. Then we pick subarrays, elements on the left of pivot and elements on the right of pivot,
# 	and we perform partitioning on them by choosing a pivot in the subarrays.

# Worst Case Time Complexity [ Big-O ]: O(n2)



def merge_sort(list):
	inner_merge_sort(list, 0, len(list) - 1)

def inner_merge_sort(list, head_index, tail_index):
	if (head_index < tail_index):
		mid_index = int((head_index + tail_index) / 2)
		inner_merge_sort(list, head_index, mid_index)
		inner_merge_sort(list, mid_index + 1, tail_index)
		merge(list, head_index, mid_index, tail_index)

def merge(list, head_index, mid_index, tail_index ):
	temp_array = [0] * len(list)
	temp_array_index = head_index

	front_index = head_index
	rear_index = mid_index + 1
		
	while temp_array_index < tail_index + 1:
		if (rear_index > tail_index) or ((list[front_index] < list[rear_index]) and (front_index < mid_index + 1)):
			temp_array[temp_array_index] = list[front_index]
			front_index += 1
		else:
			temp_array[temp_array_index] = list[rear_index]
			rear_index += 1
		temp_array_index += 1
	
	for index in range(head_index, tail_index + 1):
		list[index] = temp_array[index]



class Test(unittest.TestCase):
	def test1(self):
		list = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
		copy_list = list[:]

		merge_sort(list)
		copy_list.sort()
		self.assertEqual(list, copy_list)

if __name__ == '__main__':
	unittest.main()
