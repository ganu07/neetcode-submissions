class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        rev_list = [1] * len(nums)
        fwd_list = [1] * len(nums)
        op = [1] * len(nums)

        for i in range(1, len(nums)):
            fwd_list[i] = fwd_list[i-1] * nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            rev_list[j] = rev_list[j+1] * nums[j+1]

        
        for i in range(len(rev_list)):
            op[i] = rev_list[i] * fwd_list[i]
        

        return op


        