
# Looking for the part of s that contains all of t (duplicates too)
# Specifically the shortest segment that contains this

# Counter is required to check a segment against T

# Sliding window - just how do we get the minimum window containing t, quickest?
# Naive thought is to start a window the size of the count of chars in t, slide across s and expand until valid soln found
# however in this case if the substring doesn't exist we expand up to the size of s which is O(n^2)


# Base case: if len(t) > len(s): return ""


# Aim for O(n+m)
# Recommended space just means use a hm for the chars in s and t



# 1. Base case
# 2. Build counter for t
# 3. Allocate var for window indeces to store min range that contains t
# 4. Slide window over s, increase right 
#       if right side reaches len(s) before a valid match is found, return ""





from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # 1. Base case
        if len(t) > len(s):
            return ""
        
        
        # 2. Build t counter - O(m)
        t_counter = defaultdict(int)

        for i in range(len(t)):
            if t[i] in t_counter:
                t_counter[t[i]] += 1
            else:
                t_counter[t[i]] = 1

        # 3. Pointers and found indeces for smallest subset
        left = 0

        smallest_left, smallest_right = 0, float('inf')

        have, need = 0, len(t_counter)

        window_counter = defaultdict(int)

        # 4. Window - O(n) * O(1)
        for right in range(len(s)):

            # 1. Update window counter with new right char
            # 2. Check the current window is greater than t_counter
            #       true: check the min subset bounds vars len against current window length, update accordingly
            #               then shrink from left side, while this holds, updating the window counter along the way
            #       false: just continue on and expand right on the next iter

            # O(52)
            window_sufficient_of_t = True

            window_counter[s[right]] += 1

            if s[right] in t_counter and window_counter[s[right]] == t_counter[s[right]]:
                have += 1

            if have < need:
                window_sufficient_of_t = False
            
            if window_sufficient_of_t:
                # The current window is valid and contains the subset we're looking for
                # Update the min bounds (if smaller currently)
                # Then bring up rear
                if (right - left) < (smallest_right - smallest_left):
                    smallest_right, smallest_left = right, left
                
                while left < right and window_sufficient_of_t:

                    # While the window is still valid, bring up rear, and reassess validity

                    # Increment left
                    # Decrement window_counter[left] first
                    
                    window_counter[s[left]] -= 1

                    
                    
                    if s[left] in t and window_counter[s[left]] < t_counter[s[left]]:
                        have -= 1

                    left += 1

                    # Check sufficiency again, if it's still sufficient we update bounds, else break, go to next iter
                    

                    if have < need:
                        window_sufficient_of_t = False
                    
                    if window_sufficient_of_t:
                        if (right - left) < (smallest_right - smallest_left):
                            smallest_right, smallest_left = right, left
                    


            # Need to check each window:
            #   For each key in t_counter, is current_window_counter[key] >= t_counter[key]

            # while we still have t in the current window, bring up the left side


        # Finally, the bounds would still be at default vals here, if no subset found
        if smallest_right == float('inf') and smallest_left == 0:
            return ""
        else:
            # return the segment cut from s by the found bounds - includes left, excludes right, so add 1 to right
            return s[smallest_left:smallest_right + 1]
















