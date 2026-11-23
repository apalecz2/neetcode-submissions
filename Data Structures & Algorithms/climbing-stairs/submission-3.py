class Solution:
    def climbStairs(self, n: int) -> int:

        # table on ways to make n, start processing from top

        # base case is 1 stair = 1 way
        # 2 stairs = 2 ways

        memo = {1: 1, 2: 2}

        def getWays(stair_num):
            if stair_num in memo:
                return memo[stair_num]
            
            ways_from_n = getWays(stair_num - 1) + getWays(stair_num - 2)
            memo[stair_num] = ways_from_n
            return ways_from_n

        # fill the table starting from the close to the top, so later queries hit the hashmap
        for v in range(1, n):
            getWays(v)

        return getWays(n)
            





        