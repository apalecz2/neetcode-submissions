class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums.sort()

        res = []

        for i in range(len(nums) - 1):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:

                curr_sum = nums[i] + nums[j] + nums[k]

                if curr_sum > 0:
                    # too large, move larger number down
                    k = k - 1
                elif curr_sum < 0:
                    # too small, move smaller number up
                    j = j + 1
                else:
                    # = 0
                    res.append((nums[i], nums[j], nums[k]))

                    # move left forward
                    j = j + 1

                    while j < k and nums[j] == nums[j - 1]:
                        j = j + 1
        

        return res
                






        