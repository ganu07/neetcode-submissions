class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        result = nums[0]

        for n in nums:
            max_sum = max(max_sum+n, n)
            result = max(result, max_sum)
        
        return result 
        
