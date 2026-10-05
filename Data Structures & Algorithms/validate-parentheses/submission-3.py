class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        def corresp(c):
            if c == ")": return "("
            if c == "}": return "{"
            if c == "]": return "["
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if not stack or corresp(c) != stack.pop():
                    return False
        return False if stack else True
            
