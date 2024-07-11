class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rem_chars = [i for i in s if i not in order]
        charDict = Counter(s)
        ans = ""
        for i in order:
            if i in charDict:
                ans += i*charDict[i]
        return ans+"".join(rem_chars)