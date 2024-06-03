class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        factors = []
        for i in range(min(len(str1),len(str2))):
            if str1.replace(str1[:i+1],"") == "" and str2.replace(str1[:i+1],"") == "":
                factors.append(str1[:i+1])
        return factors[-1] if factors else ""