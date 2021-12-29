# Pair with Given Sum in a Sorted Array
"""
You are given an array arr of size N.
Find the number of all unique pairs in the array that sum to a number k.
The elements of the array are distinct and are in sorted order.

Note: (a,b) and (b,a) are considered the same. Also, an element cannot pair with itself, i.e., (a,a) is invalid.

Example 1:
Input:
N = 7
arr[] = {1, 2, 3, 4, 5, 6, 7}
k = 8
Output:
3
Explanation:
We find 3 such pairs that
sum to 8: (1,7) (2,6) (3,5)

Example 2:
Input:
N = 7
arr[] = {1, 2, 3, 4, 5, 6, 7}
k = 98
Output:
0
Explanation: 
There is no pair of these numbers that sum to 98

"""

array = [1, 2, 3, 4, 5, 6, 7]

target = 8
elements = 7


def sumpair(array, target):
    result = []
    left = 0
    right = len(array) - 1
    while (left < right):
        if array[left] + array[right] > target:
            right -= 1
        elif array[left] + array[right] < target:
            left += 1
        elif array[left] + array[right] == target:
            result.append([array[left], array[right]])
            left += 1
    if not result:
        return "Not found"
    return result


print(sumpair(array, target))
