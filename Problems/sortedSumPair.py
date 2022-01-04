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

def countPairs(arr, k):
    result = 0
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == k:
            result += 1
            left += 1
            right -= 1  # Safe to move on both ends as elements are unique and sorted.
        elif arr[left] + arr[right] < k:
            left += 1
        else:
            right -= 1
    return result



print(countPairs(array, target))
