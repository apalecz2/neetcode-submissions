
# 2 options in most cases:
# can choose to take the next number as single letter, or next 2 as single letter
# next 2 requires that there are 2 more numbers


# memo table for the subproblems
# subproblems are to convert a segment into a character (at a location)
# so map index(s) to letter


# if (i, i+1) in hm: return hm[(i, i+1)]
# if i in hm: return hm[i]

# i mean I don't think this saves that much cause the computation at each to map to letter 
# would cost the same

# need to save the number of ways to process the numbers after that index (?)

# so memo # of ways beyond i

# dfs from start of s down recusively, then roll back up with the memoed counts

# then the answer is just the last returned value from this recursion



class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}

        def dfs(i):

            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0

            if i in memo:
                return memo[i]
            
            

            # just take this letter
            # add 1 for this digit (non zero from check above)
            just_this = dfs(i + 1)

            # try this char and next after it for 2 digit decoding
            # already know there's not a leading zero
            # so just take i and i+1 as a single decoding, then recurse on the i after that
            this_and_next = 0

            if i+1 < len(s):
                if int(s[i:i+2]) > 26:
                    # cannot take the 2 digits as a valid decoding
                    this_and_next = 0 # doesn't change anything, but marks the case
                else:
                    # the decoding of s[i:i+2] (2 digits) is valid (in 1-26 inclusive)
                    # so add 1 for that decoding and 
                    this_and_next = dfs(i + 2)

            # only add the count to the memo table once we have the full count for this index
            memo[i] = just_this + this_and_next

            return just_this + this_and_next


        return dfs(0)
        













