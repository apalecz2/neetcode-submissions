# two pointers?


# i = 0, j = len - 1

# end case?

# either odd or even

# Even: they'll end up next to each other, if they are the same up to and including this position return true
# Odd: they'll end up on the same position, if that happens return true

# if at any point, the values don't match, return false



class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        # odd: they'll be equal and then it'll stop next iteration = good
        # even: they'll be beside, then swap and the condition wont clear
        while left <= right:
            
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            

            if s[left].upper() != s[right].upper():
                return False


            left += 1
            right -= 1
        
        return True


        
        
