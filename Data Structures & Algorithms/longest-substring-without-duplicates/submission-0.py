
# longest substring no dup chars
# can use a set for ascii (still constant)

# sliding window over characters while not in counter
# move back and delete chars from counter

# each step we move 1 more to the end
# this will provide a char that is in the counter or not
#    if it is, we have to move the left pointer until that character isn't in the counter anymore

# 




from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0

        counter = defaultdict(int)

        left = 0

        for right in range(len(s)):

            # Logic for if the char is in already or not
            char = s[right]

            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

                # Move left side toward right until this char is back to 1
                # Don't forget to decrement / remove the other chars on the way

                while left <= right and counter[char] > 1:
                    left_char = s[left]

                    # Decrement counter at left char
                    if counter[left_char] > 1:
                        counter[left_char] -= 1
                    else:
                        # 1 or less than 1, so remove key so that the "not in" logic will fire
                        del counter[left_char]

                    left += 1
            
            # Here we are at a position where the counter has all values 1
            curr_length = right - left + 1
            if curr_length > max_length:
                max_length = curr_length

        return max_length


