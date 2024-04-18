class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return ""
        stack = []
        stack.append(num[0])
        for i in range(1,len(num)):
            while stack and stack[-1] > num[i] and k:
                stack.pop()
                k -=1
            stack.append(num[i])
        while k:
            stack.pop()
            k = k-1
        m = "".join(stack).lstrip("0")

        return m if m != "" else "0"
