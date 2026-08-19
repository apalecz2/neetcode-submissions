# given array and target, get i and j to sum to target, i not j




# nums[i] == target - nums[j]
# 3 == 7 - 3
# 3 == 7 - 4 yes

# OHHH

# hashmap to store index and processed target - j value

# key is index, value is target - 

# Store: 
# key is index. at each index store the value nums at that index subtracted from target

# so 0: 4, 1: 3, 2: 2, 3: 1

# no its key is the difference.
# 4: 0, 3: 1, 2: 2, 1: 3

# then with this, loop over nums. if the current num is in the hashmap as a key, we know the index

# for example:
# nums[0] is 3. So check for 3 in the hm. Exists. And the value is 1, which is the index of the value we need to get the target



# 1. Build hashmap of these values. Key as difference, value as index of the corresponding number to make that

# 2. Loop over nums

from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 1.
        difference = defaultdict(int)

        for i in range(len(nums)):
            key = target - nums[i]
            value = i

            difference[key] = value
        
        # 2.
        for i in range(len(nums)):
            if nums[i] in difference:
                if i != difference[nums[i]]:
                    return [i, difference[nums[i]]]





