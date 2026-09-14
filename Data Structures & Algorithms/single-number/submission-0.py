
# sum and negative sum, difference is the value??

# running sum
# bit logic

# xor

# xor with itself is 0

# walk nums, xor each with a var to hold the cumulative xor value
# 



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        xor = 0

        for n in nums:
            xor = xor ^ n

        
        return xor