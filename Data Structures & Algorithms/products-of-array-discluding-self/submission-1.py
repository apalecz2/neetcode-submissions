class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # walk left to right, and right to left
        # multiply all left of an index, with all right of an index

        left = [1] * len(nums)
        last = 1
        for i in range(1, len(nums)):
            left[i] = last * nums[i - 1]
            last = left[i]
            

        right = [1] * len(nums)
        last = 1
        for i in range(len(nums) - 2, -1, -1):
            right[i] = last * nums[i + 1]
            last = right[i]
        
        for i in range(len(nums)):
            nums[i] = left[i] * right[i]

        return nums

        

