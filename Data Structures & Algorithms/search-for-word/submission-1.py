class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # start a dfs at each location
        # bound on if the cardinal direction is within 0 to len - 1

        # return fast if the letter is not the next required in the sequence

        # dfs(depth) where depth is the index of the character in word matching the depth of dfs

        
        # need to start dfs on all position on the board

        self.found = False

        def dfs(x, y, depth):
            
            # return early if we've already found a sequence
            if self.found:
                return
            
            # The char doesn't match the next expected in the sequence
            if board[x][y] != word[depth]:
                return
            
            # The char does match
            if board[x][y] == word[depth]:
                
                # The last char matches - since we return early in non matching cases, if the 
                # depth matches now, we know we have a valid path through the board that gives
                # the sequence in word
                if depth == len(word) - 1:
                    self.found = True
                    return

                temp = board[x][y]
                board[x][y] = "#"
                
                # if valid next char, but not complete yet, continue down dfs

                if y > 0:
                    dfs(x, y - 1, depth + 1)
                
                if y < len(board[0]) - 1:
                    dfs(x, y + 1, depth + 1)

                
                if x > 0:
                    dfs(x - 1, y, depth + 1)
                
                if x < len(board) - 1:
                    dfs(x + 1, y, depth + 1)
                
                board[x][y] = temp



        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, 0)
        
        return self.found

                

        