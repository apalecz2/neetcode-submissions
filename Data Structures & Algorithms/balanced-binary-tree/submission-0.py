# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # dfs, track height and pass up the depth below each node
        # need to do an post order traversal -> left, right, top

        # at each node, ask what the height is below at left, right, compare, continue if ok


        def process(node):
            
            if node is None:
                return 0

            hl = process(node.left)
            hr = process(node.right)

            if hl == -1 or hr == -1:
                return -1

            if (abs(hl - hr)) > 1:
                return -1
            # otherwise continue,
            # return the longer of left and right subtree as height of this node

            return max(hl, hr) + 1

        h = process(root)

        if h == -1:
            return False
        else:
            return True
        



        