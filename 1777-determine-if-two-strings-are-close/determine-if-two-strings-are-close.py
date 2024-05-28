class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_dict = Counter(word1)
        word2_dict = Counter(word2)
        if word1_dict == word2_dict:
            return True
        if word1_dict.keys() != word2_dict.keys():
            return False
        if sorted(word1_dict.values()) == sorted(word2_dict.values()):
            return True
        else:
            return False
