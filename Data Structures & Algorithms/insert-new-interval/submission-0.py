
# we're bridging spans on the number line 0-100000 and saving the condensed span(s)

# walk intervals, and look at if the start of new interval is inside a current interval

# remember that non overlap

# binary search for where the start and end of the new interval are
# store the indexes. if either are between intervals, store a tuple of the two indexes it is between

# this leaves a few cases:
# if both the start and end found locations are single indexes, replace all the intervals in that 
# span with the new interval

# if they are the same, just insert the interval in that location
# this covers the edge cases of the new interval being before or after all the other intervals

# ---

# binary search wont benefit overall

# walk the array

# build a new list

# before: current interval ends before the new one starts -> append current interval
# after: curr interval starts after new one ends -> append new one, then all remaining -> done
# overlap: mutate new with the min of starts, and max of ends to merge


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        new = []

        placed = False

        for interval in intervals:

            if placed:
                new.append(interval)
                continue
            
            # this interval ends before the new one starts
            if interval[1] < newInterval[0]:
                new.append(interval)
                continue
            
            # this interval starts after the new one ends
            if interval[0] > newInterval[1]:
                new.append(newInterval)
                new.append(interval)
                placed = True
                continue
            
            # overlap occurs
            # only case left so no condition needs to be checked here
            merged = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            
            newInterval = merged
        
        if not placed: new.append(newInterval)
        
        return new







                