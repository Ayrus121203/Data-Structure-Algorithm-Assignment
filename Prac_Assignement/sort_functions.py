staycation_booking_details_dict =[
    {"customer_name": "Bill", "package_name": "Sentosa", "cost": 200, "pax": 20},
 {"customer_name": "Amos", "package_name": "Riverside", "cost": 100, "pax": 30},
  {"customer_name": "Tan", "package_name": "Sea", "cost": 50, "pax": 7},
   {"customer_name": "Beverly", "package_name": "Wind", "cost": 900, "pax": 3},
    {"customer_name": "Theresa", "package_name": "Rock", "cost": 300, "pax": 29},
     {"customer_name": "Ellen", "package_name": "Fire", "cost": 200, "pax": 17},
      {"customer_name": "Hollow", "package_name": "Air", "cost": 190, "pax": 23},
       {"customer_name": "Bill", "package_name": "Ocean", "cost": 400, "pax": 28},
        {"customer_name": "Jane", "package_name": "Atlantic", "cost": 700, "pax": 10},
         {"customer_name": "Koen", "package_name": "Towers", "cost": 100, "pax": 36}
    ]


def bubbleSort(theSeq):

	n = len(theSeq)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if theSeq[j]["customer_name"] > theSeq[j+1]["customer_name"]:
				theSeq[j], theSeq[j+1] = theSeq[j+1], theSeq[j]


def bubbleSort_optimized(theSeq):

	n = len(theSeq)

	# Perform n-1 bubble operations on the sequence
	passCount = 0
	for i in range(n - 1, 0, -1):
		# Set boolean variable to check occurrence of swapping
		# in inner loop
		swapFlag = False

		# Bubble the largest item to the end
		for j in range(i):
			if (theSeq[j]["customer_name"] > theSeq[j + 1]["customer_name"]):
				# Swap the j and j+1 items
				# tmp = theSeq[j]
				# theSeq[j] = theSeq[j + 1]
				# theSeq[j + 1] = tmp
				theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]

				# Set boolean variable value if swapping occurred
				swapFlag = True

		#passCount += 1   #enable this code to see num of passes made
		#print(passCount)
		# Exit the loop if no swapping occurred
		# in the previous pass
		if (not swapFlag):
			break


# Python Program for implementation of
# Recursive Bubble sort
def bubbleSortRecursive(theSeq):
	n = len(theSeq)


	# Base case
	if n == 1:
		return

	# One pass of bubble sort. After
	# this pass, the largest element
	# is moved (or bubbled) to end.
	for i in range(n - 1):
		if theSeq[i]["customer_name"] > theSeq[i + 1]["customer_name"]:
			theSeq[i], theSeq[i +1] = theSeq[i + 1], theSeq[i]

	# Largest element is fixed,
	# recur for remaining array
	return (n - 1)


def selection_sort(theSeq):
	n = len(theSeq)
	for i in range(n - 1):
		current_index = i
		for j in range(i+1, n):
			if theSeq[j]["package_name"] < theSeq[current_index]["package_name"]:
				current_index = j

		if current_index != i:
			tmp = theSeq[i]
			theSeq[i] = theSeq[current_index]
			theSeq[current_index] = tmp


def insertion_sort(theSeq):
	print('Staycation booking will now be sorted using Insertion Sort')

	n = len(theSeq)

	for i in range(1,n):
		val = theSeq[i]
		pos = i
		while pos > 0 and val["cost"] < theSeq[pos - 1]["cost"]:
			theSeq[pos] = theSeq[pos - 1]
			pos -= 1

			theSeq[pos] = val

def linear_search(value, target):
	print('Staycation booking will now be searched using Linear Search')
	n = len(value)

	for i in range(n):
		if value[i]["customer_name"] == target or value[i]["customer_name"] != target:
			return value[i]
	return False


# Python3 program for implementation of Shell Sort
# Python3 program for implementation of Shell Sort
def shellSort(theSeq):
	# code here
	n = len(theSeq)
	gap=n//2


	while gap>0:
		j=gap
		# Check the array in from left to right
		# Till the last possible index of j
		while j<n:
			i=j-gap # This will keep help in maintain gap value

			while i>=0:
				# If value on right side is already greater than left side value
				# We don't do swap else we swap
				if theSeq[i+gap]["customer_name"] > theSeq[i]["customer_name"]:

					break
				else:
					theSeq[i+gap],theSeq[i]=theSeq[i],theSeq[i+gap]

				i=i-gap # To check left side also
							# If the element present is greater than current element
			j+=1
		gap=gap//2


# This code is contributed by Illion


# Python3 program to
# sort array using
# pancake sort

# Reverses arr[0..i] */
def flip(arr, i):
	start = 0
	while start < i:
		temp = arr[start]
		arr[start] = arr[i]
		arr[i] = temp
		start += 1
		i -= 1

# Returns index of the maximum
# element in arr[0..n-1] */
def findMax(arr, n):
	mi = 0
	for i in range(0,n):
		if arr[i]["package_name"] > arr[mi]["package_name"]:
			mi = i
	return mi

# The main function that
# sorts given array
# using flip operations
def pancakeSort(arr, n):

	# Start from the complete
	# array and one by one
	# reduce current size
	# by one
	curr_size = n
	while curr_size > 1:
		# Find index of the maximum
		# element in
		# arr[0..curr_size-1]
		mi = findMax(arr, curr_size)

		# Move the maximum element
		# to end of current array
		# if it's not already at
		# the end
		if mi != curr_size-1:
			# To move at the end,
			# first move maximum
			# number to beginning
			flip(arr, mi)

			# Now move the maximum
			# number to end by
			# reversing current array
			flip(arr, curr_size-1)
		curr_size -= 1

# A utility function to
# print an array of size n
def printArray(arr, n):
	for i in range(0,n):
		print ("%d"%( arr[i]),end=" ")


# This code is contributed by shreyanshi_arun.


def binary_search(val, target):
	r1 = 0
	r3 =len(val) -1

	while r1 <= r3:
		r2= (r1 + r3)// 2

		if val[r2]["package_name"] == target:
			return staycation_booking_details_dict[r2]

		elif target < val[r2]["package_name"]:
			r3 = r2 -1

		else:
			r1 = r2+1

	return -1


# Range Opt 7 Sort Func:
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(theSeq, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and theSeq[largest]["cost"] < theSeq[l]["cost"]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and theSeq[largest]["cost"] < theSeq[r]["cost"]:
		largest = r

	# Change root, if needed
	if largest != i:
		theSeq[i], theSeq[largest] = theSeq[largest], theSeq[i] # swap

		# Heapify the root.
		heapify(theSeq, n, largest)

# The main function to sort an array of given size


def heapSort(theSeq):
	n = len(theSeq)

	# Build a maxheap.
	for i in range(n//2 - 1, -1, -1):
		heapify(theSeq, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		theSeq[i], theSeq[0] = theSeq[0], theSeq[i] # swap
		heapify(theSeq, i, 0)


def val_ran(r1,r2):
	n = []

	for i in staycation_booking_details_dict:
		if i["cost"] >= r1 and i["cost"] <= r2:
			n.append(i)

	return n

