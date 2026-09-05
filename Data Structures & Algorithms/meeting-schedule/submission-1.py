"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        # sort
        intervals.sort(key = lambda x: x.start)

        # walk
        last = intervals[0]

        for i in range(1, len(intervals)):
            if last.end > intervals[i].start:
                # overlap -> conflict
                return False
            
            last = intervals[i]

        return True
