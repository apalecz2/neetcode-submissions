# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        # at each node check that left <= root <= right
        # recurse
        # need to do full tree, and keep track of where we've been, so O(H) space for call stack
        # and O(N) time to process all nodes

        # return true if the relation holds at a node, false if at any point below it doesn't to bubble back up

        
        # Guaranteed at least one node

        return self.processNode(root, float('-inf'), float('inf'))

    
    def processNode(self, node, min_val, max_val):

        # All leaves automatically hold
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False
        
        return self.processNode(node.left, min_val, node.val) and self.processNode(node.right, node.val, max_val)
                

        

        

        