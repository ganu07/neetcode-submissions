class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        total = 0

        while l < r:
            maxleft = heights[l]
            maxright = heights[r]
            et = (r-l) * min(maxleft, maxright)
            total = max(total, et)
            if maxleft < maxright:
                l += 1
            else:
                r -= 1
        
        return total




        