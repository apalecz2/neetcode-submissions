

# dfs, trim once the cumulative sum is over the target
# if it's equal we add to the count, trim dfs
# we have to fully explore all paths until they get trimmed here because we need all the counts
# cannot return early once we've found a valid solution like in coin change 1

# base case is the total is over the target
# then recurse on all coin in coins

# we can also dp store amounts that lead to a valid solution, and we can store the amount of 
# ways to get to the solution from a given value

# if curr amount in dp: return dp[curr amount]
# where dp stores the amount of ways to get to the target amount from curr amount

# how do we store the number of ways?

# also need to maybe store in a set, the ways found so we don't double count [1,3] and [3,1]
# just don't look back in the dfs?
# so when we're recursing, we just recurse on forward coins (or equal, but not back)

# dfs(subtotal, index)


# ---

# store the amount of ways so far to get from subtotal to amount
# 


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        self.dp = {}


        def dfs(subtotal, index):

            # subtotal is over: no possible way to get back to the amount, prune branch
            if subtotal > amount:
                return 0
            
            if subtotal == amount:
                return 1
            
            if (subtotal, index) in self.dp:
                return self.dp[(subtotal, index)]

            
            # recurse on all coins from the current coin of this recursion to the end of coins
            count = 0

            for i in range(index, len(coins)):
                count += dfs(subtotal + coins[i], i)

            self.dp[(subtotal, index)] = count
            return count
            
        

        # start on no coins added, and at the first element (coin)
        return dfs(0, 0)










