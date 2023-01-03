import TreeNodes


# TODO : fix and finish this

# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    if node is None:
        return None
    else:
        return TreeNodes.Node(node.val, [cloneGraph(neighbor) for neighbor in node.neighbors])


# test run
root = TreeNodes.Node(3)
root.neighbors = [TreeNodes.Node(9), TreeNodes.Node(20)]
root.neighbors[1].neighbors = [TreeNodes.Node(15), TreeNodes.Node(7)]
