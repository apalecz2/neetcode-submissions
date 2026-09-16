# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # max of sum of left height and right height

        # for any node, the longest path through it is the sum of height of left subtree and height of right subtree
        # then store max while processing all nodes

        self.max_len = 0


        def dfs(node):
            
            if not node:
                return 0
            
            
            h_left = dfs(node.left)
            h_right = dfs(node.right)

            total = h_left + h_right

            self.max_len = max(self.max_len, total)

            if total == 0:
                return 1

            return max(h_left, h_right) + 1


        dfs(root)

        return self.max_len