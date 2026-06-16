class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]
        # [1,3] [1,5] [6,7]

        i = 1
        for interval in intervals[i:]:
            last = result[-1]
            if interval[0] <= last[1]:
                last[1] = max(interval[1], last[1])
            else:
                result.append(interval)
        
        return result
