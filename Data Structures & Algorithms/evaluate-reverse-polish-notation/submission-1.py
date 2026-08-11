class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def isnum(tok):
            return tok != "+" and tok != "-" and tok != "*" and tok != "/"
        stack = []
        for tok in tokens:
            if isnum(tok):
                stack.append(int(tok))
            else:
                if tok == "+":
                    stack.append(stack.pop() + stack.pop())
                elif tok == "-":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l - r)
                elif tok == "*":
                    stack.append(stack.pop() * stack.pop())
                elif tok == "/":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(int(l / r))
        return stack[0]