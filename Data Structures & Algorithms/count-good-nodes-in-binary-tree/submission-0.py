# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # why not just track a max seen down each step?


        self.count = 0

        def process(node, max_seen):

            if node is None:
                return

            if node.val >= max_seen:
                self.count += 1
                max_seen = node.val

            process(node.left, max_seen)
            process(node.right, max_seen)
            


        process(root, float('-inf'))
        return self.count

