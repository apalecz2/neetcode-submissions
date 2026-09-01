
# looks like smaller problems

# at each step, it branches
# into climb(n-1) and climb (n-2)

# recursion is prob to slow -> O(2^n) time and space
# but n is shrinking(?) as depth of recursion increases?

# start at the top of the stairs, memo table for each step
# log(n) (base 2 since 2 options of climbing) -> height of decision tree -> time and space since still recursion

# there is a constant time expression that would map this to the result (?)




class Solution:
    def climbStairs(self, n: int) -> int:


        # map key (step count from top) to value (ways to step there)
        memo = {0: 0, 1: 1, 2: 2}

        def climb(n):

            if n in memo:
                return memo[n]
            
            if n == 0:
                return 0
            
            if n == 1:
                return 1

            if n == 2:
                return 2
            
            memo[n] = climb(n-1) + climb(n-2)
            return memo[n]

        climb(n)

        return memo[n]

        