# need to start a dfs from each element
# swap 1s to # once processed as part of an island

# global counter, increment on 1 found at start of dfs


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        # basically just process all connected 1s and convert to # to mark as processed
        def dfs(x, y):

            if grid[x][y] == "0": return
            if grid[x][y] == "#": return

            # must be a 1, so mark as processed
            grid[x][y] = "#"

            # recurse on cardinal adjacencies
            if x > 0: dfs(x - 1, y)
            if x < len(grid) - 1: dfs(x + 1, y)
            if y > 0: dfs(x, y - 1)
            if y < len(grid[0]) - 1: dfs(x, y + 1)

        
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count

        