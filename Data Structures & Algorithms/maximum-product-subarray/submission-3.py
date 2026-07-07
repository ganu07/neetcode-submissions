class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result  = max(nums)
        currmin, currmax = 1, 1

        for n in nums:
            temp = n * currmax
            currmax = max(n, n*currmax, n*currmin)
            currmin = min(n, n*currmin, temp)

            result = max(currmax, result)
        
        return result