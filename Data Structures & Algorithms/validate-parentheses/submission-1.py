# stack

# push all open ended ones

# pop if the last item was the corresponding open (top stack)

# if stack empty after s done, = valid



class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        open_pare = {"(": ")", "{": "}", "[": "]"}
        close_pare = {")": "(", "}": "{", "]": "["}

        for bracket in s:

            if bracket in open_pare.keys():
                stack.append(bracket)
            else:
                # bracket is close bracket, attempt to pop it's corresponding open
                if len(stack) == 0:
                    return False
                top = stack[-1]
                
                # If the current close bracket, matches it's open bracket at the top of the stack, pop that open b
                if close_pare[bracket] == top:
                    stack.pop()
                else:
                    # Bracket is a close bracket that doesn't match the top of the stack
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
            




        