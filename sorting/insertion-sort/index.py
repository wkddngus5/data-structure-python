import unittest

# Consider you have 10 cards out of a deck of cards in your hand. And they are sorted, or arranged in the ascending order of their numbers.
# If I give you another card, and ask you to insert the card in just the right position, so that the cards in your hand are still sorted. What will you do?
# Well, you will have to go through each card from the starting or the back and find the right position for the new card, comparing it's value with each card. Once you find the right position, you will insert the card there.
# Similarly, if more new cards are provided to you, you can easily repeat the same process and insert the new cards and keep the cards sorted too.
# This is exactly how insertion sort works. It starts from the index 1(not 0), and each index starting from index 1 is like a new card, that you have to place at the right position in the sorted subarray on the left.

# Following are some of the important characteristics of Insertion Sort:

# It is efficient for smaller data sets, but very inefficient for larger lists.
# Insertion Sort is adaptive, that means it reduces its total number of steps if a partially sorted array is provided as input, making it efficient.
# It is better than Selection Sort and Bubble Sort algorithms.
# Its space complexity is less. Like bubble Sort, insertion sort also requires a single additional memory space.
# It is a stable sorting technique, as it does not change the relative order of elements which are equal.




# Following are the steps involved in insertion sort:

# 1. We start by making the second element of the given array, i.e. element at index 1, the key.
# The key element here is the new card that we need to add to our existing sorted set of cards(remember the example with cards above).
# 
# 2. We compare the key element with the element(s) before it, in this case, element at index 0:
# 	If the key element is less than the first element, we insert the key element before the first element.
# 	If the key element is greater than the first element, then we insert it after the first element.
# 3. Then, we make the third element of the array as key and will compare it with elements to it's left and insert it at the right position.
# 4. And we go on repeating this, until the array is sorted.


# Worst Case Time Complexity [ Big-O ]: O(n2)



def insertion_sort(list):
	for index in range(1, len(list)):
		index2 = index
		while (index2 > 0) & (list[index2 - 1] > list[index2]):
			temp = list[index2]
			list[index2] = list[index2 - 1]
			list[index2 - 1] = temp
			index2 -= 1


class Test(unittest.TestCase):
	def test1(self):
		list = [5, 1, 6, 2, 4, 3]
		copy_list = list[:]

		insertion_sort(list)
		copy_list.sort()
		self.assertEqual(list, copy_list)
	
if __name__ == '__main__':
	unittest.main()