# Given two integer arrays nums1 and nums2,
# return an array of their intersection.
# Each element in the result must be unique, and you may return the result in any order.
def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    # nums1 and nums2 are not sorted
    # find the intersection of the two arrays

    # create a set of nums2
    nums2_set = set(nums2)

    ans = []
    for num in nums1:
        if nums2_set.__contains__(num):
            ans.append(num)
            # remove the num from the set, so that we don't add it again
            nums2_set.remove(num)

    return ans