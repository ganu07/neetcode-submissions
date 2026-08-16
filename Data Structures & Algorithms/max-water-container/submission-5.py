class Solution:
    def maxArea(self, heights: List[int]) -> int:     
        op = 0
        l = 0
        r = len(heights) - 1
    
        while l < r:
            max_left = heights[l]
            max_right = heights[r]
            max_storage = (r-l) * min(max_left, max_right)
            op = max(op, max_storage)

            if max_left > max_right:
                r -= 1
            else:
                l += 1
        
        return op




        
       