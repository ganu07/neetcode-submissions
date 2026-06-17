class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        prevend = intervals[0][1]
        for i in intervals[1:]:
            # [1, 2] [1, 4] [2, 4]
            if prevend <= i[0]:
                prevend = i[1]
            else:
                count += 1
        
        return count 




