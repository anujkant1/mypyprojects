array = [2, 4, 5, 7, 8, 9, 15, 20, 25, 30, 32, 35]
target = 32


def BinarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if target == array[middle]:
            return middle
        elif target < array[middle]:
            right == middle - 1
        elif target > array[middle]:
            left = middle + 1

    return -1


print(BinarySearch(array, target))
