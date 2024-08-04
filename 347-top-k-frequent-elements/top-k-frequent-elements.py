class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = Counter(nums)
        Arr = sorted(freqDict.keys(), key= lambda x: -freqDict[x])
        return Arr[:k]
