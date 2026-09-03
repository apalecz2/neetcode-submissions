# cut up s, or build all strings with the words from the dict
# that are less than the length of s and check for a match

# that's the brute force


# smaller problems? 

# walk s once through i. walk the words in dict at the same rate (that match)
# once no more words match, a restart needs to take place (word boundary)

# this will branch each time a word stops matching the next char in s

# each branch needs to also be checked, until a valid path to make s is found

# ----

# so walk s. choose a word, or walk all matches? while they match

# start from the back, and memo on indexes of how you can reach the end

# what do I store? key is index, then value is T/F can you reach the end from here
# with the words in the dict



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {i: False for i in range(len(s))}

        for i in range(len(s) - 1, -1, -1):

            for word in wordDict:
                l = len(word)

                if i + l > len(s):
                    continue
                
                # base case of just if it reaches the end with a valid word
                if i + l == len(s) and s[i:i+l] == word:
                    memo[i] = True
                    break

                # if this split reaches an index that can reach the end from that index
                if s[i:i+l] == word and memo[i+l] == True:
                    memo[i] = True
                    break
            
        
        return memo[0]
            

        
            
        

            

        