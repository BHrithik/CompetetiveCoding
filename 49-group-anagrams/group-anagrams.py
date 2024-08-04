class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = defaultdict(list)
        for index,value in enumerate(strs):
            new_strs["".join(sorted(value))].append(value)
        return new_strs.values()