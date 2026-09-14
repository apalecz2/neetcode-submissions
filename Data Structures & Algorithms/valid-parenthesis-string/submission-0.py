

# stack, dfs split each time we get a *

# if any path is valid, return true
# if we come up empty return false
# 

# O(n) time, and space

# pass the current stack into the dfs

# ideally we could trim a path if we knew there was no way to get enough closing brackets etc to make it valid 
# before getting to the bottom of a path


# dp

# memo table 

# ***

# choose ( for this, can't choose close
# could track open count, then not allow the next to be a close bracket if open count is not higher

# remaining space too could be looked at with open count vs distance to end using len(s)

# memo on index and if you can end


# what if you just keep track of min open and max open count
# single value that has to be able to be made 0

# 1. Loop s
# 2. each open - add 1, each close subtract 1, each * - add 1 to the max open, subtract 1 from min open
# 3. if at the end, max open



class Solution:
    def checkValidString(self, s: str) -> bool:

        max_open = 0
        min_open = 0

        

        for b in s:
            if b == "(":
                max_open += 1
                min_open += 1
            elif b == ")":
                max_open -= 1
                min_open -= 1
            elif b == "*":
                max_open += 1
                min_open -= 1
            
            if max_open < 0:
                return False
            
            if min_open < 0:
                min_open = 0
        

        return min_open == 0

        