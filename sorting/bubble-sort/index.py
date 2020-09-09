import unittest

# Bubble Sort is a simple algorithm which is used to sort a given set of n elements provided in form of an array with n number of elements.
# Bubble Sort compares all the element one by one and sort them based on their values.

# If the given array has to be sorted in ascending order,
# then bubble sort will start by comparing the first element of the array with the second element,
# if the first element is greater than the second element, it will swap both the elements,
# and then move on to compare the second and the third element, and so on.

# If we have total n elements, then we need to repeat this process for n-1 times.

# It is known as bubble sort, because with every complete iteration the largest element in the given array,
# bubbles up towards the last place or the highest index, just like a water bubble rises up to the water surface.

# Sorting takes place by stepping through all the elements one-by-one and comparing it with the adjacent element and swapping them if required.



# Following are the steps involved in bubble sort(for sorting a given array in ascending order):

# 1. Starting with the first element(index = 0), compare the current element with the next element of the array.
# 2. If the current element is greater than the next element of the array, swap them.
# 3. If the current element is less than the next element, move to the next element. Repeat Step 1.



# Worst Case Time Complexity [ Big-O ]: O(n2)



def bubble_sort(list):
	for index2 in range(len(list) - 1):
		for index in range(len(list) - index2 - 1):
			if list[index] > list[index + 1]:
				temp = list[index + 1]
				list[index + 1] = list[index]
				list[index] = temp

def optimized_bubble_sort(list):
	flag = False
	for index2 in range(len(list) - 1):
		for index in range(len(list) - index2 - 1):
			if list[index] > list[index + 1]:
				flag = True
				temp = list[index + 1]
				list[index + 1] = list[index]
				list[index] = temp

		if flag == False:
			break


class Test(unittest.TestCase):
	def test1(self):
		list = [5, 1, 6, 2, 4, 3]
		copy_list = list[:]

		bubble_sort(list)
		copy_list.sort()
		self.assertEqual(list, copy_list)

	def test2(self):
		list = [5, 1, 6, 2, 4, 3]
		copy_list = list[:]

		optimized_bubble_sort(list)
		copy_list.sort()
		self.assertEqual(list, copy_list)
	
if __name__ == '__main__':
	unittest.main()