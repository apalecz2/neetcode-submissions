
# so definitely a O(1) time formula for this
# that just maps m,n to path num
# probably like a geometric sequence sum or something


# for the dp approach
# memo # of paths from intermediate positions working backward

# so for 1 above the goal, there is 1 path. 


# maybe store the distances to the goal, in x and y?
# so key in memo table is (x,y) tuple of distance, then val is paths?
# distance or just the x,y coord of the square doesn't make a difference

# at any square the number of paths is the sum of 
# the number of paths from the square below it (if present)
# + the num of paths from the square to the right (if present)

# base case is at the bottom right corner, the num of paths is 0

# init the memo as 2d array by position, that will just hold the number of paths
# from that index

# 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = [[None for _ in range(n)] for _ in range(m)]

        memo[m-1][n-1] = 1


        def process(i,j):

            if i >= m or j >= n:
                return 0

            if memo[i][j] is None:
                memo[i][j] = process(i + 1, j) + process(i, j + 1)
                return memo[i][j]
            else:
                return memo[i][j]
            
        
        return process(0, 0)



        