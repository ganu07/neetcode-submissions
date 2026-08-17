class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l , r = 0, 0
        op = 0

        while r < len(s):
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
                r += 1
                op = max(op, r-l)
            else:
                del hashmap[s[l]]
                l +=  1

        
        return op

                


        
        