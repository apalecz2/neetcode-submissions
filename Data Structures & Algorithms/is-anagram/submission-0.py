# Initial thoughts:
# hashmap for count of each letter in the 2 strings
# 2 * O(length)
# then compare the 2 strings -- see if counts match



# base case: are strings the same length?

# we can use a single hashmap as a working area
# process both strings at the same time
# with s we add to the count, with t we decrease from the count
# at the end we can just check if the hashmap is empty or not,
#   since it will equal out if the 2 strings have the same count
#   of each letter (anagrams)

# This approach is: O(length) time, O(length) memory

# Recommended time is m + n (2 * length), and O(1) memory
# how do we get constant memory???
#   aha -- look at the constraints -> lowercase english chars only
#       this is O(1) since a hashmap of length 26 is still O(1)

# 1. Check base case -- same length
# 2. Init map
#       (even checking over the map for all 0 counts is O(1) since just always 26 times)
# 3. Walk s and t 1 char at a time, add / subtrack that char from the map
# 4. Walk items in map for non 0 entries
#   if all 0, the strings are anagrams, else they are not

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        counts = defaultdict(int) 

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            counts[char_s] += 1
            counts[char_t] -= 1
        
        for key, value in counts.items():
            if value != 0:
                return False
        
        return True



















