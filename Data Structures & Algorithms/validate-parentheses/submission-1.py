class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def corr(c):
            if c == ")": return "("
            if c == "}": return "{"
            if c == "]": return "["

        for c in s:
            if c in ("(", "{", "["): stack.append(c)
            elif c in (")", "}", "]"):
                if stack == [] or stack[-1] != corr(c): return False
                stack.pop()

        return stack == []