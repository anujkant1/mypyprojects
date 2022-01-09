arr = [29, 10, 14, 37, 15]


def bubbleSort(arr):
    for iter in range(len(arr)):
        # Don't need to go over the entire array everytime
        for item in range(0, len(arr) - 1 - iter):
            if arr[item] > arr[item + 1]:
                arr[item], arr[item + 1] = arr[item + 1],  arr[item]
    return arr


print(bubbleSort(arr))
