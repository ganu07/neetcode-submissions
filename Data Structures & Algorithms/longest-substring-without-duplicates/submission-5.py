class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l, r = 0, 0
        result = 0

        while r < len(s):
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
                r += 1
                result = max(result, r-l)
            else:
                del hashmap[s[l]]
                l += 1
        
        return result


        
        