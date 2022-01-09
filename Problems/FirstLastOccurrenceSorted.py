"""Find first and last positions of an element in a sorted array

Given a sorted array with possibly duplicate elements, 
the task is to find indexes of first and last occurrences
of an element x in the given array.

Examples: 
Input : arr[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}    
        x = 5
Output : First Occurrence = 2
         Last Occurrence = 5

Input : arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125}    
        x = 7
Output : First Occurrence = 6
         Last Occurrence = 6
"""


def first(array, target):
    left = 0
    right = len(array) - 1
    result = -1

    while left <= right:
        middle = (left + right) // 2
        if target < array[middle]:
            right = middle - 1
        elif target > array[middle]:
            left = middle + 1
        else:
            result = middle
            right = middle - 1

    return f'First Occurrence: {result}'


def last(array, target):
    left = 0
    right = len(array) - 1
    result = -1

    while left <= right:
        middle = (left + right) // 2
        if target < array[middle]:
            right = middle - 1
        elif target > array[middle]:
            left = middle + 1
        else:
            result = middle
            left = middle + 1

    return f'First Occurrence: {result}'


# Driver Code
array = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
print(first(array, target))
print(last(array, target))
