"""
Write a function that's given a list of integers, computes the number of times each integer occurs and print them out in descending order of integers.

input: [1, 2, 6, 7, 9, 8, 8, 6]
output:
9: 1
8: 2
7: 1
6: 2
2: 1
1: 1

Modify code to print result from the highest occurring to lowest.
What's the time complexity of your code?
Write test code for the above
"""
import sys

input= [1, 2, 6, 7, 9, 8, 8, 6]


def count_int_times(input_array):
    int_map = {}
    for integer in input_array:
        if integer in int_map.keys():
            int_map[integer] += 1
        else:
            int_map[integer] = 1
    return int_map


def sort_int_map(input_array):
    int_map = count_int_times(input_array)
    sorted_int_map = dict(sorted(int_map.items(), key=lambda x : x[1], reverse=True))
    return sorted_int_map

# Testing
def test_sort_by_frequency_desc():
    # Test 1: Basic example
    arr = [1, 2, 3, 4, 4, 5, 1, 2, 4, 5, 1, 8, 9, 2]
    expected = {1: 3, 2: 3, 4: 3, 5: 2, 3: 1, 8: 1, 9: 1}
    assert sort_int_map(arr) == expected

    # Test 2: Empty input
    arr = []
    expected = {}
    assert sort_int_map(arr) == expected

    # Test 3: Already sorted array
    arr = [1, 2, 2, 2, 6, 6, 9, 9, 9, 9, 10, 10, 10, 10, 10]
    expected = {10: 5, 9: 4, 2: 3, 6: 2, 1: 1}
    assert sort_int_map(arr) == expected

    # Test 4: Identical input
    arr = [5, 5, 5]
    expected = {5: 3}
    assert sort_int_map(arr) == expected

    # Test 5: Negative integers
    arr = [-1, -1, 2]
    expected = {-1: 2, 2: 1}
    assert sort_int_map(arr) == expected

    # Test 5: Non-int array
    arr = [1, 1, "3"]
    expected = {1: 2, "3": 1}
    assert sort_int_map(arr) == expected


# Run tests
test_sort_by_frequency_desc()