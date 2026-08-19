# Understanding:

# return an amount of the most frequent integers from the list, specified by k

# Vibe is this can be done in a single pass. Can it be done in constant memory?

# first thought is hashmap counter, then walk through hm and grab the k highest


# this would be O(n) to build counter, + O(n) to walk hm and take highest = O(n) time
# and O(n) memory

# since k is less than or equal to the size of n -- still O(n) space if all k items are built into new array to be returned


# New problem: keeping the elements as the hm is walked the highest elements, without sorting or looping over the hm
#       how can this be solved in linear time??
#       heap / in place array heap sort one at a time


# 1. Build counter hashmap -- key is number (int value), value is count
# 2. For each k, v:
#       if v > lowest in return array: 

# ??? need sorting so no



# is this not the approach then?


# ** checked topics

# seeing bucket sort in the topics list is jogging my memory for that


# max frequency of an item is length of the array if all items are the same



# array -- buckets -- index is the frequency -- so length of array + 1 because 0 would not happen


# so 1. is make the hm of the counts, then 2 is to place each count into the bucket for that amount, then 3 is to pick k from here

# = O(n) to make the counts
# + O(n) to place each count
# + O(k) to pick k (but k <= n)

# = at most / worst 3n = O(n)

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 1.
        counts = defaultdict(int)

        for i in range(len(nums)):
            val = nums[i]

            counts[val] += 1
        
        # 2.
        buckets = [[] for _ in range(len(nums) + 1)]

        for int_from_nums, count_of_int in counts.items():
            # key is the int, val is the count

            # place in corresponding bucket to count (bounded by length of array if all 1 value)

            buckets[count_of_int].append(int_from_nums)
        
        # 3. Walk bucket from most downwards

        k_highest = []


        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i] != []:
                arr = buckets[i]
                for j in range(len(arr)):
                    k_highest.append(arr[j])
                    if len(k_highest) == k:
                        return k_highest



        