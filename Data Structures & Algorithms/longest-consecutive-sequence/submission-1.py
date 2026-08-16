class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        op = 0

        for n in nums_set:
            if n-1 not in nums_set:
                result = 1
                while n+result in nums_set:
                    result += 1
                op = max(op, result)

            
        return op
        
        

        