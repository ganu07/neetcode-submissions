"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        if not intervals:
            return True
        prevend = intervals[0].end
        for i in intervals[1:]:
            # (0,30) (5, 10) (15, 20)
            if prevend > i.start:
                return False
            else:
                prevend = i.end
        
        return True

        
