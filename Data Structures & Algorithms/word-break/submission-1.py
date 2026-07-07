class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def dfs(ind):
            if ind == len(s):
                return True
            
            if ind in memo:
                return memo[ind]
            
            for word in wordDict:
                if s[ind:ind+len(word)] == word:
                    if dfs(ind+len(word)):
                        memo[ind] = True
                        return True

            memo[ind] = False
            return False
        return dfs(0)