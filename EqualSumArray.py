"""
Find an element in array such that sum of left array is equal to sum of right array

Examples: 

Input: 1 4 2 5
Output: 2
Explanation: If 2 is the partition, 
      subarrays are : {1, 4} and {5}

Input: 2 3 4 1 4 5
Output: 1
Explanation: If 1 is the partition, 
 Subarrays are : {2, 3, 4} and {4, 5}
 
"""


array = [2, 3, 4, 1, 4, 5]


def findMiddle(array):
    for i in range(1, len(array)):
        if sum(array[:i]) == sum(array[i+1:]):
            return array[i]
    return "-1"


print(findMiddle(array))
