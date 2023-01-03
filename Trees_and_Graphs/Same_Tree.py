import TreeNodes

# Given the roots of two binary trees p and q,
# write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.



def isSameTree(p, q):
    """
    :type p: TreeNodes
    :type q: TreeNodes
    :rtype: bool
    """
    # if both trees are None, return True
    if p is None and q is None:
        return True
    # if one of the trees is None, return False
    if p is None or q is None:
        return False
    # if the values of the current nodes are not equal, return False
    if p.val != q.val:
        return False
    # return the result of the recursive calls
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)