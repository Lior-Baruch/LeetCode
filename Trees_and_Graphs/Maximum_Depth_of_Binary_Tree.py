import TreeNodes
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along
# the longest path from the root node down to the farthest leaf node.
def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    else:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))

# test run
root = TreeNodes.TreeNode(3)
root.left = TreeNodes.TreeNode(9)
root.right = TreeNodes.TreeNode(20)
root.right.left = TreeNodes.TreeNode(15)
root.right.right = TreeNodes.TreeNode(7)
print(maxDepth(root))

