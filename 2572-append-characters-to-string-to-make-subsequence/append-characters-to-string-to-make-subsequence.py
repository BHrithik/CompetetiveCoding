class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        if t[0] not in s:
            return len(t)
        
        sDict = {}
        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = [i]
            else:
                sDict[s[i]].append(i)
        
        currentIndex = -1
        lastIndex = 0
        
        for i in range(len(t)):
            if t[i] in sDict and sDict[t[i]]:
                possible_positions = [pos for pos in sDict[t[i]] if pos > currentIndex]
                if possible_positions:
                    currentIndex = possible_positions[0]
                    sDict[t[i]].remove(currentIndex)
                    lastIndex = i
                else:
                    break
            else:
                break
        
        return len(t) - lastIndex - 1
