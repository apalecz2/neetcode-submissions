class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        memo = {}

        def seek(i, curr_sum):

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
                
            if i == len(nums):
                return 1 if curr_sum == target else 0
            

            curr_val = nums[i]

            # try adding this and recursing on the next
            # and try subtracking this + recursing

            add_path = seek(i + 1, curr_sum + curr_val)
            sub_path = seek(i + 1, curr_sum - curr_val)

            memo[(i, curr_sum)] = add_path + sub_path
            return memo[(i, curr_sum)]
        

        return seek(0, 0)

        
            


            