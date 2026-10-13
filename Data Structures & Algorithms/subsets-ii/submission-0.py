class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # sort, then walk forward

        nums.sort()

        # start with empty set
        all_ss = []
        

        def dfs(i, sub_set):

            if i >= len(nums):
                all_ss.append(sub_set)
                return
            
            # either skip this or add this
            nxt = sub_set + [nums[i]]
            dfs(i + 1, nxt)

            # skip to the next i that has a new val
            # if it's a valid index, recurse on it
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            dfs(j, sub_set)  


        dfs(0, [])

        return all_ss
        