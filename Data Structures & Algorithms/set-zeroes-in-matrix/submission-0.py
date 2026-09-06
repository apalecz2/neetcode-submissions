class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows, cols = len(matrix), len(matrix[0])

        rZ = False


        # Mark first row / column vals as zero if any zero found in that row / col
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rZ = True
        
        # update the matrix contents with zeros based on the markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # base case for first column
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # 0,0 is for marking the column , and can't mark the row too,
        # so check the extra var that says if the first row should 
        # be zeroed out or not, and apply it if so
        if rZ:
            for c in range(cols):
                matrix[0][c] = 0        