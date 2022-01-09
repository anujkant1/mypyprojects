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
    return -1


print(findMiddle(array))



# Below solution without using sum()

arr = [5, 25, 20, 32, 2, 23, 20, 5]

def equalSum(arr):
    left_pos, right_pos = 0, len(arr) - 1
    left_sum, right_sum = 0, 0

    while left_pos < right_pos:
        left_sum += arr[left_pos]
        right_sum += arr[right_pos]

        while (left_sum < right_sum):
            left_pos += 1
            left_sum += arr[left_pos]

        while (right_sum < left_sum):
            right_pos -= 1
            right_sum += arr[right_pos]
        right_pos -= 1
        left_pos += 1
    if (left_sum == right_sum and left_pos == right_pos):
        return(arr[left_pos])
    return -1


print(equalSum(arr))
