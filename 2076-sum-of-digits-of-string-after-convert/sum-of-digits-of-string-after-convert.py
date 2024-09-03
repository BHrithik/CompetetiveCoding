class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numStr = ""
        for ch in s:
            numStr+=str(ord(ch)-96)
        # num = int(numStr)
        while k>0:
            res = 0
            for n in numStr:
                res += int(n)
            numStr = str(res)
            k -= 1
        return res