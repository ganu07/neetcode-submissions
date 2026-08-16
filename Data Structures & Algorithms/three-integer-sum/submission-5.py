class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_num = sorted(nums)
        op = []

        # -4 -1 -1 0 1 2 
        for i in range(len(sorted_num)):
            if i > 0 and sorted_num[i] == sorted_num[i-1]:
                continue
            l = i+1
            r = len(sorted_num) - 1

            while l<r:
                triplet = sorted_num[i] + sorted_num[l] + sorted_num[r]

                if triplet > 0:
                    r -= 1
                elif triplet < 0:
                    l += 1
                elif triplet == 0:
                    op.append([sorted_num[i], sorted_num[l], sorted_num[r]])
                    l += 1
                    r -= 1
                    while l<r and sorted_num[l] == sorted_num[l-1]:
                        l += 1
            
        return op

