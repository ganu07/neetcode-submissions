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
        first_meeting_start = intervals[0].start
        meeting_rooms = 1

        for interval in intervals[1:]:
            start_time = interval.start
            end_time = interval.end
            heapq.heappush(min_heap, end_time)
            if min_heap and min_heap[0] <= start_time:
                heapq.heappop(min_heap)
                
        
        return len(min_heap)



        