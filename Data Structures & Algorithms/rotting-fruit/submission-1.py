from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        # bfs - queue all starting rotten
        # count time by depth of longest bfs

        # check over once q empty for any non rotten

        q = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        max_depth = 0

        while q:

            i, j, depth = q.popleft()

            max_depth = max(max_depth, depth)

            # check cardinals of this
            if i > 0 and grid[i - 1][j] == 1:
                grid[i - 1][j] = 2
                q.append((i - 1, j, depth + 1))
            
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                grid[i + 1][j] = 2
                q.append((i + 1, j, depth + 1))

            if j > 0 and grid[i][j - 1] == 1:
                grid[i][j - 1] = 2
                q.append((i, j - 1, depth + 1))

            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                grid[i][j + 1] = 2
                q.append((i, j + 1, depth + 1))
        

        # final pass to check for fresh fruit that couldn't be reached
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return max_depth
