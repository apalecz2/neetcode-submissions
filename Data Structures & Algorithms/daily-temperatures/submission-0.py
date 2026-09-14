# go backwards?

# monotonic stack with 

# any time it increases, we need to walk back down the stack and write in the count of the walk
# to the output array at that i


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        out = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            # while stack, pop if less than current
            # store index so you can just get the distance between the current item and the pop
            

            while stack and stack[-1][0] < temp:

                # tuple 0 holds temp, 1 holds index
                pop_temp, pop_idx = stack.pop()

                dist = i - pop_idx

                out[pop_idx] = dist



            # push this item after
            stack.append((temp, i))

        return out




        