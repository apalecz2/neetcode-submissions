
class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        memo = {}
        
        # length, i index, j index inclusive of longest palindrome
        longest = [0, None, None]


        def checkSubstring(i, j):

            if i == j:
                memo[(i, j)] = True
                if longest[0] == 0:
                    longest[0] = 1
                    longest[1] = i
                    longest[2] = j
            
            if j == i + 1:
                if j < len(s):
                    if s[i] == s[j]:
                        memo[(i, j)] = True
                        if longest[0] < (j - i + 1):
                            longest[0] = (j - i + 1)
                            longest[1] = i
                            longest[2] = j


            if (i+1, j-1) in memo and memo[(i+1, j-1)] == True:
                # the inner part is a palindrome
                # if i = j, the entire i to j is a palindrome
                if s[i] == s[j]:
                    memo[(i, j)] = True

                    # update longest found if this is longer
                    if longest[0] < (j - i + 1):
                        longest[0] = (j - i + 1)
                        longest[1] = i
                        longest[2] = j
                    

            

        for i in range(len(s)):
            checkSubstring(i, i)
            
        # k is window size growing from 2, to len(s) - 1
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
            
        return s[longest[1]:longest[2] + 1]

















