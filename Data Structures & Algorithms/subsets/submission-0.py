class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # full subsets that have made a decision on all elements, are appended
        res = []

        # the current subset
        subset = []

        def dfs(i):
            
            # made a decision on all elements, append
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # append the current element and include the current element
            subset.append(nums[i])
            dfs(i + 1)

            # exclude this element and continue down
            subset.pop()
            dfs(i + 1)

        
        dfs(0)
        return res


