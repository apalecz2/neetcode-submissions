class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        val = n

        while val not in seen:

            if val == 1:
                return True

            seen.add(val)

            curr_sum = 0
            for digit in str(val):
                curr_sum += int(digit) * int(digit)
            
            
            val = curr_sum
        
        return False
        

        
        