# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# dfs, find path, compare and get the last common value
# this is a binary search tree. so search for p and q at the same time
# when the search process selects a differing node for the two, that is the last

# so simply, this just means, that once the value of the current node, splits the values of 
# p and q, return that node

# min(p, q) < curr_node.val < max(p, q):
    # return curr_node


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root:
            return None

        min_node = min(p.val, q.val)
        max_node = max(p.val, q.val)
        
        if min_node <= root.val and root.val <= max_node:
            # the current node is between p and q, thus splitting it
            return root
        
        # Now we must recurse down left or right depending on if they're larger or smaller
        if min_node <= root.val and max_node <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if min_node >= root.val and max_node >= root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        
        

        
        