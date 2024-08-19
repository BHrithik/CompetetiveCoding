class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = {}
        for index,value in enumerate(strs):
            string = "".join(sorted(value))
            if string not in new_strs:
                new_strs[string] = []
            new_strs[string].append(value)
        return new_strs.values()