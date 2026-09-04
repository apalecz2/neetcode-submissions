
# so it branches, since you can jump less than max

# constrain is 1000, so dp is on the table. 

# dp approach is to:
# walk array
# memo if you can make it to a particular i

# why can't we just take nums[i] then what ever length that is, mark all elements in i + length as reachable
# then go to the last index marked from that length, and try to continue to mark.
# if that doesn't work, step back in a loop until you're back at i.
# if you get back to i, you can't make it. return false
# if you manage to get past length, continue recursively, but keep track that you didn't finish walking back to i

# still O(n^2) since 



# ----

# so just the key observation is that if you make it to a given index, you can make it to any index before that??
# no. just between i and the length of that element
# but that recursively works backwards. if you made it to i that means i - prior length to i is all reachable


# ---

# what if you just walk the array?
# keep it simple
# check the max jump first still, but then just go to the next
# if that doesn't get you past that original max


# keep a running var of the max reachable index as we iterate forward



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reachable_idx = 0

        for i in range(len(nums)):

            if i > max_reachable_idx:
                break

            jump = nums[i]

            land_on = i + jump

            if land_on > max_reachable_idx:
                max_reachable_idx = land_on
            
            if max_reachable_idx >= len(nums) - 1:
                return True
            
        return False
            

             



















