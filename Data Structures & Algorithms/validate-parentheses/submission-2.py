class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []

        oc = {'(': ')', '{': '}', '[': ']'}
        co = {')': '(', '}': '{', ']': '['}

        for c in s:
            
            if not stack:
                stack.append(c)
                continue

            top = stack[-1]

            # new bracket is a close
            if c in co:
                # check the last, for a match to pop both
                if top in oc and c == oc[top]:
                    stack.pop()
                # not a match - does that mean it can never be valid?
                else:
                    return False
            
            elif c in oc:
                # new bracket is an open
                stack.append(c)
            
        
        if len(stack) == 0:
            return True
        else:
            return False



