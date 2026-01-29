class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+","-","*","/"}
        for ch in tokens:
            if ch in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                if ch == "/":
                    stack.append(int(num2/num1))
                if ch == "+":
                    stack.append(num2+num1)
                if ch == "-":
                    stack.append(num2-num1)
                if ch == "*":
                    stack.append(num2*num1)
                continue
            stack.append(int(ch))
        return stack[0]
