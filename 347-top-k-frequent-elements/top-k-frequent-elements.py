class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for i in nums:
            if i not in freqDict:
                freqDict[i] = 1
            else:
                freqDict[i] += 1
        Arr = sorted(freqDict.items(), key=lambda item: -item[1])
        n = len(Arr)-1
        result = []
        print(Arr)
        for i in range(k):
            result.append(Arr[i][0])
        return(result)
