class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        max_count = 0

        l = 0
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            
            while ((r-l+1) - max(hashmap.values())) > k:
                
                if hashmap[s[l]]:
                    hashmap[s[l]] -= 1
                else:
                    del hashmap[s[l]]
                l += 1
            
            max_count = max(max_count, (r-l+1))
        
        return max_count




         


            




        