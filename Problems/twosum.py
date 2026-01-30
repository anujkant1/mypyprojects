# LeetCode
# https://leetcode.com/problems/two-sum/

array = [2, 7, 11, 15]
target = 18


## Brute Force Approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]



## Optimal Approach
def optimal_twoSum(array, target):
    hash_table = dict()
    for index, value in enumerate(array):
        if target - value in hash_table:
            return ([hash_table[target-value], index])
        else:
            hash_table[value] = index
    return "Not found"


print(optimal_twoSum(array, target))

## Alternative Optimal Approach
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        number_to_index = {}

        for index, number in enumerate(nums):
            number_to_index[number] = index

        for index, number in enumerate(nums):
            number_needed = target - number
            if (number_needed in number_to_index and number_to_index[number_needed] != index):
                return [index, number_to_index[number_needed]]