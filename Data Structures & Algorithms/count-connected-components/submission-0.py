class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        # track visited
        # start dfs on each node, stop short if in visited,
        # else on the first call increment count

        # O(V) space for the 
        # O(V + E) time, O(E) to build map, O(V) to run dfs on all nodes
        #       each node is only processed once (where it can recurse if nei present)

        relations = {i: [] for i in range(n)}

        for edge in edges:
            a, b = edge
            relations[a].append(b)
            relations[b].append(a)
        

        def dfs(val, depth, visited):

            if val in visited:
                return
            
            if depth == 0:
                self.counter += 1
            
            visited.add(val)

            for nei in relations[val]:
                dfs(nei, 1, visited)
            

        
        self.counter = 0
        visited = set()

        for node in relations.keys():

            dfs(node, 0, visited)
        
        return self.counter



