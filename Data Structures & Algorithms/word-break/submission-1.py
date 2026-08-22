class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}

        def aux(i):
            if i == len(s): return True
            if i in memo: return memo[i]

            for j in range(i+1, len(s)+1):
                if s[i:j] in words and aux(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return aux(0)

                    