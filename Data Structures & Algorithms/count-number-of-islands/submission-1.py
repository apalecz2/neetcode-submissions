class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        # Walk each element, expand and mark as searched as you go.
        # this way once you count an island, you never start to expand a search from any part again

        # O(n * m), since each el processed at most once
        # O(n * m), space for dfs recursion call stack

        def dfs(i, j):
            
            # check i and j are in bounds
            if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])):
                return
            
            # check this is still part of the island
            if grid[i][j] != "1":
                return

            # Mark as processed
            grid[i][j] = '#'

            # recurse for dfs in cardinals
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1": # if it's not 1, either it's water or processed already -> skip
                    count += 1
                    dfs(i, j)

        return count





        