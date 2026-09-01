
# since it's circular, do we need to try to start a search at each index?

# same as before, memo table solved subproblems

# what are the subproblems?

# before the base case was i >= len(nums) return 0

# since it wraps this can't be done


# just do the first version of the question twice
# once for house 1 to house n - 2 (inclusive)
# again for house 2 to house n inclusive


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def dfs(i, nums_split):

            if i >= len(nums_split):
                return 0
            
            if i in memo:
                return memo[i]

            memo[i] = max(nums_split[i] + dfs(i + 2, nums_split), dfs(i + 1, nums_split))
            return memo[i]
        
        memo = {}
        first = dfs(0, nums[:len(nums) - 1])
        memo = {}
        second = dfs(0, nums[1:])

        return max(first, second)
            
            
        