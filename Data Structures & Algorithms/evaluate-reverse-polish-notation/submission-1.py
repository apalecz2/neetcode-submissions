class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # stack

        # if top of stack is an operator, pop the last 2 items and perform that operator
        # push the answer, continue

        ops = {"+", "-", "*", "/"}

        stack = []

        for token in tokens:

            if token in ops:

                t1 = int(stack.pop())
                t2 = int(stack.pop())

                result = None

                if token == "+":
                    result = t2 + t1
                elif token == "-":
                    result = t2 - t1
                elif token == "*":
                    result = t2 * t1
                elif token == "/":
                    result = int(t2 / t1)
                

                stack.append(result)
                
            else:
                # push the number
                stack.append(token)
            
        # there should be 1 item in the stack which is the answer
        return int(stack[0])
        