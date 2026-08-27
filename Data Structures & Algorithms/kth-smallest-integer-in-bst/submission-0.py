# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        # dfs in order, count steps to reach min (left most), then continue

        self.count = k
        self.result = None

        self.processNode(root)

        return self.result


    def processNode(self, node):

        if self.result:
            return

        if node.left:
            self.processNode(node.left)
        
        self.count -= 1
        if self.count == 0:
            self.result = node.val
            return

        if node.right:
            self.processNode(node.right)
        
        
            



