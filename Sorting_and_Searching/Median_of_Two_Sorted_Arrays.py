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
    is_odd = (n + m) % 2 == 1
    median = 0
    while i + j < (n + m) // 2 + 1:
        if i == n:
            median = nums2[j]
            j += 1
        elif j == m:
            median = nums1[i]
            i += 1
        elif nums1[i] < nums2[j]:
            median = nums1[i]
            i += 1
        else:
            median = nums2[j]
            j += 1
    if is_odd:
        return median
    else:
        if i == n:
            return (median + nums2[j]) / 2
        elif j == m:
            return (median + nums1[i]) / 2
        else:
            return (median + min(nums1[i], nums2[j])) / 2


