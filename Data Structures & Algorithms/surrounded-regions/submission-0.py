class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        # O(m * n) - only process a cell once
        # O(m * n) space for call stack if recursion dfs


        # what if I start from the edges?

        # maybe better on avg but not asymtoticly better, since everything could be O
        
        # start dfs from edges, mark all Os reachable with say #, then iterate over grid, swap all other Os to Xs
        # still also mn space for call stack if all Os



        def dfs(i, j):

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            
            if board[i][j] == "X" or board[i][j] == "#":
                return
            
            # curr is O
            # mark, recurse on cardinals

            board[i][j] = "#"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)



        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
        
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)
        
        # walk all, replace #s back with Os, Os with Xs
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        
