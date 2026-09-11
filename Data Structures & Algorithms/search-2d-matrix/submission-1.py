

# binary search on the matrix

# key is just to find the mapping of i, j

# n * m // 2
# divide product of n and m by 2 to get the middle.
# round down to nearest whole n to get row, then remainder is steps to m


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of cols

        lo = 0
        hi = (m * n)

        while lo < hi:

            mid = (lo + hi) // 2

            mid_i = mid // n
            mid_j = mid % n

            if matrix[mid_i][mid_j] == target:
                return True

            if matrix[mid_i][mid_j] < target:
                lo = mid + 1
            else:
                hi = mid
        
        return False

        
        