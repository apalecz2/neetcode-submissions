
# probably sort

# for any issue where there's an overlap, how do we decide which to remove?
# if one of them overlaps another, we should remove that one, instead of removing 2 and keeping the one

# so count the overlaps at each interval?
# then since it's sorted, maybe we could 

# how?

# well brute force would be sort, then try all combos of intervals until the least are removed
# and none overlap
# which is O(2^n)

# constaint is 100k so we're looking for nlogn or n

# all vals are ints so bucket sort could be used here to keep it in n
# so n is probably the complexity we're trying for

# process the list. store a count of how many overlaps there are -> also needs a hashmap
# but counting in itself is already using n space, so n space for hm is fine in this approach

# still going to be n squared since we'd have to remove the highest count interval sequentially until no counts


# need to use the property we get from sorting
# which is:
# at any index i, if the curr interval overlaps the next, 


# is the answer in the count?
# i'd have to find a way to avoid counting twice. (or divide by 2??)
# since an overlap would count once for the first time we look at an interval and then again 
# when we look at the interval that overlaps with

# ---

# sort, then if theres an overlap, remove the second interval, since it's the only one of the 
# two that must be removed that could overlap with another interval
# add to count


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])

        count = 0
        last = None

        for interval in intervals:

            # if last, and overlap -> last end is before this start
            if last is not None and last[1] > interval[0]:
                count += 1

                # there is an overlap
                # remove the one that ends soonest
                if last[1] > interval[1]:
                    last = interval
                
                # else leave it at last
                    

            else:
                # continue walking normally
                last = interval
            
            


        return count






















        