
# dp to store distances between points?

# graphs

# min deps

# min spanning tree





class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # 1. Get and store all distances
        # 2. Sort edges based on weights
        # 3. Traverse edges, connect nodes

        edges = []

        for i in range(len(points)):

            p1 = points[i]

            for j in range(len(points)):
                if i == j: continue

                p2 = points[j]

                dist = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

                edges.append([dist, i, j])

        edges.sort()


        parent = [i for i in range(len(points))]

        rank = [1] * len(points)

        def find(n):

            if parent[n] == n:
                return n
            
            parent[n] = find(parent[n])
            return parent[n]


        def union(n1, n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        res = 0
        edges_con = 0
        
        for cost, i, j in edges:
            if union(i, j):

                res += cost
                edges_con += 1

                if edges_con == len(points) - 1:
                    break
        
        return res














