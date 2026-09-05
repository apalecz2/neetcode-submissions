"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


# any time there's a conflict, there needs to be 2 rooms
# rooms can be reused once that meeting is done
# so max concurent conflicts?


# store a counter, key by the end time, so the count at that can decrease once a walk over the intervals reaches there

# merge???
# count the number of merges that must happen to stop conflicts from happening
# this is a local count for each interval, and how many intervals conflict with it
# then take the max of these

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:


        starts = sorted(intervals, key=lambda x: x.start)

        ends = sorted(intervals, key=lambda x: x.end)

        max_count = 0
        count = 0

        s = 0
        e = 0

        while s < len(intervals):
            if starts[s].start < ends[e].end:
                count += 1
                if count > max_count:
                    max_count = count
                s += 1
            
            if s < len(starts) and ends[e].end <= starts[s].start:
                count -= 1
                e += 1

        return max_count
        
        