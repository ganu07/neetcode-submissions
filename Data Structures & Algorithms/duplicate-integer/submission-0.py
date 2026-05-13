class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_dict = {}
        for num in nums:
            if num in hash_dict:
                return True
            else:
                hash_dict[num] = 1
        return False
    
