class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        op = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue 
            j, k = i+1, len(nums) - 1
            while j < k:
                triplet = nums[i] + nums[j] + nums[k]
                if triplet > 0:
                    k -= 1
                elif triplet < 0:
                    j += 1
                elif triplet == 0:
                    op.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
        
        return op

        