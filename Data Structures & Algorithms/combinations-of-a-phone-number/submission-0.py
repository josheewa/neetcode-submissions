class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        mp = {"2": (0,2), "3": (3,5),
        "4": (6,8), "5": (9,11), "6": (12,14),
        "7": (15,18), "8": (19,21), "9": (22,25)}

        def aux(i, s):
            if i >= len(digits):
                if s != "": res.append(s)
                return
            c = digits[i]
            for x in range(mp[c][0], mp[c][1]+1):
                aux(i+1, s+chr(x+97))
        aux(0, "")
        return res