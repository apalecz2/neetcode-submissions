class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # start a dfs on all squares, track max length found
        # mark visited

        # O(n*m) time, O(1) space since visits will be tracked
        # in place, and the max is a single variable

        self.curr_length = 0


        def dfs(i, j):
            
            # 1. Check bounds, if outside grid return
            if i < 0 or i >= len(grid):
                return
            
            if j < 0 or j >= len(grid[0]):
                return

            # 2. Check value, if # - visited, return
            # if 0 - water return
            # if 1 - add to count, recurse on cardinals

            if grid[i][j] == "#" or grid[i][j] == 0:
                return
            else:
                # recurse
                # add to 
                
                # mark visited
                grid[i][j] = "#"

                self.curr_length += 1
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        
        max_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.curr_length = 0
                    dfs(i, j)
                    max_count = max(max_count, self.curr_length)
        
        return max_count
        