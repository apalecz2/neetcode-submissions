
# Build 2 extra arrays

# prefix array with the highest value to the left of a given index
# suffix array with the highest value to the right of a given index

# then loop entire array

# foreach idx: water = min(prefix, suffix) - height[idx]







class Solution:
    def trap(self, height: List[int]) -> int:
        
        pre = [0] * len(height)
        suf = [0] * len(height)

        max_left = float("-inf")
        for i in range(len(height)):
            if height[i] > max_left:
                max_left = height[i]
            
            pre[i] = max_left

        max_right = float("-inf")
        # Bounds?
        for i in range(len(height) - 1, -1, -1):
            if height[i] > max_right:
                max_right = height[i]
            
            suf[i] = max_right
        

        water_sum = 0

        for i in range(len(height)):
            water_sum += min(pre[i], suf[i]) - height[i]

        
        return water_sum

