"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""



class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        # original nodes to newly cloned corresponding nodes
        old_to_new = {}

        # walk the graph
        def dfs(curr):

            # checks if the node has already been processed
            # return the new node early if so
            if curr in old_to_new:
                return old_to_new[curr]
            
            # make the node, add to map
            copy = Node(curr.val)
            old_to_new[curr] = copy

            # for all the neighboring nodes, run dfs on it
            # which will return the new node for that neighbor
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        

        return dfs(node)



        