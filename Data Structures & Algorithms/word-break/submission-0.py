class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        res = {w: True for w in wordDict}

        def aux(s):
            if s == "" or s in words: return True

            for i in range(len(s)):
                if s[0:i] in words:
                    if s[i:] in res:
                        return res[s[i:]]
                    if aux(s[i:]):
                        res[s[i:]] = True
                        return True
                    else:
                        res[s[i:]] = False
            return False
        return aux(s)

                    