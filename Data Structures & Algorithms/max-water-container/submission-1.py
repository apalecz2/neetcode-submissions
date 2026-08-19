# First off, how is the output being calculated?

# Is it the furthest apart highest? to get the max in between?
# and the other bars in between are ignored?

# So take (1, 7) and (7, 6), distance between 7 and 1 = 6, min(7, 6) = 6 
# 6 * 6 = 36


# Getting 2 pointer vibe (sliding window???)

# And start furthest apart probably

# so like i = 0, j = len(heights) - 1
# move the shorter one in (what if equal? -> choose )


# or no, do we choose the one with the next highest?



# 2 pointers, so we are at most constant space, linear time

# Just will this always give the max?
# -> yes as long as it starts on the outside

# 1. Init pointers at start and end
# 2. Init max holder

# 3. while left < right:
#       calc max, update compared to stored max
#       update left or right, based on which has the next highest value



class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # 1.

        left = 0
        right = len(heights) - 1

        # 2.
        max_val = float('-inf')

        # 3. 
        while left < right:
            
            distance = right - left

            
            
            lower_height = min(heights[left], heights[right])

            area = distance * lower_height

            # Update max
            max_val = max(area, max_val)

            # Update pointers

            if distance == 1:
                break
            
            # Just move the smaller one inwards
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return max_val








            







        