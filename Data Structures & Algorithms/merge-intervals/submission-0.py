# not sorted -> sort

# then walk intervals, and look at adjacent intervals

# if the next interval starts before the end of the current interval
# merge - use max and min values

# if the next starts after, just move to the next



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by the start of the interval
        intervals.sort(key=lambda i: i[0])

        new = []

        # 0 to the second last interval
        i = 0 

        while i < (len(intervals) - 1):
            
            curr = intervals[i]
            nxt = intervals[i + 1]

            # next starts before end of current - merge
            if nxt[0] <= curr[1]:
                merged = [min(nxt[0], curr[0]), max(nxt[1], curr[1])]
                intervals[i + 1] = merged # don't add to the new array yet since it might get merged with again
                i += 1
                continue # don't increment i since we need to check this merged interval with the next still
            
            # otherwise just add this interval

            new.append(curr)
            
            i += 1
        
        # check the end
        if intervals:
            new.append(intervals[-1])
            


        return new



        