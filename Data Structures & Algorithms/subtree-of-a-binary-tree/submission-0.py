# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# start a full tree check at each occurence of current node being checked == subroot.val




class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        # Check l r trees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, root, subRoot):
        
        # both none
        if root is None and subRoot is None:
            return True
        
        if root is None or subRoot is None or root.val != subRoot.val:
            return False
        
        # Two nodes exist and match
        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        

        