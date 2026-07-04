class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <=2:
            return max(nums)
        
        def helper(n):
            if len(n) <=2:
                return max(n)
            
            first_house = n[0]
            second_house = max(first_house, n[1])
            for i in range(2, len(n)):
                temp = max(n[i] + first_house, second_house)
                first_house = second_house
                second_house = temp
            
            return second_house
            

        return max(helper(nums[1:]), helper(nums[:-1]))
        
