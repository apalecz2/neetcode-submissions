# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        #dfs, pre order traversal to make the array 

        if not root:
            return ""

        self.array = []
        
        def dfs(node):

            if not node:
                self.array.append(None)
                return
                
            self.array.append(node.val)

            dfs(node.left)

            dfs(node.right)
        
        dfs(root)


        string = ""
        for n in self.array:
            if n:
                string += str(n)
                string += ","
            else:
                string += "N"
                string += ","
        
        # has a trailing , - doesn't matter with split

        return string




        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        array = []

        vals = data.split(",")

        for v in vals:
            if v == "":
                continue
            if v == "N":
                array.append(None)
            else:
                array.append(int(v))
            
        if len(array) == 0:
            return None
        elif len(array) == 1:
            return TreeNode(array[0])
        

        self.i = 0

        def dfs():

            val = array[self.i] 
            self.i += 1

            if val == None:
                return None

            node = TreeNode(val)

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()



























