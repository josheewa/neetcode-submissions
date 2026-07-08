class Solution:

    def encode(self, strs: List[str]) -> str:
        decoded = ""
        for s in strs:
            decoded += s + "©"
        return decoded

    def decode(self, s: str) -> List[str]:
        strs = []
        curr = ""
        for c in s:
            if c == "©":
                strs.append(curr)
                curr = ""
            else:
                curr += c
        return strs

