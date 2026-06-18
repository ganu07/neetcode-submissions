"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        min_heap = [intervals[0].end]
        for interval in intervals[1:]:
            heapq.heappush(min_heap, interval.end)
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
                
        return len(min_heap)



        