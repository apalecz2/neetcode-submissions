from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        


        # sliding window

        # dequeue

        # largest val is always in left position of deque

        # 1. Init window

        
        right = 0

        q = deque([])

        max_vals = []

        while right < k:
            
            # Logic to enter and exist new vals into deque
            while q and nums[q[-1]] <= nums[right]:
                q.pop()
            
            # Add the new value
            q.append(right)


            right += 1

        # Add the max from the first window
        max_vals.append(nums[q[0]])

        left = 1

        while right < len(nums):

            while q and nums[q[-1]] <= nums[right]:
                q.pop()
            
            q.append(right)

            while q and q[0] < left:
                q.popleft()



            
            # Append max
            max_vals.append(nums[q[0]])

            right += 1
            left += 1
        
        return max_vals


        