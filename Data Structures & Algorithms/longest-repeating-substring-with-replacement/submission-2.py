from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        # sliding window

        # track counts in window

        # expand right while the next char is the same as the max freq item, or we have room in k

        # close left until this is met again

        counter = defaultdict(int)

        left = 0

        mlen = 0

        mfreq = 0

        for right in range(len(s)):

            r = s[right]

            counter[r] += 1

            mfreq = max(mfreq, counter[r])

            while (right - left + 1) - mfreq > k:
                counter[s[left]] -= 1
                left += 1
            
            mlen = max(mlen, right - left + 1)
        
        return mlen
        