class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower()
        s = ""
        for c in low:
            if c.isalnum():
                s+= c
        for i in range(len(s) // 2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True