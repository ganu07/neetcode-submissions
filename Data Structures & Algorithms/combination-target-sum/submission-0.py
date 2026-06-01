class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrace(start, current, remaining):
            if remaining == 0:
                result.append(current.copy())
            
            if remaining < 0:
                return
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrace(i, current, remaining - nums[i])
                current.pop()

        
        backtrace(0, [], target)
        return result

        