# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
import TwoSum


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]] of indices
    time complexity: O(n^2)
    """
    # Sort the array
    nums.sort()
    # Create a list to store the results
    results = []
    # Loop through the array
    for i in range(len(nums)):
        # If the current value is greater than zero, break the loop
        if nums[i] > 0:
            break
        # If the current value is the same as the previous value, skip it
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Create a list to store the two sum results
        twoSumResults = TwoSum.twoSum(nums[i + 1:], -nums[i])
        # Loop through the two sum results
        for j in range(len(twoSumResults)):
            # Add the current value and the two sum result to the results list
            results.append([nums[i], nums[twoSumResults[j][0] + i + 1], nums[twoSumResults[j][1] + i + 1]])
    # Return the results
    return results



# test cases
def main():
    nums = [-1, 0, 1, 2, -1, -4]
    print("Input: nums = [-1, 0, 1, 2, -1, -4]")
    print("Output: ", threeSum(nums))


if __name__ == '__main__':
    main()




