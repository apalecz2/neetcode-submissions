# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # bottom up swap at each node


        def process(node):

            if not node:
                return
            
            process(node.left)
            process(node.right)
            
            l = node.left
            node.left = node.right
            node.right = l

        
        process(root)
        return root
