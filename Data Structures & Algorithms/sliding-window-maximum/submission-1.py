
# strong heap vibes

# O(1) retrieval for each max (done at each step)

# O(n) window steps. Adding and removing the entering and exiting value at each step is 2 * O(logk)

# = O(nlogk) time, O(k) space


# ---------------


# Valid but not quite optimal - use monotonic queue. 


# 

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = 1

        max_windows = []

        dq = deque([])

        for right in range(k):
            
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)
        
        # Now the deque has the largest val at 0
        max_windows.append(nums[dq[0]])




        for right in range(k, len(nums)):

            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            
            # Evict items in dq no longer in window but that still may be left

            while dq[0] < left:
                dq.popleft()



            max_windows.append(nums[dq[0]])

            left += 1



        return max_windows
            


            


        