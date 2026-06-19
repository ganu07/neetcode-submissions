class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        while n >0:
            last_number = n & 1
            count += last_number if last_number else 0
            n = n >> 1
        
        return count
        