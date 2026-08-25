# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# could build an array tracking them, then compare. O(N) time (runs 3 times) but O(N) space

# ideally O(H) space

# for any node in p, the node must be the same as q
# so just pass the mirror node from q into a recursive check on p



class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        return self.checkNode(p, q)



    def checkNode(self, node, mirror):

        # Both are leaves
        if node is None and mirror is None:
            return True
        
        # either is leaf, other is not
        if node is None and mirror:
            return False
        if node and mirror is None:
            return False
        
        # check all values match
        if node.val != mirror.val:
            return False
        
        # recurse
        left_match = self.checkNode(node.left, mirror.left)
        right_match = self.checkNode(node.right, mirror.right)

        if left_match and right_match:
            return True
        else:
            return False
        
        

        