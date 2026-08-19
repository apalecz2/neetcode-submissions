
# log n means binary search
# how can we find the location of the rotation where the min and max are next to each other
# (in the original array this is [0] and [-1])

# at any position x check x-1 < x < x+1 
# if it doesn't hold the min value in these 3 vals is the min value
# need to allow it wrap around for rotated = n

# 1. Choose middle element
# 2. Check the above statement
#       if it's valid, 



# Choose mid point x=n/2, look ahead at y = x/2 and z = x + x/2

# if they're in order, that entire section is sorted
# if not, the wrap position exists in the bounds [y,z]

# absolutely on the right track

# just start y at 0, and z at n
# then 2 of them will be sorted, so discard that sorted half







class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        
        while left < right:

            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # mid to right out of order
                left = mid + 1
                # right stays the same
            else:
                # right side sorted
                right = mid # not + 1 since the comp was <= to get here
        
        # Now the search ends with left, right lying over the split
        # No mid because mid will = one of them
        return min(nums[left], nums[right])




























        