class Solution:
    def numDecodings(self, s: str) -> int:
        prev_prev = 1
        prev = 1 if s[0] != '0' else 0

        for i in range(2, len(s) + 1):
            temp = 0
            if s[i-1] != '0':
                temp += prev
            
            if 10 <= int(s[i-2: i]) <= 26:
                temp += prev_prev
            
            prev_prev = prev
            prev = temp
        
        return prev
            
