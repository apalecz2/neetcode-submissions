


from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counts = [0] * 26

        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        for c in t:
            counts[ord(c) - ord('a')] -= 1
        
        for l in counts:
            if l > 0 or l < 0:
                return False
        
        return True