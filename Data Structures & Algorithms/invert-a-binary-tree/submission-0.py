# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# swap left and right at each node
# can do pre order or whatever


# we have to process each node once, aside from leaves so still just O(n) where n is num of nodes
# 

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        self.processNode(root)

        return root
        
    def processNode(self, node):
        
        # base case
        if node.left is None and node.right is None:
            # leaf node
            pass
        else:
            if node.left is not None:
                self.processNode(node.left)
        
            if node.right is not None:
                self.processNode(node.right)
        
            # Swap the two pointers of this node. All lower have been swapped by now
            # if one is None it doesn't matter
            temp = node.left
            node.left = node.right
            node.right = temp
