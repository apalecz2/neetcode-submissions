
# Brute force would be check all vals against all other vals
# O(n^2), meets the space requirement

# How to improve? Binary search? pick one value, narrow in on a value that could produce the target

# O(nlogn) time, with O(1) space.



# How to get to O(n)?


# Two pointers

# look at smallest at 0 + at len -1

# if greater than target, move down since len-1 couldn't be in an pair


# if it's less -> have to move the lowest up, since even with the highest we can't make target


# 1. init pointers
# loop left< right



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) - 1

        while left < right:

            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]
            # what if they're equal?
            # found the values
            # return the 1 - indexed val

        # there will always be a solution so no need to return here
            
