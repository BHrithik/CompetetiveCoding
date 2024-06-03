class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        if t[0] not in s:
            return len(t)
        sDict = {}
        for i in range(0,len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = [i]
            else:
                sDict[s[i]].append(i)
        currentIndex = -1
        lastIndex = 0
        for i in range(0,len(t)):
            if t[i] in sDict and sDict[t[i]]:
                possibleIndexes = [element for element in sDict[t[i]] if element > currentIndex]
                if possibleIndexes:
                    currentIndex = possibleIndexes[0]
                    sDict[t[i]].remove(currentIndex)
                    lastIndex = i
                else:
                    break
            else:
                break
        return len(t)-lastIndex-1

