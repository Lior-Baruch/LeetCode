import TreeNodes


# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    # if the node is None, return None
    if node is None:
        return None

    # create a dictionary to store the visited nodes
    visited = {}

    # create a queue to store the nodes to be visited, first in first out
    queue = [node]

    # create a new node with the same value as the node
    new_node = TreeNodes.Node(node.val)
    # add the new node to the visited dictionary
    visited[node] = new_node

    # while the queue is not empty
    while len(queue) > 0:
        # get the first node from the queue
        current_node = queue.pop(0)

        # get the neighbors of the current node
        neighbors = current_node.neighbors

        # for each neighbor
        for neighbor in neighbors:
            # if the neighbor is not visited
            if neighbor not in visited:
                # create a new node with the same value as the neighbor
                new_neighbor = TreeNodes.Node(neighbor.val)
                # add the new neighbor to the visited dictionary
                visited[neighbor] = new_neighbor
                # add the neighbor to the queue
                queue.append(neighbor)

            # add the new neighbor to the neighbors of the new node
            visited[current_node].neighbors.append(visited[neighbor])

    # return the new node
    return new_node
