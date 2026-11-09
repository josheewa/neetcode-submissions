class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charset = set(s)
        res = 0

        for c in charset:
            l = 0
            ct = 0

            for r in range(len(s)):
                if s[r] == c:
                    ct += 1
                while r-l+1-ct > k:
                    if s[l] == c:
                        ct -= 1
                    l += 1
                res = max(res, r-l+1)
        return res
