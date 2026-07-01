class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        def dfs(start, current, remaining):
            if remaining == 0:
                res.append(current.copy())
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                dfs(i, current, remaining-nums[i])
                current.pop()


        dfs(0, [], target)
        return res
        






        