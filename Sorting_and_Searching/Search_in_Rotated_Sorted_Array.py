# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (
# 0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
def binary_search(sorted_nums, target):
    i = len(sorted_nums) // 2
    left = 0
    right = len(sorted_nums) - 1
    while left <= right:
        if sorted_nums[i] == target:
            return i
        elif sorted_nums[i] < target:
            left = i + 1
        else:
            right = i - 1
        i = (left + right) // 2
    return -1


# find the pivot index using smart binary search
def find_pivot_index(rotated_sorted_nums):
    pivot_index = len(rotated_sorted_nums) // 2
    left = 0
    right = len(rotated_sorted_nums) - 1
    while left <= right:
        if rotated_sorted_nums[pivot_index] < rotated_sorted_nums[pivot_index - 1]:
            return pivot_index
        elif rotated_sorted_nums[pivot_index] < rotated_sorted_nums[right]:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
        pivot_index = (left + right) // 2
    return 0


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # find the pivot index and split the array into two parts
    # the first part is sorted and the second part is sorted

    pivot_index = find_pivot_index(nums)

    # split the array into two parts
    first_part = nums[:pivot_index]
    second_part = nums[pivot_index:]

    # search the first part
    first_part_index = binary_search(first_part, target)
    if first_part_index != -1:
        return first_part_index

    # search the second part
    second_part_index = binary_search(second_part, target)
    if second_part_index != -1:
        return second_part_index + pivot_index

    return -1
