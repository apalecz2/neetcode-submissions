# if any cycle exists, it cannot be a tree


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False


        # map child to parent (and back, undirected)
        relation = {i: [] for i in range(n)}

        for edge in edges:
            parent, child = edge        
            relation[parent].append(child)
            relation[child].append(parent)

        def dfs(val, parent):

            if val in self.visited:
                return

            self.visited.add(val)

            if parent is None:
                for c in relation[val]:
                    dfs(c, val)
            else:
                for c in relation[val]:
                    if c != parent:
                        dfs(c, val)
            
            

        
        self.visited = set()

        dfs(0, None)

        if len(self.visited) != n:
            return False

        return True
        



