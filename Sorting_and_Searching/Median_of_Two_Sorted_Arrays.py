# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# TODO: fix and finish this
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    time complexity: O(log(m+n))
    """
    # num1 and num2 are sorted
    # find the median of the two sorted arrays
    # the median is the middle number if the length of the array is odd
    # or the average of the two middle numbers if the length of the array is even

    n = len(nums1)
    m = len(nums2)
    i = 0
    j = 0
    k = 0
    is_even = (n + m) % 2 == 0
    nums3 = [0] * ((n + m) // 2 + 1)
    while k < len(nums3):
        # if nums1 is empty
        if i == n:
            nums3[k] = nums2[j]
            j += 1
        # if nums2 is empty
        elif j == m:
            nums3[k] = nums1[i]
            i += 1
        # if nums1[i] < nums2[j]
        elif nums1[i] < nums2[j]:
            nums3[k] = nums1[i]
            i += 1
        # if nums1[i] >= nums2[j]
        else:
            nums3[k] = nums2[j]
            j += 1
        k += 1

    if is_even:
        return (nums3[-1] + nums3[-2]) / 2.0
    else:
        return nums3[-1]
