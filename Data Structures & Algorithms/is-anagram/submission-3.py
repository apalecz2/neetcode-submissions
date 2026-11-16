class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        s_counter = [0] * 26
        t_counter = [0] * 26

        # O(N) time, where N is s.length
        for c in s:
            s_counter[ord(c) - ord('a')] += 1
        
        # O(M) time, where M is t.length
        for c in t:
            t_counter[ord(c) - ord('a')] += 1
        
        # O(1) since both arrays are 26 elements
        return s_counter == t_counter