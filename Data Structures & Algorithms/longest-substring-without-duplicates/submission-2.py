class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        l = 0
        r = 0

        hs = set(s[l])
        res = 1

        while r + 1 < len(s):

            while s[r+1] in hs:
                hs.remove(s[l])
                l += 1
            
            hs.add(s[r+1])
            r += 1

            if r - l + 1 > res:
                res = r - l + 1

        return res