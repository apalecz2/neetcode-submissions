

# just going to expand right always. then if the expression no longer holds. shrink until it can

# how do i get the max frequency?

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = defaultdict(int)

        max_length = 0

        left = 0

        maxf = 0

        for right in range(len(s)):

            right_char = s[right]

            counter[right_char] += 1

            # Update the max frequency if the addition changed it
            maxf = max(maxf, counter[right_char])

            # Greater than k means that there are too many replacements needed, so shrink from left
            while (right - left + 1) - maxf > k:
                counter[s[left]] -= 1
                left += 1

            max_length = max(right - left + 1, max_length)

        
        return max_length








