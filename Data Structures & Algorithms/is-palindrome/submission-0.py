class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_rev = re.sub(r'[^a-z0-9]', '', s.lower())
        return s_rev == s_rev[::-1]
        