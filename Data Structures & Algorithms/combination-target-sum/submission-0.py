class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        


        # any combination
        # continue testing all subsets of sums and adding more of each element until the sum is past the target


        res = []

        current_combo = []

        def dfs(total, i):

            if total == target:
                res.append(current_combo.copy())
                return

            if total > target:
                return
            

            # do a dfs with each possible item chosen as next addition

            for j in range(i, len(nums)):
                n = nums[j]
                current_combo.append(n)
                dfs(total + n, i)
                current_combo.pop()
                i += 1
            
        

        dfs(0, 0)

        return res
            
            
            