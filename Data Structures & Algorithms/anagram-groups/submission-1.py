import numpy as np

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sort = []
        for s in strs:
            sort.append("".join(sorted(s)))

        d = defaultdict(list)
        for i in range(len(strs)):
            d[sort[i]].append(strs[i])
        
        return list(d.values())