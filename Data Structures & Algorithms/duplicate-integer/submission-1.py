class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_dict = {}

        for i in range(len(nums)):
            if nums[i] in hash_dict:
                return True
            else:
                hash_dict[nums[i]] = 1
        
        return False
    
