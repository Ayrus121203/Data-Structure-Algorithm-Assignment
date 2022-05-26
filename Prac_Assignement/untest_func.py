# Python program for implementation of Bubble Sort
# def bubbleSort(arr):
# 	n = len(arr)

	# Traverse through all array elements
	# for i in range(n):

		# Last i elements are already in place
		# for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			# if arr[j] > arr[j+1]:
			# 	arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# bubbleSort(arr)
#
# print("Sorted array is:")
# for i in range(len(arr)):
# 	print("%d" % arr[i], end=" ")



# Python Program for implementation of
# Recursive Bubble sort
# class recursive_bubbleSort:
# 	"""
# 	bubbleSort:
# 		function:
# 			bubbleSortRecursive : recursive
# 				function to sort array
# 			__str__ : format print of array
# 			__init__ : constructor
# 				function in python
# 		variables:
# 			self.array = contains array
# 			self.length = length of array
# 	"""

	# def __init__(self, array):
	# 	self.array = array
	# 	self.length = len(array)
	#
	# def __str__(self):
	# 	return " ".join([str(x)
	# 					for x in self.array])
	#
	# def bubbleSortRecursive(self, n=None):
	# 	if n is None:
	# 		n = self.length
	#
	# 	# Base case
	# 	if n == 1:
	# 		return

# 		# One pass of bubble sort. After
# 		# this pass, the largest element
# 		# is moved (or bubbled) to end.
# 		for i in range(n - 1):
# 			if self.array[i] > self.array[i + 1]:
# 				self.array[i], self.array[i +
# 				1] = self.array[i + 1], self.array[i]
#
# 		# Largest element is fixed,
# 		# recur for remaining array
# 		self.bubbleSortRecursive(n - 1)
#
# # Driver Code
# def main():
# 	array = [64, 34, 25, 12, 22, 11, 90]
#
# 	# Creating object for class
# 	sort = bubbleSort(array)
#
# 	# Sorting array
# 	sort.bubbleSortRecursive()
# 	print("Sorted array :\n", sort)
#
#
# if __name__ == "__main__":
# 	main()
#
# # Code contributed by Mohit Gupta_OMG,
# # improved by itsvinayak



#OR
# # Python program for counting sort
#
# # The main function that sort the given string arr[] in
# # alphabetical order
# def countSort(arr):
#
# 	# The output character array that will have sorted arr
# 	output = [0 for i in range(len(arr))]
#
# 	# Create a count array to store count of individual
# 	# characters and initialize count array as 0
# 	count = [0 for i in range(256)]
#
# 	# For storing the resulting answer since the
# 	# string is immutable
# 	ans = ["" for _ in arr]
#
# 	# Store count of each character
# 	for i in arr:
# 		count[ord(i)] += 1
#
# 	# Change count[i] so that count[i] now contains actual
# 	# position of this character in output array
# 	for i in range(256):
# 		count[i] += count[i-1]
#
# 	# Build the output character array
# 	for i in range(len(arr)):
# 		output[count[ord(arr[i])]-1] = arr[i]
# 		count[ord(arr[i])] -= 1
#
# 	# Copy the output array to arr, so that arr now
# 	# contains sorted characters
# 	for i in range(len(arr)):
# 		ans[i] = output[i]
# 	return ans
#
# # Driver program to test above function
# arr = "geeksforgeeks"
# ans = countSort(arr)
# print("Sorted character array is % s" %("".join(ans)))
#
# # This code is contributed by Nikhil Kumar Singh
