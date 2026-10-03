from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # bfs
        # dfs would need to start from each chest and could overwrite each cell many times
        #   O(mn * mn)

        # traverse, add all treasure chest squares to queue
        # while q, continue on cardinals
        # water = continue
        # inf = write length
        
        # can we run into a value lower? no because bfs guarantees infs will be writen by the closest to a chest first

        q = deque()


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        def process(i, j, dist):
            if grid[i][j] == 2147483647:
                grid[i][j] = dist
                q.append((i, j, dist))
        
        while q:
            
            i, j, dist = q.popleft()

            # check cardinals
            if (i - 1) >= 0:
                process(i - 1, j, dist + 1)
            if (i + 1) < len(grid):
                process(i + 1, j, dist + 1)
            if (j - 1) >= 0:
                process(i, j - 1, dist + 1)
            if (j + 1) < len(grid[0]):
                process(i, j + 1, dist + 1)
        


