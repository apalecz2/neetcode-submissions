class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # at each index store the value we would need to see later in nums to make target

        need = {}

        for i in range(len(nums)):

            n = nums[i]

            if n in need:
                return [need[n], i]
            
            need[target - n] = i


