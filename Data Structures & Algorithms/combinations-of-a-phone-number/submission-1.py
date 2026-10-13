class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        combs = []

        d_to_l = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


        def dfs(path, remaining):
            
            if len(path) == len(digits):
                combs.append(path[:])
                return
            
            if not remaining:
                return
            nxt = remaining[-1]
            new_remaining = remaining[:-1]

            for l in d_to_l[nxt]:
                new_path = path + l
                dfs(new_path, new_remaining)



        if not digits:
            return []

        first = digits[0]
        rev = digits[::-1]
        rem = rev[:-1]
        for l in d_to_l[first]:
            dfs(l, rem)

        return combs