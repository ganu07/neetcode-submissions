class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hahsmap = {}
        result = 0
        max_freq = 1
        l = 0

        for r in range(len(s)):
            hahsmap[s[r]] = hahsmap.get(s[r], 0) + 1
            max_freq = max(max_freq, hahsmap[s[r]])

            while (r-l+1)- max_freq > k:
                hahsmap[s[l]] -= 1
                l+=1
        
            result = max(result, (r-l+1))
            
            
        return result


            




        