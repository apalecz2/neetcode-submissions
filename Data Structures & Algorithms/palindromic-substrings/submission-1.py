"""

initial dp approach with recursion

def countSubstrings(self, s: str) -> int:
        
        if len(s) == 1:
            return 1

        memo = {}

        self.count = 0

        def checkSubstring(i, j):

            if i == j:
                memo[(i, j)] = True
                self.count += 1
            
            if j == i + 1:
                if j < len(s):
                    if s[i] == s[j]:
                        memo[(i, j)] = True
                        self.count += 1
            
            # if inner is in memo, and s[i] == s[j], this is also a palindrome

            if (i + 1, j - 1) in memo and s[i] == s[j]:
                memo[(i, j)] = True
                self.count += 1
        


        # Add all length 1 strings to the memo table and count
        for i in range(len(s)):
            checkSubstring(i, i)
        
        # Slide windows of size k over s, with k increasing from 1 to len(s)
        k = 1
        while k < len(s):

            i = 0
            j = i + k

            if j >= len(s):
                break
            
            while j < len(s):
                checkSubstring(i, j)
                i += 1
                j += 1

            k += 1
            
        
        return self.count


"""



class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0

        # starting from each position/index in s, expand outwards as long as palindrome rule is met
        for i in range(len(s)):

            # centered on 1 character
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            # centered on 2 characters
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count






















