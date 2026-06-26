class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)

        for n in nums_set:
            if n - 1 not in nums_set:
                longest = 1
                while n+longest in nums_set:
                    longest+= 1
                
                result = max(result, longest)

        return result


        