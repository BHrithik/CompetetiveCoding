class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        neg = False
        print("After removing whitespace",s)
        if ("+-" in s or "-+" in s):
            return 0
        start = 0
        if s[0] == "-":
            neg = True
            start = 1
        if s[0] == "+":
            start = 1
        num_zeros = 0
        for i in range(0,len(s)):
            if s[i] == "0":
                num_zeros += 1
            else:
                break
        s = s[num_zeros:]
        if not s: return 0
        print(f"After removing whitespace and zeros upfront given string is{s}")
        ans = 0
        for i in range(start,len(s)):
            if s[i].isdigit():
                ans = ans * 10 + int(s[i])
            else:
                break
        print(f"ans is {ans}")
        if neg:
            ans = -ans
        if ans < -2**31:
            return -2**31
        elif ans > 2**31-1:
            return 2**31-1
        return ans