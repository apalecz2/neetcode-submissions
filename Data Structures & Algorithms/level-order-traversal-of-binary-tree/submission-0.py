# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recurse and count the depth, append nodes to the corresponding array

# pre order traversal (root, left, right)


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.result = []

        if not root:
            return self.result

        self.processNode(root, 1)

        return self.result


    def processNode(self, node, depth):

        if not node:
            return

        # at most we're going to be at a depth 1 larger than result
        # in this case we can't just access that next index in result
        # need to safely append
        if len(self.result) < depth:
            self.result.append([node.val])
        else:
            self.result[depth - 1].append(node.val)

        # add the value of this node to the array of the depth

        # recurse on left first, then right

        self.processNode(node.left, depth + 1)

        self.processNode(node.right, depth + 1)



