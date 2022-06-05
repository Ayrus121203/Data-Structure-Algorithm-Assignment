#Nmame: Surya Moorthy S/O Sathia Moorthy
#Admin Number: 201296F
#Group: IT2653-03


staycation_booking_details_dict = [
        {"customer_name": "Bill", "package_name": "Dc", "cost": 15, "pax": 10},
            {"customer_name": "Amos", "package_name": "Air", "cost": 21, "pax": 5},
                {"customer_name": "Tan", "package_name": "Water", "cost": 17, "pax": 4},
                    {"customer_name": "Beverly", "package_name": "Earth", "cost": 9, "pax": 3},
                        {"customer_name": "Theresa", "package_name": "Lava", "cost": 5, "pax": 1},
                            {"customer_name": "Ellen", "package_name": "Sea", "cost": 27, "pax": 2},
                                {"customer_name": "Hollow", "package_name": "Mountain", "cost": 19, "pax": 10},
                                    {"customer_name": "Jill", "package_name": "Zoo", "cost": 10, "pax": 15},
                                        {"customer_name": "Jane", "package_name": "Desert", "cost": 11, "pax": 4},
                                            {"customer_name": "Koen", "package_name": "Oceania", "cost": 12, "pax": 4}
                                        ]




#------------------------------------------------------------------------------------------------------
# menu option 2

def bubbleSort(theSeq):     #theSeq is any var name. Meant to reference staycation_dict in main.py
    print('Display will be sorted using BubbleSort')   #import basic_sort_searches_func
    print('')

    n = len(theSeq)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if theSeq[j]["customer_name"] > theSeq[j+1]["customer_name"]:  #Can change the key name to any name in staycation_dict
                theSeq[j], theSeq[j+1] = theSeq[j+1], theSeq[j]             #Refer to Optimised ver for Package name Sort



def bubbleSort_reverse(theSeq):#theSeq is any var name. Meant to reference staycation_dict in main.py
    print('Display will be sorted using BubbleSort Reverse')    #import sort_functions
    print('')

    n = len(theSeq)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if theSeq[j]["customer_name"] < theSeq[j+1]["customer_name"]:  #Reverse change the sign from More Than to Less Than
                theSeq[j], theSeq[j+1] = theSeq[j+1], theSeq[j]             #Refer to Optimised ver for Package name Sort


def bubbleSort_optimized(theSeq):
    print('Display will be sorted using BubbleSort Optimized')
    print('')
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



def bubbleSort_optimized_reverse(theSeq):
    print('Display will be sorted using BubbleSort Optimized Reversed')
    print('')

    n = len(theSeq)

    # Perform n-1 bubble operations on the sequence
    passCount = 0
    for i in range(n - 1, 0, -1):
        # Set boolean variable to check occurrence of swapping
        # in inner loop
        swapFlag = False

        # Bubble the largest item to the end
        for j in range(i):
            if (theSeq[j]["customer_name"] < theSeq[j + 1]["customer_name"]):
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

#---------------------------------------------------------------------------------
#menu option 3
def selection_sort(theSeq):
    print('Display will be sorted using Selection Sort')
    print('')

    # Sort a sequence in ascending order using the selection sort algorithm
    n = len(theSeq)
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        currNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i+1, n):
            if theSeq[j]["package_name"] < theSeq[currNdx]["package_name"]:
                currNdx = j
        # Swap the ith value and currNdx value on ly if the
        # smallest/biggest value is not already in its proper position.
        if currNdx != i:
            # tmp = theSeq[i]
            # theSeq[i] = theSeq[currNdx]
            # theSeq[currNdx] = tmp
            theSeq[i], theSeq[currNdx] = theSeq[currNdx], theSeq[i]


def selection_sort_reverse(theSeq):
    print('Display will be sorted using Selection Sort Reverse')
    print('')

    # Sort a sequence in ascending order using the selection sort algorithm
    n = len(theSeq)
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        currNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i+1, n):
            if theSeq[j]["package_name"] > theSeq[currNdx]["package_name"]:
                currNdx = j
        # Swap the ith value and currNdx value on ly if the
        # smallest/biggest value is not already in its proper position.
        if currNdx != i:
            # tmp = theSeq[i]
            # theSeq[i] = theSeq[currNdx]
            # theSeq[currNdx] = tmp
            theSeq[i], theSeq[currNdx] = theSeq[currNdx], theSeq[i]
#-----------------------------------------------------------------------------------
#menu option 4
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


def insertion_sort_reverse(theSeq):
    print('Staycation booking will now be sorted using Insertion Sort Reversed')

    n = len(theSeq)

    for i in range(1,n):
        val = theSeq[i]
        pos = i
        while pos > 0 and val["cost"] > theSeq[pos - 1]["cost"]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1

            theSeq[pos] = val

#------------------------------------------------------------------------------------
#menu option 5

def linear_search_cust_name(value, target):
    print('Customer Name will now be searched using Linear Search')
    n = len(value)

    for i in range(n):
        if value[i]["customer_name"] == target:
            return value[i]

    return False

def linear_search_pack_name(value, target):
    print('Package Name will now be searched using Linear Search')
    n = len(value)

    for i in range(n):
        if value[i]["package_name"] == target:
            return value[i]

    return False

#-----------------------------------------------------------------------------------
#menu option 6
def binary_search( theValues, target ):
    print('Package Name will now be sorted by Binary Search')
    # Start with the entire sequence of elements
    low = 0
    high = len(theValues)-1

    # Repeatedly subdivide the sequence in half # until the target is found
    while low<=high:
        # Find the midpoint of the sequence
        mid = (low+high)//2 # or int(low/high)/2

        # Does the midpoint contain the target?
        # If yes, return midpoint (i.e. index of the list)
        if theValues[mid]["package_name"] == target:
            return theValues[mid]
        # Or is the target before the midpoint?
        elif target < theValues[mid]["package_name"]:
            high = mid-1
        #     low-----------------mid-------------high
        #     low----mid-----high

        # Or is the target after the midpoint?
        else:
            low = mid+1
    #         low-----------------mid-------------high
    #                                low----mid---high

    # If the sequence cannot be subdivided further,
    # target is not in the list of values
    return -1

#-----------------------------------------------------------------------------------
#menu option 7
def val_ran_validation(r1,r2):

    if r1 > r2:
        print('High Value must be higher than low value')
        return True
    elif r1 == r2:
        print('Low value and high value should be different')
        return True
    else:
        return False


def val_ran(r1,r2):
    n = []

    for i in staycation_booking_details_dict:
        if i["cost"] >= r1 and i["cost"] <= r2:
            n.append(i)

    return n

#----------------------------------------------------------------------------------------------------------
