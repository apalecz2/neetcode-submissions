# So you can pull from wherever in the list for the next element.

# throw it in a hashmap, start at min value -- can find while putting things in the map
# then increase by one each time, we find another value that's next?

# what if the first value is 1, and then second is 10,000? if we increment and check next if exists that won't work

# can't sort


# they need to be next to each other


# 1. Make hashmap of counts of each number
# 2. Walk list again. Each element, check if there's a next value in the array
# 3. If there is, add the count of the last number, and move to the next number to repeat and check after that.

# 4. If there isn't, check the subtotal of longest, against a global longest count. 


# Side note: also a bucket sort approach since it's all int values


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hs = set()

        for n in nums:
            hs.add(n)


        max_length = 0
        
        for i in range(len(nums)):

            number = nums[i]

            if i > 0 and number-1 in hs:
                continue

            # this value is now the start of a chain
            length = 1
            while True:
                if number + length in hs:
                    length += 1
                else:
                    break
            
            if length > max_length:
                max_length = length
        
        return max_length
            




















        