class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # min cost to reach top starting at i
        memo = {}
        memo[len(cost) - 1] = cost[-1]

        def dfs(i):

            if i in memo:
                return memo[i]

            if i >= len(cost):
                return 0
            
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]

        

        return min(dfs(0), dfs(1))


        