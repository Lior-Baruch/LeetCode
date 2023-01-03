# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # Create a dictionary to store the values and their indices
    dict = {}
    # Loop through the array
    for i in range(len(nums)):
        # Check if the difference between the target and the current value is in the dictionary keys
        if target - nums[i] in dict.keys():
            # If it is, return the index of the difference and the current index
            return [dict[target - nums[i]], i]
        # If it is not, add the current value and its index to the dictionary
        dict[nums[i]] = i

    # If no solution is found, return an empty array
    return []

# Time Complexity: O(n)
# Space Complexity: O(n)

# test cases
def main():
    nums = [2, 7, 11, 15]
    target = 9
    print("Input: nums = [2, 7, 11, 15], target = 9")
    print("Output: ", twoSum(nums, target))

    nums = [3, 2, 4]
    target = 6
    print("Input: nums = [3, 2, 4], target = 6")
    print("Output: ", twoSum(nums, target))

    nums = [3, 3]
    target = 6
    print("Input: nums = [3, 3], target = 6")
    print("Output: ", twoSum(nums, target))
    pass


if __name__ == '__main__':
    main()


