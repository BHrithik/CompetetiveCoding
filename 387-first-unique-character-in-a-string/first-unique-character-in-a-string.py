class Solution:
    def firstUniqChar(self, s: str) -> int:
        countDict = Counter(s)
        print(countDict)
        for i in countDict.keys():
            if countDict[i] == 1:
                return s.find(i)
        return -1