class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numDict = Counter(arr)
        return len(numDict.keys()) == len(list(set(numDict.values())))