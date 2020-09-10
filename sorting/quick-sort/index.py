import unittest

# Quick Sort is also based on the concept of Divide and Conquer, just like merge sort.
# But in quick sort all the heavy lifting(major work) is done while dividing the array into subarrays,
# while in case of merge sort, all the real work happens during merging the subarrays. In case of quick sort,
# the combine step does absolutely nothing.

# It is also called partition-exchange sort. This algorithm divides the list into three main parts:
# 1. Elements less than the Pivot element
# 2. Pivot element(Central element)
# 3. Elements greater than the pivot element

# Pivot element can be any element from the array, it can be the first element, the last element or any random element. In this tutorial, we will take the rightmost element or the last element as pivot.



# Following are the steps involved in quick sort algorithm:

# 1. After selecting an element as pivot, which is the last index of the array in our case, we divide the array for the first time.
# 2. In quick sort, we call this partitioning. It is not simple breaking down of array into 2 subarrays, but in case of partitioning,
# 	the array elements are so positioned that all the elements smaller than the pivot will be on the left side of the pivot
# 	and all the elements greater than the pivot will be on the right side of it.
# 3. And the pivot element will be at its final sorted position.
# 4. The elements to the left and right, may not be sorted.
# 5. Then we pick subarrays, elements on the left of pivot and elements on the right of pivot,
# 	and we perform partitioning on them by choosing a pivot in the subarrays.



# Worst Case Time Complexity [ Big-O ]: O(n2)



def quick_sort(list):
	head_index = 0
	tail_index = len(list) - 1
	inner_quick_sort(list, head_index, tail_index)

def inner_quick_sort(list, head_index, tail_index):	
	if head_index < tail_index:
		partition_index = partition(list, head_index, tail_index)
		inner_quick_sort(list, head_index, partition_index - 1)
		inner_quick_sort(list, partition_index + 1, tail_index)
		return

def partition(list, head_index, tail_index):
	pivot_index = tail_index
	left = head_index
	right = tail_index - 1

	to_change_left_index = left
	to_change_right_index = right

	while True:
		while to_change_left_index < tail_index:
			if list[to_change_left_index] > list[pivot_index]:
				break
			to_change_left_index += 1
		while to_change_right_index > head_index:
			if list[to_change_right_index] < list[pivot_index]:
				break
			to_change_right_index -= 1

		if to_change_left_index < to_change_right_index:
			temp = list[to_change_right_index]
			list[to_change_right_index] = list[to_change_left_index]
			list[to_change_left_index] = temp
		else:
			temp = list[pivot_index]
			list[pivot_index] = list[to_change_left_index]
			list[to_change_left_index]= temp
			break

	return to_change_right_index + 1

class Test(unittest.TestCase):
	def test1(self):
		list = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
		copy_list = list[:]

		quick_sort(list)
		copy_list.sort()
		self.assertEqual(list, copy_list)

if __name__ == '__main__':
	unittest.main()
