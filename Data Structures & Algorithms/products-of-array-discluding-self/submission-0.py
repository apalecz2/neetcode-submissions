
# Could do it by shifting by 1???

# [1, 2, 4, 6]

# Make second array where all items are the product of all others

# So at 1: 1 * 4 * 6 = 24

# keep sum of all except self and left, wrap



# pass once, to make an array with the product of all nums left of the index
# pass again the opposite direction with the product of all nums right


# left = [1, 1, 2, 8]
# right = [48,24,6,1]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1] * len(nums)
        right = [1] * len(nums)

        left_accumulator = 1
        for i in range(1, len(nums)):
            left[i] = left_accumulator * nums[i-1]
            left_accumulator = left[i]
        
        right_accumulator = 1
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right_accumulator * nums[i+1]
            right_accumulator = right[i]
        
        # now for each index, in left and right we 
        for i in range(len(nums)):
            nums[i] = left[i] * right[i]

        return nums

