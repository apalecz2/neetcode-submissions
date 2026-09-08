# dfs

# with n pairs of parenthesis
# pairs is key

# exponential paths

# backtracking

# walk down all open for length n
# add that 
# then backup, 

# can open n times and close n times

# so base case in dfs is depth = n
# then back up and form the next

# track how many open and closed?
# if open > closed 

# just check what the last item is in the current string



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        self.results = []

        def dfs(depth, current, open_count, close_count):
            
            # base case: add the fully formed generation to the results, stop this path
            if depth == n * 2:
                self.results.append(current)
                return
            
            # can always add an open bracket as long as they haven't all been used
            if open_count < n:
                dfs(depth + 1, current + "(", open_count + 1, close_count)
            
            # can add a close bracket if there's a matching open bracket for it
            if close_count < open_count:
                dfs(depth + 1, current + ")", open_count, close_count + 1)
            

        dfs(0, "", 0, 0)
        

        return self.results














