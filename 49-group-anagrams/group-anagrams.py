class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = defaultdict(list)
        for index,value in enumerate(strs):
            new_strs[tuple(sorted(value))].append(value)
        res = []
        for anagram in sorted(new_strs.keys()):
            dummy = []
            for s in new_strs[anagram]:
                dummy.append(s)
            res.append(dummy)
        return res