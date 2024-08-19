class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        for i in range(len(tokens)):
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
                stack.append(int(tokens[i]))
        return int(stack[-1])