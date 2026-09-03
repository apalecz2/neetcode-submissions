

# can't return early from any window expanding outward (except for 0s)
# since a negative value could appear again or any number of times

# how can this be smaller problems?
# start with length 1 subarrays, then all length 2, ...

# memo each, and use each when computing larger subarrays


# memo on the indexs, for single index use i twice (i, i)
# store the product as the value

# then slide windows across

# there's no way to not check all possible subarrays
# since any non zero value could increase the product
# (don't know if there's odd or even negative values in subarray)




class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result = max(nums)

        curr_min = 1
        curr_max = 1

        for n in nums:

            p_min = curr_min * n
            p_max = curr_max * n

            curr_max = max(n, p_min, p_max)
            curr_min = min(n, p_max, p_min)
            
            result = max(curr_max, result)
        
        return result


        


