
# max the sum
# check all paths

# if the last house was chosen, can either pick the house after this, or 2 after
# or just skip again?


# rule:
# if last house was robbed skip this house
# if last house was not robbed, expand path of this house / expand path of skipping this

# how can we break into smaller problems?

# start at the end and work back, memo the shorter paths already expanded







class Solution:
    def rob(self, nums: List[int]) -> int:


        memo = {}


        def dfs(i):

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]
            else:
                
                memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))

            return memo[i]



        return dfs(0)

        