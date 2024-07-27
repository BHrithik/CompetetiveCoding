class Solution:
    def uniqueLetterString(self, s: str) -> int:
        hashMap = defaultdict(list)
        for i in range(0,len(s)):
            hashMap[s[i]].append(i)
        count = 0
        for indexes in hashMap.values():
            for i,index in enumerate(indexes):
                l = 0 if i == 0 else indexes[i-1]+1
                r = len(s)-1 if i == len(indexes)-1 else indexes[i+1]-1
                count += (index-l+1)*(r-index+1)
        return count