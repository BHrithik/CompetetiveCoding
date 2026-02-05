class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}
        for word in strs:
            word_dict = Counter(word)
            key = tuple(sorted(word_dict.items()))
            if key not in new_dict:
                new_dict[key] = []
            new_dict[key].append(word)
        return list(new_dict.values())