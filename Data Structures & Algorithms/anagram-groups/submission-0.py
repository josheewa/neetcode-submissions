import numpy as np

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = []
        for s in strs:
            sort.append("".join(sorted(s)))
        sort = np.array(sort)
        idx = np.argsort(sort)

        curr_word = sort[idx[0]]
        res = []
        curr_group = [strs[idx[0]]]
        for i in idx[1:]:
            print(strs[i])
            if sort[i] == curr_word:
                curr_group.append(strs[i])
            else:
                res.append(curr_group)
                curr_group = [strs[i]]
                curr_word = sort[i]
        res.append(curr_group)
        return res