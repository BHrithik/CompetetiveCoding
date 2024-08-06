class Solution:
    def minimumPushes(self, word: str) -> int:
        wordDict = Counter(word)
        keys = sorted(wordDict.keys(),key=lambda x: wordDict[x],reverse = True)
        keyPad = {}
        count = 0
        cur_count = 1
        for i in keys:
            count += 1
            if count <= 8:
                keyPad[i] = 1
            elif count <= 16:
                keyPad[i] = 2
            elif count <= 24:
                keyPad[i] = 3
            else:
                keyPad[i] = 4
        res = 0
        for i in word:
            res += keyPad[i]
        return res
            


