# Import the unittest module
import unittest

# Import the time module
import time

# Bubble Sort  implements the bubble Sort algorithm
def bubbleSort(list):
    # Find the length of the input list
    n = len(list)

    # Loop through the list for n-1 times (the last element will be in its correct position after n-1 iterations)
    for i in range(n-1):
        # Compare each pair of adjacent elements and swap them if the left element is larger than the right
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                # Swap the elements using a temporary variable
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    # Return the sorted list
    return list

# Quick Sort implements the Quick Sort algorithm
def quickSort(list):
    if not list: # check if list is empty
        return []
    pivot = list[0] # choose first element as pivot
    left = [x for x in list[1:] if x <= pivot] # all elements less than pivot
    right = [x for x in list[1:] if x > pivot] # all elements greater than pivot
    return quickSort(left) + [pivot] + quickSort(right)


# The function to merge two lists into one sorted list
def merge(left, right):
    # Initialize an empty list for the result
    result = []

    # While both lists are not empty
    while len(left) and len(right):
        # Compare the first elements of both lists
        if left[0] < right[0]:
            # If the left list's first element is smaller, append it to the result and remove it from the left list
            result.append(left.pop(0))
        else:
            # If the right list's first element is smaller, append it to the result and remove it from the right list
            result.append(right.pop(0))

    # If there are still elements in the left list, add them to the result
    if len(left):
        result += left
    # If there are still elements in the right list, add them to the result
    else:
        result += right

    # Return the result
    return result

# The function to sort a list using the merge sort algorithm
def mergeSort(list):
    # If the list has fewer than 2 elements, return the list as it is
    if len(list) < 2:
        return list

    # Find the middle index of the list
    mid = len(list) // 2

    # Split the list into two parts at the middle index
    leftlist = list[:mid]
    rightlist = list[mid:]

    # Recursively sort both halves
    leftlist = mergeSort(leftlist)
    rightlist = mergeSort(rightlist)

    # Merge the two sorted halves into a single sorted list
    return merge(leftlist, rightlist)


def hybridSort(L, BIG, SMALL, T):
    # Check if the length of the list is greater than the threshold
    if len(L) > T:
        # If the BIG parameter is "mergeSort"
        if BIG == "mergeSort":
            # Divide the list into two halves
            mid = len(L) // 2
            leftList = L[:mid]
            rightList = L[mid:]
            
            # Recursively sort the two halves and return the merged result
            return merge(hybridSort(leftList, BIG, SMALL, T),
                         hybridSort(rightList, BIG, SMALL, T))
        # If the BIG parameter is "quickSort"
        elif BIG == "quickSort":
            # Use the quicksort technique to sort the list
            pivot = L[len(L) // 2]
            right = [x for x in L if x > pivot]
            mid = [x for x in L if x == pivot]
            left = [x for x in L if x < pivot]
            
            # Recursively sort the left and right sublists and return the combined result
            return hybridSort(left, BIG, SMALL, T) + mid + hybridSort(right, BIG, SMALL, T)
        # If the BIG parameter is not "mergeSort" or "quickSort"
        else:
            print("Input value for BIG search is not valid returninng None")
            return None
    # If the length of the list is less than or equal to the threshold
    else:
        # If the SMALL parameter is "bubbleSort"
        if SMALL == "bubbleSort":
            # Sort the list using bubble sort
            return bubbleSort(L)
        # If the SMALL parameter is not "bubbleSort"
        else:
            print("Input value for SMALL search is not valid returninng None")
            return None


# This function computes the sorting time of hybrid Sort
# Param L - the list to be sorted
# Param BIG - the name of a sort algorithm to be used for large lists
# Param SMALL - the name of a sort algorithm to be used for small lists
# Param T - the threshold on the number of elements in the list
# Returns the sorted list L

def computeTime(L, BIG, SMALL, T):
    t1 = time.process_time_ns()# Determine which sorting algorithm to use
    if BIG == "quickSort" and SMALL == "bubbleSort":
        result = hybridSort(L, "quickSort", "bubbleSort", T)
    elif BIG == "mergeSort" and SMALL == "bubbleSort":
        result = hybridSort(L, "mergeSort", "bubbleSort", T)
    elif BIG == "quickSort" or BIG == "mergeSort" and SMALL == None:
        if BIG == "quickSort":
            result = quickSort(L)
        else:
            result = mergeSort(L)
    elif BIG == None and SMALL == "bubbleSort":
        result = bubbleSort(L)
    else:
        print("Input value for SMALL search is not valid returninng None")
        return None

    t2 = time.process_time_ns()
    print(f'{BIG} or {SMALL} execution time: {t2-t1} ns')
    return result

'''
Test case design
Based on ISP(Input Space Partitioning) and ECC(Each Choice Coverage)

1. List length is an empty list
L = []

2. List length is less than 5 and contains all negative numbers
L = [-1,-14]

3. List length is less than 5 and contains negative numbers and zeros
L = [-2,0,0]

4. List length is less that 5 and contains negative numbers, positive numbers, and zeros
L = [-7, 0, 3, 0]

5. List length is equal to 5 and contains all negative numbers
L = [-99, -5, -34, -29, -33]

6. List length is equal to 5 and contains negative numbers and zeros
L = [-1000, -39, 0, -36, 0]

7. List length is equal to 5 and contains negative numbers, positive numbers, and zeros
L = [10000, -3, 0, 200, -999]

8. List length is more then 5 and contains all negative numbers
L = [-99, -5, -34, -29, -33, -30003, -30444, -273]

9. List length is more than 5 and contains negative numbers and zeros
L = [-1000, -39, 0, -36, 0, -3984, -93984, -392930, -387474, -999384]

10. List length is more that 5 and contains negative numbers, positive numbers, and zeros
L = [10000, -3, 0, 200, -999, 3004, 83874, 928394, 2, 34, 0, 0, 3948, -394874]

11. List length is 100 and are random numbers for -99999 to 99999
L = [58440, -33687, -73105, -38087, -72145, 24450, -71917, 82329, 27933, -28549, 
-36083, -24402, -69557, -36295, 16728, 26374, 32050, -12880, 11061, 23335, 
12690, 34388, -56410, 22188, 98687, 95222, 15093, -38629, -22993, 24375, -90733, 
7863, 77007, -68985, 96729, 78436, -48356, 24148, 87091, -11723, -78274, -10068, 
73131, 40159, -60112, -48119, 16344, -60689, 64448, -71, 46456, -73390, -41682, -13379, 
15346, 75668, -71784, -55314, 33099, -29102, 50975, -20081, 93151, 83497, 27479, 88259, 
28738, 14789, -98034, -90735, -7528, 11050, 6400, 92626, 26945, -4411, 36843, 18341, -37701, 
-6338, -21917, -3205, -9417, 97810, -99872, 46716, -93313, -17223, 48110, -22827, -62031, -52794, 
-4268, -67904, -32079, -81682, 58192, 264, -75571, 94542]
'''

# Test Class used for testing the different sort algo
class SortingTest(unittest.TestCase):
    def test_01(self):
        print("TestCase01")
        print("An empty list")
        
        L = []
        print(f"The input list length = {len(L)}")
        result = computeTime(L, None, "bubbleSort", 5)
        self.assertEqual([], result)
        
        L = []
        result = computeTime(L, "quickSort", None, 5)
        self.assertEqual([], result)
        
        L = []
        result = computeTime(L, "mergeSort", None, 5)
        self.assertEqual([], result)
        
        L = []
        result = computeTime(L,"quickSort", "bubbleSort", 5)
        self.assertEqual([], result)

        L = []
        result = computeTime(L,"mergeSort", "bubbleSort", 5)
        self.assertEqual([], result)
        print("\n")

    def test_02(self):
        print("TestCase02")
        print("List length is less than 5 and contains all negative numbers")
        L = [-1, -14]
        print(f"The input list length = {len(L)}")
        result = computeTime(L, None, "bubbleSort", 5)
        self.assertEqual([-14, -1], result)
        
        L = [-1, -14]
        result = computeTime(L, "quickSort", None, 5)
        self.assertEqual([-14, -1], result)
        
        L = [-1, -14]
        result = computeTime(L, "mergeSort", None, 5)
        self.assertEqual([-14, -1], result)
        
        L = [-1, -14]
        result = computeTime(L,"quickSort", "bubbleSort", 5)
        self.assertEqual([-14, -1], result)

        L = [-1, -14]
        result = computeTime(L,"mergeSort", "bubbleSort", 5)
        self.assertEqual([-14, -1], result)
        print("\n")

    def test_03(self):
        print("TestCase03")
        print("List length is less than 5 and contains negative numbers and zeros")
        L = [-2, 0, 0]
        print(f"The input list length = {len(L)}")
        result = computeTime(L, None, "bubbleSort", 5)
        self.assertEqual([-2, 0, 0], result)
        
        L = [-2, 0, 0]
        result = computeTime(L, "quickSort", None, 5)
        self.assertEqual([-2, 0, 0], result)
        
        L = [-2, 0, 0]
        result = computeTime(L, "mergeSort", None, 5)
        self.assertEqual([-2, 0, 0], result)
        
        L = [-2, 0, 0]
        result = computeTime(L,"quickSort", "bubbleSort", 5)
        self.assertEqual([-2, 0, 0], result)

        L = [-2, 0, 0]
        result = computeTime(L,"mergeSort", "bubbleSort", 5)
        self.assertEqual([-2, 0, 0], result)
        print("\n")

    def test_04(self):
        print("TestCase04")
        print("List length is less that 5 and contains negative numbers, positive numbers, and zeros")
        L = [-7, 0, 3, 0]
        result = computeTime(L, None, "bubbleSort", 5)
        self.assertEqual([-7, 0, 0, 3], result)
        
        L = [-7, 0, 3, 0]
        result = computeTime(L, "quickSort", None, 5)
        self.assertEqual([-7, 0, 0, 3], result)
        
        L = [-7, 0, 3, 0]
        result = computeTime(L, "mergeSort", None, 5)
        self.assertEqual([-7, 0, 0, 3], result)
        
        L = [-7, 0, 3, 0]
        result = computeTime(L,"quickSort", "bubbleSort", 5)
        self.assertEqual([-7, 0, 0, 3], result)

        L = [-7, 0, 3, 0]
        result = computeTime(L,"mergeSort", "bubbleSort", 5)
        self.assertEqual([-7, 0, 0, 3], result)
        print("\n")

    def test_05(self):
        print("TestCase05")
        print("List length is equal to 5 and contains all negative numbers")
        L = [-99, -5, -34, -29, -33]
        print(f"The input list length = {len(L)}")
        result = computeTime(L, None, "bubbleSort", 5)
        self.assertEqual([-99, -34, -33, -29, -5], result)
        
        L = [-99, -5, -34, -29, -33]
        result = computeTime(L, "quickSort", None, 5)
        self.assertEqual([-99, -34, -33, -29, -5], result)
        
        L = [-99, -5, -34, -29, -33]
        result = computeTime(L, "mergeSort", None, 5)
        self.assertEqual([-99, -34, -33, -29, -5], result)
        
        L = [-99, -5, -34, -29, -33]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-99, -34, -33, -29, -5], result)

        L = [-99, -5, -34, -29, -33]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-99, -34, -33, -29, -5], result)
        print("\n")

    def test_06(self):
        print("TestCase06")
        print("List length is equal to 5 and contains negative numbers and zeros")
        L = [-1000, -39, 0, -36, 0]
        print(f"The input list length = {len(L)}")
        result = computeTime(L, None, "bubbleSort", 5)
        self.assertEqual([-1000, -39, -36, 0, 0], result)
        
        L = [-1000, -39, 0, -36, 0]
        result = computeTime(L, "quickSort", None, 5)
        self.assertEqual([-1000, -39, -36, 0, 0], result)
        
        L = [-1000, -39, 0, -36, 0]
        result = computeTime(L, "mergeSort", None, 5)
        self.assertEqual([-1000, -39, -36, 0, 0], result)
        
        L = [-1000, -39, 0, -36, 0]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-1000, -39, -36, 0, 0], result)

        L = [-1000, -39, 0, -36, 0]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-1000, -39, -36, 0, 0], result)
        print("\n")

    def test_07(self):
        print("TestCase07")
        print("List length is equal to 5 and contains negative numbers, positive numbers, and zeros")
        L = [10000, -3, 0, 200, -999]
        print(f"The input list length = {len(L)}")
        result = computeTime(L, None, "bubbleSort", 5)
        self.assertEqual([-999, -3, 0, 200, 10000], result)
        
        L = [10000, -3, 0, 200, -999]
        result = computeTime(L, "quickSort", None, 5)
        self.assertEqual([-999, -3, 0, 200, 10000], result)
        
        L = [10000, -3, 0, 200, -999]
        result = computeTime(L, "mergeSort", None, 5)
        self.assertEqual([-999, -3, 0, 200, 10000], result)
        
        L = [10000, -3, 0, 200, -999]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-999, -3, 0, 200, 10000], result)

        L = [10000, -3, 0, 200, -999]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-999, -3, 0, 200, 10000], result)
        print("\n")

    def test_08(self):
        print("TestCase08")
        print("List length is more then 5 and contains all negative numbers")
        L = [-99, -5, -34, -29, -33, -30003, -30444, -273]
        print(f"The input list length = {len(L)}")
        result = computeTime(L, None, "bubbleSort", 5)
        self.assertEqual([-30444, -30003, -273, -99, -34, -33, -29, -5], result)
        
        L = [-99, -5, -34, -29, -33, -30003, -30444, -273]
        result = computeTime(L, "quickSort", None, 5)
        self.assertEqual([-30444, -30003, -273, -99, -34, -33, -29, -5], result)
        
        L = [-99, -5, -34, -29, -33, -30003, -30444, -273]
        result = computeTime(L, "mergeSort", None, 5)
        self.assertEqual([-30444, -30003, -273, -99, -34, -33, -29, -5], result)
        
        L = [-99, -5, -34, -29, -33, -30003, -30444, -273]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-30444, -30003, -273, -99, -34, -33, -29, -5], result)

        L = [-99, -5, -34, -29, -33, -30003, -30444, -273]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-30444, -30003, -273, -99, -34, -33, -29, -5], result)
        print("\n")

    def test_09(self):
        print("TestCase09")
        print("List length is more than 5 and contains negative numbers and zeros")
        L = [-1000, -39, 0, -36, 0, -3984, -93984, -392930, -387474, -999384]
        print(f"The input list length = {len(L)}")
        result = computeTime(L, None, "bubbleSort", 5)
        self.assertEqual([-999384, -392930, -387474, -93984, -3984, -1000, -39, -36, 0, 0], result)
        
        L = [-1000, -39, 0, -36, 0, -3984, -93984, -392930, -387474, -999384]
        result = computeTime(L, "quickSort", None, 5)
        self.assertEqual([-999384, -392930, -387474, -93984, -3984, -1000, -39, -36, 0, 0], result)
        
        L = [-1000, -39, 0, -36, 0, -3984, -93984, -392930, -387474, -999384]
        result = computeTime(L, "mergeSort", None, 5)
        self.assertEqual([-999384, -392930, -387474, -93984, -3984, -1000, -39, -36, 0, 0], result)
        
        L = [-1000, -39, 0, -36, 0, -3984, -93984, -392930, -387474, -999384]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-999384, -392930, -387474, -93984, -3984, -1000, -39, -36, 0, 0],
                         result)

        L = [-1000, -39, 0, -36, 0, -3984, -93984, -392930, -387474, -999384]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-999384, -392930, -387474, -93984, -3984, -1000, -39, -36, 0, 0],
                         result)
        print("\n")
    
    def test_10(self):
        print("TestCase10")
        print("List length is more that 5 and contains negative numbers, positive numbers, and zeros")
        L = [10000, -3, 0, 200, -999, 3004, 83874, 928394, 2, 34, 0, 0, 3948, -394874]
        print(f"The input list length = {len(L)}")
        result = computeTime(L, None, "bubbleSort", 5)
        self.assertEqual([-394874, -999, -3, 0, 0, 0, 2, 34, 200, 3004, 3948, 10000, 83874, 928394], result)
        
        L = [10000, -3, 0, 200, -999, 3004, 83874, 928394, 2, 34, 0, 0, 3948, -394874]
        result = computeTime(L, "quickSort", None, 5)
        self.assertEqual([-394874, -999, -3, 0, 0, 0, 2, 34, 200, 3004, 3948, 10000, 83874, 928394], result)
        
        L = [10000, -3, 0, 200, -999, 3004, 83874, 928394, 2, 34, 0, 0, 3948, -394874]
        result = computeTime(L, "mergeSort", None, 5)
        self.assertEqual([-394874, -999, -3, 0, 0, 0, 2, 34, 200, 3004, 3948, 10000, 83874, 928394], result)
        
        L = [10000, -3, 0, 200, -999, 3004, 83874, 928394, 2, 34, 0, 0, 3948, -394874]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-394874, -999, -3, 0, 0, 0, 2, 34, 200, 3004, 3948, 10000, 83874, 928394],
                        result)

        L = [10000, -3, 0, 200, -999, 3004, 83874, 928394, 2, 34, 0, 0, 3948, -394874]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-394874, -999, -3, 0, 0, 0, 2, 34, 200, 3004, 3948, 10000, 83874, 928394],
                        result)
        print("\n")

    def test_11(self):
        print("TestCase11")
        print("List length is 100 and are random numbers for -99999 to 99999")
        L = [58440, -33687, -73105, -38087, -72145, 24450, -71917, 82329, 27933, -28549, 
        -36083, -24402, -69557, -36295, 16728, 26374, 32050, -12880, 11061, 23335, 
        12690, 34388, -56410, 22188, 98687, 95222, 15093, -38629, -22993, 24375, -90733, 
        7863, 77007, -68985, 96729, 78436, -48356, 24148, 87091, -11723, -78274, -10068, 
        73131, 40159, -60112, -48119, 16344, -60689, 64448, -71, 46456, -73390, -41682, -13379, 
        15346, 75668, -71784, -55314, 33099, -29102, 50975, -20081, 93151, 83497, 27479, 88259, 
        28738, 14789, -98034, -90735, -7528, 11050, 6400, 92626, 26945, -4411, 36843, 18341, -37701, 
        -6338, -21917, -3205, -9417, 97810, -99872, 46716, -93313, -17223, 48110, -22827, -62031, -52794, 
        -4268, -67904, -32079, -81682, 58192, 264, -75571, 94542]
        print(f"The input list length = {len(L)}")
        result = computeTime(L, None, "bubbleSort", 5)
        self.assertEqual([-99872, -98034, -93313, -90735, -90733, -81682, -78274, -75571, -73390, -73105, 
        -72145, -71917, -71784, -69557, -68985, -67904, -62031, -60689, -60112, -56410, -55314, -52794, 
        -48356, -48119, -41682, -38629, -38087, -37701, -36295, -36083, -33687, -32079, -29102, -28549, 
        -24402, -22993, -22827, -21917, -20081, -17223, -13379, -12880, -11723, -10068, -9417, -7528, -6338, 
        -4411, -4268, -3205, -71, 264, 6400, 7863, 11050, 11061, 12690, 14789, 15093, 15346, 16344, 16728, 18341, 
        22188, 23335, 24148, 24375, 24450, 26374, 26945, 27479, 27933, 28738, 32050, 33099, 34388, 36843, 40159, 46456, 
        46716, 48110, 50975, 58192, 58440, 64448, 73131, 75668, 77007, 78436, 82329, 83497, 87091, 88259, 92626, 93151, 
        94542, 95222, 96729, 97810, 98687], result)
        
        L = [58440, -33687, -73105, -38087, -72145, 24450, -71917, 82329, 27933, -28549, 
        -36083, -24402, -69557, -36295, 16728, 26374, 32050, -12880, 11061, 23335, 
        12690, 34388, -56410, 22188, 98687, 95222, 15093, -38629, -22993, 24375, -90733, 
        7863, 77007, -68985, 96729, 78436, -48356, 24148, 87091, -11723, -78274, -10068, 
        73131, 40159, -60112, -48119, 16344, -60689, 64448, -71, 46456, -73390, -41682, -13379, 
        15346, 75668, -71784, -55314, 33099, -29102, 50975, -20081, 93151, 83497, 27479, 88259, 
        28738, 14789, -98034, -90735, -7528, 11050, 6400, 92626, 26945, -4411, 36843, 18341, -37701, 
        -6338, -21917, -3205, -9417, 97810, -99872, 46716, -93313, -17223, 48110, -22827, -62031, -52794, 
        -4268, -67904, -32079, -81682, 58192, 264, -75571, 94542]
        result = computeTime(L, "quickSort", None, 5)
        self.assertEqual([-99872, -98034, -93313, -90735, -90733, -81682, -78274, -75571, -73390, -73105, 
        -72145, -71917, -71784, -69557, -68985, -67904, -62031, -60689, -60112, -56410, -55314, -52794, 
        -48356, -48119, -41682, -38629, -38087, -37701, -36295, -36083, -33687, -32079, -29102, -28549, 
        -24402, -22993, -22827, -21917, -20081, -17223, -13379, -12880, -11723, -10068, -9417, -7528, -6338, 
        -4411, -4268, -3205, -71, 264, 6400, 7863, 11050, 11061, 12690, 14789, 15093, 15346, 16344, 16728, 18341, 
        22188, 23335, 24148, 24375, 24450, 26374, 26945, 27479, 27933, 28738, 32050, 33099, 34388, 36843, 40159, 46456, 
        46716, 48110, 50975, 58192, 58440, 64448, 73131, 75668, 77007, 78436, 82329, 83497, 87091, 88259, 92626, 93151, 
        94542, 95222, 96729, 97810, 98687], result)
        
        L = [58440, -33687, -73105, -38087, -72145, 24450, -71917, 82329, 27933, -28549, 
        -36083, -24402, -69557, -36295, 16728, 26374, 32050, -12880, 11061, 23335, 
        12690, 34388, -56410, 22188, 98687, 95222, 15093, -38629, -22993, 24375, -90733, 
        7863, 77007, -68985, 96729, 78436, -48356, 24148, 87091, -11723, -78274, -10068, 
        73131, 40159, -60112, -48119, 16344, -60689, 64448, -71, 46456, -73390, -41682, -13379, 
        15346, 75668, -71784, -55314, 33099, -29102, 50975, -20081, 93151, 83497, 27479, 88259, 
        28738, 14789, -98034, -90735, -7528, 11050, 6400, 92626, 26945, -4411, 36843, 18341, -37701, 
        -6338, -21917, -3205, -9417, 97810, -99872, 46716, -93313, -17223, 48110, -22827, -62031, -52794, 
        -4268, -67904, -32079, -81682, 58192, 264, -75571, 94542]
        result = computeTime(L, "mergeSort", None, 5)
        self.assertEqual([-99872, -98034, -93313, -90735, -90733, -81682, -78274, -75571, -73390, -73105, 
        -72145, -71917, -71784, -69557, -68985, -67904, -62031, -60689, -60112, -56410, -55314, -52794, 
        -48356, -48119, -41682, -38629, -38087, -37701, -36295, -36083, -33687, -32079, -29102, -28549, 
        -24402, -22993, -22827, -21917, -20081, -17223, -13379, -12880, -11723, -10068, -9417, -7528, -6338, 
        -4411, -4268, -3205, -71, 264, 6400, 7863, 11050, 11061, 12690, 14789, 15093, 15346, 16344, 16728, 18341, 
        22188, 23335, 24148, 24375, 24450, 26374, 26945, 27479, 27933, 28738, 32050, 33099, 34388, 36843, 40159, 46456, 
        46716, 48110, 50975, 58192, 58440, 64448, 73131, 75668, 77007, 78436, 82329, 83497, 87091, 88259, 92626, 93151, 
        94542, 95222, 96729, 97810, 98687], result)
        
        L = [58440, -33687, -73105, -38087, -72145, 24450, -71917, 82329, 27933, -28549, 
        -36083, -24402, -69557, -36295, 16728, 26374, 32050, -12880, 11061, 23335, 
        12690, 34388, -56410, 22188, 98687, 95222, 15093, -38629, -22993, 24375, -90733, 
        7863, 77007, -68985, 96729, 78436, -48356, 24148, 87091, -11723, -78274, -10068, 
        73131, 40159, -60112, -48119, 16344, -60689, 64448, -71, 46456, -73390, -41682, -13379, 
        15346, 75668, -71784, -55314, 33099, -29102, 50975, -20081, 93151, 83497, 27479, 88259, 
        28738, 14789, -98034, -90735, -7528, 11050, 6400, 92626, 26945, -4411, 36843, 18341, -37701, 
        -6338, -21917, -3205, -9417, 97810, -99872, 46716, -93313, -17223, 48110, -22827, -62031, -52794, 
        -4268, -67904, -32079, -81682, 58192, 264, -75571, 94542]
        result = computeTime(L, "quickSort", "bubbleSort", 5)
        self.assertEqual([-99872, -98034, -93313, -90735, -90733, -81682, -78274, -75571, -73390, -73105, 
        -72145, -71917, -71784, -69557, -68985, -67904, -62031, -60689, -60112, -56410, -55314, -52794, 
        -48356, -48119, -41682, -38629, -38087, -37701, -36295, -36083, -33687, -32079, -29102, -28549, 
        -24402, -22993, -22827, -21917, -20081, -17223, -13379, -12880, -11723, -10068, -9417, -7528, -6338, 
        -4411, -4268, -3205, -71, 264, 6400, 7863, 11050, 11061, 12690, 14789, 15093, 15346, 16344, 16728, 18341, 
        22188, 23335, 24148, 24375, 24450, 26374, 26945, 27479, 27933, 28738, 32050, 33099, 34388, 36843, 40159, 46456, 
        46716, 48110, 50975, 58192, 58440, 64448, 73131, 75668, 77007, 78436, 82329, 83497, 87091, 88259, 92626, 93151, 
        94542, 95222, 96729, 97810, 98687],
                         result)

        L = [58440, -33687, -73105, -38087, -72145, 24450, -71917, 82329, 27933, -28549, 
        -36083, -24402, -69557, -36295, 16728, 26374, 32050, -12880, 11061, 23335, 
        12690, 34388, -56410, 22188, 98687, 95222, 15093, -38629, -22993, 24375, -90733, 
        7863, 77007, -68985, 96729, 78436, -48356, 24148, 87091, -11723, -78274, -10068, 
        73131, 40159, -60112, -48119, 16344, -60689, 64448, -71, 46456, -73390, -41682, -13379, 
        15346, 75668, -71784, -55314, 33099, -29102, 50975, -20081, 93151, 83497, 27479, 88259, 
        28738, 14789, -98034, -90735, -7528, 11050, 6400, 92626, 26945, -4411, 36843, 18341, -37701, 
        -6338, -21917, -3205, -9417, 97810, -99872, 46716, -93313, -17223, 48110, -22827, -62031, -52794, 
        -4268, -67904, -32079, -81682, 58192, 264, -75571, 94542]
        result = computeTime(L, "mergeSort", "bubbleSort", 5)
        self.assertEqual([-99872, -98034, -93313, -90735, -90733, -81682, -78274, -75571, -73390, -73105, 
        -72145, -71917, -71784, -69557, -68985, -67904, -62031, -60689, -60112, -56410, -55314, -52794, 
        -48356, -48119, -41682, -38629, -38087, -37701, -36295, -36083, -33687, -32079, -29102, -28549, 
        -24402, -22993, -22827, -21917, -20081, -17223, -13379, -12880, -11723, -10068, -9417, -7528, -6338, 
        -4411, -4268, -3205, -71, 264, 6400, 7863, 11050, 11061, 12690, 14789, 15093, 15346, 16344, 16728, 18341, 
        22188, 23335, 24148, 24375, 24450, 26374, 26945, 27479, 27933, 28738, 32050, 33099, 34388, 36843, 40159, 46456, 
        46716, 48110, 50975, 58192, 58440, 64448, 73131, 75668, 77007, 78436, 82329, 83497, 87091, 88259, 92626, 93151, 
        94542, 95222, 96729, 97810, 98687],
                         result)
        print("\n")

if __name__ == '__main__':
    unittest.main()