class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = Counter(nums)
        # Arr = 
        return sorted(freqDict.keys(), key= lambda x: -freqDict[x])[:k]
