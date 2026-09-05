class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # get it upside down
        matrix.reverse()

        # swap along main diagonal
        # for i < j swap i,j w/ j,i
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]