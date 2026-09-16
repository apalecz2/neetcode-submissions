class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_counter = [0] * 26

        for c in s1:
            i = ord(c) - ord('a')
            s1_counter[i] += 1

        window_counter = [0] * 26

        left = 0

        # start at 0 to count the start
        # only move left forward once the window is the right size of s1

        for right in range(len(s2)):

            # update counts
            c = s2[right]
            i = ord(c) - ord('a')
            window_counter[i] += 1

            # O(26)
            if window_counter == s1_counter:
                return True

            if right >= len(s1) - 1:
                c2 = s2[left]
                i2 = ord(c2) - ord('a')
                window_counter[i2] -= 1
                left += 1

        return False

        