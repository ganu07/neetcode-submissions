class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        c = 0

        prev = intervals[0][1]
        for interval in intervals[1:]:
            if prev <= interval[0]:
                prev = interval[1]
            else:
                c += 1
        
        return c




            
 