class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        combs = []

        d_to_l = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


        def dfs(i, path):
            
            if i == len(digits):
                combs.append(path)
                return
            
            for l in d_to_l[digits[i]]:
                dfs(i + 1, path + l)


        dfs(0, "")

        return combs