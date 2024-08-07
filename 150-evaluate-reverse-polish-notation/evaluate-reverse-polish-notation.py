class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)
            elif tokens[i] == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b/a)
            elif tokens[i] == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)
            elif tokens[i] == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a*b)
            else:
                stack.append(tokens[i])
            i+=1
        return int(stack[-1])