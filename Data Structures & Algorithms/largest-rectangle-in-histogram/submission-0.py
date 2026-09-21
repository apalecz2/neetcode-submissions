
# can take the max of the heights and take that as the starting point
# then check subsets taking the min height and length

# start from full length and the min of heights, then move in the lower side



# start from the max, try left and right, min x len

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        n = len(heights)

        max_area = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area