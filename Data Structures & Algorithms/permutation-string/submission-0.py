
# sliding window of count

# is the length of the sliding window always the length of s1?


# 1. init pointers, left 0, right len s1
# 2. Build counter of s1


# main issue is how to compare each window against the counter of s1
# could get to O(n) * O(len(s1)),

# it only contains lower case letters, so array of 26 length
# means O(n) * O(1)






class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        s1_counter = [0] * 26

        for c in s1:
            s1_counter[ord(c)-ord('a')] += 1
        
        left = 0
        right = len(s1) - 1

        while right < len(s2):

            # build the counter for this window
            window_counter = [0] * 26

            for i in range(left, right + 1):
                curr_char = s2[i]
                window_counter[ord(curr_char) - ord('a')] += 1
            

            # compare against s1_counter
            if s1_counter == window_counter:
                return True

            # update window
            left += 1
            right += 1

        return False

        