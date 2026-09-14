class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        
        check = {}
        for c in t: check[c] = 1 + check.get(c, 0)
        reslen = float("inf")
        res = ""

        have = 0
        need = len(check)
        window = {}

        l = 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in check and window[s[r]] == check[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < reslen:
                    res = s[l:r+1]
                    reslen = len(res)
                window[s[l]] -= 1
                if s[l] in check and window[s[l]] < check[s[l]]:
                    have -= 1
                l += 1
        return res if reslen < float("inf") else ""
            
