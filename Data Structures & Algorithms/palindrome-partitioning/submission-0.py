class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # all length 1 strings are palindromes

        # backtracking?
        # could take the approach of starting a pal at each of these
        # then dp on indexes that are palindromes

        # length is 20. can i do dfs to get all contiguous substrings, then 
        # check if palindrome for each? 

        # its partitions
        # so you just have to check splits up from the length 1 array

        # so start with [a, a, b]
        # then try adding 1 merge first on 0,1, then 1,2, check if all are valid
        self.res = []

        def dfs(i, path):
            
            if i == len(s):
                self.res.append(path[:])
                return
            
            for idx in range(i, len(s)):
                if isPal(i, idx):
                    path.append(s[i : idx + 1])
                    dfs(idx + 1, path)
                    path.pop()

        
        def isPal(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True

        

        dfs(0, [])

        return self.res