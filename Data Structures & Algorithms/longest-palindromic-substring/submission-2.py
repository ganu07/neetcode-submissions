class Solution:
    def longestPalindrome(self, s: str) -> str:

        def helper(left, right, s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
        
        result = ""
        for i in range(len(s)):
            even = helper(i, i+1, s)
            odd = helper(i, i, s)

            if len(odd) > len(result):
                result = odd
            
            if len(even) > len(result):
                result = even
            
        return result
            


        