class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r =0, len(numbers) - 1

        while l < r:
            et_t = numbers[r] + numbers[l]
            if et_t == target:
                return [l+1, r+1]
            elif et_t > target:
                r -= 1
            elif et_t < target:
                l += 1
            

        