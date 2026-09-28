class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for tok in tokens:
            if tok.isnumeric() or tok[1:].isnumeric():
                stack.append(int(tok))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if tok == "+":
                    stack.append(op1 + op2)
                elif tok == "-":
                    stack.append(op1 - op2)
                elif tok == "*":
                    stack.append(op1 * op2)
                elif tok == "/":
                    stack.append(int(op1 / op2))
        
        return stack.pop()

