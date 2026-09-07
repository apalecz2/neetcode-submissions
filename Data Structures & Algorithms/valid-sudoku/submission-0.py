

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".": continue

                val = board[r][c]
                if val in rows[r]: return False
                else: rows[r].add(val)
                if val in cols[c]: return False
                else: cols[c].add(val)

                if val in sqs[r // 3, c // 3]: return False
                else: sqs[r // 3, c // 3].add(val)
            
        return True
