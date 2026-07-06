class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1:r]
        
        
        result = ""
        for i in range(len(s)):
            odd = helper(i, i, s)
            even = helper(i, i+1, s)

            if len(result) < len(even):
                result = even
            
            if len(result) < len(odd):
                result = odd
        
        return result


            
