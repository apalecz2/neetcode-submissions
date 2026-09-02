


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        memo = {}

        def dfs(remainder):

            if remainder == 0:
                return 0
            
            if remainder < 0:
                return float('inf')

            if remainder in memo:
                return memo[remainder]
            
            min_coins = float('inf')


            for coin in coins:
                result = dfs(remainder - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)
            
            memo[remainder] = min_coins
            return min_coins


        answer = dfs(amount)
        return answer if answer != float('inf') else -1
            


            


        