class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i, number in enumerate(nums):
            diff = target - number
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[number] = i
        
        