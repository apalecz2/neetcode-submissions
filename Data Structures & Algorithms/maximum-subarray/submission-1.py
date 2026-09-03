
# can maybe immediately discard a subarray once a negative value is reached?

# negative is always bad, unlike the maximum product question

# expand out from middle? no wont get anywhere

# constrains mean it can't be dp
# looking like nlogn could be the target based on the constraints
# 

# every time there's a negative number, start a new branch of the search
# on a subarray starting with that value.

# if it's still less than a previous subarray that's being checked currently
# it can never be larger  -> every new value that subarray gets, the original larger subarray
# will also get. (?)

# doesn't matter between the two options here, since the longer one and the 
# newer one will even out based on the condition being checked

# SO:
# walk nums
# on every negative num look at if starting a new array on that value (or the next value)
# will give a value greater than the current subarry

# this only works because the subarray is contiguous


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = 0
        max_sum = nums[0]

        for n in nums:

            # 1. add the new value
            curr_sum += n

            # 2. Make the new subarray starting here, to see if starting fresh will make a larger one
            # which is just n

            # if it's equal it doesn't matter which subarray is chosen
            if n > curr_sum:
                # discard the old subarray and sum
                curr_sum = n
            
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        return max_sum












        