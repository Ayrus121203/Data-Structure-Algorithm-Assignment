#Nmame: Surya Moorthy S/O Sathia Moorthy
#Admin Number: 201296F
#Group: IT2653-03

def insertionSortRecursive(arr, n):

    # base case
    if n<=1:   #if only 1 element left, return
        return

    # Sort first n-1 elements
    insertionSortRecursive(arr,n-1)  # Recursive call
    '''Insert last element at its correct position
        in sorted array.'''
    last = arr[n-1]
    j = n-2

      # Move elements of arr[0..i-1], that are
      # greater than key, to one position ahead
      # of their current position
    while (j>=0 and arr[j]["cost"] > last["cost"]):  #loops through every element in the array to insert current element
        arr[j+1] = arr[j]    #shifts element by 1 to find the spot
        j = j-1

    arr[j+1]=last               #places the element in the appropriate pos


def insertionSortRecursive_package_name(arr, n):

    # base case
    if n<=1:   #if only 1 element left, return
        return

    # Sort first n-1 elements
    insertionSortRecursive(arr,n-1)  # Recursive call
    '''Insert last element at its correct position
        in sorted array.'''
    last = arr[n-1]
    j = n-2

      # Move elements of arr[0..i-1], that are
      # greater than key, to one position ahead
      # of their current position
    while (j>=0 and arr[j]["package_name"] > last["package_name"]):  #loops through every element in the array to insert current element
        arr[j+1] = arr[j]    #shifts element by 1 to find the spot
        j = j-1

    arr[j+1]=last               #places the element in the appropriate pos





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



# Python program for implementation of CombSort
# To find next gap from current
def getNextGap(gap):

    # Shrink gap by Shrink factor
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap
# Function to sort arr[] using Comb Sort
def combSort(arr):
    print('Package Cost will be sorted using Comb Sort')
    print('')

    n = len(arr)

    # Initialize gap
    gap = n

    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True

    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap !=1 or swapped == 1:

        # Find next gap
        gap = getNextGap(gap)

        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False

        # Compare all elements with current gap
        for i in range(0, n-gap):
            if arr[i]["cost"] > arr[i + gap]["cost"]:
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swapped = True



def oddEvenSort(arr, n):
    print('Pax per package will now be sorted using OddEven Sort')

    # Initially array is unsorted
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if arr[i]["pax"] > arr[i+1]["pax"]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0

        for i in range(0, n-1, 2):
            if arr[i]["pax"] > arr[i+1]["pax"]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0

    return


# pancake sort start
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
        if arr[i]["customer_name"] > arr[mi]["customer_name"]:
            mi = i
    return mi

# The main function that
# sorts given array
# using flip operations
def pancakeSort(arr):

    n = len(arr)
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
#pancake sort end
# *Pancake sort consists of flip, findMax and Pancake functions

def cocktailSort(a):

    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):

        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False

        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            if (a[i]["package_name"] > a[i + 1]["package_name"]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1

        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1, -1):
            if (a[i]["package_name"] > a[i + 1]["package_name"]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start + 1



def gnomeSort( arr):

    n= len(arr)
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index]["package_name"] >= arr[index - 1]["package_name"]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1

    return arr


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
#-----------------------------------------------------------------------------------------------------

# Python program for implementation of heap Sort
# To heapify subtree rooted at index i.
# n is size of heap
def heapify_reverse(theSeq, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1	 # left = 2*i + 1
    r = 2 * i + 2	 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and theSeq[largest]["cost"] > theSeq[l]["cost"]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and theSeq[largest]["cost"] > theSeq[r]["cost"]:
        largest = r

    # Change root, if needed
    if largest != i:
        theSeq[i], theSeq[largest] = theSeq[largest], theSeq[i] # swap

        # Heapify the root.
        heapify(theSeq, n, largest)

# The main function to sort an array of given size
def heapSort_reverse(theSeq):

    n = len(theSeq)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify_reverse(theSeq, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        theSeq[i], theSeq[0] = theSeq[0], theSeq[i] # swap
        heapify_reverse(theSeq, i, 0)
