class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        for s in strs:
            a = str(sorted(s))
            d[a].append(s)
        
        res = []
        for k in d:
            res.append(d[k])
        return res
