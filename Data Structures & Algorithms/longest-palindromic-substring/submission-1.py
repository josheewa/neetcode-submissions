class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = s[0]
        reslen = 1

        def check(p, q):
            nonlocal res, reslen
            tmp = ""
            while p >= 0 and q < len(s) and s[p] == s[q]:
                tmp = s[p:q+1]
                p -= 1
                q += 1
            
            ln = len(tmp)
            if ln > reslen:
                res = tmp
                reslen = ln

        for i in range(len(s)):

            if i+1<len(s) and s[i] == s[i+1]:
                check(i, i+1)
            if i-1 >= 0 and i+1 < len(s) and s[i-1] == s[i+1]:
                check(i-1, i+1)

        return res   