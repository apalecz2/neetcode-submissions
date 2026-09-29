class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # backtrack, maintain path of what's left to be chosen


        self.perms = []

        def backtrack(path, left):
            
            # base case:
            # left has no more, add path to perms
            if not left:
                self.perms.append(path[:])
                return
            
            # otherwise pick a num from left, recurse
            for v in list(left):
                left.remove(v)
                path.append(v)
                backtrack(path, left)

                path.pop()
                left.add(v)
            
        

        left = set(nums)

        backtrack([], left)

        return self.perms
            
