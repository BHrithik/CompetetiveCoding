class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        n = min(len(word1),len(word2))
        for i in range(n):
            s = s+word1[i]+word2[i]
        if n == len(word1):
            s = s + word2[n:]
        else:
            s = s + word1[n:]
        return s