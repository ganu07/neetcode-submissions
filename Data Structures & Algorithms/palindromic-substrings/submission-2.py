class Solution:
    def countSubstrings(self, s: str) -> int:
        
        result = 0
        def helper(left, right, s):
            c = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                c += 1
            
            return c
        
        for i in range(len(s)):
            odd = helper(i, i, s)
            even = helper(i, i+1, s)

            result += odd
            result += even
        
        return result