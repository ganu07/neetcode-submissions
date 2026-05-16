class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1
            while l < r:
                triplet = nums[i] + nums[l] + nums[r]
                if triplet == 0:
                    op.append([nums[i], nums[l], nums[r]])
                    l +=1 
                    r -= 1
                
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif triplet > 0:
                    r -= 1
                elif triplet < 0:
                    l += 1        

        return op

