# LeetCode
# https://leetcode.com/problems/two-sum/

array = [2, 7, 11, 15]
target = 18


def optimal_twoSum(array, target):
    hash_table = dict()
    for index, value in enumerate(array):
        if target - value in hash_table:
            return ([hash_table[target-value], index])
        else:
            hash_table[value] = index
    return "Not found"


print(optimal_twoSum(array, target))
