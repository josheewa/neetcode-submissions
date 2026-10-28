class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= s + "一"
        return res

    def decode(self, s: str) -> List[str]:

        return s.split("一")[:-1]
