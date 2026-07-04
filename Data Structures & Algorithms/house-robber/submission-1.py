class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return max(nums)

        first_house = nums[0]
        second_house = max(first_house, nums[1])

        for i in range(2, len(nums)):
            temp = max(first_house + nums[i], second_house)
            first_house = second_house
            second_house = temp
        
        return second_house