# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# dfs, track max depth reached, update at each node

class Solution:

    max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        global max_depth
        
        if not root:
            return 0

        self.processNode(root, 1)

        return self.max_depth


    def processNode(self, node, depth):

        global max_depth

        # base case is leaf, update global max here
        if node.left is None and node.right is None:
            
            if depth > self.max_depth:
                self.max_depth = depth
        else:

            if node.left is not None:
                # continue down the left branch
                self.processNode(node.left, depth + 1)
        
            if node.right is not None:
                self.processNode(node.right, depth + 1)
        
        

        